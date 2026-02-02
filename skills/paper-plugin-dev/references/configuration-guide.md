# Configuration Guide

Complete guide to Paper server and plugin configuration.

## Table of Contents

- [Server Configuration Files](#server-configuration-files)
- [Plugin Configuration](#plugin-configuration)
- [Performance Tuning](#performance-tuning)
- [World Configuration](#world-configuration)

## Server Configuration Files

### paper-global.yml

Global server configuration affecting all worlds:

```yaml
# Anti-cheat settings
anticheat:
  anti-xray:
    enabled: true
    engine-mode: 2
    max-block-height: 64
    update-radius: 2
    lava-obscures: false
    use-permission: false
    
# Performance
chunk-loading:
  autoconfig-send-distance: true
  enable-frustum-priority: true
  global-max-chunk-load-rate: 300.0
  global-max-chunk-send-rate: 75.0
  max-concurrent-sends: 2
  
# Misc
misc:
  chat-threads:
    chat-executor-core-size: 2
    chat-executor-max-size: 2
```

### paper-world-defaults.yml

Default settings for all worlds (can be overridden per-world):

```yaml
# Entities
entities:
  spawning:
    all-chunks-are-slime-chunks: false
    alt-item-despawn-rate:
      enabled: true
      items:
        cobblestone: 300
        netherrack: 300
    despawn-ranges:
      ambient:
        hard: 128
        soft: 32
      monster:
        hard: 128
        soft: 32
        
  behavior:
    baby-zombie-movement-modifier: 0.5
    disable-chest-cat-detection: false
    
# Environment
environment:
  disable-explosion-knockback: false
  treasure-maps:
    enabled: true
    find-already-discovered:
      loot-tables: false
      villager-trade: false
      
# Hopper optimization
hopper:
  cooldown-when-full: true
  disable-move-event: false
  ignore-occluding-blocks: false
  
# Tick rates
tick-rates:
  behavior:
    villager:
      validatenearbypoi: 60
  sensor:
    villager:
      secondarypoisensor: 120
```

### spigot.yml

Spigot configuration (still used by Paper):

```yaml
settings:
  debug: false
  timeout-time: 60
  restart-on-crash: false
  
world-settings:
  default:
    # Mob spawn ranges
    mob-spawn-range: 6
    
    # View distance
    view-distance: default
    
    # Entity tracking ranges
    entity-tracking-range:
      players: 48
      animals: 48
      monsters: 48
      misc: 32
      other: 64
      
    # Tick range
    entity-activation-range:
      animals: 32
      monsters: 32
      raiders: 48
      misc: 16
      water: 16
      villagers: 32
      flying-monsters: 32
      
    # Hopper settings
    hopper-transfer: 8
    hopper-check: 1
    hopper-amount: 1
```

### bukkit.yml

Core Bukkit settings:

```yaml
settings:
  allow-end: true
  warn-on-overload: true
  permissions-file: permissions.yml
  update-folder: update
  shutdown-message: Server closed
  
spawn-limits:
  monsters: 70
  animals: 10
  water-animals: 5
  water-ambient: 20
  water-underground-creature: 5
  axolotls: 5
  ambient: 15
  
chunk-gc:
  period-in-ticks: 600
  
ticks-per:
  animal-spawns: 400
  monster-spawns: 1
  water-spawns: 1
  water-ambient-spawns: 1
  water-underground-creature-spawns: 1
  axolotl-spawns: 1
  ambient-spawns: 1
```

## Plugin Configuration

### Basic plugin.yml

```yaml
name: MyPlugin
version: 1.0.0
main: com.example.myplugin.MyPlugin
api-version: '1.21'
description: Plugin description
author: YourName
website: https://example.com

# Load order
load: POSTWORLD # or STARTUP

# Dependencies
depend: [Vault]
softdepend: [PlaceholderAPI]
loadbefore: [AnotherPlugin]

# Permissions
permissions:
  myplugin.*:
    description: All permissions
    children:
      myplugin.use: true
      myplugin.admin: true
      
  myplugin.use:
    description: Basic permission
    default: true
    
  myplugin.admin:
    description: Admin permission
    default: op
    
# Commands
commands:
  mycommand:
    description: My command description
    usage: /<command> [args]
    permission: myplugin.use
    permission-message: You don't have permission!
    aliases: [mc, mycmd]
```

### Paper plugin.yml (New Format)

```yaml
name: MyPlugin
version: 1.0.0
main: com.example.myplugin.MyPlugin
api-version: '1.21'
description: Plugin description

# Folia support
folia-supported: true

# Bootstrap dependencies (loaded before plugin)
bootstrap-dependencies:
  - id: some-lib
    load: AFTER # or BEFORE

# Server dependencies (runtime)
dependencies:
  server:
    Vault:
      required: true
      load: BEFORE
    PlaceholderAPI:
      required: false
      load: AFTER
```

### config.yml Best Practices

```yaml
# Version for migration
config-version: 1

# Feature toggles
features:
  feature1:
    enabled: true
    setting1: value
  feature2:
    enabled: false
    
# Messages using MiniMessage
messages:
  prefix: "<gold>[MyPlugin]</gold> "
  welcome: "<prefix><green>Welcome <player>!</green>"
  error: "<prefix><red>Error: <message></red>"
  no-permission: "<prefix><red>You don't have permission!</red>"
  
# Numeric settings
settings:
  max-value: 100
  cooldown-seconds: 30
  radius: 10.5
  
# Lists
allowed-worlds:
  - world
  - world_nether
  - world_the_end
  
blocked-items:
  - BEDROCK
  - BARRIER
  - COMMAND_BLOCK
  
# Complex structures
rewards:
  daily:
    money: 100
    items:
      - type: DIAMOND
        amount: 5
      - type: EMERALD
        amount: 3
  weekly:
    money: 1000
    items:
      - type: NETHERITE_INGOT
        amount: 1
```

### Configuration Loading

```java
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.configuration.file.YamlConfiguration;

public class ConfigManager {
    private final JavaPlugin plugin;
    private FileConfiguration config;
    
    public ConfigManager(JavaPlugin plugin) {
        this.plugin = plugin;
        reload();
    }
    
    public void reload() {
        // Save default if doesn't exist
        plugin.saveDefaultConfig();
        plugin.reloadConfig();
        config = plugin.getConfig();
        
        // Migrate old configs
        if (!config.contains("config-version")) {
            migrateConfig();
        }
    }
    
    private void migrateConfig() {
        // Update config structure
        config.set("config-version", 1);
        plugin.saveConfig();
    }
    
    // Type-safe getters
    public boolean isFeatureEnabled(String feature) {
        return config.getBoolean("features." + feature + ".enabled", false);
    }
    
    public int getCooldown() {
        return config.getInt("settings.cooldown-seconds", 30);
    }
    
    public List<String> getAllowedWorlds() {
        return config.getStringList("allowed-worlds");
    }
}
```

## Performance Tuning

### Startup Flags (Aikar's Flags)

```bash
java -Xms10G -Xmx10G \
  -XX:+UseG1GC \
  -XX:+ParallelRefProcEnabled \
  -XX:MaxGCPauseMillis=200 \
  -XX:+UnlockExperimentalVMOptions \
  -XX:+DisableExplicitGC \
  -XX:+AlwaysPreTouch \
  -XX:G1NewSizePercent=30 \
  -XX:G1MaxNewSizePercent=40 \
  -XX:G1HeapRegionSize=8M \
  -XX:G1ReservePercent=20 \
  -XX:G1HeapWastePercent=5 \
  -XX:G1MixedGCCountTarget=4 \
  -XX:InitiatingHeapOccupancyPercent=15 \
  -XX:G1MixedGCLiveThresholdPercent=90 \
  -XX:G1RSetUpdatingPauseTimePercent=5 \
  -XX:SurvivorRatio=32 \
  -XX:+PerfDisableSharedMem \
  -XX:MaxTenuringThreshold=1 \
  -Dusing.aikars.flags=https://mcflags.emc.gs \
  -Daikars.new.flags=true \
  -jar paper.jar --nogui
```

### View Distance Optimization

```yaml
# spigot.yml
world-settings:
  default:
    view-distance: 6  # Reduce if laggy (default: server.properties value)
    simulation-distance: 8  # Paper 1.18+
```

### Entity Optimization

```yaml
# paper-world-defaults.yml
entities:
  spawning:
    despawn-ranges:
      monster:
        hard: 96
        soft: 32
  behavior:
    # Disable pathfinding through water
    disable-water-creature-pathfinding: true
```

### Chunk Loading

```yaml
# paper-global.yml
chunk-loading:
  max-concurrent-sends: 2
  global-max-chunk-load-rate: 300.0
  global-max-chunk-send-rate: 75.0
```

### Anti-Xray

```yaml
# paper-world-defaults.yml
anticheat:
  anti-xray:
    enabled: true
    engine-mode: 2  # Most effective
    max-block-height: 64
    hidden-blocks:
      - copper_ore
      - deepslate_copper_ore
      - gold_ore
      - deepslate_gold_ore
      - iron_ore
      - deepslate_iron_ore
      - coal_ore
      - deepslate_coal_ore
      - lapis_ore
      - deepslate_lapis_ore
      - mossy_cobblestone
      - obsidian
      - chest
      - diamond_ore
      - deepslate_diamond_ore
      - redstone_ore
      - deepslate_redstone_ore
      - clay
      - emerald_ore
      - deepslate_emerald_ore
      - ender_chest
    replacement-blocks:
      - stone
      - oak_planks
      - deepslate
```

## World Configuration

### Per-World Settings

Create `config/paper-world/world_name.yml` for world-specific config:

```yaml
# world_name.yml (e.g., world_nether.yml)
entities:
  spawning:
    despawn-ranges:
      monster:
        hard: 128
        soft: 64
        
environment:
  treasure-maps:
    enabled: false
```

### Server.properties

```properties
# Server basics
level-name=world
gamemode=survival
difficulty=normal
hardcore=false

# Network
server-port=25565
server-ip=
online-mode=true
max-players=100

# World generation
level-seed=
generate-structures=true
level-type=minecraft\:normal

# Performance
view-distance=10
simulation-distance=10
max-tick-time=60000
spawn-protection=16

# Misc
allow-nether=true
enable-command-block=false
pvp=true
spawn-animals=true
spawn-monsters=true
spawn-npcs=true
```

## Common Performance Issues

### High TPS Lag

1. Check entity counts: `/minecraft:kill @e[type=!player]`
2. Reduce view distance
3. Clear dropped items regularly
4. Limit entity spawners
5. Use Paper's entity activation ranges

### Memory Issues

1. Allocate appropriate RAM (6-10GB recommended)
2. Use Aikar's flags
3. Monitor heap usage
4. Clear unused chunks
5. Limit world borders

### Chunk Loading Lag

1. Reduce chunk load rate
2. Pre-generate world
3. Limit max chunk sends
4. Use concurrent loading

### Network Lag

1. Reduce view distance
2. Limit player count per chunk
3. Optimize entity tracking ranges
4. Use compression

## Monitoring

### Built-in Commands

```bash
# TPS and performance
/tps
/timings report

# Debug info
/debug start
/debug stop

# Chunk info
/paper heap
/paper entity list
```

### Timings Report

1. Run `/timings on`
2. Wait 10-15 minutes
3. Run `/timings paste`
4. Analyze report at timings.aikar.co

### Spark Profiler

Install Spark plugin for detailed profiling:

```bash
/spark profiler
/spark profiler --stop
```

## Migration

### From Vanilla

1. Stop vanilla server
2. Replace server JAR with Paper
3. Update startup script
4. Start server (auto-converts world format)

### From Spigot/CraftBukkit

1. Stop server
2. Replace JAR with Paper
3. No world conversion needed
4. Configuration files remain compatible
