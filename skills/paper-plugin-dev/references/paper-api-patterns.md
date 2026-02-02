# Paper API Patterns and Best Practices

Comprehensive guide to Paper-specific APIs and patterns for modern plugin development.

## Table of Contents

- [Scheduler APIs](#scheduler-apis)
- [Entity and World Access](#entity-and-world-access)
- [Configuration](#configuration)
- [Events](#events)
- [Performance Patterns](#performance-patterns)
- [Anti-Patterns](#anti-patterns)

## Scheduler APIs

### Region Schedulers (Folia-compatible)

For operations involving entities or world locations, use region schedulers:

```java
// Entity scheduler
entity.getScheduler().run(plugin, task -> {
    // Safe to access entity here
    entity.setHealth(20.0);
}, null);

// Execute after delay (20 ticks = 1 second)
entity.getScheduler().runDelayed(plugin, task -> {
    entity.damage(5.0);
}, null, 20L);

// Location/Chunk scheduler
Location loc = new Location(world, x, y, z);
Bukkit.getRegionScheduler().run(plugin, loc, task -> {
    // Safe to access chunk at this location
    world.getBlockAt(loc).setType(Material.STONE);
});
```

### Async Scheduler

For I/O, database queries, HTTP requests (NOT Bukkit API):

```java
Bukkit.getAsyncScheduler().runNow(plugin, task -> {
    // NO Bukkit API calls here!
    // Only use for: database, file I/O, HTTP, heavy computations
    String data = database.query("SELECT * FROM users");
    
    // To use results with Bukkit API, schedule back to main thread:
    Bukkit.getGlobalRegionScheduler().run(plugin, innerTask -> {
        // Now safe to use Bukkit API
        player.sendMessage(Component.text(data));
    });
});
```

### Global Region Scheduler

For server-wide tasks not tied to specific locations:

```java
Bukkit.getGlobalRegionScheduler().run(plugin, task -> {
    // Execute once
    Bukkit.broadcast(Component.text("Server announcement!"));
});

Bukkit.getGlobalRegionScheduler().runAtFixedRate(plugin, task -> {
    // Repeating task (every 100 ticks)
    performCleanup();
}, 100L, 100L);
```

## Entity and World Access

### Safe Entity Operations

Always check entity validity and use schedulers:

```java
public void damageEntity(Entity entity, double amount) {
    if (!entity.isValid()) {
        return;
    }
    
    entity.getScheduler().run(plugin, task -> {
        if (entity.isValid()) { // Re-check in scheduler
            entity.damage(amount);
        }
    }, null);
}
```

### World Modifications

```java
// Bulk operations - use chunked processing
public void fillArea(World world, Location corner1, Location corner2, Material material) {
    List<Block> blocks = getBlocksInArea(corner1, corner2);
    
    // Process in batches to avoid lag
    int batchSize = 1000;
    for (int i = 0; i < blocks.size(); i += batchSize) {
        int start = i;
        int end = Math.min(i + batchSize, blocks.size());
        
        Bukkit.getRegionScheduler().run(plugin, corner1, task -> {
            for (int j = start; j < end; j++) {
                blocks.get(j).setType(material, false); // false = no physics
            }
        });
    }
}
```

### Persistent Data Container (PDC)

Store custom data on entities, blocks, items, chunks:

```java
import org.bukkit.NamespacedKey;
import org.bukkit.persistence.PersistentDataType;

// Create a key
NamespacedKey key = new NamespacedKey(plugin, "custom_data");

// Store data
entity.getPersistentDataContainer().set(key, PersistentDataType.STRING, "value");
entity.getPersistentDataContainer().set(key, PersistentDataType.INTEGER, 42);

// Retrieve data
String value = entity.getPersistentDataContainer().get(key, PersistentDataType.STRING);

// Check existence
if (entity.getPersistentDataContainer().has(key, PersistentDataType.STRING)) {
    // Has data
}

// Remove data
entity.getPersistentDataContainer().remove(key);
```

### Item Meta Modifications

```java
ItemStack item = new ItemStack(Material.DIAMOND_SWORD);
item.editMeta(meta -> {
    // Set display name
    meta.displayName(Component.text("Legendary Sword", NamedTextColor.GOLD));
    
    // Set lore (must remove italic decoration)
    meta.lore(List.of(
        Component.text("A powerful weapon").decoration(TextDecoration.ITALIC, false),
        Component.text("+10 Attack").color(NamedTextColor.RED).decoration(TextDecoration.ITALIC, false)
    ));
    
    // Add enchantments
    meta.addEnchant(Enchantment.SHARPNESS, 5, true);
    
    // Custom model data
    meta.setCustomModelData(12345);
    
    // PDC on items
    NamespacedKey key = new NamespacedKey(plugin, "weapon_id");
    meta.getPersistentDataContainer().set(key, PersistentDataType.STRING, "legendary_sword");
});
```

## Configuration

### Custom Config Files

```java
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.configuration.file.YamlConfiguration;

public class CustomConfig {
    private final File configFile;
    private FileConfiguration config;
    
    public CustomConfig(Plugin plugin, String fileName) {
        this.configFile = new File(plugin.getDataFolder(), fileName);
        reload();
    }
    
    public void reload() {
        if (!configFile.exists()) {
            configFile.getParentFile().mkdirs();
            // Save default from resources
            plugin.saveResource(fileName, false);
        }
        config = YamlConfiguration.loadConfiguration(configFile);
    }
    
    public void save() {
        try {
            config.save(configFile);
        } catch (IOException e) {
            plugin.getLogger().severe("Could not save config: " + e.getMessage());
        }
    }
    
    public FileConfiguration get() {
        return config;
    }
}
```

### Type-Safe Config Wrapper

```java
public class ConfigSettings {
    private final FileConfiguration config;
    
    public ConfigSettings(FileConfiguration config) {
        this.config = config;
    }
    
    public boolean isFeatureEnabled() {
        return config.getBoolean("settings.feature-enabled", true);
    }
    
    public int getMaxPlayers() {
        return config.getInt("settings.max-players", 100);
    }
    
    public Component getWelcomeMessage() {
        String raw = config.getString("messages.welcome", "<green>Welcome!");
        return MiniMessage.miniMessage().deserialize(raw);
    }
}
```

## Events

### Event Priority

```java
// Priority order: LOWEST -> LOW -> NORMAL -> HIGH -> HIGHEST -> MONITOR
@EventHandler(priority = EventPriority.HIGH)
public void onEvent(PlayerJoinEvent event) {
    // Higher priority runs later
}

// MONITOR - only for observation, never modify
@EventHandler(priority = EventPriority.MONITOR, ignoreCancelled = true)
public void onEventMonitor(BlockBreakEvent event) {
    // Log only, don't modify event
    logBlockBreak(event.getBlock());
}
```

### Custom Events

```java
import org.bukkit.event.Event;
import org.bukkit.event.HandlerList;

public class CustomEvent extends Event {
    private static final HandlerList HANDLERS = new HandlerList();
    private final Player player;
    private String message;
    
    public CustomEvent(Player player, String message) {
        this.player = player;
        this.message = message;
    }
    
    public Player getPlayer() {
        return player;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    @Override
    public HandlerList getHandlers() {
        return HANDLERS;
    }
    
    public static HandlerList getHandlerList() {
        return HANDLERS;
    }
}

// Calling the event
CustomEvent event = new CustomEvent(player, "Hello");
Bukkit.getPluginManager().callEvent(event);
// Event can be modified by listeners
String finalMessage = event.getMessage();
```

## Performance Patterns

### Caching

```java
import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import java.util.concurrent.TimeUnit;

// Cache with expiration
private final Cache<UUID, PlayerData> cache = CacheBuilder.newBuilder()
    .expireAfterAccess(10, TimeUnit.MINUTES)
    .maximumSize(1000)
    .build();

public PlayerData getPlayerData(UUID uuid) {
    return cache.get(uuid, () -> loadFromDatabase(uuid));
}
```

### Batch Processing

```java
// Process large operations in batches
private final Queue<BlockChange> pendingChanges = new ConcurrentLinkedQueue<>();

public void queueBlockChange(Location loc, Material material) {
    pendingChanges.offer(new BlockChange(loc, material));
}

// Process in fixed-rate task
Bukkit.getGlobalRegionScheduler().runAtFixedRate(plugin, task -> {
    int processed = 0;
    while (processed < 100 && !pendingChanges.isEmpty()) {
        BlockChange change = pendingChanges.poll();
        change.location().getBlock().setType(change.material());
        processed++;
    }
}, 1L, 1L);
```

### Entity Lookup Optimization

```java
// Bad: Iterate all entities
for (Entity entity : world.getEntities()) {
    if (entity instanceof Player) {
        // Process
    }
}

// Good: Use getNearbyEntities or getEntitiesByClass
world.getNearbyEntities(location, radius, radius, radius, entity -> entity instanceof Player)
    .forEach(entity -> {
        Player player = (Player) entity;
        // Process
    });

// Even better: Direct player getter
world.getPlayers().forEach(player -> {
    // Process
});
```

## Anti-Patterns

### ❌ Don't Use These Legacy APIs

```java
// WRONG - Legacy color codes
player.sendMessage(ChatColor.RED + "Error!");

// RIGHT - Adventure components
player.sendMessage(Component.text("Error!", NamedTextColor.RED));
```

```java
// WRONG - String join messages
event.setJoinMessage("§e" + player.getName() + " §7joined");

// RIGHT - Adventure components
event.joinMessage(Component.text()
    .append(Component.text(player.getName(), NamedTextColor.YELLOW))
    .append(Component.text(" joined", NamedTextColor.GRAY))
    .build()
);
```

```java
// WRONG - BukkitRunnable
new BukkitRunnable() {
    @Override
    public void run() {
        // Task
    }
}.runTaskLater(plugin, 20L);

// RIGHT - Region scheduler
Bukkit.getGlobalRegionScheduler().runDelayed(plugin, task -> {
    // Task
}, 20L);
```

### ❌ Reflection for NMS

```java
// WRONG - NMS reflection (breaks between versions)
Class<?> craftPlayer = Class.forName("org.bukkit.craftbukkit.v1_20_R1.entity.CraftPlayer");

// RIGHT - Use Paper API or request feature
// Paper provides most needed functionality without NMS
```

### ❌ Blocking I/O on Main Thread

```java
// WRONG - Blocks server tick
String data = httpClient.get("https://api.example.com/data");
player.sendMessage(data);

// RIGHT - Async scheduler
Bukkit.getAsyncScheduler().runNow(plugin, task -> {
    String data = httpClient.get("https://api.example.com/data");
    
    Bukkit.getGlobalRegionScheduler().run(plugin, innerTask -> {
        player.sendMessage(Component.text(data));
    });
});
```

### ❌ Storing Players/Entities

```java
// WRONG - Stores entire player object (memory leak)
private final Map<UUID, Player> players = new HashMap<>();

// RIGHT - Store UUID, lookup when needed
private final Set<UUID> trackedPlayers = new HashSet<>();

public void processPlayer(UUID uuid) {
    Player player = Bukkit.getPlayer(uuid);
    if (player != null && player.isOnline()) {
        // Process
    }
}
```

### ✅ Thread-Safe Collections

```java
// For concurrent access from multiple threads
private final Map<UUID, PlayerData> data = new ConcurrentHashMap<>();
private final Set<UUID> players = ConcurrentHashMap.newKeySet();
private final Queue<Task> tasks = new ConcurrentLinkedQueue<>();
```

## Paper-Specific Features

### Paper Events

```java
import com.destroystokyo.paper.event.player.PlayerJumpEvent;

@EventHandler
public void onJump(PlayerJumpEvent event) {
    // Fired when player jumps
}
```

### Async Chunk Loading

```java
world.getChunkAtAsync(x, z).thenAccept(chunk -> {
    // Chunk is loaded, safe to use
    Bukkit.getRegionScheduler().run(plugin, chunk.getBlock(0, 64, 0).getLocation(), task -> {
        // Modify chunk
    });
});
```

### Paper Player API

```java
// Get player's client brand
String brand = player.getClientBrandName(); // e.g., "vanilla", "fabric"

// Player locale
Locale locale = player.locale();

// Ping
int ping = player.getPing();
```

### Paper World API

```java
// Get spawn chunks
Collection<Chunk> spawnChunks = world.getForceLoadedChunks();

// Set simulation distance
world.setSimulationDistance(8);
```
