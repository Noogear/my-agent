# Adventure API Examples

Comprehensive examples for using Adventure API in Paper plugins.

> **Note**: Adventure is bundled natively with Paper - no additional dependencies required!

## Table of Contents

- [Audiences](#audiences)
- [Text Components](#text-components)
- [Text Serializers](#text-serializers)
- [MiniMessage](#minimessage)
- [Titles and Subtitles](#titles-and-subtitles)
- [Action Bar](#action-bar)
- [Boss Bars](#boss-bars)
- [Sounds](#sounds)
- [Books](#books)
- [Signs](#signs)
- [Inventory](#inventory)
- [Common Patterns](#common-patterns)

## Audiences

An `Audience` is a universal interface for any entity that can receive text, titles, boss bars, sounds, and other content. This includes players, command senders, the console, or groups of receivers.

### Getting Audience Instances

```java
import net.kyori.adventure.audience.Audience;
import net.kyori.adventure.identity.Identity;

// Player as audience
Audience playerAudience = player;
playerAudience.sendMessage(Component.text("Hello!"));

// Console as audience
Audience console = Bukkit.getConsoleSender();

// All online players
Audience allPlayers = Audience.audience(Bukkit.getOnlinePlayers());

// Empty audience (does nothing)
Audience empty = Audience.empty();

// Forward to multiple audiences
Audience combined = Audience.audience(player1, player2, player3);
```

### Pointers (Audience Properties)

Audiences can provide arbitrary information via the pointer system:

```java
import net.kyori.adventure.identity.Identity;

// Get UUID from audience (returns Optional<UUID>)
Optional<UUID> uuid = audience.get(Identity.UUID);

// Get display name with default fallback
Component displayName = audience.getOrDefault(
    Identity.DISPLAY_NAME,
    Component.text("Unknown")
);

// Check if pointer exists
if (audience.get(Identity.UUID).isPresent()) {
    // Has UUID
}
```

## Text Components

### Basic Text

```java
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import net.kyori.adventure.text.format.TextColor;
import net.kyori.adventure.text.format.TextDecoration;

// Simple text
Component simple = Component.text("Hello World!");

// Colored text
Component colored = Component.text("Error!", NamedTextColor.RED);

// RGB colors
Component rgb = Component.text("Rainbow!", TextColor.color(0xFF00FF));

// With decorations
Component styled = Component.text("Bold and Italic", NamedTextColor.GOLD)
    .decorate(TextDecoration.BOLD)
    .decorate(TextDecoration.ITALIC);

// Remove decoration
Component noItalic = Component.text("Not italic")
    .decoration(TextDecoration.ITALIC, false);

// Apply decoration only if not already set (useful for lore)
Component safeLore = component.decorationIfAbsent(TextDecoration.ITALIC, TextDecoration.State.FALSE);
```

### Shadow Color (since 1.21.4)

```java
import net.kyori.adventure.text.format.ShadowColor;

// Apply custom shadow color
Component withShadow = Component.text("Hello!", NamedTextColor.WHITE)
    .shadowColor(ShadowColor.shadowColor(0x880000FF)); // Blue shadow with alpha

// Disable shadow
Component noShadow = Component.text("No shadow")
    .shadowColor(ShadowColor.none());

// Shadow color with hex
Component customShadow = Component.text("Custom")
    .shadowColor(ShadowColor.shadowColor(0xFF55FF55)); // Green shadow
```

### Building Complex Components

```java
// Using builder
Component complex = Component.text()
    .append(Component.text("[", NamedTextColor.GRAY))
    .append(Component.text("Admin", NamedTextColor.RED, TextDecoration.BOLD))
    .append(Component.text("] ", NamedTextColor.GRAY))
    .append(Component.text(player.getName(), NamedTextColor.YELLOW))
    .append(Component.text(": ", NamedTextColor.GRAY))
    .append(Component.text("Hello everyone!", NamedTextColor.WHITE))
    .build();

// Using append (immutable)
Component message = Component.text("[", NamedTextColor.GRAY)
    .append(Component.text("Warning", NamedTextColor.GOLD))
    .append(Component.text("] ", NamedTextColor.GRAY))
    .append(Component.text("This is a warning!", NamedTextColor.YELLOW));
```

### Click Events

```java
import net.kyori.adventure.text.event.ClickEvent;

// Run command
Component runCmd = Component.text("Click to teleport!", NamedTextColor.AQUA)
    .clickEvent(ClickEvent.runCommand("/spawn"));

// Suggest command
Component suggest = Component.text("Click to message", NamedTextColor.GREEN)
    .clickEvent(ClickEvent.suggestCommand("/msg PlayerName "));

// Open URL
Component url = Component.text("Visit our website!", NamedTextColor.BLUE)
    .clickEvent(ClickEvent.openUrl("https://example.com"));

// Copy to clipboard
Component copy = Component.text("Click to copy IP", NamedTextColor.YELLOW)
    .clickEvent(ClickEvent.copyToClipboard("play.example.com"));
```

### Hover Events

```java
import net.kyori.adventure.text.event.HoverEvent;

// Show text on hover
Component hover = Component.text("Hover me!", NamedTextColor.AQUA)
    .hoverEvent(HoverEvent.showText(
        Component.text("This is hover text!", NamedTextColor.GRAY)
    ));

// Multi-line hover
Component multiHover = Component.text("Player Info", NamedTextColor.YELLOW)
    .hoverEvent(HoverEvent.showText(
        Component.text()
            .append(Component.text("Name: ", NamedTextColor.GRAY))
            .append(Component.text(player.getName(), NamedTextColor.WHITE))
            .appendNewline()
            .append(Component.text("Health: ", NamedTextColor.GRAY))
            .append(Component.text(player.getHealth() + " ❤", NamedTextColor.RED))
            .build()
    ));

// Show item
ItemStack item = new ItemStack(Material.DIAMOND_SWORD);
Component itemHover = Component.text("Epic Sword", NamedTextColor.GOLD)
    .hoverEvent(item.asHoverEvent());

// Show entity
Component entityHover = Component.text("Entity Info")
    .hoverEvent(entity.asHoverEvent());
```

### Combined Click and Hover

```java
Component interactive = Component.text("Click for help!", NamedTextColor.GREEN)
    .clickEvent(ClickEvent.runCommand("/help"))
    .hoverEvent(HoverEvent.showText(
        Component.text("Click to open help menu", NamedTextColor.GRAY)
    ));

player.sendMessage(interactive);
```

### Keybind Components

```java
// Shows the player's actual keybind
Component keybind = Component.text("Press ")
    .append(Component.keybind("key.jump"))
    .append(Component.text(" to jump!"));
// Displays as: "Press Space to jump!" (or whatever their jump key is)

Component attack = Component.text("Fight with ")
    .append(Component.keybind("key.attack").color(NamedTextColor.RED))
    .append(Component.text("!"));
```

### Translatable Components

```java
// Uses client's language
Component translatable = Component.translatable("block.minecraft.dirt");
// Shows "Dirt" in English, "Terre" in French, etc.

// With arguments
Component withArgs = Component.translatable(
    "commands.give.success.single",
    Component.text("64"),
    Component.text("Diamond"),
    Component.text(player.getName())
);
```

### Score Components

```java
// Display scoreboard value
Component score = Component.score("player_name", "objective_name");
```

### Selector Components

```java
// Target selector (shows matched entity names)
Component selector = Component.selector("@a[team=red]");

// Selector with custom separator
Component selectorWithSep = Component.selector("@e[limit=5]")
    .separator(Component.text(", ", NamedTextColor.GRAY));
```

### NBT Components

```java
// NBT from entity
Component entityNbt = Component.storageNBT()
    .nbtPath("Health")
    .interpret(false)
    .build();

// These require server-side rendering to display properly
```

## Text Serializers

Adventure provides multiple serializers for converting between Components and other formats.

### JSON Serializer

```java
import net.kyori.adventure.text.serializer.json.JSONComponentSerializer;

// Component to JSON
Component component = Component.text("Hello", NamedTextColor.RED);
String json = JSONComponentSerializer.json().serialize(component);
// Result: {"text":"Hello","color":"red"}

// JSON to Component
Component fromJson = JSONComponentSerializer.json().deserialize(json);
```

### Legacy Serializer

```java
import net.kyori.adventure.text.serializer.legacy.LegacyComponentSerializer;

// Component to legacy string (§ codes)
String legacy = LegacyComponentSerializer.legacySection().serialize(component);
// Result: "§cHello"

// Component to legacy string (& codes)
String ampersand = LegacyComponentSerializer.legacyAmpersand().serialize(component);
// Result: "&cHello"

// Legacy string to Component
Component fromLegacy = LegacyComponentSerializer.legacyAmpersand().deserialize("&cHello &bWorld");
```

### Plain Text Serializer

```java
import net.kyori.adventure.text.serializer.plain.PlainTextComponentSerializer;

// Component to plain text (strips all formatting)
String plain = PlainTextComponentSerializer.plainText().serialize(
    Component.text("Hello", NamedTextColor.RED)
        .append(Component.text(" World", NamedTextColor.BLUE))
);
// Result: "Hello World"

// Plain text to Component
Component fromPlain = PlainTextComponentSerializer.plainText().deserialize("Hello World");
```

## MiniMessage

### Basic MiniMessage

```java
import net.kyori.adventure.text.minimessage.MiniMessage;

MiniMessage mm = MiniMessage.miniMessage();

// Colors
Component colored = mm.deserialize("<red>This is red!</red>");
Component hex = mm.deserialize("<#00ff00>This is green!</#00ff00>");
Component named = mm.deserialize("<gold>Golden text</gold>");

// Decorations
Component bold = mm.deserialize("<bold>Bold text</bold>");
Component italic = mm.deserialize("<italic>Italic text</italic>");
Component underlined = mm.deserialize("<underlined>Underlined</underlined>");
Component strikethrough = mm.deserialize("<strikethrough>Strikethrough</strikethrough>");
Component obfuscated = mm.deserialize("<obfuscated>Secret</obfuscated>");

// Combined
Component styled = mm.deserialize("<gold><bold>Bold Gold Text</bold></gold>");

// Reset
Component reset = mm.deserialize("<red>Red <reset>Normal");
```

### MiniMessage Gradients

```java
// Gradient
Component gradient = mm.deserialize("<gradient:red:blue>Gradient Text</gradient>");
Component multiGradient = mm.deserialize("<gradient:red:yellow:green>Rainbow</gradient>");

// With phase
Component phased = mm.deserialize("<gradient:red:blue:1.5>Shifted gradient</gradient>");
```

### MiniMessage Rainbow

```java
Component rainbow = mm.deserialize("<rainbow>Rainbow text!</rainbow>");
Component rainbowPhase = mm.deserialize("<rainbow:2>Rainbow with phase</rainbow>");
Component reversedRainbow = mm.deserialize("<rainbow:!>Reversed rainbow</rainbow>");
Component reversed = mm.deserialize("<rainbow:!2>Reversed and shifted</rainbow>");
```

### MiniMessage Transition

```java
// Smooth transition between colors based on phase
Component transition = mm.deserialize("<transition:red:blue:0.5>Text at 50%</transition>");
```

### MiniMessage Pride (since 4.18.0)

```java
// Pride flag gradients
Component pride = mm.deserialize("<pride>Pride text!</pride>");
Component trans = mm.deserialize("<pride:trans>Trans rights!</pride>");
Component bi = mm.deserialize("<pride:bi>Bi pride!</pride>");
// Flags: pride, progress, trans, bi, pan, nb, lesbian, ace, agender,
//        demisexual, genderqueer, genderfluid, intersex, aro, baker,
//        philly, queer, gay, bigender, demigender
```

### MiniMessage Shadow Color (since 1.21.4)

```java
// Custom shadow color
Component shadow = mm.deserialize("<shadow:yellow>Yellow shadow</shadow>");
Component hexShadow = mm.deserialize("<shadow:#FF5555>Red shadow</shadow>");
Component alphaShadow = mm.deserialize("<shadow:aqua:0.5>50% opacity shadow</shadow>");
Component noShadow = mm.deserialize("<!shadow>No shadow</!shadow>");
```

### MiniMessage Font

```java
// Change font
Component uniform = mm.deserialize("<font:uniform>Uniform font</font>");
Component alt = mm.deserialize("<font:alt>Alt font</font>");
Component custom = mm.deserialize("<font:myplugin:custom_font>Custom font</font>");
```

### MiniMessage Newline

```java
Component newline = mm.deserialize("Line 1<newline>Line 2");
Component br = mm.deserialize("Line 1<br>Line 2"); // Alias
```

### MiniMessage Insertion

```java
// Shift-click to insert text
Component insert = mm.deserialize("<insert:hello>Shift-click me!</insert>");
```

### MiniMessage Sprite (since 4.25.0)

```java
// Insert sprite from atlas
Component sprite = mm.deserialize("<sprite:blocks:block/stone>");
Component itemSprite = mm.deserialize("<sprite:\"minecraft:items\":item/porkchop>");
```

### MiniMessage Head (since 4.25.0)

```java
// Player head by name, UUID, or texture
Component headName = mm.deserialize("<head:Notch>");
Component headUuid = mm.deserialize("<head:1f085b2d-9548-4159-a8c7-f3ccdf0c2054>");
Component headNoHat = mm.deserialize("<head:Steve:false>"); // Without outer layer
```

### MiniMessage Click Events

```java
Component click = mm.deserialize("<click:run_command:/help>Click for help!</click>");
Component suggest = mm.deserialize("<click:suggest_command:/msg >Click to message</click>");
Component url = mm.deserialize("<click:open_url:'https://example.com'>Visit website</click>");
Component copy = mm.deserialize("<click:copy_to_clipboard:'play.example.com'>Copy IP</click>");
```

### MiniMessage Hover Events

```java
Component hover = mm.deserialize("<hover:show_text:'Hover text'>Hover me!</hover>");

// Multi-line hover
Component multiHover = mm.deserialize(
    "<hover:show_text:'<red>Line 1<newline><blue>Line 2'>Hover me!</hover>"
);
```

### MiniMessage Placeholders

```java
import net.kyori.adventure.text.minimessage.tag.resolver.Placeholder;

String template = "<gold>Hello <player>!</gold>";
Component message = mm.deserialize(
    template,
    Placeholder.unparsed("player", player.getName())
);

// Multiple placeholders
String multiTemplate = "<player> has <health> health";
Component multi = mm.deserialize(
    multiTemplate,
    Placeholder.unparsed("player", player.getName()),
    Placeholder.unparsed("health", String.valueOf(player.getHealth()))
);

// Component placeholder
Component comp = mm.deserialize(
    "Welcome <player>!",
    Placeholder.component("player", Component.text(player.getName(), NamedTextColor.YELLOW))
);
```

### MiniMessage Tag Resolvers

```java
import net.kyori.adventure.text.minimessage.tag.resolver.TagResolver;
import net.kyori.adventure.text.minimessage.tag.Tag;

// Custom tag
TagResolver customTag = TagResolver.resolver("custom", (argumentQueue, context) -> {
    return Tag.selfClosingInserting(Component.text("Custom Value", NamedTextColor.GOLD));
});

Component result = mm.deserialize("This is <custom>!", customTag);

// Dynamic placeholder tag
TagResolver playerTag = TagResolver.resolver("player", (argumentQueue, context) -> {
    return Tag.selfClosingInserting(Component.text(player.getName(), NamedTextColor.YELLOW));
});

// Tag with arguments
TagResolver colorTag = TagResolver.resolver("col", (args, ctx) -> {
    String colorName = args.popOr("Missing color argument").value();
    NamedTextColor color = NamedTextColor.NAMES.value(colorName);
    return Tag.styling(color != null ? color : NamedTextColor.WHITE);
});

// Combine multiple resolvers
TagResolver combined = TagResolver.builder()
    .resolver(Placeholder.unparsed("player", player.getName()))
    .resolver(customTag)
    .resolver(playerTag)
    .build();

Component msg = mm.deserialize("<player> says <custom>", combined);
```

### PlaceholderAPI Integration

```java
/**
 * Creates a tag resolver for PlaceholderAPI placeholders.
 * Usage: <papi:luckperms_prefix>
 */
public @NotNull TagResolver papiTag(final @NotNull Player player) {
    return TagResolver.resolver("papi", (argumentQueue, context) -> {
        final String papiPlaceholder = argumentQueue.popOr("papi tag requires an argument").value();
        final String parsedPlaceholder = PlaceholderAPI.setPlaceholders(player, '%' + papiPlaceholder + '%');
        final Component componentPlaceholder = LegacyComponentSerializer.legacySection().deserialize(parsedPlaceholder);
        return Tag.selfClosingInserting(componentPlaceholder);
    });
}

// Usage
Component message = mm.deserialize(
    "Your prefix: <papi:luckperms_prefix>",
    papiTag(player)
);
```

### MiniMessage Configuration

```java
import net.kyori.adventure.text.minimessage.MiniMessage;

// Strict mode (throws on invalid tags)
MiniMessage strict = MiniMessage.builder()
    .strict(true)
    .build();

// Custom tags
MiniMessage custom = MiniMessage.builder()
    .tags(TagResolver.resolver("myTag", customTag))
    .build();
```

## Titles and Subtitles

```java
import net.kyori.adventure.title.Title;
import java.time.Duration;

// Simple title
player.showTitle(Title.title(
    Component.text("Welcome!", NamedTextColor.GOLD),
    Component.text("to the server", NamedTextColor.GRAY)
));

// With timings
player.showTitle(Title.title(
    Component.text("Warning!", NamedTextColor.RED),
    Component.text("Danger ahead", NamedTextColor.YELLOW),
    Title.Times.times(
        Duration.ofMillis(500),  // Fade in
        Duration.ofSeconds(3),    // Stay
        Duration.ofSeconds(1)     // Fade out
    )
));

// Title only
player.showTitle(Title.title(
    Component.text("Big Title", NamedTextColor.GOLD),
    Component.empty()
));

// Clear title
player.clearTitle();

// Reset title (clears and resets timings)
player.resetTitle();
```

## Action Bar

```java
// Simple action bar
player.sendActionBar(Component.text("Action bar message!", NamedTextColor.YELLOW));

// With formatting
player.sendActionBar(Component.text()
    .append(Component.text("HP: ", NamedTextColor.GRAY))
    .append(Component.text("❤".repeat((int) player.getHealth()), NamedTextColor.RED))
    .build()
);

// MiniMessage
player.sendActionBar(
    MiniMessage.miniMessage().deserialize("<gold>⚠</gold> <yellow>Warning!</yellow>")
);
```

## Boss Bars

```java
import net.kyori.adventure.bossbar.BossBar;

// Create boss bar
BossBar bossBar = BossBar.bossBar(
    Component.text("Boss Fight", NamedTextColor.RED),
    1.0f, // Progress (0.0 to 1.0)
    BossBar.Color.RED,
    BossBar.Overlay.PROGRESS
);

// Show to player
player.showBossBar(bossBar);

// Update progress
bossBar.progress(0.5f);

// Update name
bossBar.name(Component.text("Boss: 50% HP", NamedTextColor.RED));

// Update color
bossBar.color(BossBar.Color.YELLOW);

// Add flags
bossBar.addFlag(BossBar.Flag.DARKEN_SCREEN);
bossBar.addFlag(BossBar.Flag.CREATE_WORLD_FOG);

// Hide boss bar
player.hideBossBar(bossBar);

// Colors: PINK, BLUE, RED, GREEN, YELLOW, PURPLE, WHITE
// Overlays: PROGRESS, NOTCHED_6, NOTCHED_10, NOTCHED_12, NOTCHED_20
```

## Sounds

```java
import net.kyori.adventure.sound.Sound;
import org.bukkit.Sound as BukkitSound;

// Play sound
player.playSound(Sound.sound(
    org.bukkit.Sound.ENTITY_EXPERIENCE_ORB_PICKUP,
    Sound.Source.PLAYER,
    1.0f, // Volume
    1.0f  // Pitch
));

// At location
player.playSound(Sound.sound(
    org.bukkit.Sound.BLOCK_NOTE_BLOCK_PLING,
    Sound.Source.BLOCK,
    1.0f,
    1.0f
), location.x(), location.y(), location.z());

// Stop sound
player.stopSound(org.bukkit.Sound.ENTITY_EXPERIENCE_ORB_PICKUP);

// Stop all sounds
player.stopSound(Sound.Source.MASTER);
```

## Books

```java
import net.kyori.adventure.inventory.Book;

// Create book
Book book = Book.book(
    Component.text("Book Title", NamedTextColor.GOLD),
    Component.text("Author Name", NamedTextColor.GRAY),
    Component.text("Page 1 content\nWith multiple lines"),
    Component.text("Page 2 content")
);

// Open book
player.openBook(book);

// Complex pages
Component page1 = Component.text()
    .append(Component.text("Chapter 1", NamedTextColor.GOLD, TextDecoration.BOLD))
    .appendNewline()
    .appendNewline()
    .append(Component.text("Once upon a time...", NamedTextColor.BLACK))
    .build();

Component page2 = Component.text()
    .append(Component.text("Interactive Page", NamedTextColor.BLUE))
    .appendNewline()
    .append(
        Component.text("[Click here]", NamedTextColor.GREEN)
            .clickEvent(ClickEvent.runCommand("/home"))
            .hoverEvent(HoverEvent.showText(Component.text("Go home")))
    )
    .build();

Book complexBook = Book.book(
    Component.text("Story Book"),
    Component.text("Server"),
    page1, page2
);
```

## Signs

```java
// Update sign text (Paper)
Sign sign = (Sign) block.getState();

// Set lines
sign.line(0, Component.text("Line 1", NamedTextColor.GOLD));
sign.line(1, Component.text("Line 2", NamedTextColor.BLUE));
sign.line(2, Component.text("Click me!", NamedTextColor.GREEN)
    .clickEvent(ClickEvent.runCommand("/shop")));
sign.line(3, Component.text("Line 4", NamedTextColor.GRAY));

// Update sign
sign.update();

// Get sign text
Component line1 = sign.line(0);
```

## Inventory

```java
import net.kyori.adventure.text.Component;

// Create inventory with title
Inventory inv = Bukkit.createInventory(
    null,
    27,
    Component.text("Shop", NamedTextColor.GOLD)
);

// Item with custom name and lore
ItemStack item = new ItemStack(Material.DIAMOND_SWORD);
item.editMeta(meta -> {
    meta.displayName(Component.text("Epic Sword", NamedTextColor.GOLD, TextDecoration.BOLD)
        .decoration(TextDecoration.ITALIC, false));
    
    meta.lore(List.of(
        Component.text("Damage: ", NamedTextColor.GRAY)
            .append(Component.text("+10", NamedTextColor.RED))
            .decoration(TextDecoration.ITALIC, false),
        Component.empty(),
        Component.text("Right-click to use", NamedTextColor.YELLOW)
            .decoration(TextDecoration.ITALIC, false)
    ));
});

inv.setItem(13, item);

// Open inventory
player.openInventory(inv);
```

## Utility Functions

### Component to Legacy String

```java
import net.kyori.adventure.text.serializer.legacy.LegacyComponentSerializer;

Component component = Component.text("Hello", NamedTextColor.RED);
String legacy = LegacyComponentSerializer.legacySection().serialize(component);
// Result: "§cHello"
```

### Component to Plain Text

```java
import net.kyori.adventure.text.serializer.plain.PlainTextComponentSerializer;

Component component = Component.text("Hello", NamedTextColor.RED)
    .append(Component.text(" World", NamedTextColor.BLUE));
String plain = PlainTextComponentSerializer.plainText().serialize(component);
// Result: "Hello World"
```

### Component to JSON

```java
import net.kyori.adventure.text.serializer.json.JSONComponentSerializer;

Component component = Component.text("Hello", NamedTextColor.RED);
String json = JSONComponentSerializer.json().serialize(component);
// Result: {"text":"Hello","color":"red"}
```

### MiniMessage to Component to MiniMessage

```java
MiniMessage mm = MiniMessage.miniMessage();

// Deserialize
Component component = mm.deserialize("<red>Hello</red>");

// Serialize back
String miniMessage = mm.serialize(component);
// Result: "<red>Hello</red>"
```

## Common Patterns

### Message Prefixes

```java
public class Messages {
    private static final Component PREFIX = Component.text("[MyPlugin] ", NamedTextColor.GOLD);
    
    public static void send(Player player, Component message) {
        player.sendMessage(PREFIX.append(message));
    }
    
    public static void error(Player player, String message) {
        send(player, Component.text(message, NamedTextColor.RED));
    }
    
    public static void success(Player player, String message) {
        send(player, Component.text(message, NamedTextColor.GREEN));
    }
}

// Usage
Messages.send(player, Component.text("Welcome!"));
Messages.error(player, "An error occurred!");
Messages.success(player, "Action completed!");
```

### Config Messages with MiniMessage

```java
public class ConfigMessages {
    private final MiniMessage mm = MiniMessage.miniMessage();
    private final FileConfiguration config;
    
    public Component get(String key, TagResolver... resolvers) {
        String raw = config.getString("messages." + key, "<red>Message not found</red>");
        return mm.deserialize(raw, resolvers);
    }
}

// In config.yml:
// messages:
//   welcome: "<gold>Welcome <player>!</gold>"
//   balance: "<gray>Your balance: <green>$<amount></green></gray>"

// Usage:
Component welcome = messages.get("welcome",
    Placeholder.unparsed("player", player.getName())
);

Component balance = messages.get("balance",
    Placeholder.unparsed("amount", String.valueOf(playerBalance))
);
```

## FAQ and Best Practices

### Why is my lore in italics?

Components inherit style from their parent. Vanilla Minecraft applies italic styling to lore by default. Fix it by explicitly setting italic to false:

```java
// Use decorationIfAbsent to avoid overriding user formatting
Component loreLine = Component.text("My lore line")
    .decorationIfAbsent(TextDecoration.ITALIC, TextDecoration.State.FALSE);

// Or in item lore:
meta.lore(List.of(
    Component.text("Damage: +10", NamedTextColor.GRAY)
        .decoration(TextDecoration.ITALIC, false)
));
```

### Hex Colors Not Working?

- Test on vanilla client (mods can break formatting)
- RGB colors require Minecraft 1.16+
- Check for other plugins modifying packets

### Supporting Both MiniMessage and Legacy Formatting

**Don't try to combine them.** Instead, migrate legacy messages once:

```java
// One-time migration
String legacyMessage = "&cHello &bWorld";
Component component = LegacyComponentSerializer.legacyAmpersand().deserialize(legacyMessage);
String miniMessage = MiniMessage.miniMessage().serialize(component);
// Result: "<red>Hello <aqua>World"
```

### Common Errors

**NoSuchMethodError/ClassNotFoundException:**
- Don't shade Adventure on Paper (it's provided natively)
- If using Adventure separately, ensure proper relocation
- Check dependency versions match
