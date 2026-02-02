---
name: paper-plugin-dev
description: Minecraft Paper/Spigot/Bukkit/Folia plugin development expert. Activate for ANY Minecraft plugin coding, including commands, events, listeners, GUI/inventory, configurations (YAML/config.yml), entities, items, worlds, permissions, databases, schedulers, async tasks, NBT, packets, or API usage. Covers Adventure API, MiniMessage, ComponentLogger, modern Paper APIs, thread safety, Folia compatibility, performance optimization. Use for plugin creation, debugging, refactoring, or any Minecraft server plugin development question. Supports both English and Chinese (我的世界插件开发/服务端插件/Paper插件/Bukkit插件).
---

# Paper Plugin Development

Modern Minecraft server plugin development using PaperMC and Adventure API.

## Quick Start

### Creating a New Plugin

Use the bundled template for standard Maven-based plugin structure:

```bash
cp -r assets/plugin-template/ /path/to/new-plugin
cd /path/to/new-plugin
# Update pom.xml with your plugin details
# Update paper-plugin.yml with your plugin metadata
```

Or use the initialization script for automated setup:

```bash
python scripts/create_plugin_structure.py "MyPlugin" "com.example.myplugin" /path/to/output
```

### Core Concepts

1. **Paper API**: Use Paper-specific APIs when available - they're better optimized and feature-rich than Bukkit/Spigot equivalents
2. **Adventure API**: Use Adventure for all text/chat components - never use legacy ChatColor or legacy serializers
3. **Thread Safety**: Always consider thread safety, especially for Folia compatibility
4. **Performance**: Follow Aikar's flags and optimization best practices

## Essential Patterns

### Plugin Main Class

```java
import io.papermc.paper.plugin.lifecycle.event.types.LifecycleEvents;
import net.kyori.adventure.text.Component;
import org.bukkit.plugin.java.JavaPlugin;

public class MyPlugin extends JavaPlugin {
    
    @Override
    public void onEnable() {
        // Register lifecycle events
        this.getLifecycleManager().registerEventHandler(
            LifecycleEvents.COMMANDS,
            event -> {
                // Register commands here
            }
        );
        
        getLogger().info("Plugin enabled!");
    }
    
    @Override
    public void onDisable() {
        getLogger().info("Plugin disabled!");
    }
}
```

### Sending Messages with Adventure

```java
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import net.kyori.adventure.text.format.TextDecoration;
import org.bukkit.entity.Player;

// Simple colored message
player.sendMessage(Component.text("Hello!", NamedTextColor.GREEN));

// Complex formatted message
Component message = Component.text()
    .append(Component.text("Welcome ", NamedTextColor.GOLD))
    .append(Component.text(player.getName(), NamedTextColor.YELLOW, TextDecoration.BOLD))
    .append(Component.text("!", NamedTextColor.GOLD))
    .build();
player.sendMessage(message);

// With click/hover events
Component clickable = Component.text("Click me!", NamedTextColor.AQUA)
    .clickEvent(ClickEvent.runCommand("/help"))
    .hoverEvent(HoverEvent.showText(Component.text("Run /help")));
player.sendMessage(clickable);
```

### MiniMessage for User Input

```java
import net.kyori.adventure.text.minimessage.MiniMessage;
import net.kyori.adventure.text.minimessage.tag.resolver.Placeholder;

// MiniMessage instance (reuse for performance)
private static final MiniMessage mm = MiniMessage.miniMessage();

// Parse MiniMessage from config/user input
Component parsed = mm.deserialize("<rainbow>Rainbow text!</rainbow>");
player.sendMessage(parsed);

// With placeholders (ALWAYS use unparsed for user input!)
Component withPlaceholders = mm.deserialize(
    "Hello <player>!",
    Placeholder.unparsed("player", player.getName())
);

// Multiple placeholders
Component message = mm.deserialize(
    "<prefix> <player> has <amount> coins",
    Placeholder.unparsed("player", player.getName()),
    Placeholder.unparsed("amount", String.valueOf(balance)),
    Placeholder.parsed("prefix", "<gold>[Server]</gold>")
);

// New features (4.18+): Pride gradients
Component pride = mm.deserialize("<pride:trans>Trans rights!</pride>");

// New features (4.25+): Sprites and heads
Component sprite = mm.deserialize("<sprite:blocks:block/stone>");
Component head = mm.deserialize("<head:Notch>");

// For complete MiniMessage syntax, see minimessage-guide.md
```

### Event Handling

```java
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class JoinListener implements Listener {
    
    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        Player player = event.getPlayer();
        
        // Set join message with Adventure
        event.joinMessage(Component.text()
            .append(Component.text("→ ", NamedTextColor.GREEN))
            .append(Component.text(player.getName(), NamedTextColor.YELLOW))
            .append(Component.text(" joined", NamedTextColor.GRAY))
            .build()
        );
    }
}

// Register in onEnable():
getServer().getPluginManager().registerEvents(new JoinListener(), this);
```

### Configuration

```java
import org.bukkit.configuration.file.FileConfiguration;

// Access config.yml
FileConfiguration config = getConfig();

// Set defaults
config.addDefault("messages.welcome", "<green>Welcome!");
config.addDefault("settings.enabled", true);
config.options().copyDefaults(true);
saveConfig();

// Read values
String welcomeMsg = config.getString("messages.welcome");
boolean enabled = config.getBoolean("settings.enabled");
```

## Advanced Topics

### Thread Safety & Folia

For Folia compatibility or async operations:

```java
// Schedule on entity's region
entity.getScheduler().run(plugin, task -> {
    // This runs on the entity's region thread
}, null);

// Schedule on chunk's region  
Bukkit.getRegionScheduler().run(plugin, location, task -> {
    // This runs on the chunk's region thread
});

// Async tasks (for I/O, database, etc.)
Bukkit.getAsyncScheduler().runNow(plugin, task -> {
    // This runs asynchronously - NO BUKKIT API CALLS HERE
});
```

### Commands (Modern Brigadier API)

```java
import io.papermc.paper.command.brigadier.Commands;
import io.papermc.paper.command.brigadier.argument.ArgumentTypes;
import io.papermc.paper.command.brigadier.argument.resolvers.PlayerSelectorArgumentResolver;
import com.mojang.brigadier.Command;
import com.mojang.brigadier.arguments.StringArgumentType;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;

// In LifecycleEvents.COMMANDS handler
Commands commands = event.registrar();

// Simple command with permission check
commands.register(
    Commands.literal("heal")
        .requires(source -> source.getSender().hasPermission("myplugin.heal"))
        .executes(ctx -> {
            if (!(ctx.getSource().getExecutor() instanceof Player player)) {
                ctx.getSource().getSender().sendMessage(
                    Component.text("Players only!", NamedTextColor.RED)
                );
                return 0;
            }
            player.setHealth(player.getMaxHealth());
            player.sendMessage(Component.text("Healed!", NamedTextColor.GREEN));
            return Command.SINGLE_SUCCESS;
        })
        .build(),
    "Restore your health"
);

// Command with arguments and sub-commands
commands.register(
    Commands.literal("give")
        .requires(source -> source.getSender().hasPermission("myplugin.give"))
        .then(Commands.argument("player", ArgumentTypes.player())
            .then(Commands.argument("amount", IntegerArgumentType.integer(1, 64))
                .executes(ctx -> {
                    Player target = ctx.getArgument("player", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    int amount = ctx.getArgument("amount", Integer.class);
                    
                    // Give items logic
                    target.sendMessage(Component.text(
                        "Received " + amount + " items",
                        NamedTextColor.GREEN
                    ));
                    return Command.SINGLE_SUCCESS;
                })
            )
        )
        .build(),
    "Give items to a player",
    List.of("item") // Aliases
);

// Command with custom suggestions (tab completion)
commands.register(
    Commands.literal("warp")
        .then(Commands.argument("name", StringArgumentType.word())
            .suggests((ctx, builder) -> {
                // Custom tab completion
                for (String warpName : warpManager.getWarps()) {
                    builder.suggest(warpName);
                }
                return builder.buildFuture();
            })
            .executes(ctx -> {
                String warpName = ctx.getArgument("name", String.class);
                // Teleport to warp
                return Command.SINGLE_SUCCESS;
            })
        )
        .build()
);

// For complete command API guide, see command-api-guide.md
```

### Database Access (Async)

```java
import java.util.concurrent.CompletableFuture;

public CompletableFuture<UserData> loadUserAsync(UUID uuid) {
    return CompletableFuture.supplyAsync(() -> {
        // Database query here (blocking I/O)
        return database.getUser(uuid);
    }, Bukkit.getAsyncScheduler().executor(plugin));
}

// Usage:
loadUserAsync(player.getUniqueId()).thenAccept(userData -> {
    // Back on main thread - safe to use Bukkit API
    Bukkit.getScheduler().runTask(plugin, () -> {
        player.sendMessage(Component.text("Loaded: " + userData));
    });
});
```

## Reference Documentation

For detailed information on specific topics:

- **[paper-api-patterns.md](references/paper-api-patterns.md)** - Common API patterns, anti-patterns to avoid, and best practices
- **[adventure-examples.md](references/adventure-examples.md)** - Comprehensive Adventure API examples: text components, audiences, serializers, titles, boss bars, sounds, books
- **[minimessage-guide.md](references/minimessage-guide.md)** - Complete MiniMessage syntax including all tags (colors, gradients, rainbow, pride, click/hover, sprites, heads, NBT), placeholders, and advanced patterns
- **[command-api-guide.md](references/command-api-guide.md)** - Complete Brigadier command system guide with arguments, permissions, tab completion
- **[configuration-guide.md](references/configuration-guide.md)** - Server configuration, performance tuning, and plugin configs
- **[plugin-dependencies.md](references/plugin-dependencies.md)** - Maven dependencies, shading, relocation, and dependency management
- **[debugging-troubleshooting.md](references/debugging-troubleshooting.md)** - Debugging techniques, reading logs, solving common errors

## Anti-Patterns to Avoid

**NEVER use these legacy APIs:**

- ❌ `ChatColor` → ✅ Use Adventure `NamedTextColor` or `TextColor`
- ❌ `player.sendMessage(String)` → ✅ Use `player.sendMessage(Component)`
- ❌ Legacy `&` color codes in code → ✅ Use MiniMessage format in configs
- ❌ `Placeholder.parsed()` with user input → ✅ Use `Placeholder.unparsed()` for safety
- ❌ Creating new `MiniMessage.miniMessage()` each call → ✅ Reuse static instance
- ❌ `Bukkit.getScheduler().runTaskAsynchronously()` for Bukkit API calls → ✅ Use region schedulers
- ❌ `BukkitRunnable` → ✅ Use Paper's scheduler APIs
- ❌ `event.setMessage(String)` → ✅ Use `event.message(Component)` when available
- ❌ Reflection for NMS access → ✅ Use Paper API or request feature addition
- ❌ Legacy command API in plugin.yml only → ✅ Use modern Brigadier API via LifecycleEvents.COMMANDS
- ❌ Manual string parsing for command arguments → ✅ Use Brigadier argument types
- ❌ No tab completion → ✅ Implement suggestions for better UX

**Thread Safety:**
- Never access Bukkit API from async threads
- Use region schedulers for entity/chunk operations (Folia)
- Use async scheduler only for I/O, network, database operations

**Command Best Practices:**
- Always validate permissions with `.requires()`
- Provide clear error messages for invalid input
- Use appropriate argument types (ArgumentTypes.player() for players, not strings)
- Implement tab completion for better user experience
- Return Command.SINGLE_SUCCESS (1) on success, 0 on failure
- Handle edge cases (player offline, insufficient permissions, invalid arguments)

## Version Requirements

- **Java**: 21+ (for Paper 1.17.1+)
- **Paper**: Latest stable version
- **Adventure**: Bundled with Paper (natively supported)

## Plugin Structure

```
MyPlugin/
├── pom.xml
├── src/
│   └── main/
│       ├── java/
│       │   └── com/example/myplugin/
│       │       ├── MyPlugin.java (main class)
│       │       ├── commands/
│       │       ├── listeners/
│       │       └── config/
│       └── resources/
│           ├── paper-plugin.yml (or plugin.yml for legacy)
│           └── config.yml
└── target/ (compiled output)
```

## Testing

1. Build with Maven: `mvn clean package`
2. Copy JAR from `target/` to server's `plugins/` folder
3. Start/restart server
4. Check `logs/latest.log` for errors
5. Use `/plugins` command to verify loading

## Debugging and Troubleshooting

### Common Issues

**Plugin not loading:**
- Check paper-plugin.yml syntax (valid YAML, correct main path)
- Verify Java version compatibility (need Java 21+)
- Check dependencies in paper-plugin.yml match installed plugins
- Look for errors in `logs/latest.log`

**NoSuchMethodError/NoClassDefFoundError:**
- Ensure dependencies are shaded with correct relocation
- Don't relocate Paper/Adventure APIs (already provided)
- Check dependency tree: `mvn dependency:tree`
- See plugin-dependencies.md for shading guide

**NullPointerException:**
- Always null-check before accessing objects
- Use Optional for nullable values
- Check if players are online before accessing

**Async errors:**
- Never call Bukkit API from async threads
- Use region schedulers for entity/chunk operations
- Only use async scheduler for I/O operations

**Events not firing:**
- Ensure listener is registered in onEnable()
- Check @EventHandler annotation is present
- Verify event priority and ignoreCancelled settings
- Make sure method signature matches event type

**For detailed debugging guide, see debugging-troubleshooting.md**
