# Debugging and Troubleshooting Guide

Complete guide to debugging Paper plugins, reading logs, and solving common issues.

## Table of Contents

- [Logging](#logging)
- [Reading Stack Traces](#reading-stack-traces)
- [Common Errors](#common-errors)
- [Debugging Tools](#debugging-tools)
- [Performance Profiling](#performance-profiling)
- [Plugin Conflicts](#plugin-conflicts)

## Logging

### Using Plugin Logger

```java
public class MyPlugin extends JavaPlugin {
    
    @Override
    public void onEnable() {
        // Different log levels
        getLogger().info("Plugin enabled");
        getLogger().warning("This is a warning");
        getLogger().severe("This is an error");
        
        // Debug logging (conditional)
        if (getConfig().getBoolean("debug", false)) {
            getLogger().info("[DEBUG] Debug information");
        }
    }
    
    public void logException(String message, Exception e) {
        getLogger().severe(message);
        getLogger().severe("Exception: " + e.getMessage());
        e.printStackTrace();
    }
}
```

### Structured Logging

```java
public class LogHelper {
    private final Logger logger;
    private final boolean debug;
    
    public LogHelper(JavaPlugin plugin) {
        this.logger = plugin.getLogger();
        this.debug = plugin.getConfig().getBoolean("debug", false);
    }
    
    public void info(String message) {
        logger.info(message);
    }
    
    public void debug(String message) {
        if (debug) {
            logger.info("[DEBUG] " + message);
        }
    }
    
    public void warn(String message) {
        logger.warning(message);
    }
    
    public void error(String message) {
        logger.severe(message);
    }
    
    public void error(String message, Throwable throwable) {
        logger.severe(message);
        logger.severe("Exception: " + throwable.getMessage());
        throwable.printStackTrace();
    }
    
    public void logMethod(String methodName) {
        debug("Entering method: " + methodName);
    }
    
    public void logVariable(String name, Object value) {
        debug(name + " = " + value);
    }
}
```

### Log File Locations

```
server/
├── logs/
│   ├── latest.log          # Current session log
│   ├── 2026-01-25-1.log.gz # Archived logs
│   └── ...
```

## Reading Stack Traces

### Anatomy of a Stack Trace

```
[12:34:56 ERROR]: Could not pass event PlayerJoinEvent to MyPlugin v1.0.0
org.bukkit.event.EventException: null
    at org.bukkit.plugin.RegisteredListener.callEvent(RegisteredListener.java:123)
    at org.bukkit.plugin.SimplePluginManager.fireEvent(SimplePluginManager.java:456)
Caused by: java.lang.NullPointerException: Cannot invoke method getName() on null
    at com.example.myplugin.JoinListener.onJoin(JoinListener.java:45)
    at com.example.myplugin.JoinListener$$FastReflection.invoke(Unknown Source)
```

**Reading Tips**:
1. **First line**: General error message
2. **Exception type**: `NullPointerException` - what went wrong
3. **Message**: "Cannot invoke method getName() on null" - detailed info
4. **"at" lines**: Stack trace showing call chain
5. **Your plugin lines**: Look for your package name (com.example.myplugin)
6. **Line numbers**: `JoinListener.java:45` - exact location of error

### Common Stack Trace Patterns

```java
// NullPointerException - Trying to use null object
Player player = null;
player.getName(); // NPE at this line

// ClassCastException - Wrong type conversion
Object obj = "string";
Integer num = (Integer) obj; // ClassCastException

// ArrayIndexOutOfBoundsException - Invalid array/list index
List<String> list = new ArrayList<>();
String item = list.get(0); // IndexOutOfBoundsException

// IllegalArgumentException - Invalid method argument
player.setHealth(-10); // IllegalArgumentException

// ConcurrentModificationException - Modifying while iterating
for (Player p : Bukkit.getOnlinePlayers()) {
    p.kick(); // Can cause ConcurrentModificationException
}
```

## Common Errors

### Plugin Not Loading

**Symptoms**: Plugin not listed when running `/plugins`

**Possible Causes**:

1. **Invalid paper-plugin.yml**:
```yaml
# ❌ Common mistakes:
name: My Plugin  # Spaces not allowed
main: MyPlugin   # Missing package path
api-version: 1.21  # Wrong format (needs quotes)

# ✅ Correct:
name: MyPlugin
main: com.example.MyPlugin
api-version: '1.21'
```

2. **Missing dependencies**:
```
[ERROR] Could not load 'MyPlugin.jar'
org.bukkit.plugin.UnknownDependencyException: Unknown dependency: Vault
```
**Solution**: Install required dependency plugins

3. **Wrong Java version**:
```
[ERROR] Unsupported class file major version 65
```
**Solution**: Update to Java 21+

4. **Main class not found**:
```
[ERROR] Cannot find main class 'com.example.MyPlugin'
```
**Solution**: Check main class path in paper-plugin.yml matches actual package

### NullPointerException

**Most common cause**: Not checking if object is null

```java
// ❌ BAD
public void onJoin(PlayerJoinEvent event) {
    String worldName = event.getPlayer().getWorld().getName();
    // What if player or world is null?
}

// ✅ GOOD
public void onJoin(PlayerJoinEvent event) {
    Player player = event.getPlayer();
    if (player == null) {
        plugin.getLogger().warning("Player is null in join event!");
        return;
    }
    
    World world = player.getWorld();
    if (world == null) {
        plugin.getLogger().warning("World is null for player: " + player.getName());
        return;
    }
    
    String worldName = world.getName();
}
```

**Common NPE scenarios**:
```java
// Config value missing
String value = config.getString("missing.key"); // Returns null
value.toUpperCase(); // NPE!

// Player offline
UUID uuid = UUID.fromString("...");
Player player = Bukkit.getPlayer(uuid); // Null if offline
player.sendMessage("..."); // NPE!

// Item meta missing
ItemStack item = new ItemStack(Material.STONE);
item.getItemMeta().setDisplayName("..."); // NPE! Stone has no meta

// Collection element missing
Map<UUID, PlayerData> dataMap = new HashMap<>();
PlayerData data = dataMap.get(player.getUniqueId()); // Null if not in map
data.update(); // NPE!
```

**Solutions**:
```java
// Use Optional
Optional<PlayerData> optData = Optional.ofNullable(dataMap.get(uuid));
optData.ifPresent(PlayerData::update);

// Use getOrDefault
String value = config.getString("key", "default");

// Null checks
if (player != null && player.isOnline()) {
    player.sendMessage("...");
}

// Edit meta safely
item.editMeta(meta -> {
    meta.displayName(Component.text("Custom Name"));
});
```

### Thread-related Errors

```
[ERROR] java.lang.IllegalStateException: Asynchronous entity track!
[ERROR] java.lang.IllegalStateException: Asynchronous chunk load!
```

**Cause**: Accessing Bukkit API from async thread

```java
// ❌ BAD - Calling Bukkit API from async thread
Bukkit.getAsyncScheduler().runNow(plugin, task -> {
    player.sendMessage("Hello"); // WRONG! This is Bukkit API
});

// ✅ GOOD - Schedule back to main thread
Bukkit.getAsyncScheduler().runNow(plugin, task -> {
    // Do async work (database, HTTP, etc.)
    String data = database.query("...");
    
    // Return to main thread for Bukkit API
    Bukkit.getGlobalRegionScheduler().run(plugin, innerTask -> {
        player.sendMessage(Component.text(data));
    });
});
```

### Event Not Firing

**Checklist**:

1. **Listener registered?**
```java
@Override
public void onEnable() {
    getServer().getPluginManager().registerEvents(new MyListener(), this);
}
```

2. **@EventHandler annotation present?**
```java
public class MyListener implements Listener {
    @EventHandler  // Don't forget this!
    public void onJoin(PlayerJoinEvent event) {
        // ...
    }
}
```

3. **Correct event priority?**
```java
@EventHandler(priority = EventPriority.MONITOR)
public void onEvent(PlayerJoinEvent event) {
    // Runs last, after other plugins
}
```

4. **Event cancelled?**
```java
@EventHandler(ignoreCancelled = true)
public void onEvent(BlockBreakEvent event) {
    // Won't run if another plugin cancelled the event
}
```

5. **Method signature correct?**
```java
// ❌ WRONG - wrong parameter type
@EventHandler
public void onJoin(Event event) { } // Too generic

// ✅ CORRECT
@EventHandler
public void onJoin(PlayerJoinEvent event) { }
```

### ClassNotFoundException / NoClassDefFoundError

```
[ERROR] java.lang.ClassNotFoundException: net.kyori.adventure.text.Component
```

**Causes**:
1. Missing dependency
2. Not shading dependency
3. Wrong relocation

**Solutions**:

1. **Add to pom.xml**:
```xml
<dependency>
    <groupId>net.kyori</groupId>
    <artifactId>adventure-api</artifactId>
    <version>4.26.1</version>
    <scope>provided</scope> <!-- Don't shade if Paper provides it -->
</dependency>
```

2. **Shade third-party libraries**:
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.5.0</version>
    <configuration>
        <relocations>
            <relocation>
                <pattern>com.zaxxer.hikari</pattern>
                <shadedPattern>com.example.myplugin.libs.hikari</shadedPattern>
            </relocation>
        </relocations>
    </configuration>
</plugin>
```

## Debugging Tools

### Using IDE Debugger

**IntelliJ IDEA**:
1. Create "Remote JVM Debug" configuration
2. Add to server startup: `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005`
3. Set breakpoints in code
4. Start server, then "Debug" in IDE

### Breakpoint Logging

```java
public class DebugHelper {
    public static void checkpoint(String location) {
        System.out.println("[CHECKPOINT] " + location + " at " + 
            new SimpleDateFormat("HH:mm:ss").format(new Date()));
    }
    
    public static void dumpPlayerInfo(Player player) {
        System.out.println("=== Player Debug Info ===");
        System.out.println("Name: " + player.getName());
        System.out.println("UUID: " + player.getUniqueId());
        System.out.println("Location: " + player.getLocation());
        System.out.println("Health: " + player.getHealth());
        System.out.println("Game Mode: " + player.getGameMode());
        System.out.println("========================");
    }
}
```

### Command Debugging

```java
public class DebugCommand implements CommandExecutor {
    
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (!sender.hasPermission("myplugin.debug")) {
            return true;
        }
        
        if (args.length == 0) {
            sender.sendMessage("=== Debug Info ===");
            sender.sendMessage("Online Players: " + Bukkit.getOnlinePlayers().size());
            sender.sendMessage("Loaded Chunks: " + getLoadedChunksCount());
            sender.sendMessage("TPS: " + Bukkit.getTPS()[0]);
            return true;
        }
        
        switch (args[0].toLowerCase()) {
            case "player":
                if (sender instanceof Player) {
                    Player player = (Player) sender;
                    dumpPlayerInfo(player);
                }
                break;
                
            case "memory":
                Runtime runtime = Runtime.getRuntime();
                long used = runtime.totalMemory() - runtime.freeMemory();
                sender.sendMessage("Memory: " + (used / 1024 / 1024) + "MB / " +
                                 (runtime.maxMemory() / 1024 / 1024) + "MB");
                break;
        }
        
        return true;
    }
}
```

## Performance Profiling

### Timings

```bash
# Enable timings
/timings on

# Wait 10-15 minutes during normal server activity

# Generate report
/timings paste

# View at https://timings.aikar.co
```

**Reading Timings Report**:
- Look for red bars (high time usage)
- Check your plugin's event handlers
- Compare with other plugins

### Spark Profiler

```bash
# Install Spark plugin
# https://spark.lucko.me/

# Start profiling
/spark profiler

# Stop after ~30 seconds
/spark profiler --stop

# View report in web browser
```

### Manual Performance Tracking

```java
public class PerformanceMonitor {
    
    public static void measureOperation(Runnable operation, String name) {
        long start = System.nanoTime();
        try {
            operation.run();
        } finally {
            long duration = System.nanoTime() - start;
            double ms = duration / 1_000_000.0;
            
            if (ms > 50) { // Warn if over 50ms
                System.out.println("[PERF] " + name + " took " + 
                                 String.format("%.2f", ms) + "ms (SLOW!)");
            }
        }
    }
}

// Usage:
PerformanceMonitor.measureOperation(() -> {
    // Your code here
    processLargeDataset();
}, "Data Processing");
```

## Plugin Conflicts

### Detecting Conflicts

```bash
# List all plugins
/plugins

# Check for conflicts in logs
grep -i "conflict\|error" logs/latest.log
```

### Common Conflict Scenarios

1. **Multiple plugins handling same event**:
```java
// Use priority to control order
@EventHandler(priority = EventPriority.LOW)
public void onChat(AsyncChatEvent event) {
    // Runs early
}

@EventHandler(priority = EventPriority.HIGH)
public void onChatLater(AsyncChatEvent event) {
    // Runs after LOW priority handlers
}
```

2. **Command conflicts**:
```yaml
# In paper-plugin.yml - use unique command names
commands:
  myplugin:home:
    description: Teleport home
    aliases: [myhome, mphome]
```

3. **Different API versions**:
```
[ERROR] Plugin A uses Adventure 4.26.1
[ERROR] Plugin B uses Adventure 4.10.0 (relocated)
```
**Solution**: Ensure proper relocation in Maven shade

### Binary Search for Conflicts

1. Disable half of your plugins
2. Test if issue persists
3. If yes, disable half of enabled plugins
4. If no, enable half of disabled plugins
5. Repeat until you find the conflicting plugin

## Best Practices

### Defensive Programming

```java
// Always validate input
public void setPlayerHealth(Player player, double health) {
    if (player == null) {
        throw new IllegalArgumentException("Player cannot be null");
    }
    if (health < 0 || health > 20) {
        throw new IllegalArgumentException("Health must be between 0 and 20");
    }
    player.setHealth(health);
}

// Use try-catch for external operations
public void saveData(PlayerData data) {
    try {
        database.save(data);
    } catch (SQLException e) {
        plugin.getLogger().severe("Failed to save player data: " + e.getMessage());
        e.printStackTrace();
    }
}
```

### Error Recovery

```java
public class PlayerDataManager {
    
    public PlayerData loadPlayerData(UUID uuid) {
        try {
            return database.load(uuid);
        } catch (Exception e) {
            plugin.getLogger().severe("Failed to load data for " + uuid);
            e.printStackTrace();
            
            // Return default data instead of crashing
            return new PlayerData(uuid);
        }
    }
}
```

### Fail-Safe Configuration

```java
public class Config {
    
    public int getInt(String path, int defaultValue, int min, int max) {
        int value = config.getInt(path, defaultValue);
        
        if (value < min || value > max) {
            plugin.getLogger().warning(
                "Invalid value for " + path + ": " + value + 
                ". Using default: " + defaultValue
            );
            return defaultValue;
        }
        
        return value;
    }
}
```
