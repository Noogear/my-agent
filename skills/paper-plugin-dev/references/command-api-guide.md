# Command API Guide

Complete guide to implementing commands in Paper plugins using modern Brigadier-based API.

## Table of Contents

1. [Command Registration](#command-registration)
2. [Brigadier Basics](#brigadier-basics)
3. [Argument Types](#argument-types)
4. [Command Permissions](#command-permissions)
5. [Sub-commands](#sub-commands)
6. [Tab Completion](#tab-completion)
7. [Error Handling](#error-handling)
8. [Command Feedback](#command-feedback)
9. [Best Practices](#best-practices)

---

## Command Registration

### Modern Lifecycle API (Recommended)

Paper's modern API uses lifecycle events for command registration:

```java
import io.papermc.paper.command.brigadier.Commands;
import io.papermc.paper.plugin.lifecycle.event.types.LifecycleEvents;

public class MyPlugin extends JavaPlugin {
    
    @Override
    public void onEnable() {
        // Register commands through lifecycle events
        this.getLifecycleManager().registerEventHandler(
            LifecycleEvents.COMMANDS,
            event -> {
                final Commands commands = event.registrar();
                registerMyCommands(commands);
            }
        );
    }
    
    private void registerMyCommands(Commands commands) {
        // Register your commands here
        commands.register(
            Commands.literal("mycommand")
                .executes(ctx -> {
                    ctx.getSource().getSender().sendPlainMessage("Command executed!");
                    return 1; // Return 1 for success, 0 for failure
                })
                .build(),
            "Command description",
            List.of("alias1", "alias2") // Optional aliases
        );
    }
}
```

### Legacy Command API (Still Supported)

For backward compatibility, you can still use the traditional command API:

```java
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;

public class LegacyCommand implements CommandExecutor {
    
    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (args.length == 0) {
            sender.sendMessage(Component.text("Usage: /mycommand <arg>"));
            return true;
        }
        
        // Command logic
        return true; // Return false to show usage from plugin.yml
    }
}

// Register in onEnable():
getCommand("mycommand").setExecutor(new LegacyCommand());
```

**⚠️ Note:** Legacy API requires defining commands in `paper-plugin.yml` or `plugin.yml`.

---

## Brigadier Basics

Brigadier is Minecraft's command framework. Paper exposes it for plugin developers.

### Command Structure

Commands are built using a fluent API:

```java
Commands.literal("commandname")          // Root literal node
    .requires(source -> /* permission */) // Permission check
    .then(Commands.argument(/* ... */))   // Add arguments
    .executes(ctx -> /* logic */)         // Execution logic
    .build();
```

### Execution Context

The `CommandContext<CommandSourceStack>` provides access to:

```java
commands.register(
    Commands.literal("info")
        .executes(ctx -> {
            // Get the command sender
            CommandSender sender = ctx.getSource().getSender();
            
            // Get the executing location
            Location location = ctx.getSource().getLocation();
            
            // Get the executor (if player)
            if (ctx.getSource().getExecutor() instanceof Player player) {
                player.sendMessage(Component.text("You executed this!"));
            }
            
            // Get the server
            Server server = ctx.getSource().getServer();
            
            return Command.SINGLE_SUCCESS;
        })
        .build()
);
```

### Return Values

- `Command.SINGLE_SUCCESS` (1) - Command executed successfully
- `0` - Command failed
- Custom values can be used for command blocks

---

## Argument Types

### String Arguments

```java
import com.mojang.brigadier.arguments.StringArgumentType;

// Single word (no spaces)
Commands.argument("name", StringArgumentType.word())

// Quoted string (allows spaces if quoted)
Commands.argument("message", StringArgumentType.string())

// Greedy string (consumes all remaining input)
Commands.argument("reason", StringArgumentType.greedyString())

// Retrieving the value:
String name = ctx.getArgument("name", String.class);
```

### Integer Arguments

```java
import com.mojang.brigadier.arguments.IntegerArgumentType;

// Simple integer
Commands.argument("amount", IntegerArgumentType.integer())

// With range constraints
Commands.argument("amount", IntegerArgumentType.integer(1, 100)) // 1-100

// Retrieving:
int amount = ctx.getArgument("amount", Integer.class);
```

### Double/Float Arguments

```java
import com.mojang.brigadier.arguments.DoubleArgumentType;
import com.mojang.brigadier.arguments.FloatArgumentType;

Commands.argument("multiplier", DoubleArgumentType.doubleArg(0.0, 10.0))
Commands.argument("speed", FloatArgumentType.floatArg())

double multiplier = ctx.getArgument("multiplier", Double.class);
float speed = ctx.getArgument("speed", Float.class);
```

### Boolean Arguments

```java
import com.mojang.brigadier.arguments.BoolArgumentType;

Commands.argument("enabled", BoolArgumentType.bool())

boolean enabled = ctx.getArgument("enabled", Boolean.class);
```

### Game-Specific Arguments

Paper provides Minecraft-specific argument types:

```java
import io.papermc.paper.command.brigadier.argument.ArgumentTypes;

// Player selector
Commands.argument("player", ArgumentTypes.player())
    .executes(ctx -> {
        Player player = ctx.getArgument("player", PlayerSelectorArgumentResolver.class)
            .resolve(ctx.getSource())
            .get(0);
        // Use player
        return Command.SINGLE_SUCCESS;
    })

// Players (multiple)
Commands.argument("players", ArgumentTypes.players())
    .executes(ctx -> {
        List<Player> players = ctx.getArgument("players", PlayerSelectorArgumentResolver.class)
            .resolve(ctx.getSource());
        // Use players
        return Command.SINGLE_SUCCESS;
    })

// Entity selector
Commands.argument("entity", ArgumentTypes.entity())

// Multiple entities
Commands.argument("entities", ArgumentTypes.entities())

// Block position
Commands.argument("pos", ArgumentTypes.blockPosition())
    .executes(ctx -> {
        BlockPosition pos = ctx.getArgument("pos", PositionResolver.class)
            .resolve(ctx.getSource());
        Location loc = pos.toLocation(ctx.getSource().getLocation().getWorld());
        return Command.SINGLE_SUCCESS;
    })

// World/dimension
Commands.argument("world", ArgumentTypes.dimension())

// Resource location (namespaced key)
Commands.argument("key", ArgumentTypes.resource())

// Component (text)
Commands.argument("message", ArgumentTypes.component())
```

### Custom Argument Types

Create custom argument types for validation:

```java
import com.mojang.brigadier.arguments.ArgumentType;
import com.mojang.brigadier.StringReader;
import com.mojang.brigadier.context.CommandContext;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.mojang.brigadier.exceptions.SimpleCommandExceptionType;
import com.mojang.brigadier.suggestion.Suggestions;
import com.mojang.brigadier.suggestion.SuggestionsBuilder;

public class ColorArgumentType implements ArgumentType<NamedTextColor> {
    
    private static final SimpleCommandExceptionType INVALID_COLOR = 
        new SimpleCommandExceptionType(Component.text("Invalid color"));
    
    @Override
    public NamedTextColor parse(StringReader reader) throws CommandSyntaxException {
        String input = reader.readUnquotedString();
        NamedTextColor color = NamedTextColor.NAMES.value(input);
        
        if (color == null) {
            throw INVALID_COLOR.createWithContext(reader);
        }
        
        return color;
    }
    
    @Override
    public <S> CompletableFuture<Suggestions> listSuggestions(
            CommandContext<S> context, 
            SuggestionsBuilder builder) {
        // Provide tab completion
        for (String name : NamedTextColor.NAMES.keys()) {
            builder.suggest(name);
        }
        return builder.buildFuture();
    }
    
    public static ColorArgumentType color() {
        return new ColorArgumentType();
    }
}

// Usage:
Commands.argument("color", ColorArgumentType.color())
    .executes(ctx -> {
        NamedTextColor color = ctx.getArgument("color", NamedTextColor.class);
        return Command.SINGLE_SUCCESS;
    })
```

---

## Command Permissions

### Basic Permission Check

```java
Commands.literal("admin")
    .requires(source -> source.getSender().hasPermission("myplugin.admin"))
    .executes(ctx -> {
        // Only executes if permission check passes
        return Command.SINGLE_SUCCESS;
    })
```

### Permission Levels

```java
Commands.literal("op")
    .requires(source -> source.getSender().isOp())
    .executes(ctx -> {
        return Command.SINGLE_SUCCESS;
    })
```

### Multiple Permission Checks

```java
Commands.literal("command")
    .requires(source -> 
        source.getSender().hasPermission("myplugin.command.use") &&
        source.getSender().hasPermission("myplugin.command.special")
    )
    .executes(ctx -> {
        return Command.SINGLE_SUCCESS;
    })
```

### Per-Subcommand Permissions

```java
Commands.literal("manage")
    .then(Commands.literal("create")
        .requires(source -> source.getSender().hasPermission("myplugin.manage.create"))
        .executes(ctx -> {
            // Create logic
            return Command.SINGLE_SUCCESS;
        })
    )
    .then(Commands.literal("delete")
        .requires(source -> source.getSender().hasPermission("myplugin.manage.delete"))
        .executes(ctx -> {
            // Delete logic
            return Command.SINGLE_SUCCESS;
        })
    )
```

---

## Sub-commands

### Flat Sub-commands

```java
Commands.literal("config")
    .then(Commands.literal("reload")
        .executes(ctx -> {
            // Reload config
            ctx.getSource().getSender().sendMessage(
                Component.text("Config reloaded!", NamedTextColor.GREEN)
            );
            return Command.SINGLE_SUCCESS;
        })
    )
    .then(Commands.literal("save")
        .executes(ctx -> {
            // Save config
            return Command.SINGLE_SUCCESS;
        })
    )
```

### Nested Sub-commands with Arguments

```java
Commands.literal("player")
    .then(Commands.literal("teleport")
        .then(Commands.argument("target", ArgumentTypes.player())
            .executes(ctx -> {
                // /player teleport <target>
                return Command.SINGLE_SUCCESS;
            })
            .then(Commands.argument("destination", ArgumentTypes.player())
                .executes(ctx -> {
                    // /player teleport <target> <destination>
                    Player target = ctx.getArgument("target", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    Player dest = ctx.getArgument("destination", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    
                    target.teleport(dest.getLocation());
                    return Command.SINGLE_SUCCESS;
                })
            )
        )
    )
    .then(Commands.literal("heal")
        .then(Commands.argument("target", ArgumentTypes.player())
            .executes(ctx -> {
                // /player heal <target>
                return Command.SINGLE_SUCCESS;
            })
        )
    )
```

### Dynamic Sub-commands

For commands based on runtime data:

```java
LiteralArgumentBuilder<CommandSourceStack> mainCommand = Commands.literal("warp");

// Add dynamic sub-commands based on available warps
for (String warpName : warpManager.getWarpNames()) {
    mainCommand.then(Commands.literal(warpName)
        .executes(ctx -> {
            // Teleport to warp
            Location warpLoc = warpManager.getWarp(warpName);
            if (ctx.getSource().getExecutor() instanceof Player player) {
                player.teleport(warpLoc);
            }
            return Command.SINGLE_SUCCESS;
        })
    );
}

commands.register(mainCommand.build());
```

---

## Tab Completion

### Automatic Completion

Brigadier provides automatic tab completion for:
- Literal nodes (sub-commands)
- Registered argument types
- Custom argument types with `listSuggestions()` implemented

### Custom Suggestions

```java
Commands.argument("player", StringArgumentType.word())
    .suggests((ctx, builder) -> {
        // Suggest online player names
        for (Player player : Bukkit.getOnlinePlayers()) {
            builder.suggest(player.getName());
        }
        return builder.buildFuture();
    })
    .executes(ctx -> {
        String playerName = ctx.getArgument("player", String.class);
        return Command.SINGLE_SUCCESS;
    })
```

### Filtered Suggestions

```java
Commands.argument("warp", StringArgumentType.word())
    .suggests((ctx, builder) -> {
        String input = builder.getRemaining().toLowerCase();
        
        for (String warp : warpManager.getWarpNames()) {
            if (warp.toLowerCase().startsWith(input)) {
                builder.suggest(warp);
            }
        }
        
        return builder.buildFuture();
    })
```

### Suggestions with Tooltips

```java
Commands.argument("item", StringArgumentType.word())
    .suggests((ctx, builder) -> {
        builder.suggest("diamond_sword", Component.text("A powerful weapon"));
        builder.suggest("golden_apple", Component.text("Restores health"));
        builder.suggest("ender_pearl", Component.text("Teleportation item"));
        return builder.buildFuture();
    })
```

### Context-Aware Suggestions

```java
Commands.literal("permission")
    .then(Commands.literal("grant")
        .then(Commands.argument("player", ArgumentTypes.player())
            .then(Commands.argument("permission", StringArgumentType.word())
                .suggests((ctx, builder) -> {
                    // Get the player from context
                    Player player = ctx.getArgument("player", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    
                    // Suggest permissions the player doesn't have
                    for (String perm : getAllPermissions()) {
                        if (!player.hasPermission(perm)) {
                            builder.suggest(perm);
                        }
                    }
                    
                    return builder.buildFuture();
                })
                .executes(ctx -> {
                    // Grant permission
                    return Command.SINGLE_SUCCESS;
                })
            )
        )
    )
```

---

## Error Handling

### Built-in Exceptions

```java
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import static com.mojang.brigadier.arguments.IntegerArgumentType.integer;

Commands.literal("setlevel")
    .then(Commands.argument("level", integer(1, 100))
        .executes(ctx -> {
            int level = ctx.getArgument("level", Integer.class);
            // Brigadier automatically validates range (1-100)
            // Invalid input throws CommandSyntaxException automatically
            return Command.SINGLE_SUCCESS;
        })
    )
```

### Custom Exceptions

```java
import com.mojang.brigadier.exceptions.SimpleCommandExceptionType;
import com.mojang.brigadier.exceptions.DynamicCommandExceptionType;

public class MyCommands {
    
    // Static error message
    private static final SimpleCommandExceptionType PLAYER_ONLY = 
        new SimpleCommandExceptionType(Component.text("This command is for players only!"));
    
    // Dynamic error message
    private static final DynamicCommandExceptionType PLAYER_NOT_FOUND = 
        new DynamicCommandExceptionType(name -> 
            Component.text("Player " + name + " not found!"));
    
    public void register(Commands commands) {
        commands.register(
            Commands.literal("heal")
                .executes(ctx -> {
                    // Check if sender is a player
                    if (!(ctx.getSource().getExecutor() instanceof Player player)) {
                        throw PLAYER_ONLY.create();
                    }
                    
                    player.setHealth(player.getMaxHealth());
                    player.sendMessage(Component.text("Healed!", NamedTextColor.GREEN));
                    return Command.SINGLE_SUCCESS;
                })
                .then(Commands.argument("target", StringArgumentType.word())
                    .executes(ctx -> {
                        String targetName = ctx.getArgument("target", String.class);
                        Player target = Bukkit.getPlayer(targetName);
                        
                        if (target == null) {
                            throw PLAYER_NOT_FOUND.create(targetName);
                        }
                        
                        target.setHealth(target.getMaxHealth());
                        return Command.SINGLE_SUCCESS;
                    })
                )
                .build()
        );
    }
}
```

### Try-Catch in Execution

```java
Commands.literal("dangerous")
    .executes(ctx -> {
        try {
            // Risky operation
            performDangerousOperation();
            ctx.getSource().getSender().sendMessage(
                Component.text("Success!", NamedTextColor.GREEN)
            );
            return Command.SINGLE_SUCCESS;
        } catch (Exception e) {
            ctx.getSource().getSender().sendMessage(
                Component.text("Error: " + e.getMessage(), NamedTextColor.RED)
            );
            return 0; // Failure
        }
    })
```

---

## Command Feedback

### Sending Messages

```java
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;

Commands.literal("hello")
    .executes(ctx -> {
        CommandSender sender = ctx.getSource().getSender();
        
        // Simple message
        sender.sendMessage(Component.text("Hello!", NamedTextColor.GREEN));
        
        // Formatted message
        Component message = Component.text()
            .append(Component.text("Hello, ", NamedTextColor.GRAY))
            .append(Component.text(sender.getName(), NamedTextColor.YELLOW))
            .append(Component.text("!", NamedTextColor.GRAY))
            .build();
        sender.sendMessage(message);
        
        return Command.SINGLE_SUCCESS;
    })
```

### Action Bar Messages

```java
Commands.literal("actionbar")
    .executes(ctx -> {
        if (ctx.getSource().getExecutor() instanceof Player player) {
            player.sendActionBar(
                Component.text("Action bar message!", NamedTextColor.GOLD)
            );
        }
        return Command.SINGLE_SUCCESS;
    })
```

### Title Messages

```java
import net.kyori.adventure.title.Title;
import java.time.Duration;

Commands.literal("welcometitle")
    .executes(ctx -> {
        if (ctx.getSource().getExecutor() instanceof Player player) {
            Title title = Title.title(
                Component.text("Welcome!", NamedTextColor.GOLD),
                Component.text("Enjoy your stay", NamedTextColor.GRAY),
                Title.Times.times(
                    Duration.ofMillis(500),  // Fade in
                    Duration.ofSeconds(3),   // Stay
                    Duration.ofMillis(1000)  // Fade out
                )
            );
            player.showTitle(title);
        }
        return Command.SINGLE_SUCCESS;
    })
```

### Sound Effects

```java
import org.bukkit.Sound;

Commands.literal("ding")
    .executes(ctx -> {
        if (ctx.getSource().getExecutor() instanceof Player player) {
            player.playSound(
                player.getLocation(),
                Sound.ENTITY_EXPERIENCE_ORB_PICKUP,
                1.0f,  // Volume
                1.0f   // Pitch
            );
        }
        return Command.SINGLE_SUCCESS;
    })
```

### Broadcasting

```java
Commands.literal("announce")
    .requires(source -> source.getSender().hasPermission("myplugin.announce"))
    .then(Commands.argument("message", StringArgumentType.greedyString())
        .executes(ctx -> {
            String message = ctx.getArgument("message", String.class);
            
            Component announcement = Component.text()
                .append(Component.text("[Announcement] ", NamedTextColor.GOLD, TextDecoration.BOLD))
                .append(Component.text(message, NamedTextColor.YELLOW))
                .build();
            
            // Broadcast to all players
            Bukkit.broadcast(announcement);
            
            return Command.SINGLE_SUCCESS;
        })
    )
```

---

## Best Practices

### 1. Validate Input

Always validate user input, even with argument types:

```java
Commands.literal("pay")
    .then(Commands.argument("player", ArgumentTypes.player())
        .then(Commands.argument("amount", IntegerArgumentType.integer(1))
            .executes(ctx -> {
                Player sender = (Player) ctx.getSource().getExecutor();
                Player target = ctx.getArgument("player", PlayerSelectorArgumentResolver.class)
                    .resolve(ctx.getSource()).get(0);
                int amount = ctx.getArgument("amount", Integer.class);
                
                // Validate sender has enough money
                if (economy.getBalance(sender) < amount) {
                    sender.sendMessage(Component.text(
                        "Insufficient funds!", NamedTextColor.RED
                    ));
                    return 0;
                }
                
                // Validate target isn't sender
                if (target.equals(sender)) {
                    sender.sendMessage(Component.text(
                        "You can't pay yourself!", NamedTextColor.RED
                    ));
                    return 0;
                }
                
                // Process payment
                economy.withdraw(sender, amount);
                economy.deposit(target, amount);
                
                return Command.SINGLE_SUCCESS;
            })
        )
    )
```

### 2. Provide Clear Feedback

Always inform users about success, failure, and errors:

```java
Commands.literal("warp")
    .then(Commands.argument("name", StringArgumentType.word())
        .executes(ctx -> {
            Player player = (Player) ctx.getSource().getExecutor();
            String warpName = ctx.getArgument("name", String.class);
            
            Warp warp = warpManager.getWarp(warpName);
            
            if (warp == null) {
                player.sendMessage(Component.text(
                    "Warp '" + warpName + "' not found!", 
                    NamedTextColor.RED
                ));
                return 0;
            }
            
            player.teleport(warp.getLocation());
            player.sendMessage(Component.text(
                "Teleported to " + warpName, 
                NamedTextColor.GREEN
            ));
            
            // Sound feedback
            player.playSound(player.getLocation(), Sound.ENTITY_ENDERMAN_TELEPORT, 1.0f, 1.0f);
            
            return Command.SINGLE_SUCCESS;
        })
    )
```

### 3. Use Permission Nodes Hierarchically

```yaml
# In paper-plugin.yml
permissions:
  myplugin.command:
    description: Base permission for all commands
    default: true
  myplugin.command.admin:
    description: Admin commands
    default: op
    children:
      myplugin.command.reload: true
      myplugin.command.debug: true
  myplugin.command.reload:
    description: Reload plugin configuration
    default: op
```

### 4. Handle Async Operations Properly

```java
Commands.literal("lookup")
    .then(Commands.argument("username", StringArgumentType.word())
        .executes(ctx -> {
            String username = ctx.getArgument("username", String.class);
            CommandSender sender = ctx.getSource().getSender();
            
            // Send immediate feedback
            sender.sendMessage(Component.text(
                "Looking up " + username + "...", 
                NamedTextColor.GRAY
            ));
            
            // Perform async lookup
            CompletableFuture.supplyAsync(() -> {
                return databaseManager.lookupPlayer(username);
            }, Bukkit.getAsyncScheduler().executor(plugin))
            .thenAcceptAsync(result -> {
                if (result == null) {
                    sender.sendMessage(Component.text(
                        "Player not found!", 
                        NamedTextColor.RED
                    ));
                } else {
                    sender.sendMessage(Component.text(
                        "Found: " + result.getDisplayName(), 
                        NamedTextColor.GREEN
                    ));
                }
            }, ctx.getSource().getServer().getScheduler().mainThreadExecutor(plugin));
            
            return Command.SINGLE_SUCCESS;
        })
    )
```

### 5. Keep Command Classes Organized

Structure your commands logically:

```
commands/
├── CommandManager.java          // Central registration
├── admin/
│   ├── ReloadCommand.java
│   ├── DebugCommand.java
│   └── MaintenanceCommand.java
├── player/
│   ├── WarpCommand.java
│   ├── HomeCommand.java
│   └── TeleportCommand.java
└── economy/
    ├── PayCommand.java
    ├── BalanceCommand.java
    └── ShopCommand.java
```

### 6. Document Commands

Provide descriptions and examples:

```java
commands.register(
    Commands.literal("warp")
        .then(Commands.argument("name", StringArgumentType.word())
            .suggests((ctx, builder) -> {
                // Show available warps as suggestions
                for (String warp : warpManager.getWarpNames()) {
                    builder.suggest(warp, Component.text("Warp to " + warp));
                }
                return builder.buildFuture();
            })
            .executes(ctx -> {
                // Command logic
                return Command.SINGLE_SUCCESS;
            })
        )
        .build(),
    "Teleport to a warp location",  // Description shown in /help
    List.of("tp", "teleport")       // Aliases
);
```

### 7. Handle Edge Cases

```java
Commands.literal("give")
    .then(Commands.argument("player", ArgumentTypes.player())
        .then(Commands.argument("item", StringArgumentType.word())
            .then(Commands.argument("amount", IntegerArgumentType.integer(1, 64))
                .executes(ctx -> {
                    Player target = ctx.getArgument("player", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    String itemName = ctx.getArgument("item", String.class);
                    int amount = ctx.getArgument("amount", Integer.class);
                    
                    // Validate item exists
                    Material material = Material.matchMaterial(itemName);
                    if (material == null || !material.isItem()) {
                        ctx.getSource().getSender().sendMessage(Component.text(
                            "Invalid item: " + itemName, NamedTextColor.RED
                        ));
                        return 0;
                    }
                    
                    // Check inventory space
                    ItemStack item = new ItemStack(material, amount);
                    if (target.getInventory().firstEmpty() == -1) {
                        ctx.getSource().getSender().sendMessage(Component.text(
                            target.getName() + "'s inventory is full!", 
                            NamedTextColor.RED
                        ));
                        return 0;
                    }
                    
                    // Give item
                    target.getInventory().addItem(item);
                    target.sendMessage(Component.text(
                        "Received " + amount + "x " + itemName, 
                        NamedTextColor.GREEN
                    ));
                    
                    return Command.SINGLE_SUCCESS;
                })
            )
        )
    )
```

---

## Complete Example

Here's a complete command implementation with all best practices:

```java
package com.example.myplugin.commands;

import com.mojang.brigadier.Command;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.arguments.StringArgumentType;
import com.mojang.brigadier.tree.LiteralCommandNode;
import io.papermc.paper.command.brigadier.CommandSourceStack;
import io.papermc.paper.command.brigadier.Commands;
import io.papermc.paper.command.brigadier.argument.ArgumentTypes;
import io.papermc.paper.command.brigadier.argument.resolvers.PlayerSelectorArgumentResolver;
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.Sound;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;

public class TeleportCommands {
    
    private final JavaPlugin plugin;
    
    public TeleportCommands(JavaPlugin plugin) {
        this.plugin = plugin;
    }
    
    public void register(Commands commands) {
        LiteralCommandNode<CommandSourceStack> tpCommand = Commands.literal("tp")
            .requires(source -> source.getSender().hasPermission("myplugin.tp"))
            // /tp <player>
            .then(Commands.argument("target", ArgumentTypes.player())
                .executes(ctx -> {
                    if (!(ctx.getSource().getExecutor() instanceof Player player)) {
                        ctx.getSource().getSender().sendMessage(
                            Component.text("Only players can use this command!", NamedTextColor.RED)
                        );
                        return 0;
                    }
                    
                    Player target = ctx.getArgument("target", PlayerSelectorArgumentResolver.class)
                        .resolve(ctx.getSource()).get(0);
                    
                    if (target.equals(player)) {
                        player.sendMessage(Component.text(
                            "You can't teleport to yourself!", NamedTextColor.RED
                        ));
                        return 0;
                    }
                    
                    player.teleport(target.getLocation());
                    player.sendMessage(Component.text(
                        "Teleported to " + target.getName(), NamedTextColor.GREEN
                    ));
                    player.playSound(player.getLocation(), Sound.ENTITY_ENDERMAN_TELEPORT, 1.0f, 1.0f);
                    
                    return Command.SINGLE_SUCCESS;
                })
                // /tp <player> <destination>
                .then(Commands.argument("destination", ArgumentTypes.player())
                    .requires(source -> source.getSender().hasPermission("myplugin.tp.others"))
                    .executes(ctx -> {
                        Player target = ctx.getArgument("target", PlayerSelectorArgumentResolver.class)
                            .resolve(ctx.getSource()).get(0);
                        Player destination = ctx.getArgument("destination", PlayerSelectorArgumentResolver.class)
                            .resolve(ctx.getSource()).get(0);
                        
                        target.teleport(destination.getLocation());
                        
                        ctx.getSource().getSender().sendMessage(Component.text(
                            "Teleported " + target.getName() + " to " + destination.getName(),
                            NamedTextColor.GREEN
                        ));
                        target.sendMessage(Component.text(
                            "You were teleported to " + destination.getName(),
                            NamedTextColor.GREEN
                        ));
                        
                        return Command.SINGLE_SUCCESS;
                    })
                )
            )
            .build();
        
        commands.register(
            tpCommand,
            "Teleport to another player",
            List.of("teleport")
        );
    }
}
```

---

## Migration from Legacy API

If you're migrating from the old command API:

**Before (Legacy):**
```java
public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
    if (args.length == 0) {
        sender.sendMessage("Usage: /heal [player]");
        return true;
    }
    // ...
}
```

**After (Brigadier):**
```java
Commands.literal("heal")
    .executes(ctx -> {
        // /heal (self)
        return Command.SINGLE_SUCCESS;
    })
    .then(Commands.argument("player", ArgumentTypes.player())
        .executes(ctx -> {
            // /heal <player>
            return Command.SINGLE_SUCCESS;
        })
    )
```

**Benefits:**
- Automatic tab completion
- Better error handling
- More robust argument parsing
- Type-safe arguments
- Better permission integration
- Client-side validation

---

## Additional Resources

- **Brigadier GitHub**: <https://github.com/Mojang/brigadier>
- **Paper API Docs**: <https://jd.papermc.io/paper/1.21/>
- **Command Examples**: See `adventure-examples.md` for more message formatting
- **Permission Plugins**: LuckPerms for advanced permission management
