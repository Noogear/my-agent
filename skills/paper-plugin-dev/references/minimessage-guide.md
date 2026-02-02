# MiniMessage Complete Guide

Comprehensive guide to MiniMessage syntax, tags, and advanced usage patterns.

> **Note**: MiniMessage is bundled natively with Paper. Test your messages at [MiniMessage Web Viewer](https://webui.advntr.dev).

## Table of Contents

- [Basic Syntax](#basic-syntax)
- [Color Tags](#color-tags)
- [Shadow Color Tags](#shadow-color-tags)
- [Formatting Tags](#formatting-tags)
- [Advanced Color Effects](#advanced-color-effects)
- [Interactive Elements](#interactive-elements)
- [Special Components](#special-components)
- [Tag Resolvers](#tag-resolvers)
- [Strict Mode](#strict-mode)
- [Common Patterns](#common-patterns)

## Basic Syntax

MiniMessage uses XML-like tags for formatting text:

```java
MiniMessage mm = MiniMessage.miniMessage();

// Basic tag
Component result = mm.deserialize("<red>This is red</red>");

// Self-closing tag
Component result = mm.deserialize("<red>Red text<reset> normal text");

// Nested tags
Component result = mm.deserialize("<red><bold>Bold red text</bold></red>");
```

### Tag Nesting

Tags can be nested and inherit from parent tags:

```java
// Both parts will be red, inner part will also be bold
mm.deserialize("<red>Red <bold>and bold</bold></red>");

// Colors override parent colors
mm.deserialize("<red>Red <blue>Blue</blue> Red again</red>");
```

## Color Tags

### Named Colors

All standard Minecraft colors are available:

```java
mm.deserialize("<black>Black</black>");
mm.deserialize("<dark_blue>Dark Blue</dark_blue>");
mm.deserialize("<dark_green>Dark Green</dark_green>");
mm.deserialize("<dark_aqua>Dark Aqua</dark_aqua>");
mm.deserialize("<dark_red>Dark Red</dark_red>");
mm.deserialize("<dark_purple>Dark Purple</dark_purple>");
mm.deserialize("<gold>Gold</gold>");
mm.deserialize("<gray>Gray</gray>");
mm.deserialize("<dark_gray>Dark Gray</dark_gray>");
mm.deserialize("<blue>Blue</blue>");
mm.deserialize("<green>Green</green>");
mm.deserialize("<aqua>Aqua</aqua>");
mm.deserialize("<red>Red</red>");
mm.deserialize("<light_purple>Light Purple</light_purple>");
mm.deserialize("<yellow>Yellow</yellow>");
mm.deserialize("<white>White</white>");
```

### Hex Colors

Use hex color codes for any RGB color:

```java
// Full hex format
mm.deserialize("<#ff0000>Red</color>");
mm.deserialize("<#00ff00>Green</color>");
mm.deserialize("<#0000ff>Blue</color>");

// Shorthand (automatically closes)
mm.deserialize("<#ff0000>Red text");

// Multiple hex colors
mm.deserialize("<#ff0000>Red <#00ff00>Green <#0000ff>Blue");
```

### Color Aliases

You can use alternative names:

```java
mm.deserialize("<colour:#ff0000>British spelling works too</colour>");
mm.deserialize("<c:#ff0000>Short form</c>");
```

## Shadow Color Tags

*(Minecraft 1.21.4+)* Change the text shadow color:

```java
// Named color shadow
mm.deserialize("<shadow:yellow>Yellow shadow</shadow>");
mm.deserialize("<shadow:aqua>Aqua shadow</shadow>");

// Hex color shadow
mm.deserialize("<shadow:#FF5555>Red shadow</shadow>");
mm.deserialize("<shadow:#55FF55>Green shadow</shadow>");

// With alpha (0-1 float, defaults to 0.25)
mm.deserialize("<shadow:aqua:0.5>50% opacity shadow</shadow>");

// Full hex with alpha (RRGGBBAA)
mm.deserialize("<shadow:#000000FF>Full opacity black shadow</shadow>");

// Disable shadow
mm.deserialize("<!shadow>No shadow at all</!shadow>");
// Or
mm.deserialize("<shadow:#00000000>Transparent shadow</shadow>");
```

## Formatting Tags

### Text Decorations

```java
// Bold
mm.deserialize("<bold>Bold text</bold>");
mm.deserialize("<b>Also bold</b>");

// Italic
mm.deserialize("<italic>Italic text</italic>");
mm.deserialize("<em>Also italic</em>");
mm.deserialize("<i>Short form</i>");

// Underlined
mm.deserialize("<underlined>Underlined</underlined>");
mm.deserialize("<u>Short form</u>");

// Strikethrough
mm.deserialize("<strikethrough>Strikethrough</strikethrough>");
mm.deserialize("<st>Short form</st>");

// Obfuscated (magic)
mm.deserialize("<obfuscated>Secret text</obfuscated>");
mm.deserialize("<obf>Short form</obf>");
```

### Removing Decorations

Use `!` prefix to explicitly remove a decoration:

```java
// Remove bold
mm.deserialize("<bold>Bold <b:!>not bold</b></bold>");

// Remove italic (useful for item lore)
mm.deserialize("<i:false>Not italic</i>");
mm.deserialize("<!italic>Also not italic</!italic>");
```

### Reset Tag

Reset all formatting:

```java
mm.deserialize("<red><bold>Red and bold <reset>Normal text");
```

## Advanced Color Effects

### Gradients

Create smooth color transitions:

```java
// Two-color gradient
mm.deserialize("<gradient:red:blue>Gradient text</gradient>");

// Multi-color gradient
mm.deserialize("<gradient:red:yellow:green:blue>Rainbow gradient</gradient>");

// Gradient with hex colors
mm.deserialize("<gradient:#ff0000:#0000ff>Custom gradient</gradient>");

// Gradient with phase (shift the gradient)
mm.deserialize("<gradient:red:blue:1.5>Shifted gradient</gradient>");

// Negative phase (reverse direction)
mm.deserialize("<gradient:red:blue:-1>Reversed gradient</gradient>");
```

### Rainbow Effect

Animated rainbow effect (cycles through hue):

```java
// Basic rainbow
mm.deserialize("<rainbow>Rainbow text!</rainbow>");

// Rainbow with phase
mm.deserialize("<rainbow:2>Shifted rainbow</rainbow>");

// Reversed rainbow
mm.deserialize("<rainbow:!>Reversed rainbow</rainbow>");

// Rainbow with custom phase
mm.deserialize("<rainbow:!2>Reversed and shifted</rainbow>");
```

### Transition Tag

Smooth transition between colors. Unlike gradient, the entire text is the same color based on phase:

```java
// Phase 0 = first color, 0.5 = middle color, 1 = last color
mm.deserialize("<transition:#00ff00:#ff0000:0>All green (at phase 0)</transition>");
mm.deserialize("<transition:#00ff00:#ff0000:0.5>50% between</transition>");
mm.deserialize("<transition:#00ff00:#ff0000:1>All red (at phase 1)</transition>");

// Multi-color transition
mm.deserialize("<transition:white:black:red:0.3>At 30%</transition>");
```

### Pride Flag Colors

*(since 4.18.0)* Apply pride flag gradient colors:

```java
// Default pride flag
mm.deserialize("<pride>Pride text!</pride>");

// Specific flags
mm.deserialize("<pride:trans>Trans rights!</pride>");
mm.deserialize("<pride:bi>Bi pride!</pride>");
mm.deserialize("<pride:pan>Pan pride!</pride>");
mm.deserialize("<pride:nb>Non-binary pride!</pride>");
mm.deserialize("<pride:lesbian>Lesbian pride!</pride>");
mm.deserialize("<pride:ace>Ace pride!</pride>");
mm.deserialize("<pride:aro>Aro pride!</pride>");
mm.deserialize("<pride:gay>Gay pride!</pride>");

// With phase
mm.deserialize("<pride:trans:0.5>Shifted trans colors</pride>");

// Available flags: pride, progress, trans, bi, pan, nb, lesbian, ace,
// agender, demisexual, genderqueer, genderfluid, intersex, aro, baker,
// philly, queer, gay, bigender, demigender
```

## Interactive Elements

### Click Events

```java
// Run command when clicked
mm.deserialize("<click:run_command:/help>Click for help</click>");

// Suggest command (fills chat box)
mm.deserialize("<click:suggest_command:/msg player >Click to PM</click>");

// Open URL
mm.deserialize("<click:open_url:'https://example.com'>Visit website</click>");

// Copy text to clipboard
mm.deserialize("<click:copy_to_clipboard:'mc.example.com'>Copy server IP</click>");

// Change book page (only works in books)
mm.deserialize("<click:change_page:2>Go to page 2</click>");
```

### Hover Events

```java
// Show text on hover
mm.deserialize("<hover:show_text:'Tooltip text'>Hover me</hover>");

// Multi-line hover
mm.deserialize("<hover:show_text:'Line 1<newline>Line 2'>Hover me</hover>");

// Formatted hover
mm.deserialize("<hover:show_text:'<red>Red tooltip<newline><blue>Blue line'>Text</hover>");

// Show item (requires NBT)
mm.deserialize("<hover:show_item:'minecraft:diamond_sword'>Hover for item</hover>");

// Show entity
mm.deserialize("<hover:show_entity:'minecraft:pig':'Custom Name'>Hover for entity</hover>");
```

### Combined Click and Hover

```java
mm.deserialize(
    "<click:run_command:/home>" +
    "<hover:show_text:'Click to teleport home'>" +
    "Teleport Home" +
    "</hover></click>"
);

// Or nested
mm.deserialize(
    "<hover:show_text:'Click to teleport'>" +
    "<click:run_command:/spawn>" +
    "Spawn" +
    "</click></hover>"
);
```

## Special Components

### Keybind

Display the player's configured key binding:

```java
// Shows player's actual keybind
mm.deserialize("Press <key:key.jump> to jump!");
// Displays as: "Press Space to jump!" (or their actual binding)

mm.deserialize("Attack with <red><key:key.attack></red>!");
```

### Translatable

Uses client's language for translation:

```java
// Basic translatable
mm.deserialize("<lang:block.minecraft.diamond_block>");
// "Diamond Block" in English, "Bloc de diamant" in French

// Aliases: tr, translate
mm.deserialize("<tr:block.minecraft.dirt>");

// With arguments
mm.deserialize("<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>");

// Fallback (since 1.19.4) - shows fallback if translation not found
mm.deserialize("<lang_or:my.custom.key:'Default Text'>");
// Aliases: tr_or, translate_or
```

### Insertion

Insert text into chat with Shift+click:

```java
mm.deserialize("<insert:hello world>Shift-click to insert!</insert>");
```

### Selector

*(since 4.11.0)* Display entity selector results:

```java
// Basic selector
mm.deserialize("Hello <selector:@e[limit=5]>!");

// With custom separator
mm.deserialize("Players: <sel:@a[team=red]:' and '>");
// Alias: sel
```

### Score

*(since 4.13.0)* Display scoreboard value (requires server-side rendering):

```java
mm.deserialize("You have won <score:rymiel:gamesWon/> games!");
// Format: <score:name:objective>
```

### NBT / Data

*(since 4.13.0)* Display NBT data (requires server-side rendering):

```java
// Entity NBT
mm.deserialize("Your health is <nbt:entity:'@s':Health/>");

// Block entity NBT
mm.deserialize("<nbt:block:'0 64 0':CustomName/>");

// Storage NBT
mm.deserialize("<nbt:storage:'minecraft:saved_data':my_path/>");

// With separator for multiple values
mm.deserialize("<nbt:entity:'@a':Health:', '/>");

// With interpret flag (parse as component JSON)
mm.deserialize("<nbt:storage:'my:data':message:interpret/>");

// Alias: data
mm.deserialize("<data:entity:'@s':Health/>");
```

### Font

Change the text font:

```java
// Built-in fonts
mm.deserialize("<font:uniform>Uniform font</font>");
mm.deserialize("<font:alt>Alt font (enchanting table)</font>");

// Custom font from resource pack
mm.deserialize("<font:myplugin:custom_font>Custom font</font>");

// Nested
mm.deserialize("Normal <font:uniform>Uniform <font:alt>Alt</font> Uniform</font>");
```

### Newline

Insert line breaks:

```java
mm.deserialize("Line 1<newline>Line 2");
mm.deserialize("Line 1<br>Line 2"); // Alias: br

// In hover text
mm.deserialize("<hover:show_text:'Line 1<newline>Line 2'>Hover me</hover>");
```

### Reset

Reset all formatting (cannot be closed, forbidden in strict mode):

```java
mm.deserialize("<red><bold>Red bold <reset>Normal text");
```

### Sprite

*(since 4.25.0)* Insert a sprite from texture atlas:

```java
// Format: <sprite[:atlas]:sprite>
mm.deserialize("Look at my <sprite:blocks:block/stone>!");
mm.deserialize("Cost: 10 x <sprite:\"minecraft:items\":item/porkchop>");
```

### Head

*(since 4.25.0)* Display player head:

```java
// By player name
mm.deserialize("My favorite dev is <head:Notch>.");

// By UUID
mm.deserialize("Thanks <head:1f085b2d-9548-4159-a8c7-f3ccdf0c2054>!");

// By texture path
mm.deserialize("Steve: <head:entity/player/wide/steve>");
mm.deserialize("Alex: <head:entity/player/slim/alex>");

// Without outer layer (hat)
mm.deserialize("<head:Strokkur24:false>");
```

## Tag Resolvers

Tag resolvers bind tag names to logic that produces Components. They are composable and can be customized per-parse.

> **Tag naming**: Only `a-z`, `0-9`, `_`, `-` allowed. Can optionally start with `!`, `?`, or `#`.

### Built-in Placeholders

```java
import net.kyori.adventure.text.minimessage.tag.resolver.Placeholder;

// Unparsed placeholder (safe for user input - escapes formatting)
mm.deserialize(
    "Hello <player>!",
    Placeholder.unparsed("player", player.getName())
);

// Parsed placeholder (allows formatting - DANGEROUS with user input!)
mm.deserialize(
    "Hello <player>!",
    Placeholder.parsed("player", "<gold>" + player.getName() + "</gold>")
);

// Component placeholder
mm.deserialize(
    "Welcome <player>!",
    Placeholder.component("player", Component.text(player.getName(), NamedTextColor.GOLD))
);
```

### Multiple Placeholders

```java
mm.deserialize(
    "<prefix> <player> has <amount> coins",
    Placeholder.unparsed("player", player.getName()),
    Placeholder.unparsed("amount", String.valueOf(coins)),
    Placeholder.parsed("prefix", "<gold>[Server]</gold>")
);
```

### Custom Tag Resolvers

```java
import net.kyori.adventure.text.minimessage.tag.Tag;
import net.kyori.adventure.text.minimessage.tag.resolver.TagResolver;

// Simple custom tag (self-closing)
TagResolver myTag = TagResolver.resolver("custom", (args, ctx) -> {
    return Tag.selfClosingInserting(Component.text("Custom Value", NamedTextColor.GOLD));
});

Component result = mm.deserialize("This is <custom>!", myTag);

// Tag with arguments
TagResolver colorTag = TagResolver.resolver("col", (args, ctx) -> {
    String colorName = args.popOr("Missing color argument").value();
    TextColor color = NamedTextColor.NAMES.value(colorName);
    if (color == null) {
        color = NamedTextColor.WHITE;
    }
    return Tag.styling(color);
});

Component result = mm.deserialize("This is <col:red>red</col>!", colorTag);

// Styling tag (applies style to children)
TagResolver boldRed = TagResolver.resolver("danger", (args, ctx) -> {
    return Tag.styling(NamedTextColor.RED, TextDecoration.BOLD);
});
// Usage: <danger>Warning!</danger>
```

### Tag Types

There are three main types of tags:

```java
// 1. Inserting (most common) - inserts a Component
Tag.selfClosingInserting(Component.text("Hello"));

// 2. Styling - applies style to wrapped content
Tag.styling(NamedTextColor.RED, TextDecoration.BOLD);
Tag.styling(ClickEvent.runCommand("/help"), HoverEvent.showText(Component.text("Click!")));

// 3. Pre-process - replaces with raw MiniMessage before parsing
// (Advanced - use sparingly)
```

### Tag Resolver Builder

```java
TagResolver resolver = TagResolver.builder()
    .resolver(Placeholder.unparsed("player", player.getName()))
    .resolver(Placeholder.unparsed("world", world.getName()))
    .resolver(myCustomTag)
    .build();

Component result = mm.deserialize(
    "<player> is in <world>",
    resolver
);
```

### Caching Resolvers

For frequently used resolvers, cache them:

```java
public class MessageCache {
    private final Map<UUID, TagResolver> playerResolvers = new ConcurrentHashMap<>();
    
    public TagResolver getPlayerResolver(Player player) {
        return playerResolvers.computeIfAbsent(player.getUniqueId(), uuid -> 
            TagResolver.builder()
                .resolver(Placeholder.unparsed("player", player.getName()))
                .resolver(Placeholder.unparsed("displayname", player.getDisplayName()))
                .resolver(Placeholder.unparsed("world", player.getWorld().getName()))
                .build()
        );
    }
}
```

## Strict Mode

Strict mode enforces proper tag structure:

```java
MiniMessage strict = MiniMessage.builder()
    .strict(true)
    .build();

// In strict mode:
// - <reset> tag is FORBIDDEN
// - All tags must be closed in reverse order of opening
// - Invalid tags throw exceptions

// ❌ Invalid in strict mode:
// "<red><bold>Hello</red></bold>" - wrong closing order
// "<red>Hello<reset>" - reset not allowed

// ✅ Valid in strict mode:
// "<red><bold>Hello</bold></red>"

// Will throw exception on unknown/invalid tags
try {
    strict.deserialize("<invalid>Text</invalid>");
} catch (Exception e) {
    // Handle invalid syntax
}
```

### Debug Mode

Enable debug output for parsing issues:

```java
MiniMessage debug = MiniMessage.builder()
    .debug(System.out::println) // Or your logger
    .build();

// Will print parsing information
debug.deserialize("<red>Test</red>");
```

### Customizing Available Tags

```java
import net.kyori.adventure.text.minimessage.tag.standard.StandardTags;

// Only allow specific tags
MiniMessage limited = MiniMessage.builder()
    .tags(TagResolver.builder()
        .resolver(StandardTags.color())        // Only colors
        .resolver(StandardTags.decorations())  // Only decorations
        .build()
    )
    .build();

// Disable specific tag types
MiniMessage noClicks = MiniMessage.builder()
    .tags(TagResolver.builder()
        .resolver(StandardTags.defaults())
        .resolver(TagResolver.empty()) // No clicks
        .build()
    )
    .build();

// Add custom tags to defaults
MiniMessage extended = MiniMessage.builder()
    .editTags(builder -> builder.resolver(myCustomResolver))
    .build();
```

## Common Patterns

### Message Prefix System

```java
public class Messages {
    private static final MiniMessage mm = MiniMessage.miniMessage();
    private static final String PREFIX = "<gold>[MyPlugin]</gold> ";
    
    public static Component format(String message, TagResolver... resolvers) {
        return mm.deserialize(PREFIX + message, resolvers);
    }
    
    public static Component error(String message) {
        return format("<red>" + message + "</red>");
    }
    
    public static Component success(String message) {
        return format("<green>" + message + "</green>");
    }
    
    public static Component info(String message) {
        return format("<gray>" + message + "</gray>");
    }
}

// Usage
player.sendMessage(Messages.success("Action completed!"));
player.sendMessage(Messages.error("An error occurred!"));
```

### Config Message System

```java
public class ConfigMessages {
    private final FileConfiguration config;
    private final MiniMessage mm;
    private final Map<String, String> cache;
    
    public ConfigMessages(FileConfiguration config) {
        this.config = config;
        this.mm = MiniMessage.miniMessage();
        this.cache = new ConcurrentHashMap<>();
    }
    
    public Component get(String key, TagResolver... resolvers) {
        String template = cache.computeIfAbsent(key, k -> 
            config.getString("messages." + k, "<red>Message not found: " + k + "</red>")
        );
        return mm.deserialize(template, resolvers);
    }
    
    public void reload() {
        cache.clear();
    }
}

// In config.yml:
// messages:
//   welcome: "<gradient:green:aqua>Welcome <player>!</gradient>"
//   balance: "<gray>Balance: <green>$<amount></green></gray>"
//   error: "<red>Error: <message></red>"

// Usage
Component welcome = messages.get("welcome",
    Placeholder.unparsed("player", player.getName())
);

Component balance = messages.get("balance",
    Placeholder.unparsed("amount", String.valueOf(balance))
);
```

### PlaceholderAPI Integration

```java
import me.clip.placeholderapi.PlaceholderAPI;

public class PAPIResolver {
    
    /**
     * Creates a tag resolver for PlaceholderAPI.
     * Usage in MiniMessage: <papi:luckperms_prefix>
     */
    public static TagResolver create(Player player) {
        return TagResolver.resolver("papi", (args, ctx) -> {
            String placeholder = args.popOr("papi requires an argument").value();
            String result = PlaceholderAPI.setPlaceholders(player, "%" + placeholder + "%");
            
            // Parse legacy colors from PAPI output
            Component component = LegacyComponentSerializer.legacySection().deserialize(result);
            return Tag.selfClosingInserting(component);
        });
    }
}

// Usage
Component message = mm.deserialize(
    "Your prefix: <papi:luckperms_prefix> | Balance: <papi:vault_eco_balance>",
    PAPIResolver.create(player)
);
```

### Item Lore Anti-Italic

```java
// Lore is italic by default - disable it
public static List<Component> formatLore(List<String> loreLines) {
    return loreLines.stream()
        .map(line -> mm.deserialize(line)
            .decorationIfAbsent(TextDecoration.ITALIC, TextDecoration.State.FALSE))
        .toList();
}

// Or in MiniMessage directly
mm.deserialize("<!italic><gray>This lore line won't be italic</gray>");
```

### Pagination with MiniMessage

```java
public class PaginatedMessage {
    private final MiniMessage mm = MiniMessage.miniMessage();
    private final List<String> lines;
    private final String header;
    private final String footer;
    
    public void send(Player player, int page) {
        int linesPerPage = 8;
        int totalPages = (int) Math.ceil((double) lines.size() / linesPerPage);
        page = Math.max(1, Math.min(page, totalPages));
        
        TagResolver resolver = TagResolver.builder()
            .resolver(Placeholder.unparsed("page", String.valueOf(page)))
            .resolver(Placeholder.unparsed("total", String.valueOf(totalPages)))
            .build();
        
        player.sendMessage(mm.deserialize(header, resolver));
        
        int start = (page - 1) * linesPerPage;
        int end = Math.min(start + linesPerPage, lines.size());
        
        for (int i = start; i < end; i++) {
            player.sendMessage(mm.deserialize(lines.get(i)));
        }
        
        player.sendMessage(mm.deserialize(footer, resolver));
    }
}
```

### Markdown-style Formatting

```java
public class MarkdownStyle {
    private static final MiniMessage mm = MiniMessage.miniMessage();
    
    public static Component parse(String markdown) {
        // Pre-process markdown-style formatting
        String processed = markdown
            .replaceAll("\\*\\*(.+?)\\*\\*", "<bold>$1</bold>")
            .replaceAll("\\*(.+?)\\*", "<italic>$1</italic>")
            .replaceAll("__(.+?)__", "<underlined>$1</underlined>")
            .replaceAll("~~(.+?)~~", "<strikethrough>$1</strikethrough>")
            .replaceAll("`(.+?)`", "<gray>$1</gray>");
        
        return mm.deserialize(processed);
    }
}

// Usage:
// "**Bold** *italic* __underlined__ ~~strikethrough~~ `code`"
// Becomes: "<bold>Bold</bold> <italic>italic</italic> ..." etc
```

### Color Cycling Animation

```java
public class ColorAnimation {
    private final String text;
    private double phase = 0;
    
    public Component getFrame() {
        phase += 0.1;
        if (phase > 2) phase = 0;
        
        MiniMessage mm = MiniMessage.miniMessage();
        return mm.deserialize("<rainbow:" + phase + ">" + text + "</rainbow>");
    }
}

// In a repeating task:
Bukkit.getGlobalRegionScheduler().runAtFixedRate(plugin, task -> {
    Component frame = animation.getFrame();
    player.sendActionBar(frame);
}, 1L, 1L);
```

## Best Practices

### Security (CRITICAL)

**NEVER** use `parsed()` placeholders with user input:

```java
// ❌ DANGEROUS - User can inject formatting, click events, etc.
mm.deserialize(
    "Message: <msg>",
    Placeholder.parsed("msg", userInput) // BAD! User could inject <click:run_command:/op hacker>
);

// ✅ SAFE - User input is escaped
mm.deserialize(
    "Message: <msg>",
    Placeholder.unparsed("msg", userInput) // GOOD! Treats input as plain text
);

// ✅ SAFE - Component placeholder
mm.deserialize(
    "Message: <msg>",
    Placeholder.component("msg", Component.text(userInput))
);
```

### Performance

```java
// ❌ BAD - Creates new MiniMessage instance each time
public Component format(String msg) {
    return MiniMessage.miniMessage().deserialize(msg);
}

// ✅ GOOD - Reuse instance (thread-safe)
private static final MiniMessage MM = MiniMessage.miniMessage();

public Component format(String msg) {
    return MM.deserialize(msg);
}

// ✅ GOOD - Cache frequently used resolvers
private final Map<UUID, TagResolver> playerResolvers = new ConcurrentHashMap<>();

public TagResolver getPlayerResolver(Player player) {
    return playerResolvers.computeIfAbsent(player.getUniqueId(), uuid ->
        TagResolver.builder()
            .resolver(Placeholder.unparsed("player", player.getName()))
            .resolver(Placeholder.unparsed("world", player.getWorld().getName()))
            .build()
    );
}
```

### Escaping Characters

```java
// Escape < in plain text with backslash
mm.deserialize("5 \\< 10"); // Displays: "5 < 10"

// Escape quotes within quoted strings
mm.deserialize("<hover:show_text:'It\\'s working'>Hover</hover>");

// Escape backslash itself
mm.deserialize("Path: C:\\\\Users"); // Displays: "Path: C:\Users"
```

### Validation

```java
public boolean isValidMiniMessage(String input) {
    try {
        MiniMessage.builder().strict(true).build().deserialize(input);
        return true;
    } catch (Exception e) {
        return false;
    }
}
```

## Migration from Legacy

### Legacy to MiniMessage Converter

```java
public class LegacyConverter {
    private static final MiniMessage mm = MiniMessage.miniMessage();
    private static final LegacyComponentSerializer legacy = 
        LegacyComponentSerializer.legacyAmpersand();
    
    public static String convertLegacyToMiniMessage(String legacyText) {
        // First deserialize legacy format to component
        Component component = legacy.deserialize(legacyText);
        
        // Then serialize to MiniMessage format
        return mm.serialize(component);
    }
}

// Example:
// Input:  "&6Hello &b&lWorld&r!"
// Output: "<gold>Hello <aqua><bold>World</bold></aqua></gold>!"
```

## Debugging Tips

### Preview Components

```java
// Serialize to see the actual MiniMessage format
String miniMsg = mm.serialize(component);
System.out.println("MiniMessage: " + miniMsg);

// Serialize to plain text
String plain = PlainTextComponentSerializer.plainText().serialize(component);
System.out.println("Plain: " + plain);

// Serialize to legacy (for debugging)
String legacy = LegacyComponentSerializer.legacySection().serialize(component);
System.out.println("Legacy: " + legacy);
```

### Tag Debugging

```java
MiniMessage debug = MiniMessage.builder()
    .debug(System.out::println)
    .build();

// Will print parsing information
debug.deserialize("<red>Test</red>");
```
