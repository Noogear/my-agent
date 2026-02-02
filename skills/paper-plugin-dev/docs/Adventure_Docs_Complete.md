# Adventure Documentation
> Generated: 2026-01-25 01:19:41
> Source: https://docs.papermc.io/adventure/

---



================================================================================
Chapter Title: Getting started
Original Link: https://docs.papermc.io/adventure/getting-started/
================================================================================

To use Adventure in your project, you will need to add the following dependency (and repository if using Gradle):

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-3)
* [Gradle (Groovy)](#tab-panel-4)
* [Maven](#tab-panel-5)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-api:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-api:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-api</artifactId>

<version>4.26.1</version>

</dependency>
```

 

Need development/snapshot builds? [Using Snapshot Builds](#using-snapshot-builds)

Some platforms already use Adventure natively.
In this case, you will not need to add Adventure as a dependency.
To view the list of platforms that include Adventure, see [Native Support](https://docs.papermc.io/adventure/platform/native).

To use Adventure with other platforms, you may wish to look at the platform-specific adapters.
A list of platforms with supported adapters can be found at [Platforms](https://docs.papermc.io/adventure/platform).

## Using snapshot builds

[Section titled “Using snapshot builds”](#using-snapshot-builds)

To use snapshot builds, you will need to add the following repository:

* [Gradle (Kotlin)](#tab-panel-0)
* [Gradle (Groovy)](#tab-panel-1)
* [Maven](#tab-panel-2)

build.gradle.kts

```java
repositories {

maven(url = "https://central.sonatype.com/repository/maven-snapshots/") {

name = "central-snapshots"

}

}
```

build.gradle

```java
repositories {

maven {

name = 'central-snapshots'

url = 'https://central.sonatype.com/repository/maven-snapshots/'

}

}
```

pom.xml

```java
<repositories>

<repository>

<id>central-snapshots</id>

<url>https://central.sonatype.com/repository/maven-snapshots/</url>

</repository>

</repositories>
```


================================================================================
Chapter Title: Community libraries
Original Link: https://docs.papermc.io/adventure/community-libraries/
================================================================================

Adventure aims to provide the core libraries needed for interacting with chat components. However, with
our limited time and the sheer number of possible use cases, we can’t hope to provide direct solutions for every problem.

Luckily, many of our community members have produced libraries that complement Adventure, providing additional features and integrations with other software.

Note

This list of libraries is provided for reference only. The Kyori team does not endorse any specific ones, and cannot provide any information beyond the provided links.

If you have a library that you’d like included, please open a pull request on the [PaperMC/docs](https://github.com/PaperMC/docs) repository.

## Libraries for Adventure

[Section titled “Libraries for Adventure”](#libraries-for-adventure)

These are libraries focused around providing additional functionality using Adventure components.
They typically have no dependencies on a specific platform, just Adventure and potentially a library with which they integrate.

| Name | Description | Link |
| --- | --- | --- |
| adventure-binary-serializer | Serializer for converting to packed bytes | [Moulberry/adventure-binary-serializer](https://github.com/Moulberry/adventure-binary-serializer) |
| EnhancedLegacyText | Alternative input format that is legacy compatible with new features | [Vankka/EnhancedLegacyText](https://github.com/Vankka/EnhancedLegacyText) |
| MCDiscordReserializer | Serializers for going between Minecraft & Discord | [Vankka/MCDiscordReserializer](https://github.com/Vankka/MCDiscordReserializer) |
| Minedown | A markdown-style format for representing components | [Phoenix616/MineDown](https://github.com/Phoenix616/MineDown) |

## Libraries that use Adventure

[Section titled “Libraries that use Adventure”](#libraries-that-use-adventure)

These are libraries with a focus on something other than chat components, that use Adventure in their API.
These libraries will often depend on one or more specific platforms to support their functionality.

| Name | Description | Link |
| --- | --- | --- |
| Cloud | A general-purpose Java command dispatcher & framework | [Incendo/cloud](https://github.com/Incendo/cloud) |
| Core | The Core allows you to register (mini)messages to a central database in multiple languages and access them via a very intuitive “key” and “locale” query. | [JuliGamesCore](https://github.com/JuliGames/JuliGamesCore) |
| Creative | A resource-pack library for Minecraft: Java Edition | [Creative](https://github.com/unnamed/creative) |
| Inventory Framework | An inventory framework for managing GUIs | [Inventory Framework](https://github.com/stefvanschie/IF) |
| LiteCommands | A annotation based command framework for Velocity, Bukkit, BungeeCord | [LiteCommands](https://github.com/Rollczi/LiteCommands) |
| MiniPlaceholders | A platform-agnostic MiniMessage Component-based Placeholders library | [MiniPlaceholders](https://github.com/MiniPlaceholders/MiniPlaceholders) |
| ProtocolSidebar | An easy to use sidebar library for Paper/Spigot servers | [CatCoderr/ProtocolSidebar](https://github.com/CatCoderr/ProtocolSidebar) |
| ScoreboardLibrary | A scoreboard library for Paper/Spigot servers | [MegavexNetwork/scoreboard-library](https://github.com/MegavexNetwork/scoreboard-library) |
| Triumph GUI | A library made to simplify the creation of inventory GUIs | [Triumph GUI](https://triumphteam.dev/docs/triumph-gui/introduction) |


================================================================================
Chapter Title: FAQ
Original Link: https://docs.papermc.io/adventure/faq/
================================================================================

We find that there are some issues users come across relatively frequently while applying the Adventure library in certain contexts. These may not be directly related to Adventure itself, but these answers are published here those that ask them:

## Why is my lore in italics?

[Section titled “Why is my lore in italics?”](#why-is-my-lore-in-italics)

Components will inherit style from their parent. For example, in the following code snippet, each word will be red, despite red not being explicitly set on the appended component: `text("hi", RED).append(text("also red!"))`.

In vanilla Minecraft, some places where components are rendered have parent styles. For example, lore text has a parent style that makes all text italic. This means that you will need to set italic to false if you do not want any component you are storing in lore to be italic. The `Component.decorationIfAbsent()` method can apply this to existing components without overriding any formatting specifically set by users.

## Messages not sending? Hex colors not working? Events not appearing? Fonts messed up?

[Section titled “Messages not sending? Hex colors not working? Events not appearing? Fonts messed up?”](#messages-not-sending-hex-colors-not-working-events-not-appearing-fonts-messed-up)

* Test on a vanilla client, without any mods or resource packs. Modded clients (such as Badlion), client mods, and even resource packs can break many elements of the modern JSON chat format and mess with incoming chat packets in ways that cause a myriad of issues.
* Try without other plugins/mods. If another plugin/mod is modifying outgoing packets or formatting chat messages, this could cause a loss of formatting in the messages you send. Try without any other plugins to see if any are causing issues.
* For RGB colors, test on a client of at least version *1.16*. Mojang added RGB support in this version. The JSON message format has evolved over time and has had many new additions since its introduction many, many years ago. For a full version history, see [the Minecraft wiki](https://minecraft.wiki/w/Text_component_format).

## How can I support both MiniMessage and legacy (§-code) formatting?

[Section titled “How can I support both MiniMessage and legacy (§-code) formatting?”](#how-can-i-support-both-minimessage-and-legacy--code-formatting)

If you have legacy in configuration files, or other places, it is suggested that you migrate them once using the legacy deserializer to turn them into a component and then MiniMessage to serialize them into proper MiniMessage format.

There are no working, recommended, or supported ways of using both MiniMessage and legacy color codes and there never will be. Even simple find-and-replace style techniques do not work and will fail to take into account the quirks of style resetting in legacy formatting.

## How can I use Bukkit’s PlaceholderAPI in MiniMessage messages?

[Section titled “How can I use Bukkit’s PlaceholderAPI in MiniMessage messages?”](#how-can-i-use-bukkits-placeholderapi-in-minimessage-messages)

PlaceholderAPI placeholders are not supported in MiniMessage. However, you can easily create a custom tag resolver that can allow users to use PlaceholderAPI placeholders in MiniMessage strings, like in the following example:

Example
Example method to create a MiniMessage placeholder that parses PlaceholderAPI placeholders for a player.

The tag added is of the format `<papi:[papi_placeholder]>`. For example, `<papi:luckperms_prefix>`.

Credit to `mbaxter`.

```java
/**

* Creates a tag resolver capable of resolving PlaceholderAPI tags for a given player.

*

* @param player the player

* @return the tag resolver

*/

public @NotNull TagResolver papiTag(final @NotNull Player player) {

return TagResolver.resolver("papi", (argumentQueue, context) -> {

// Get the string placeholder that they want to use.

final String papiPlaceholder = argumentQueue.popOr("papi tag requires an argument").value();

// Then get PAPI to parse the placeholder for the given player.

final String parsedPlaceholder = PlaceholderAPI.setPlaceholders(player, '%' + papiPlaceholder + '%');

// We need to turn this ugly legacy string into a nice component.

final Component componentPlaceholder = LegacyComponentSerializer.legacySection().deserialize(parsedPlaceholder);

// Finally, return the tag instance to insert the placeholder!

return Tag.selfClosingInserting(componentPlaceholder);

});

}
```

## Why am I getting a `NoSuchFieldError`, `NoSuchMethodError`, `ClassNotFoundException` or similar when updating/using `adventure-platform-*`, `adventure-text-minimessage`, `adventure-api` or other related libraries/tools?

[Section titled “Why am I getting a NoSuchFieldError, NoSuchMethodError, ClassNotFoundException or similar when updating/using adventure-platform-\*, adventure-text-minimessage, adventure-api or other related libraries/tools?”](#why-am-i-getting-a-nosuchfielderror-nosuchmethoderror-classnotfoundexception-or-similar-when-updatingusing-adventure-platform--adventure-text-minimessage-adventure-api-or-other-related-librariestools)

In the case of `adventure-platform-fabric`, you need to make sure you are properly `include()`-`ing` the mod. For legacy platform implementations, you need to make sure you are properly shading and relocating your specific dependencies. Specific issues may include:

* Not shading the correct version of `adventure-api`. You can check your dependency tree to see what or why your build tool is not including the correct version of the API that matches the one used by the platform version you are using.
* Not relocating your dependencies. If you are running on a platform that includes an older version of the API, or another mod/plugin is also not properly relocating their dependencies, you will use their out-of-date version of the API, causing errors.
* Building/running against a native implementation of `adventure-api`. If you are running on a platform that includes an older version of the API, this could cause issues if the library depends on newer features that are not available in the outdated version of the API, your library will not be able to find these methods, causing errors.
* Relocating `adventure-api` and trying to use native/library methods. If you relocate the API, you will not be able to use any methods that use the API in native implementations or libraries as method signatures will differ. Either shade and relocate this software, or do not use native methods. Alternatively, if you are shading and relocating a library but want to use the API, make sure you are only relocating the packages that you are shading.

Please consult the documentation for your build tool for more information on how to shade, relocate and manage your dependencies. We do not provide one-on-one support for these sorts of issues, as there are far too many project-specific variables that make isolating issues difficult.


================================================================================
Chapter Title: Audiences
Original Link: https://docs.papermc.io/adventure/audiences/
================================================================================

An audience, at its core, is a grouping of 0 or more viewers of some content.
The concept of an audience is where Adventure makes its most clear break from
other Minecraft platforms.

As an API, `Audience` is designed to be a universal interface for any player,
command sender, console, or otherwise who can receive text, titles, boss bars,
and other Minecraft media. This allows extending audiences to cover more than
one individual receiver - possible “audiences” could include a team, server,
world, or all players that satisfy some predicate (such as having a certain
permission). The universal interface also allows reducing boilerplate by
gracefully degrading functionality if it is not applicable. For instance, it
does not make much sense to send a boss bar to a command sender, and you can’t
send titles to Minecraft 1.7 clients.

You will normally get audience instances from one of the [Platforms](https://docs.papermc.io/adventure/platform).
The Adventure API includes two audience implementations itself: one that does not
support any action (and thus does nothing). `Audience.empty()`, and one that
forwards an action to each member in the audience, `Audience.audience()` and related
methods, along with the `ForwardingAudience` that implements the forwarding logic
for you.

Most users using will primarily use this API to show content created by other parts
of the API.

## Pointers

[Section titled “Pointers”](#pointers)

Audiences can also provide arbitrary information, such as display name or UUID.
This is done using the pointer system.

Examples:

```java
// get the uuid from an audience member, returning an Optional<UUID>

audience.get(Identity.UUID);

// get the display name, returning a default

audience.getOrDefault(Identity.DISPLAY_NAME, Component.text("no display name!"));
```


================================================================================
Chapter Title: Text (Chat Components)
Original Link: https://docs.papermc.io/adventure/text/
================================================================================

Components represent Minecraft chat components.

## Creating components

[Section titled “Creating components”](#creating-components)

```java
// Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some coloring and styling.

final TextComponent textComponent = Component.text("You're a ")

.color(TextColor.color(0x443344))

.append(Component.text("Bunny", NamedTextColor.LIGHT_PURPLE))

.append(Component.text("! Press "))

.append(

Component.keybind("key.jump")

.color(NamedTextColor.LIGHT_PURPLE)

.decoration(TextDecoration.BOLD, true)

)

.append(Component.text(" to jump!"));

// now you can send `textComponent` to something, such as a client
```

You can also use a builder, which is mutable, and creates one final
component with the children.

```java
// Creates a line of text saying "You're a Bunny! Press <key> to jump!", with some coloring and styling.

final TextComponent textComponent2 = Component.text()

.content("You're a ")

.color(TextColor.color(0x443344))

.append(Component.text().content("Bunny").color(NamedTextColor.LIGHT_PURPLE))

.append(Component.text("! Press "))

.append(

Component.keybind().keybind("key.jump")

.color(NamedTextColor.LIGHT_PURPLE)

.decoration(TextDecoration.BOLD, true)

.build()

)

.append(Component.text(" to jump!"))

.build();

// now you can send `textComponent2` to something, such as a client
```

## Styling components

[Section titled “Styling components”](#styling-components)

Styles are a superset of TextColor and TextDecoration and can be applied to text components.
TextColor represents any color in the RGB spectrum.
You can also use NamedTextColor to choose from the default color palette.
The following TextDecorations are available:

* *Italic*
* **Bold**
* Strikethrough
* Underlined
* Obfuscated

## Events

[Section titled “Events”](#events)

There are currently two types of events available for text components.
Hover events allow you to show another component, item or entity when a user hovers their mouse over the text.
When a user clicks on the text component, a click event is fired which can perform one of the following actions:

* Open a URL
* Open a file
* Run a command
* Suggest a command
* Change a book’s page
* Copy a string to clipboard

## Serializing and deserializing components

[Section titled “Serializing and deserializing components”](#serializing-and-deserializing-components)

Serialization to JSON, legacy, and plain representations is also
supported.

Components can be serialized with [Text Serializers](https://docs.papermc.io/adventure/serializer).

## Using components within your application

[Section titled “Using components within your application”](#using-components-within-your-application)

The way you use components within your application will of course vary
depending on what you’re aiming to achieve.

However, the most common task is likely to be sending a component to
some sort of Minecraft client. The method for doing this will depend on
the platform your program is running on, however it is likely to involve
serializing the component to Minecraft’s JSON format, and then sending
the JSON through another method provided by the platform.

The text library is platform-agnostic and therefore doesn’t provide any
way to send components to clients. Some platforms implement [Adventure natively](https://docs.papermc.io/adventure/platform/native), so `Components`
can be directly used with their API. For other platforms (Spigot/Bukkit, BungeeCord, and SpongeAPI 7),
we provide compatibility bridges as [Platforms](https://docs.papermc.io/adventure/platform) which can be distributed with your own plugins.


================================================================================
Chapter Title: Overview
Original Link: https://docs.papermc.io/adventure/serializer/
================================================================================

The lowest-level way to convert between Adventure’s data and other formats
are serializers. Some serializers convert to standard formats, while others
convert to Adventure’s own formats.

* [JSON](https://docs.papermc.io/adventure/serializer/json)
* [Gson](https://docs.papermc.io/adventure/serializer/gson)
* [Legacy](https://docs.papermc.io/adventure/serializer/legacy)
* [Plain](https://docs.papermc.io/adventure/serializer/plain)
* [MiniMessage](https://docs.papermc.io/adventure/minimessage)

Components can be converted using any of these serializers:

```java
// Creates a text component

final TextComponent textComponent = Component.text()

.content("Hello ")

.color(NamedTextColor.GOLD)

.append(Component.text("world", NamedTextColor.AQUA, TextDecoration.BOLD))

.append(Component.text("!", NamedTextColor.RED))

.build();

// Converts textComponent to the JSON form used for serialization by Minecraft.

final String json = JSONComponentSerializer.json().serialize(textComponent);

// Converts textComponent to a legacy string - "&6Hello &b&lworld&c!"

final String legacy = LegacyComponentSerializer.legacyAmpersand().serialize(textComponent);

// Converts textComponent to a plain string - "Hello world!"

final String plain = PlainTextComponentSerializer.plainText().serialize(textComponent);
```

The same is of course also possible in reverse for deserialization.

```java
// Converts JSON in the form used for serialization by Minecraft to a Component

final Component component = JSONComponentSerializer.json().deserialize(json);

// Converts a legacy string (using formatting codes) to a TextComponent

final Component component = LegacyComponentSerializer.legacyAmpersand().deserialize("&6Hello &b&lworld&c!");

// Converts a plain string to a TextComponent

final Component component = PlainTextComponentSerializer.plainText().deserialize("Hello world!");
```

## Text encoders

[Section titled “Text encoders”](#text-encoders)

Text encoders are similar to serializers, but they only provide one-way
operations, allowing for serialization but not deserialization.

* [ANSI](https://docs.papermc.io/adventure/serializer/ansi)


================================================================================
Chapter Title: JSON
Original Link: https://docs.papermc.io/adventure/serializer/json/
================================================================================

The JSON serializer provides a common interface for serializer implementations that translate between a Component and JSON strings. This allows a library to support any underlying JSON library that an application may want to use.

## Use

[Section titled “Use”](#use)

The JSON serializer works similar to all others, providing the basic serialize and deserialize operations:

```java
// Component to text

final String jsonText = JSONComponentSerializer.json().serialize(Component.text("Hello world", NamedTextColor.LIGHT_PURPLE));

// JSON string to component

final Component comp = JSONComponentSerializer.json().deserialize(jsonText);
```

Additionally, there is a `JSONComponentSerializer.builder()` available for advanced use that requires configuring legacy compatibility options.

## Known implementations

[Section titled “Known implementations”](#known-implementations)

| Name | Description |
| --- | --- |
| [adventure-text-serializer-gson](https://docs.papermc.io/adventure/serializer/gson) | A mature serializer working with Google’s Gson library. |


================================================================================
Chapter Title: Gson
Original Link: https://docs.papermc.io/adventure/serializer/gson/
================================================================================

The Gson text serializer converts chat components to their JSON representation
and back using the Gson library. If you are interested in sending a chat component
for display in a Minecraft client, or want to support advanced chat component features,
you should use the Gson text serializer.

An average user of this text serializer will typically want to only deserialize a
component from an external source - serialization is done automatically by the
[Platforms](https://docs.papermc.io/adventure/platform) when the component is sent to the user.

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-30)
* [Gradle (Groovy)](#tab-panel-31)
* [Maven](#tab-panel-32)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-text-serializer-gson:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-text-serializer-gson:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-text-serializer-gson</artifactId>

<version>4.26.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

In Minecraft 1.16, Mojang made several major changes to the JSON chat format, adding
RGB chat colors and changing how hover events are serialized. Components generated for
older versions of Minecraft will still be able to be displayed in a 1.16 client,
however components serialized for a 1.16 client will not be able to be displayed in
a Minecraft 1.15.2 client or lower.

To get a serializer that works with 1.16 clients and above, use
`GsonComponentSerializer.gson()`. To get a serializer that works with all versions
of Minecraft that support text components, use `GsonComponentSerializer.colorDownsamplingGson()`.
This serializer downsamples RGB colors to the closest Mojang legacy color and serializes
hover events in a way that is backwards compatible with older clients.

### Which serializer should I use?

[Section titled “Which serializer should I use?”](#which-serializer-should-i-use)

If all you’re doing is loading and saving components to a configuration file or a database,
you probably want to use the default 1.16 serializer.

If you’re looking to send a component to a client, first consider whether you can one of the
provided platforms. If you can’t use a platform, generally you should prefer the default
serializer for deserializing components (as it is backwards-compatible), and make a decision
on whether to use the default or the color downsampling serializer based on the version the
client is on.

### Advanced usage

[Section titled “Advanced usage”](#advanced-usage)

The Gson serializer exposes both the backing `Gson` instance and a populator that allows
registering Adventure serializers on any `GsonBuilder` instance.


================================================================================
Chapter Title: Legacy
Original Link: https://docs.papermc.io/adventure/serializer/legacy/
================================================================================

The legacy text serializer converts text to and from the traditional chat format used
in Minecraft prior to Minecraft 1.7, and continues to be used to this day for its
familiarity to server owners.

The legacy text serializer does not support most advanced features, including hover
and click events, components besides text components, and insertions. RGB colors
are supported (see more in the [RGB support](#rgb-support) section) and URLs can be transformed
into clickable components if explicitly requested (note, however, that click events
containing a URL will *not* be serialized). If advanced features are desired, consider
using [MiniMessage](https://docs.papermc.io/adventure/minimessage).

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-33)
* [Gradle (Groovy)](#tab-panel-34)
* [Maven](#tab-panel-35)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-text-serializer-legacy:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-text-serializer-legacy:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-text-serializer-legacy</artifactId>

<version>4.26.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

The legacy text serializer is accessed using the `LegacyComponentSerializer`. The default
pre-provided serializers include one that uses the section symbol (§) (for display in
old clients) and another that uses an ampersand (&) typically used in configuration and
commands to specify color codes.

The default configuration for the legacy text serializer will deserialize all three of
the RGB formats supported by Adventure but will only serialize legacy Mojang colors
(downsampling to the nearest color as needed) and does not transform URLs in text to
links. You can configure an instance to automatically add click events to URLs in
components and allow the serializer to serialize RGB colors in either the Adventure
RGB format or the BungeeCord RGB format using the builder.

## RGB support

[Section titled “RGB support”](#rgb-support)

The legacy serializer supports deserializing three different formats:

* Legacy Mojang color and formatting codes (such as `§a` or `§l`).
* An Adventure-specific RGB format that is intended to be easy to edit
  (such as `§#a25981`).
* A BungeeCord RGB color code format that is backwards compatible with
  older deserialization routines but is difficult to manipulate and makes
  it the user’s responsibility to assign a fallback for non-RGB clients (such
  as `§x§a§2§5§9§8§1`).

The legacy serializer downsamples RGB colors by default, but you can create a serializer
that serializes RGB colors in either the Adventure or BungeeCord RGB formats using the
builder.


================================================================================
Chapter Title: Plain
Original Link: https://docs.papermc.io/adventure/serializer/plain/
================================================================================

The plain text serializer converts chat components to their plain-text representation
and back. It is thus the simplest text serializer in Adventure. This serializer is
useful for supporting legacy clients, logging, clearing formatting from a component that
originates from external source, and provides a small, self-contained example of a
text serializer.

The plain text serializer, by its nature, does not support any advanced features, including
color, hover and click events, URL linking, or insertions. If advanced features are desired,
consider using [MiniMessage](https://docs.papermc.io/adventure/minimessage).

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-36)
* [Gradle (Groovy)](#tab-panel-37)
* [Maven](#tab-panel-38)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-text-serializer-plain:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-text-serializer-plain:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-text-serializer-plain</artifactId>

<version>4.26.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

This produces a default instance that silently ignores keybind and translatable components. You can also construct your own
`PlainTextComponentSerializer` that maps the components to some plain-text representation.

The deserialization of plain text is equivalent to `Component.text(string)`. No
preprocessing is done on the input. The deserialization is implemented in order to provide
API consistency.


================================================================================
Chapter Title: Overview
Original Link: https://docs.papermc.io/adventure/minimessage/
================================================================================

The MiniMessage format is a simple string representation of chat components, designed to be easy for end users to learn, and for developers to extend.

```java
Hello <rainbow>world</rainbow>, isn't <blue><u><click:open_url:'https://docs.advntr.dev/minimessage'>MiniMessage</click></u></blue> fun?
```

If you’re looking to write messages with MiniMessage, take a look at the [MiniMessage Format](https://docs.papermc.io/adventure/minimessage/format), or if you’re looking to develop software that uses MiniMessage, take a look at the [API overview](https://docs.papermc.io/adventure/minimessage/api).

* [Format](https://docs.papermc.io/adventure/minimessage/format)
* [API](https://docs.papermc.io/adventure/minimessage/api)
* [Dynamic replacements](https://docs.papermc.io/adventure/minimessage/dynamic-replacements)
* [MiniMessage translator](https://docs.papermc.io/adventure/minimessage/translator)


================================================================================
Chapter Title: Format
Original Link: https://docs.papermc.io/adventure/minimessage/format/
================================================================================

The MiniMessage language uses tags. Everything you do will be defined with tags. Tags have a start tag and an end tag (the `<reset>` tag is an exception here).
Start tags are mandatory (obviously), but end tags aren’t outside of `strict` mode. The following are all visually identical:

```java
<yellow>Hello <blue>World<yellow>!

<yellow>Hello <blue>World</blue>!

<yellow>Hello </yellow><blue>World</blue><yellow>!</yellow>
```

For tags with no content, tags can be auto-closed by using the format `<tag/>`. With this format, even in strict mode no separate closing tag should be provided.

All tag names are case-insensitive to reduce the possibility for conflict, but we recommend keeping all tag names lowercase (or at the very least, being consistent).

Some tags have argument. Those look like this: `<tag:argument>stuff</tag>`.
For example:

```java
<hover:show_text:"<red>test:TEST">TEST

<click:run_command:test>TEST
```

As you can see, those sometimes contain components, sometimes just numbers, strings, or other types. Refer to the detailed docs below.

Single (`'`) and double (`"`) quotes can be used interchangeably. We recommend staying consistent, though in order to minimize escaping it might make more sense to switch quote types for some arguments.

Any meaningful token can be escaped in the locations where they have influence. In plain text, tag open characters (`<`) can be escaped with a leading backslash (`\`). Within quoted strings,
the opening quote character can be escaped (`'` or `"`). In either place, the escape character can be escaped in places where it would otherwise be relevant. Unquoted tag arguments cannot have escapes, for simplicity.
In locations where escaping is not supported, the literal escape character will be passed through. In locations where escaping *is* supported but a literal escape character is desired, the escape character can itself be escaped to produce a `\`.

The default tags try to represent components in a manner compatible with Vanilla, but simplifying some elements. It might be helpful to
use [the Minecraft wiki](https://minecraft.wiki/w/Text_component_format) as a reference for the Vanilla component system, especially
for things like the actions and values of click and hover events.

The [MiniMessage Web Viewer](https://webui.advntr.dev) allows testing MiniMessage text locally, without having to spin up a Minecraft instance.
It can be helpful to put examples from these docs into the viewer while learning.

## Strict mode

[Section titled “Strict mode”](#strict-mode)

By default, MiniMessage is extremely lenient, and any invalid tags will just be ignored. Any tags left unclosed at the end of an input string will be automatically closed.

Applications can optionally enable *strict mode*, which prohibits using `<reset>`, and requires all tags to be closed in reverse order of opening. Any application
using MiniMessage should make it clear to end users which language variant is being used.

## Standard tags

[Section titled “Standard tags”](#standard-tags)

These are the tags included and enabled by default in MiniMessage. Specific parses of MiniMessage may add custom tags to this list, or restrict the available tags to a subset of this list. Consult application documentation for details.

### Color

[Section titled “Color”](#color)

Color the next parts

Tag

* `<_colorname_>`

Arguments

* `_colorname_`, any minecraft color constant: `black`, `dark_blue`, `dark_green`, `dark_aqua`, `dark_red`, `dark_purple`, `gold`, `gray`, `dark_gray`, `blue`, `green`, `aqua`, `red`, `light_purple`, `yellow`, or `white`.

  `dark_grey` can be used in place of `dark_gray`, and so can `grey` in place of `gray`.
  Hex colors are supported as well, with the format `#RRGGBB`.

Examples

```java
<yellow>Hello <blue>World</blue>!

<red>This is a <green>test!

<#00ff00>R G B!
```

  
![The result of parsing `<yellow>Hello <blue>World</blue>!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/color_1.IcvdrsE-_ZhRgTT.webp)
![The result of parsing `<red>This is a <green>test!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/color_2.lNFDCgYx_9quus.webp)

### Color (verbose)

[Section titled “Color (verbose)”](#color-verbose)

A more verbose way of defining colors

Tag

* `<color:_colorNameOrHex_>`

Aliases

* `colour`, `c`

Arguments

* `_colorNameOrHex_`, can be any of the values from above (so named colors or hex colors)

Examples

```java
<color:yellow>Hello <color:blue>World</color:blue>!

<color:#FF5555>This is a <color:#55FF55>test!
```

  
![The result of parsing `<color:yellow>Hello <color:blue>World</color:blue>!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/color_1.IcvdrsE-_ZhRgTT.webp)
![The result of parsing `<color:#FF5555>This is a <color:#55FF55>test!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/color_2.lNFDCgYx_9quus.webp)

### Shadow Color

[Section titled “Shadow Color”](#shadow-color)

Color the shadow of the next parts

Tag

* `<shadow:_colorNameOrHex_:[alpha_as_float]>`
* `<!shadow>` as an alias to disable the shadow (equivalent to `<shadow:#00000000>`)

Arguments

* `_colorNameOrHex_`, a named color or hex color string with the format `#RRGGBB` or `#RRGGBBAA`
* `[alpha_as_float]`, a float value between 0 and 1, representing the alpha value of the shadow. Optional, defaults to 0.25. Has no effect if an alpha value is already provided in the hex color string.

Examples

```java
<shadow:yellow>Hello <shadow:aqua:0.5>World</shadow>!

<shadow:#FF5555>This is a <shadow:#55FF55>test!

<shadow:#000000FF><b>Thicc
```

  
![The result of parsing `<shadow:yellow>Hello <shadow:aqua:0.5>World</shadow>!` shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/shadow_1.BKCci3At_1BQXBk.webp)
![The result of parsing `<shadow:#FF5555>This is a <shadow:#55FF55>test!` shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/shadow_2.kx89mZsr_Z5AKy4.webp)
![The result of parsing `<shadow:#000000FF><b>Thicc` shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/shadow_3.DB_UDhhl_2oD0b.webp)

### Decoration

[Section titled “Decoration”](#decoration)

Decorate the next parts

Tag

* `<_decorationname_[:false]>`, or `<!_decorationname_>` as an alias to invert the decoration.

Arguments

* `_decorationname_`, Any decoration supported in Minecraft:

| Decoration | Aliases |
| --- | --- |
| `bold` | `b` |
| `italic` | `em` or `i` |
| `underlined` | `u` |
| `strikethrough` | `st` |
| `obfuscated` | `obf` |

Examples

```java
<underlined>This is <bold>important</bold>!
```

  
![The result of parsing `<underlined>This is <bold>important</bold>!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/decoration_1.YHM0gk3g_Z2qhVv5.webp)

### Reset

[Section titled “Reset”](#reset)

Close all currently open tags, resetting color/decoration/etc. The reset tag cannot be closed.

In strict mode, reset tags are forbidden.

Tag

* `<reset>`

Arguments

* none

Examples

```java
<yellow><bold>Hello <reset>world!
```

  
![The result of parsing `<yellow><bold>Hello <reset>world!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/reset_1.CaE1z_qU_IVz8K.webp)

### Click

[Section titled “Click”](#click)

Allows doing multiple things when clicking on the component.

Tag

* `<click:_action_:_value_>`

Arguments

* `_action_`, the type of click event, one of [this list](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/ClickEvent.Action.html#enum.constant.summary)
* `_value_`, the argument for that particular event, refer to [the minecraft wiki](https://minecraft.wiki/w/Text_component_format)

Examples

```java
<click:run_command:/seed>Click</click> to show the world seed!

Click <click:copy_to_clipboard:Haha you suck> this </click>to copy your score!
```

  
![The result of parsing `<click:run_command:/seed>Click</click> to show the world seed!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/click_1.Dlx2nqaC_4OtA4.webp)

Caution

Since the introduction of chat signatures in 1.19.1, the client no longer executes commands that require signed arguments
like the `/say` or `/tell` command to prevent the server from sending signed messages on the client’s behalf.

### Hover

[Section titled “Hover”](#hover)

Allows doing multiple things when hovering on the component.

Tag

* `<hover:_action_:_value..._>`

Arguments

* `_action_`, the type of hover event, one of this [list](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/event/HoverEvent.Action.html#field.summary)
* `_value..._`, arguments specific to each event action:

| Action | Value |
| --- | --- |
| `show_text` | `_text_` (a MiniMessage string) |
| `show_item` | `_type_[:_count_[:tag]]` (a `Key` for the item’s type, optionally followed by count (an integer) and tag (a SNBT string)) |
| `show_entity` | `_type_:_uuid_[:_name_]` (a `Key` ID of the entity type, the entity’s UUID, and an optional custom name) |

Examples

```java
<hover:show_text:'<red>test'>TEST
```

  
![The result of parsing `<hover:show_text:'<red>test'>TEST`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/hover_1.D4vGWpwW_1UUGvg.webp)

### Keybind

[Section titled “Keybind”](#keybind)

Allows displaying the configured key for actions

Tag

* `<key:_key_>`

Arguments

* `_key_`, the keybind identifier of the action

Examples

```java
Press <red><key:key.jump> to jump!
```

  
![The result of parsing `Press <red><key:key.jump> to jump!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/key_1.CJD6vo1W_23jqWf.webp)

### Translatable

[Section titled “Translatable”](#translatable)

Allows displaying minecraft messages using the player locale

Tag

* `<lang:_key_:_value1_:_value2_...>`

Aliases

* `tr`, `translate`

Arguments

* `_key_`, the translation key
* `_valueX_`, optional values that are used for placeholders in the key (they will end up in the `with` tag in the JSON)

Examples

```java
You should get a <lang:block.minecraft.diamond_block>!

<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!
```

  
![The result of parsing `You should get a <lang:block.minecraft.diamond_block>!`, shown in-game in the Minecraft client's chat window in English](https://docs.papermc.io/_astro/translatable_1.DfyS0jwu_ZJoXsP.webp)
![The result of parsing `<lang:commands.drop.success.single:'<red>1':'<blue>Stone'>!`, shown in-game in the Minecraft client's chat window in English](https://docs.papermc.io/_astro/translatable_2.x3w4Igoy_Z2hVj72.webp)

### Fallback

[Section titled “Fallback”](#fallback)

Note

The fallback option is only available since Minecraft 1.19.4.

Allows displaying minecraft messages using the player locale, or a fallback if no text is available

Tag

* `<lang_or:_key_:_fallback_:_value1_:_value2_...>`

Aliases

* `tr_or`, `translate_or`

Arguments

* `_key_`, the translation key
* `_fallback_`, the fallback text to display
* `_valueX_`, optional values that are used for placeholders in the key (they will end up in the `with` tag in the JSON)

Examples

```java
You should get a <lang_or:block.minecraft.diamond_block:'Dirt Block'>!
```

### Insertion

[Section titled “Insertion”](#insertion)

Allow insertion of text into chat via shift click

Tag

* `<insert:_text_>`

Arguments

* `_text_`, the text to insert

Examples

```java
Shift-click <insert:test>this</insert> to insert!
```

  
![The result of parsing `Shift-click <insert:test>this</insert> to insert!`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/insertion_1.BQGGa26X_xJf2q.webp)

### Rainbow

[Section titled “Rainbow”](#rainbow)

Rainbow-colored text?!

Tag

* `<rainbow:[!][phase]>`

Arguments

* phase, optional
* `!`, literal value which reverses the rainbow, optional

Examples

```java
<yellow>Woo: <rainbow>||||||||||||||||||||||||</rainbow>!

<yellow>Woo: <rainbow:!>||||||||||||||||||||||||</rainbow>!

<yellow>Woo: <rainbow:2>||||||||||||||||||||||||</rainbow>!

<yellow>Woo: <rainbow:!2>||||||||||||||||||||||||</rainbow>!
```

  
![The result of parsing all four examples in series, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/rainbow_1.BiomJch9_lGn2N.webp)

### Gradient

[Section titled “Gradient”](#gradient)

Gradient colored text

Tag

* `<gradient:[color1]:[color...]:[phase]>`

Arguments

* a list of 1 to n colors, either hex or named colors and an optional phase parameter (range -1 to 1) allows you to shift the gradient around, creating animations.

Examples

```java
<yellow>Woo: <gradient>||||||||||||||||||||||||</gradient>!

<yellow>Woo: <gradient:#5e4fa2:#f79459>||||||||||||||||||||||||</gradient>!

<yellow>Woo: <gradient:#5e4fa2:#f79459:red>||||||||||||||||||||||||</gradient>!

<yellow>Woo: <gradient:green:blue>||||||||||||||||||||||||</gradient>!
```

  
![The result of parsing the examples for the gradient tag, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/gradient_1.BJ83LXbF_Z1xKTo6.webp)

### Transition

[Section titled “Transition”](#transition)

Transitions between colors.
Similar to a gradient, but everything is the same color and the phase chooses that color

Tag

* `<transition:[color1]:[color...]:[phase]>`
  Arguments
* a list of 1 to n colors, either hex or named colors and an optional phase parameter (range -1 to 1) allows you to shift the transition around, creating animations.
  Examples

```java
<transition:#00ff00:#ff0000:0>|||||||||</transition>

<transition:white:black:red:[phase]>Hello world [phase]</transition>
```

  
![The result of parsing `<transition:white:black:red:[phase]>Hello World [phase]</transition>`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/transition_1.C8s6W3Vr_D6Ea4.webp)

### Font

[Section titled “Font”](#font)

Allows to change the font of the text

Tag

* `<font:key>`

Arguments

* the namespaced key of the font, defaulting to `minecraft`

Examples

```java
Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform

<font:myfont:custom_font>Uses a custom font from a resource pack</font>
```

  
![The result of parsing `Nothing <font:uniform>Uniform <font:alt>Alt  </font> Uniform`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/font_1.C16TEtLm_ZS9WVt.webp)

### Newline

[Section titled “Newline”](#newline)

Insert a newline character.

Tag

* `<newline>`

Aliases

* `br`

Arguments

* none

Examples

```java
Let me insert a <newline>line break here.

<hover:show_text:'<red>Hover with a<newline><green>line break'>Text with<newline>line break</hover>
```

  
![The result of parsing `<hover:show_text:'<red>Hover with a<newline><green>line break'>Text with<newline>line break</hover>`, shown in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/newline_1.DYHjw1ME_Z2wwfj3.webp)

### Selector

[Section titled “Selector”](#selector)

*(since v4.11.0)* Insert a selector component

Tag

* `<selector:_sel_[:_separator_]>`

Aliases

* `sel`

Arguments

* `_sel_`, the selector pattern to insert
* `_separator_` (optional), the separator to insert between values the selector matches

Examples

```java
Hello <selector:@e[limit=5]>, I'm <selector:@s>!
```

  
![The result of parsing `Hello <selector:@e[limit=5]>, I'm <selector:@s>!`, show in-game in the Minecraft client's chat window](https://docs.papermc.io/_astro/selector_1.B99vc1oz_Z29VxoV.webp)

### Score

[Section titled “Score”](#score)

*(since v4.13.0)* Insert a score component.

Note

The score component requires *rendering* on the server to be seen by clients. This is a platform-specific operation.

Tag

* `<score:_name_:_objective_>`

Arguments:

* `_name_`, the name of the score holder on the server scoreboard, or a selector resolved with receiver context
* `_objective_`, the name of the objective to get `name`’s score in

Examples

```java
You have won <score:rymiel:gamesWon/> games!
```

### NBT

[Section titled “NBT”](#nbt)

*(since v4.13.0)* Insert a NBT component. The syntax of this tag is intended to be familiar to users of vanilla Minecraft’s `/data` command.

Note

The produced NBT component requires *rendering* on the server to be seen by clients. This is a platform-specific operation.

Tag

* `<nbt:block|entity|storage:id:path[:_separator_][:interpret]>`

Aliases

* `data`

Arguments:

* `block|entity|storage` the type of data source to read from — a `block` entity, an `entity` selector, or the persistent command `storage` container
* `_id_`, the position for a block NBT component, a selector for an entity NBT component, or a key (resource location) for a storage NBT component
* `_path_`, the NBT path to resolve from within the data source
* `_separator_`, the separator between multiple values, if (primarily for entity NBT) the data source returns more than one
* `interpret`, the literal text `interpret` if the result should be parsed as component JSON

Examples

```java
Your health is <nbt:entity:'@s':Health/>
```

### Pride

[Section titled “Pride”](#pride)

*(since v4.18.0)* Colors the text inside the tags with a gradient corresponding to a pride flag.

Tag

* `<pride[:flag|phase]>`

Arguments

* `flag` the flag to use, may be one of pride, progress, trans, bi, pan, nb, lesbian, ace, agender, demisexual, genderqueer, genderfluid, intersex, aro, baker, philly, queer, gay, bigender or demigender.
* `phase` phase, a number between -1 and 1, optional

Examples

```java
Happy <pride>pride month</pride>!

Kyori supports <pride:trans>trans rights</pride>!
```

### Sprite

[Section titled “Sprite”](#sprite)

*(since v4.25.0)* Inserts a sprite.

Tag

* `<sprite[:atlas]:sprite>`

Arguments

* `atlas` the atlas to use, e.g. `minecraft:blocks`.
* `sprite` the sprite to use, e.g. `item/emerald`.

Examples

```java
Look at my <sprite:blocks:block/stone>!

This item costs 10 x <sprite:"minecraft:items":item/porkchop>.
```

### Head

[Section titled “Head”](#head)

*(since v4.25.0)* Inserts a player head.

Tag

* `<head:name|uuid|texture[:outer_layer]>`

Arguments

* `name|uuid|texture` the name, UUID or path to the texture of the skin to use to draw the head.
* `outer_layer` either `true` or `false`, determines if the outer layer (or “hat” layer) should be drawn.
  Defaults to `true`.

Examples

```java
My favorite dev is <head:1f085b2d-9548-4159-a8c7-f3ccdf0c2054>.

Do you prefer <head:entity/player/wide/steve> Steve or <head:entity/player/slim/alex> Alex?

Thanks <head:Strokkur24:false> for the docs!
```


================================================================================
Chapter Title: MiniMessage API
Original Link: https://docs.papermc.io/adventure/minimessage/api/
================================================================================

## Dependency

[Section titled “Dependency”](#dependency)

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-6)
* [Gradle (Groovy)](#tab-panel-7)
* [Maven](#tab-panel-8)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-text-minimessage:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-text-minimessage:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-text-minimessage</artifactId>

<version>4.26.1</version>

</dependency>
```

  

Note

Some platforms already provide MiniMessage natively. In this case you will not need to add MiniMessage as a dependency.

## Getting started

[Section titled “Getting started”](#getting-started)

MiniMessage exposes a simple API via the `MiniMessage` class.

A standard instance of the serializer is available through the `miniMessage()` method. This uses the default set of tags and is not in strict mode.

Additional customization of MiniMessage is possible via the [Builder](#builder).

MiniMessage allows you to both serialize components into MiniMessage strings and to parse/deserialize MiniMessage strings into components.

Here’s a short example to try things out:

```java
Audience player = ...;

MiniMessage mm = MiniMessage.miniMessage();

Component parsed = mm.deserialize("Hello <rainbow>world</rainbow>, isn't <underlined>MiniMessage</underlined> fun?");

player.sendMessage(parsed);
```

For more advanced uses, additional tag resolvers can be registered, which when given a tag name and arguments will produce a `Tag` instance. These are described in more detail below.

### Builder

[Section titled “Builder”](#builder)

To make customizing MiniMessage easier, we provide a Builder. The specific methods on the builder are explained in the javadoc.

```java
MiniMessage minimessage = MiniMessage.builder()

.tags(TagResolver.builder()

.resolver(StandardTags.color())

.resolver(StandardTags.decorations())

.resolver(this.someResolvers)

.build()

)

.build();
```

Tip

It’s a good idea to initialize such a MiniMessage instance once, in a central location, and then use it for all your messages.
Exception being if you want to customize MiniMessage based on permissions of a user (for example, admins should be allowed to use color and decoration in the message, normal users not)

### Error handling

[Section titled “Error handling”](#error-handling)

By default, MiniMessage will never throw an exception caused by user input. Instead, it will treat any invalid tags as normal text. `MiniMessage.Builder#strict(true)` mode will enable strict mode,
which throws exceptions on unclosed tags, but still will allow any improperly specified tags through.

To capture information on why a parse may have failed, `MiniMessage.Builder#debug(Consumer<String>)` can be provided, which will accept debug logging for an input string.

## Tag resolvers

[Section titled “Tag resolvers”](#tag-resolvers)

All tag resolution goes through tag resolvers. There is one global tag resolver, which describes the tags available through a `MiniMessage` instance, plus parse-specific resolvers which can provide additional input-specific tags.

Tag resolvers are the binding between a name and arguments, and the logic to produce a `Component` contained in a `Tag` instance. They are composable so a `TagResolver` can produce any number of actual `Tag` instances. The tag name passed to resolvers will always be lower-cased, to ensure case-insensitive searches.

Tag names are only allowed to contain the characters a-z, 0-9, `_`, and `-`. They can also optionally start with any of the following characters: `!?#`.

You can create your own `TagResolver` by using the static factory methods in `TagResolver`. To replace tags dynamically with text MiniMessage has built-in `Placeholder` and `Formatter`.
Where possible, these built-in resolvers should be used, as MiniMessage can flatten combinations of these resolvers into a more efficient format.
For built-in dynamic replacements take a look [here](https://docs.papermc.io/adventure/minimessage/dynamic-replacements).

To combine multiple resolvers, take a look at the tag resolver builder, `TagResolver.builder()`.

The builder for `MiniMessage` allows providing a custom tag resolver rather than the default (`StandardTags.all()`), allowing

MiniMessage also provides convenience methods to do that:

```java
MiniMessage serializer = MiniMessage.builder()

.tags(TagResolver.builder()

.resolver(StandardTags.color())

.build()

)

.build();

Component parsed = serializer.deserialize("<green><bold>Hai");

// Assertion passes

assertEquals(Component.text("<bold>Hai", NamedTextColor.GREEN), parsed);
```

Because the `<bold>` tag is not enabled on this builder, the bold tag is interpreted as literal text.

### Handling arguments

[Section titled “Handling arguments”](#handling-arguments)

Tag resolvers have an `ArgumentQueue` parameter, which provides any tag arguments that are present in the input. Helper methods on `Tag.Argument` can assist with conversions of the tag.

Exceptions thrown by the `popOr()` methods will interrupt execution, but are not currently exposed to users outside of debug output. We plan to add an auto-completion function that can
reveal some of this information to the user, so please do try to write useful error messages in custom tag resolvers.

## Tags

[Section titled “Tags”](#tags)

Once a tag resolver has handled arguments, it returns a `Tag` object. These objects implement the logic of producing or modifying a component tree. There are three main kinds of `Tag` — all custom implementations must implement one of these interfaces.

### Pre-process

[Section titled “Pre-process”](#pre-process)

These tags implement the `PreProcess` interface, and have a value of a raw MiniMessage string that is replaced into the user input before parsing continues.

Due to limitations in the current parser implementation, note that pre-process tags will adjust offsets in error messages, and may inhibit tab completion. However, they are currently the only way to integrate markup fragments into a message.

### Inserting

[Section titled “Inserting”](#inserting)

These tags are fairly straightforward: they represent a literal `Component`. The vast majority of Tag implementations will want
to be `Inserting` tags. `Inserting` tags may also optionally be self-closing — by default, this is only true for tags created by `Placeholder.unparsed(String)` and `Placeholder.component(Component)`,
so that placeholders are self-contained.

Most `standard tags <./format>` are `Inserting`. These tags will either directly insert a component, or use the helper `Tag.styling(StyleBuilderApplicable...)` to apply style to components.

This helper can be used to efficiently apply a collection of styles with one tag. For example, to create a `<a:[href]>Title</a>` tag, that makes the `Title` text into a link that opens a URL with traditional link styling, this could be used:

```java
Component aTagExample() {

final String input = "Hello, <a:https://docs.advntr.dev>click me!</a> but not me!";

final MiniMessage extendedInstance = MiniMessage.builder()

.editTags(b -> b.tag("a", MiniMessageTest::createA))

.build();

return extendedInstance.deserialize(input);

}

static Tag createA(final ArgumentQueue args, final Context ctx) {

final String link = args.popOr("The <a> tag requires exactly one argument, the link to open").value();

return Tag.styling(

NamedTextColor.BLUE,

TextDecoration.UNDERLINED,

ClickEvent.openUrl(link),

HoverEvent.showText(Component.text("Open " + link))

);

}
```

This allows producing rich styling relatively quickly.

### Modifying

[Section titled “Modifying”](#modifying)

Modifying tags are the most complex, and most specialized of the tag types available. These tags receive the node tree and have an opportunity to analyze it before
components are constructed, and then receive every produced child component and can modify those children. This is used for the built-in `<rainbow>` and `<gradient>` tags,
but can be applied for similar complex transformations.

Modifying tags are first given an opportunity to visit every node of the tree in a depth-first traversal. If a `Modifying` instance stores any state during this traversal, its resolver should return a new instance every time to prevent state corruption.

Note

The `Node` API in 4.10.0 is currently not very well developed — most aspects are still internal. Additional information can be exposed as needed by tag developers.

Once the whole parse tree has been visited, the `postVisit()` method is called. This method can optionally be overridden if any additional calculations must be performed.

Next, the `Modifying` instance enters the application phase, where the component tree is presented to the tag for transformation. This allows the tag to *modify* the contents of these components, giving it its name.

### Parser directives

[Section titled “Parser directives”](#parser-directives)

Parser directives are a special kind of tag, as they are instructions for the parser, and therefore cannot be implemented by end users.

There is currently only one, but more may be added at any time.

| Directive | Description |
| --- | --- |
| RESET | This indicates to the parser that this tag should close all currently open tags. |

This can be used to provide the functionality of a `<reset>` tag under a different name. For example:

```java
final var clearTag = TagResolver.resolver("clear", ParserDirective.RESET);

final var parser = MiniMessage.builder()

.editTags(t -> t.resolver(clearTag))

.build();

final Component parsed = parser.deserialize("<red>hello <bold>world<clear>, how are you?");
```

This code would add a `<clear>` tag, behaving identically to the `<reset>` tag available by default — ”, how are you?” would not be bold or colored red.


================================================================================
Chapter Title: Dynamic replacements
Original Link: https://docs.papermc.io/adventure/minimessage/dynamic-replacements/
================================================================================

MiniMessage has some included `TagResolver` s which can replace tags dynamically when parsing those. Those resolvers can replace a tag with dynamic input such as a string or a formatted number.

## Placeholders

[Section titled “Placeholders”](#placeholders)

Placeholders replace the tag with a specific text. Those are the most basic replacements:

### Insert a component

[Section titled “Insert a component”](#insert-a-component)

You can simply insert a component for the tag with the component placeholder.

```java
MiniMessage.miniMessage().deserialize("<gray>Hello <name> :)", Placeholder.component("name", Component.text("TEST", NamedTextColor.RED)));
```

This will insert the red text component “TEST” for the tag name.

### Insert some unparsed text

[Section titled “Insert some unparsed text”](#insert-some-unparsed-text)

Sometimes it’s better to not parse dynamic text such as user inputs. For those things MiniMessage provides the unparsed placeholder.
With this method you can sanitize user input without escaping the tags directly.

```java
MiniMessage.miniMessage().deserialize("<gray>Hello <name>", Placeholder.unparsed("name", "<red>TEST :)"));
```

This will insert the text without parsing. The result will be a gray text with `Hello <red>TEST :)`.

### Insert and parse text

[Section titled “Insert and parse text”](#insert-and-parse-text)

When you want to insert a text and allow MiniMessage to parse the tags you can use the parsed placeholder.
The parsed placeholder will insert the replacement before parsing the string. The tags in the placeholder can affect the parsed result after the placeholder.

```java
MiniMessage.miniMessage().deserialize("<gray>Hello <name> :)", Placeholder.parsed("name", "<red>TEST"));

// returns Component.text("Hello ", NamedTextColor.GRAY).append(Component.text("TEST :)", NamedTextColor.RED));
```

This will insert and parse the text.

### Insert a style

[Section titled “Insert a style”](#insert-a-style)

When you want to create your own styling tag you can use the styling placeholder.

```java
MiniMessage.miniMessage().deserialize("<my-style>Hello :)</my-style> How are you?",

Placeholder.styling("my-style", ClickEvent.suggestCommand("/say hello"), NamedTextColor.RED, TextDecoration.BOLD));

// will apply a click event, a red text color and bold decoration to the text
```

This will insert the style with a click event and a red text. Styling placeholders can be used for any style, e.g. colors, text decoration and events.

Create your own styling tags:

```java
Placeholder.styling("fancy", TextColor.color(150, 200, 150)); // will replace the color between "<fancy>" and "</fancy>"

Placeholder.styling("myhover", HoverEvent.showText(Component.text("test"))); // will display your custom text as hover

Placeholder.styling("mycmd", ClickEvent.runCommand("/mycmd is cool")); // will create a clickable text which will run your specified command.
```

Tip

Styling placeholders can be used to sanitize input from players in click events. Instead of using a parsed placeholder the string can be used directly.

## Formatters

[Section titled “Formatters”](#formatters)

Not everything is a text, sometimes its useful to display a number or a date.
For that you can use the provided formatters from MiniMessage

### Insert a number

[Section titled “Insert a number”](#insert-a-number)

You can insert a `Number` by using the number formatter in MiniMessage.

To specify the locale and format of the number the formatter accepts optionally tag arguments.
You can specify the locale and the number format. It’s possible to pass both as arguments to the tag but you have provide the locale first.

```java
MiniMessage.miniMessage().deserialize("<gray>Hello my number <no>!", Formatter.number("no", 250.25d));

MiniMessage.miniMessage().deserialize("<gray>Hello my number <no:'#.00'>!", Formatter.number("no", 250.25d));

MiniMessage.miniMessage().deserialize("<gray>Hello my number <no:'de-DE':'#.00'>!", Formatter.number("no", 250.25d));

MiniMessage.miniMessage().deserialize("<gray>Hello my number <no:'de-DE'>!", Formatter.number("no", 250.25d));
```

All those examples are valid and will insert the number as the tag.

Refer to Locale and DecimalFormat for valid locale tags and usable patterns.

Tip

You can change the style such as the color by a more complex pattern:

```java
MiniMessage.miniMessage().deserialize("<gray>Your current balance is <no:'en-EN':'<green>#.00;<red>-#.00'>.", Formatter.number("no", 250.25d));
```

This will display the balance in red for negative numbers, otherwise the number will be green.

### Insert a date

[Section titled “Insert a date”](#insert-a-date)

To insert an instance of an `TemporalAccessor` such as a `LocalDateTime` you can use the date formatter.

The tag resolver requires a tag argument for the format. Refer to DateTimeFormatter for a usable patterns.

```java
MiniMessage.miniMessage().deserialize("<gray>Current date is: <date:'yyyy-MM-dd HH:mm:ss'>!", Formatter.date("date", LocalDateTime.now(ZoneId.systemDefault()));
```

This will display the current date with the specified format. E.g. as `2022-05-27 11:30:25`.

### Insert a choice

[Section titled “Insert a choice”](#insert-a-choice)

To insert a number and format some text based on the number you can use the choice formatter.

This will accept a ChoiceFormat pattern.

```java
MiniMessage.miniMessage().deserialize("<gray>I met <choice:'0#no developer|1#one developer|1<many developers'>!", Formatter.choice("choice", 5));
```

This will format your input based on the provided ChoiceFormat. In this case it will be `I met many developers!`

## Complex placeholders

[Section titled “Complex placeholders”](#complex-placeholders)

You can simply create your own placeholders. Take a look at the [Formatter](https://github.com/PaperMC/adventure/blob/main/5/text-minimessage/src/main/java/net/kyori/adventure/text/minimessage/tag/resolver/Formatter.java) and [Placeholder](https://github.com/PaperMC/adventure/blob/main/5/text-minimessage/src/main/java/net/kyori/adventure/text/minimessage/tag/resolver/Placeholder.java) class from MiniMessage for examples.

### Examples

[Section titled “Examples”](#examples)

Create a custom tag which makes its contents clickable:

```java
TagResolver.resolver("click-by-version", (args, context) -> {

final String version = args.popOr("version expected").value();

return Tag.styling(ClickEvent.openUrl("https://jd.advntr.dev/api/ " + version + "/"));

});

// creates a tag to get javadocs of adventure by the version: <click-by-version:'4.14.0'>
```

You can create your own complex placeholders with multiple arguments and their own logic.


================================================================================
Chapter Title: MiniMessage translator
Original Link: https://docs.papermc.io/adventure/minimessage/translator/
================================================================================

Note

For more information about both Minecraft and Adventure’s localization systems, see [`localization`](https://docs.papermc.io/adventure/localization).

MiniMessage provides a `Translator` implementation that allows you to use MiniMessage as translation strings.
It also provides automatic support for argument placeholders, letting you use simple translatable components throughout your codebase.

## Creating a MiniMessage translator

[Section titled “Creating a MiniMessage translator”](#creating-a-minimessage-translator)

To start, create an implementation of the `MiniMessageTranslator` and register it to the `GlobalTranslator`.
This can be done using `GlobalTranslator.translator().addSource(myMiniMessageTranslator)`.
For an example of how to create your own `MiniMessageTranslator`, see the code
block below.

```java
public class MyMiniMessageTranslator extends MiniMessageTranslator {

public MyMiniMessageTranslator() {

// By default, the standard MiniMessage instance will be used.

// You can specify a custom one in the super constructor.

super(MiniMessage.miniMessage());

}

@Override

public @Nullable String getMiniMessageString(final @NotNull String key, final @NotNull Locale locale) {

// Creating a custom MiniMessage translator is as simple as overriding this one method.

// All you need to do is return a MiniMessage string for the provided key and locale.

// In this example we will hardcode this, but you could pull it from a resource bundle, a properties file, a config file or something else entirely.

if (key.equals("mykey") && locale == Locale.US) {

return "<red>Hello, <name>! Today is <day_of_week>."

} else {

// Returning null "ignores" this translation.

return null;

}

}

}
```

### MiniMessage translation store

[Section titled “MiniMessage translation store”](#minimessage-translation-store)

In order to make managing a `MiniMessageTranslator` easier, we also provide a `TranslationStore` implementation using MiniMessage strings.
For documentation on how to use translation stores, see `localization`.

Note that the `MiniMessageTranslationStore` contains the same methods as the message format translation store for populating a translation store using resource bundles.

## Using a MiniMessage translator

[Section titled “Using a MiniMessage translator”](#using-a-minimessage-translator)

The MiniMessage translator will automatically turn translatable component arguments into a custom tag.
This tag will be `<arg:index>` or `<argument:index>` where `index` is the zero indexed position of the argument.
For example, this component `Component.translatable(key, Component.text("Kezz"))` with the MiniMessage string `Hello, <arg:0>!` will produce “Hello, Kezz!”.

You can also use the `Argument` class to create named tags for ease of use.
For example, this component `Component.translatable(key, Argument.component("name", Component.text("Kezz"))` will produce the string “Hello, Kezz!”
when used with either `Hello, <arg:0>!` or `Hello, <name>!`.

Finally, you can also add entirely custom tags or tag resolvers to the deserialization by using the rest of the methods on `Argument`.
For a full list, please see the Javadocs for the `Argument` class.


================================================================================
Chapter Title: ANSI
Original Link: https://docs.papermc.io/adventure/serializer/ansi/
================================================================================

The ANSI text serializer is an encoder that converts components to text containing
[ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code), which allows
for styled text in a terminal. This can then be used to, for example, output server
logs containing components while preserving their color and style.

Note that since it’s an encoder, it can only serialize components, and can’t
deserialize text back into components.

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-24)
* [Gradle (Groovy)](#tab-panel-25)
* [Maven](#tab-panel-26)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-text-serializer-ansi:4.26.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-text-serializer-ansi:4.26.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-text-serializer-ansi</artifactId>

<version>4.26.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

Different kind of ANSI escape codes exist, allowing for different levels of color
precision, however, not all terminals support newer kinds of ANSI escape sequences.
By default, `ANSIComponentSerializer` will attempt to guess the supported kinds of
escape sequences based on the system’s environment variables.

This can be overridden individually for a single serializer instance using the
`colorLevel` method of the builder.

It can also be overridden globally using system properties, using the property
`net.kyori.ansi.colorLevel`, which can be set when launching the JVM using the
command-line option `-Dnet.kyori.ansi.colorLevel=value`. 4 different values can
be set:

* `none`: Prevent any ANSI escape sequences from being emitted at all.
* `indexed16`: The original set of 16 colors.
* `indexed256`: Slightly newer set of 256 colors.
* `truecolor`: Full 24-bit spectrum of colors.

ANSI escape sequences can also be disabled using the `terminal.ansi` system property,
by setting it to `false`.

## ANSI library

[Section titled “ANSI library”](#ansi-library)

Note

This section talks about the component-agnostic library. If you are only interested in
the Adventure component-specific implementation, you do not need to read this section.

The `AnsiComponentSerializer` is built upon a separate ANSI library, which deals with
the lower-level ANSI escape sequence logic, and also allows for creating an ANSI
converter for any kind of component, not just those by Adventure.

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-27)
* [Gradle (Groovy)](#tab-panel-28)
* [Maven](#tab-panel-29)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:ansi:1.1.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:ansi:1.1.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>ansi</artifactId>

<version>1.1.1</version>

</dependency>
```

 

### Implementation usage

[Section titled “Implementation usage”](#implementation-usage)

To begin with, you need to create a class that implements `StyleOps<S>`, where `S` is
the “style” type for your component type. This adapter class allows for the ANSI logic to
access properties about the style.

To actually begin conversion, create an instance of a `ANSIComponentRenderer`, by using
one of the static methods, the simplest of which is `ANSIComponentRenderer.toString()`,
passing it an instance of your `StyleOps` adapter described above.

Then, you will need to traverse the structure of your component’s tree, using the
`pushStyle()`, `text()` and `popStyle()` methods of the renderer instance.

Finally, call `complete()` after traversing the tree has finished. The renderer’s job
is now concluded. In the case of the `ToString` renderer, you can access the result
using the `asString()` method.

As described in the [ANSI Usage](#usage) section, the library will, by default, try to guess the
supported colors of the current environment. This may be overridden by passing a custom
`ColorLevel` when creating the renderer, or by using the system properties as previously
described.


================================================================================
Chapter Title: Boss bars
Original Link: https://docs.papermc.io/adventure/bossbar/
================================================================================

## Constructing a BossBar

[Section titled “Constructing a BossBar”](#constructing-a-bossbar)

Boss Bars are composed of:

* A component used for the title of the boss bar
* A number from 0 to 1 used to determine how full the boss bar should be
* A color, will be downsampled for clients <1.9
* An overlay that determines the amount of visual segments on the boss bar

**Examples:**

```java
private @Nullable BossBar activeBar;

public void showMyBossBar(final @NonNull Audience target) {

final Component name = Component.text("Awesome BossBar");

// Creates a red boss bar which has no progress and no notches

final BossBar emptyBar = BossBar.bossBar(name, 0, BossBar.Color.RED, BossBar.Overlay.PROGRESS);

// Creates a green boss bar which has 50% progress and 10 notches

final BossBar halfBar = BossBar.bossBar(name, 0.5f, BossBar.Color.GREEN, BossBar.Overlay.NOTCHED_10);

// etc..

final BossBar fullBar = BossBar.bossBar(name, 1, BossBar.Color.BLUE, BossBar.Overlay.NOTCHED_20);

// Send a bossbar to your audience

target.showBossBar(fullBar);

// Store it locally to be able to hide it manually later

this.activeBar = fullBar;

}

public void hideActiveBossBar(final @NonNull Audience target) {

target.hideBossBar(this.activeBar);

this.activeBar = null;

}
```

## Changing an active BossBar

[Section titled “Changing an active BossBar”](#changing-an-active-bossbar)

Boss bars are mutable and listen for changes on their object,
the in-game view will change automatically without having to manually refresh it!

Therefore, if this boss bar is currently active

```java
final BossBar bossBar = BossBar.bossBar(Component.text("Cat counter"), 0, BossBar.Color.RED, BossBar.Overlay.PROGRESS);
```

and `BossBar.name()` with a component is called

```java
final Component newText = Component.text("Duck counter");

bossBar.name(newText);
```

the boss bar will be updated automatically. The same thing goes for `progress`, `color` and `overlay`.


================================================================================
Chapter Title: Sound
Original Link: https://docs.papermc.io/adventure/sound/
================================================================================

Adventure contains an API to play any built-in or resource pack-provided sound. Note that
not all platforms implement playing sound.

## Constructing a Sound

[Section titled “Constructing a Sound”](#constructing-a-sound)

Sounds are composed of:

* A Key (also known as `Identifier` or `ResourceLocation`) that decides which sound to play. Any custom sounds from resource packs can be used. If a client does not know about sounds, it will ignore the sound (though a warning will be printed to the client log).
* A Sound source, used to tell the client what type of sound its hearing. The clients sound settings are also attributed to a source.
* A number, determining the radius where the sound can be heard
* A number from 0 to 2 determining the pitch the sound will be played at

**Examples:**

```java
// Create a built-in sound using standard volume and pitch

Sound musicDisc = Sound.sound(Key.key("music_disc.13"), Sound.Source.MUSIC, 1f, 1f);

// Create a sound from our resource pack with a higher pitch

Sound myCustomSound = Sound.sound(Key.key("adventure", "rawr"), Sound.Source.AMBIENT, 1f, 1.1f);
```

## Playing a Sound

[Section titled “Playing a Sound”](#playing-a-sound)

Caution

The client can play multiple sounds at once, but as of version 1.16 is limited to 8 sounds playing at once.

In 1.15.2-1.16.5, due to [`MC-138832`](https://bugs.mojang.com/browse/MC-138832), the volume and pitch of sounds played with an emitter are ignored.

As documented in [`MC-146721`](https://bugs.mojang.com/browse/MC-146721), any stereo sounds will not play at a specific position or following an entity, therefore, the location or emitter parameters will be ignored.

Once you’ve created a sound, they can be played to an audience using multiple methods:

```java
// Play a sound at the location of the audience

audience.playSound(sound);

// Play a sound at a specific location

audience.playSound(sound, 100, 0, 150);

// Play a sound that follows the audience member

audience.playSound(sound, Sound.Emitter.self());

// Play a sound that follows another emitter (usually an entity)

audience.playSound(sound, someEntity);
```

## Stopping Sounds

[Section titled “Stopping Sounds”](#stopping-sounds)

A sound stop will stop the chosen sounds — ranging from every sound the client is playing, to specific named sounds.

```java
public void stopMySound(final @NonNull Audience target) {

// Stop a sound for the target

target.stopSound(SoundStop.named(Key.key("music_disc.13"));

// Stop all weather sounds for the target

target.stopSound(SoundStop.source(Sound.Source.WEATHER));

// Stop all sounds for the target

target.stopSound(SoundStop.all());
```

Sound stops can be constructed using the methods in the example block above.
Alternatively, they can be constructed directly from a sound.

```java
// Get a sound stop that will stop a specific sound

mySound.asStop();

// Sounds can also be stopped directly using the stopSound method

audience.stopSound(mySound);
```

## Creating a custom sound

[Section titled “Creating a custom sound”](#creating-a-custom-sound)

Use the `sounds.json` file to define sounds in a resource pack. Further reading about this limits can be done at the [Minecraft Wiki](https://minecraft.wiki/w/Sounds.json)


================================================================================
Chapter Title: Titles
Original Link: https://docs.papermc.io/adventure/titles/
================================================================================

## Constructing a Title

[Section titled “Constructing a Title”](#constructing-a-title)

Titles are composed of:

* A component used for the main title
* A component used for the subtitle
* Optionally, a `Title.Times` object can be used to determine the fade-in, stay on screen and fade-out durations

**Examples:**

```java
public void showMyTitle(final @NonNull Audience target) {

final Component mainTitle = Component.text("This is the main title", NamedTextColor.WHITE);

final Component subtitle = Component.text("This is the subtitle", NamedTextColor.GRAY);

// Creates a simple title with the default values for fade-in, stay on screen and fade-out durations

final Title title = Title.title(mainTitle, subtitle);

// Send the title to your audience

target.showTitle(title);

}

public void showMyTitleWithDurations(final @NonNull Audience target) {

final Title.Times times = Title.Times.times(Duration.ofMillis(500), Duration.ofMillis(3000), Duration.ofMillis(1000));

// Using the times object this title will use 500ms to fade in, stay on screen for 3000ms and then fade out for 1000ms

final Title title = Title.title(Component.text("Hello!"), Component.empty(), times);

// Send the title, you can also use Audience#clearTitle() to remove the title at any time

target.showTitle(title);

}
```


================================================================================
Chapter Title: Books
Original Link: https://docs.papermc.io/adventure/book/
================================================================================

## Constructing a Book

[Section titled “Constructing a Book”](#constructing-a-book)

Books are composed of:

* A component used for the title of the book
* A component used for the author of the book
* A collection of components used for the book pages

**Example:**

```java
// Create and open a book about cats for the target audience

public void openMyBook(final @NonNull Audience target) {

Component bookTitle = Component.text("Encyclopedia of cats");

Component bookAuthor = Component.text("kashike");

Collection<Component> bookPages = Cats.getCatKnowledge();

Book myBook = Book.book(bookTitle, bookAuthor, bookPages);

target.openBook(myBook);

}
```

## Extra info regarding Books

[Section titled “Extra info regarding Books”](#extra-info-regarding-books)

Books in adventure are not necessarily connected to an interactable book item in the client.
As of the current release such a connection needs to be implemented outside of adventure.

Any component that surpasses the game limit for text per page will be truncated client side, the same applies
to the amount of components (pages). Further reading about these limits can be done at the [Minecraft Wiki](https://minecraft.wiki/w/Book_and_Quill#Writing).


================================================================================
Chapter Title: Player list/Tab list
Original Link: https://docs.papermc.io/adventure/tablist/
================================================================================

Adventure only supports changing the header (above the players) and footer (below the players) of the tab list.

![Image showing a tab list from a multiplayer server with the header and footer encased, shown through the vanilla Minecraft client](https://docs.papermc.io/_astro/tablist.B62gkSy1_u5fKU.webp)

**Usage**

With any `Audience` use `Audience.sendPlayerListHeader(Component)`, `Audience.sendPlayerListFooter(Component)`
and/or `Audience.sendPlayerListHeaderAndFooter(Component, Component)`.

Whether sending a header or footer by itself will display another existing header or footer will vary depending on which platform
you are working on. Servers will most likely support keeping headers or footers when sending them separately, while proxies are
more likely to only let you send everything at once.

**Examples**

```java
public void onPlayerJoin(final Audience player) {

final Component header = Component.text("My Cool Server", NamedTextColor.BLUE);

final Component footer = Component.text("It is: today!");

player.sendPlayerListHeaderAndFooter(header, footer);

}
```

Depending on your platform this next example might display an existing header as well

```java
public void onDayChange(final Audience server) {

final Component footer = Component.text("It is: tomorrow!");

server.sendPlayerListFooter(footer);

}
```


================================================================================
Chapter Title: Resource packs
Original Link: https://docs.papermc.io/adventure/resource-pack/
================================================================================

On top of the resource packs controlled by each player on their client, the game allows servers to send resource pack URLs to clients that the players can choose to accept. This allows servers to provide customized styling.

Initially this just allowed sending a single resource pack, but starting with *Minecraft 1.20.3* the server can send multiple resource packs to be stacked, and if needed removed individually.

## Sending resource packs

[Section titled “Sending resource packs”](#sending-resource-packs)

A resource pack is identified by:

* its UUID
* a URI to the resource pack ZIP file
* the SHA-1 hash of the resource pack ZIP file as a hex string

This is referred to as `ResourcePackInfo`.

For every batch of resource packs being sent, a `ResourcePackRequest`, there is:

* one or more resource packs
* a callback to perform actions based on the responses from the client
* a toggle for whether to replace any existing server-provided resource packs, or stack the most recent packs on top
* whether these resource packs are required
* a prompt to display to the user if they have not yet chosen whether to allow server resource packs

## Examples

[Section titled “Examples”](#examples)

Send a single resource pack to a client that is required, with a UUID computed based on its name.

```java
private static final ResourcePackInfo PACK_INFO = ResourcePackInfo.resourcePackInfo()

.uri(URI.create("https://example.com/resourcepack.zip"))

.hash("2849ace6aa689a8c610907a41c03537310949294")

.build();

public void sendResourcePack(final @NonNull Audience target) {

final ResourcePackRequest request = ResourcePackRequest.resourcePackRequest()

.packs(PACK_INFO)

.prompt(Component.text("Please download the resource pack!"))

.required(true)

.build();

// Send the resource pack request to the target audience

target.sendResourcePacks(request);

}

public void sendOptionalResourcePack(final @NonNull Audience target) {

final ResourcePackRequest request = ResourcePackRequest.resourcePackRequest()

.packs(PACK_INFO)

.prompt(Component.text("Please download the resource pack!"))

.required(false)

.build();

// Send the resource pack request to the target audience

target.sendResourcePacks(request);

}
```

## Callbacks

[Section titled “Callbacks”](#callbacks)

The callback function allows servers to respond to pack download feedback sent by the client. Newer versions of the game provide more information about different phases, but any version will provide basic status info about download and application. Keep in mind that the responses are entirely driven by the client, so modded clients may send incorrect information (for example, saying a required resource pack has been applied when it has not), none at all, or even nonsensical information (status updates after a terminal update has been received). Any action taken based on a callback should therefore be defensively designed to cope with client creativity.

The audience provided in the callback aims to be the exact same audience the resource pack was sent to in the case of wrapping audiences, re-wrapping any underlying returned value where necessary.

## Removing resource packs

[Section titled “Removing resource packs”](#removing-resource-packs)

Resource packs can be removed, either some quantity at a time with `Audience.removeResourcePacks()`, or all at once with `Audience.clearResourcePacks()`.

The removal methods have multiple overloads, allowing removal by a bare UUID, or by reusing the data structures used for applying resource packs.


================================================================================
Chapter Title: Localization
Original Link: https://docs.papermc.io/adventure/localization/
================================================================================

Adventure provides a way to utilize Minecraft’s built-in localization system for client-side translations as well as an additional Adventure-specific system for translating text.

## Using Minecraft’s localization

[Section titled “Using Minecraft’s localization”](#using-minecrafts-localization)

To send text to a player that will be translated in the language they have selected in their client settings, use a translatable component.
For example, `Component.translatable("block.minecraft.diamond_block")` will render as “Block of Diamond” (or translated to another language) when viewed by the client.
Some translation keys have arguments which are inserted into the translated content.
For example, `Component.translatable("block.minecraft.player_head.named", Component.text("Mark"))` will render as “Mark’s Head”.
Translatable components can have styling, hover/click events and children components just like any other component type.

### Resource pack language files

[Section titled “Resource pack language files”](#resource-pack-language-files)

You can provide translation files in a resource pack in order to change existing translations or add new ones.
For a guide on how to do that, see the [Minecraft Wiki](https://minecraft.wiki/w/Resource_pack#Language).

### Using Adventure’s localization

[Section titled “Using Adventure’s localization”](#using-adventures-localization)

Adventure also provides a way to handle localization in Adventure itself.
This can be useful in environments where you do not have access to resource packs, or wish to do translations yourself, without relying on Minecraft’s translation system.

Any component that is sent to a client is ran through the `GlobalTranslator` using the locale of the client.
This means that if you wish to have automatic translation of components using your own translation data, you can add a `Translator` to the `GlobalTranslator`.
You can either provide your own implementation of `Translator` or use one of the implementations that Adventure provides.

Once you have a `Translator` instance, you can register it to the `GlobalTranslator` using `GlobalTranslator.translator().addSource(myTranslator)`.
This will then make it available for automatic translation across the platform.

Caution

Some implementations may not use the `GlobalTranslator` in every area, or at all.
For example, Paper does not use it for items, and Minestom does not use it unless specifically enabled.
Please consult the documentation for your platform for any limitations.

## Using a custom `Translator`

[Section titled “Using a custom Translator”](#using-a-custom-translator)

A `Translator` is a simple interface that provides two ways of translating content.

The first `translate` method provides the translation key and locale as an argument and expects a nullable `MessageFormat` in return.
This system is comparable to Minecraft’s built-in localization system, using the standard Java
[message format](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/text/MessageFormat.html) for arguments.

If the first `translate` method returns `null`, the second method which provides the translatable component and locale as an argument can be used.
This method allows for much richer customization of the translation process as you can return an entire component.
This means you can, for example, customize the color and styling of the translated component, rather than relying solely on strings for the message format system.

Caution

If you are overriding the component `translate` method, you should be careful not to unintentionally lose the children of the translatable component.
See the Javadocs for the translate method for a code example of how to avoid this common error.

Below is an example of how one might implement a custom `Translator`.

MyTranslator.java

```java
public class MyTranslator implements Translator {

@Override

public @NotNull Key name() {

// Every translator has a name which is used to identify this specific translator instance.

return Key.key("mynamespace:mykey");

}

@Override

public @Nullable MessageFormat translate(final @NotNull String key, final @NotNull Locale locale) {

// You could retrieve a string from a properties file, a config file, or some other system.

// An an example, we will hard-code a check for a specific key here.

if (key.equals("mytranslation.key") && locale == Locale.US) {

return new MessageFormat("Hello %s!", locale);

} else {

// If you only want to use component translation, you can override this method and always return `null`.

return null;

}

}

@Override

public @Nullable Component translate(@NotNull TranslatableComponent component, @NotNull Locale locale) {

// As above, we will hardcode a check here, but you should be reading this from elsewhere.

if (key.equals("mytranslation.colorful") && locale == Locale.US) {

return Component.text("Hello, ", NamedTextColor.GREEN)

.append(component.arguments().get(0).color(NamedTextColor.RED))

.append(component.children()); // Always make sure to copy the children over!

} else {

return null;

}

}

}
```

### Using a `TranslationStore`

[Section titled “Using a TranslationStore”](#using-a-translationstore)

A `TranslationStore` is a store of translations.
It provides a simpler way creating a `Translator` without having to implement the logic for determining and storing translations yourself.
You can create a translation store and then add or remove translations at will, even after registering it to the global translator.

Adventure provides two translation stores, one for message format translating and one for component translating.
An example of how to use a translation store is below.

```java
// As above, every translator needs an identifying name!

// Could also use TranslationStore#component(Key) to work with components instead.

final TranslationStore myStore = TranslationStore.messageFormat(Key.key("mynamespace:mykey"));

// You can add translations one-by-one, or in bulk. Consult the Javadocs for a full list of methods.

myStore.register("mytranslation.key", Locale.US, new MessageFormat("Hello %s!", Locale.US));

// You can then register this to the global translator so the translations are available there!

GlobalTranslator.translator().addSource(myStore);
```

There are additional methods on the message format translation store to bulk register from [resource bundles](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ResourceBundle.html).
You may also want to use Adventure’s `UTF8ResourceBundleControl` utility class to create your bundle.

### Using MiniMessage for translations

[Section titled “Using MiniMessage for translations”](#using-minimessage-for-translations)

Adventure also provides a translator that can use MiniMessage strings, with automatic support for placeholders and arguments.
For more information, see [MiniMessage Translator](https://docs.papermc.io/adventure/minimessage/translator).


================================================================================
Chapter Title: Overview
Original Link: https://docs.papermc.io/adventure/platform/
================================================================================

Adventure integrates with many of the Minecraft platforms out there. Some platforms support
Adventure natively, but other legacy platforms have their own types and need an adapter to handle Adventure types. To enable you to use Adventure with these platforms, Adventure provides a number of platform-specific adapters to
allow you to obtain `Audience` instances from native user types.

FAQ

**Why is adventure-platform not sending any messages or not working correctly?**

Firstly, please ensure you are on the latest stable version. It can be found on [Maven Central](https://central.sonatype.com/search?q=g%3Anet.kyori+adventure-platform*).

Next, make sure that the feature you are using exists on the client version that is receiving the action.
For example, hex color codes won’t work on clients older than 1.16, so hex colors will be down-sampled.

If it’s still not working, it is useful to enable debug mode by setting the system property `net.kyori.adventure.debug` to `true` and
looking at the output. This will show what facets are being selected which will help point towards why it is not working for you.
If you still cannot figure out the issue by yourself, you can always ask in the
[`#adventure-platform-help`](https://discord.com/channels/289587909051416579/1342379165663363112) channel in the PaperMC Discord!

### Content:

[Section titled “Content:”](#content)

* [Native support](https://docs.papermc.io/adventure/platform/native)
* [Bukkit](https://docs.papermc.io/adventure/platform/bukkit)
  + [Usage](https://docs.papermc.io/adventure/platform/bukkit#usage)
  + [Component serializers](https://docs.papermc.io/adventure/platform/bukkit#component-serializers)
* [BungeeCord](https://docs.papermc.io/adventure/platform/bungeecord)
  + [Usage](https://docs.papermc.io/adventure/platform/bungeecord#usage)
  + [Component serializers](https://docs.papermc.io/adventure/platform/bungeecord#component-serializers)
* [SpongeAPI](https://docs.papermc.io/adventure/platform/spongeapi)
  + [Usage](https://docs.papermc.io/adventure/platform/spongeapi#usage)
* [Modded (Fabric and NeoForge shared API)](https://docs.papermc.io/adventure/platform/modded)
  + [Dependency](https://docs.papermc.io/adventure/platform/modded#dependency)
  + [Basic use](https://docs.papermc.io/adventure/platform/modded#basic-use)
  + [Working with native types](https://docs.papermc.io/adventure/platform/modded#working-with-native-types)
* [Fabric](https://docs.papermc.io/adventure/platform/fabric)
  + [Dependency](https://docs.papermc.io/adventure/platform/fabric#dependency)
  + [Basic use](https://docs.papermc.io/adventure/platform/fabric#basic-use)
  + [Server](https://docs.papermc.io/adventure/platform/fabric#server)
  + [Client](https://docs.papermc.io/adventure/platform/fabric#dependency)
  + [Working with native types](https://docs.papermc.io/adventure/platform/fabric#working-with-native-types)
* [NeoForge](https://docs.papermc.io/adventure/platform/neoforge)
  + [Dependency](https://docs.papermc.io/adventure/platform/neoforge#dependency)
  + [Basic use](https://docs.papermc.io/adventure/platform/neoforge#basic-use)
  + [Server](https://docs.papermc.io/adventure/platform/neoforge#server)
  + [Commands](https://docs.papermc.io/adventure/platform/neoforge#commands)
  + [Client](https://docs.papermc.io/adventure/platform/neoforge#dependency)
* [ViaVersion](https://docs.papermc.io/adventure/platform/viaversion)
* [Implementing platforms](https://docs.papermc.io/adventure/platform/implementing)
  + [Services](https://docs.papermc.io/adventure/platform/implementing#services)
  + [Conventional behaviors](https://docs.papermc.io/adventure/platform/implementing#conventional-behaviors)


================================================================================
Chapter Title: Native support
Original Link: https://docs.papermc.io/adventure/platform/native/
================================================================================

Native platforms integrate Adventure directly with their platform’s provided API, and bundle Adventure automatically.
This allows them to more tightly integrate Adventure with the rest of the game, and avoids users having to handle distributing
Adventure and some platform adapter themselves.

The following software provide native support for Adventure.

| Platform | Minimum Version | Additional Notes |
| --- | --- | --- |
| Sponge | Sponge 8 (1.16.5) |  |
| Velocity | 1.1.0 build 158 | For more information, see the [Velocity Docs](https://docs.papermc.io/velocity/dev/pitfalls#audience-operations-are-not-fully-supported) |
| Paper | 1.16.5 build 473 |  |
| Minestom | Build 7494725 | For more information, see the [Minestom Wiki](https://minestom.net/docs/feature/adventure) |
| Fabric | `adventure-platform-fabric` 5.3.0 | This is not strictly native, but injected interfaces provide a near-native experience |


================================================================================
Chapter Title: Bukkit
Original Link: https://docs.papermc.io/adventure/platform/bukkit/
================================================================================

The Adventure platform implementation for Bukkit targets Paper, Spigot, and Bukkit for
Minecraft 1.7.10 through 1.21.11.

Caution

This page documents only the *legacy* platform adapter for Bukkit. Most users should use [Paper](https://docs.papermc.io/paper)’s native implementation instead.
This native implementation provides more functionality, better integration with the server, and does not require the `BukkitAudiences` adapter.

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-9)
* [Gradle (Groovy)](#tab-panel-10)
* [Maven](#tab-panel-11)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-platform-bukkit:4.4.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-platform-bukkit:4.4.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-platform-bukkit</artifactId>

<version>4.4.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

You should first obtain a `BukkitAudiences` object by using `BukkitAudiences.create(plugin)`. This object is thread-safe
and can be reused from different threads if needed. From here, Bukkit `CommandSender`s and `Player`s may be converted into
`Audience`s using the appropriate methods on `BukkitAudiences`.

The audiences object should also be closed when a plugin is disabled in order to clean up resources and increase the likelihood of a successful `/reload`.

```java
public class MyPlugin extends JavaPlugin {

private BukkitAudiences adventure;

@NonNull

public BukkitAudiences adventure() {

if (this.adventure == null) {

throw new IllegalStateException("Tried to access Adventure when the plugin was disabled!");

}

return this.adventure;

}

@Override

public void onEnable() {

// Initialize an audiences instance for the plugin

this.adventure = BukkitAudiences.create(this);

// then do any other initialization

}

@Override

public void onDisable() {

if (this.adventure != null) {

this.adventure.close();

this.adventure = null;

}

}

}
```

This audience provider should be used over the serializers directly, since it will handle compatibility measures for sending messages across versions.

## Component serializers

[Section titled “Component serializers”](#component-serializers)

For areas that aren’t covered by the `Audience` interface, the Bukkit platform provides the `MinecraftComponentSerializer`
(available on CraftBukkit-based servers), and the `BungeeComponentSerializer` (available on Spigot and Paper servers)
to convert directly between Adventure [Components](https://docs.papermc.io/adventure/text) and other component types. For uses that don’t integrate
directly with native types, JSON and legacy format serializers for the running server version are exposed in `BukkitComponentSerializer`.


================================================================================
Chapter Title: BungeeCord
Original Link: https://docs.papermc.io/adventure/platform/bungeecord/
================================================================================

Adventure targets the latest version of BungeeCord and BungeeCord-compatible
forks, such as Waterfall.

Caution

The BungeeCord platform is intended for legacy environments only.
Most developers will want to write plugins for [Velocity](https://docs.papermc.io/velocity), which natively implements the Adventure API. No adapters required!

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-12)
* [Gradle (Groovy)](#tab-panel-13)
* [Maven](#tab-panel-14)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-platform-bungeecord:4.4.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-platform-bungeecord:4.4.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-platform-bungeecord</artifactId>

<version>4.4.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

You should first obtain a `BungeeAudiences` object by using `BungeeAudiences.create(plugin)`. This object is thread-safe
and can be reused from different threads if needed. This object should also be *closed* when the plugin is disabled.

Note that not all functionality is available on the proxy. Sending chat messages, action bar messages, titles, and boss bars,
and tab list header and footer are supported, but all other requests will fail silently.

A simple example of how to appropriately initialize this platform follows:

```java
public class MyPlugin extends Plugin {

private BungeeAudiences adventure;

@NonNull

public BungeeAudiences adventure() {

if (this.adventure == null) {

throw new IllegalStateException("Cannot retrieve audience provider while plugin is not enabled");

}

return this.adventure;

}

@Override

public void onEnable() {

this.adventure = BungeeAudiences.create(this);

}

@Override

public void onDisable() {

if (this.adventure != null) {

this.adventure.close();

this.adventure = null;

}

}

}
```

## Component serializers

[Section titled “Component serializers”](#component-serializers)

For functionality not already supported by `Audience`, the `BungeeComponentSerializer` allows you to convert between
Adventure [Components](https://docs.papermc.io/adventure/text) and the native BungeeCord chat component API and back.

For some areas of the proxy (notably, sending server list responses), the component serializer cannot be appropriately
injected unless a `BungeeAudiences` instance has been initialized. Using Adventure `Component` instances **will not**
work without a created `BungeeAudiences` instance.


================================================================================
Chapter Title: SpongeAPI
Original Link: https://docs.papermc.io/adventure/platform/spongeapi/
================================================================================

Adventure provides a platform for SpongeAPI 7 for *Minecraft: Java Edition* 1.12.

Warning

For SpongeAPI 8 and up (targeting *Minecraft: Java Edition* 1.16.4), Adventure is the native text library, so no platform adapter is needed.
Sponge’s API interfaces directly extend Adventure’s rather than needing a `SpongeAudiences` adapter.

Declaring the dependency:

* [Gradle (Kotlin)](#tab-panel-21)
* [Gradle (Groovy)](#tab-panel-22)
* [Maven](#tab-panel-23)

build.gradle.kts

```java
repositories {

mavenCentral()

}

dependencies {

implementation("net.kyori:adventure-platform-spongeapi:4.4.1")

}
```

build.gradle

```java
repositories {

mavenCentral()

}

dependencies {

implementation 'net.kyori:adventure-platform-spongeapi:4.4.1'

}
```

pom.xml

```java
<dependency>

<groupId>net.kyori</groupId>

<artifactId>adventure-platform-spongeapi</artifactId>

<version>4.4.1</version>

</dependency>
```

  

## Usage

[Section titled “Usage”](#usage)

The SpongeAPI platform can either be created through Guice dependency injection, or created directly. We recommend using injection, since less boilerplate is required.

An example plugin is fairly straightforward:

```java
@Plugin(/* [...] */)

public class MyPlugin {

private final SpongeAudiences adventure;

@Inject

MyPlugin(final SpongeAudiences adventure) {

this.adventure = adventure;

}

@NonNull

public SpongeAudiences adventure() {

return this.adventure;

}

}
```

This sets up a `SpongeAudiences` instance that can provide audiences for players, or any `MessageReceiver`.


================================================================================
Chapter Title: Modded (Fabric and NeoForge shared API)
Original Link: https://docs.papermc.io/adventure/platform/modded/
================================================================================

Starting with *Minecraft: Java Edition* 1.21.2, Adventure is implemented using mostly shared code between NeoForge and Fabric.
Each major version of Minecraft will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

## Dependency

[Section titled “Dependency”](#dependency)

When building multi-loader mods, we often want to move as much code as possible into a loader-agnostic part of our projects.

Adventure facilities this through the `net.kyori:adventure-platform-mod-shared` artifact.

A second variant, `net.kyori:adventure-platform-mod-shared-fabric-repack`, is also published. This variant should be used
when your common code is managed by `fabric-loom`.

Note

These artifacts are for the common module on multi-platform mods. For specific platforms, take a look at the
[Fabric](https://docs.papermc.io/adventure/platform/fabric) or [NeoForge](https://docs.papermc.io/adventure/platform/neoforge) pages. If you are building a
Fabric-only or NeoForge-only mod, or do not care to use the platform API in shared code, then you don’t need to use
this artifact explicitly. This is because both platforms depend on it transitively.

As with the rest of the Adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS:

* [Gradle (Kotlin)](#tab-panel-17)
* [Gradle (Groovy)](#tab-panel-18)

build.gradle.kts

```java
repositories {

// for development builds

maven(url = "https://central.sonatype.com/repository/maven-snapshots/") {

name = "central-snapshots"

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

// Loom project

modCompileOnly("net.kyori:adventure-platform-mod-shared-fabric-repack:6.8.0") // for Minecraft 1.21.11

// NeoGradle/ModDevGradle/VanillaGradle project

compileOnly("net.kyori:adventure-platform-mod-shared:6.8.0") // for Minecraft 1.21.11

}
```

build.gradle

```java
repositories {

// for development builds

maven {

name = 'central-snapshots'

url = 'https://central.sonatype.com/repository/maven-snapshots/'

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

// Loom project

modCompileOnly('net.kyori:adventure-platform-mod-shared-fabric-repack:6.8.0') // for Minecraft 1.21.11

// NeoGradle/ModDevGradle/VanillaGradle project

compileOnly('net.kyori:adventure-platform-mod-shared:6.8.0') // for Minecraft 1.21.11

}
```

  

Attention

Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table below.

Historic Versions

| Minecraft Version | Adventure version | `adventure-platform-(mod-shared/fabric/neoforge)` version |
| --- | --- | --- |
| 1.21.9-1.21.10 | 4.25.0 | 6.7.0 |
| 1.21.6-1.21.8 | 4.24.0 | 6.6.0 |
| 1.21.5 | 4.21.0 | 6.4.0 |
| 1.21.2-1.21.4 | 4.20.0 | 6.3.0 |
| 1.21-1.21.1 | 4.17.0 | 6.0.0 |

## Basic use

[Section titled “Basic use”](#basic-use)

The easiest way to get started with this platform is to work with the Minecraft game objects that directly implement Adventure interfaces.

This covers almost all cases where the default renderer is used.

On Fabric, interface injection is used so that you can directly call interface methods on Minecraft objects (with loom 0.11+).

On NeoForge, you must manually cast or use the helpers provided in `MinecraftAudiences`.

The following Adventure interfaces are directly implemented:

`Audience`

* `net.minecraft.commands.CommandSourceStack`, `net.minecraft.server.MinecraftServer`, `net.minecraft.server.rcon.RconConsoleSource`,
* `net.minecraft.server.level.ServerPlayer`, `net.minecraft.client.player.LocalPlayer`

`AdventureCommandSourceStack`

* `net.minecraft.commands.CommandSourceStack`

`Sound.Emitter`

* `net.minecraft.world.entity.Entity`

`Sound.Type`

* `net.minecraft.sounds.SoundEvent`

`Identified`

* `net.minecraft.world.entity.player.Player`

`ComponentLike`

* `net.minecraft.network.chat.Component`

`Key`

* `net.minecraft.resources.ResourceLocation`

`Keyed`

* `net.minecraft.resources.ResourceKey`

`HoverEventSource`

* `net.minecraft.world.entity.Entity`,
* `net.minecraft.world.item.ItemStack`

`SignedMessage.Signature`

* `net.minecraft.network.chat.MessageSignature`

Using these injections, getting started is as simple as:

```java
void greet(final ServerPlayer player) {

Component message = Component.text()

.content("Hello ")

.append(player.get(Identity.DISPLAY_NAME)

.get()

.color(NamedTextColor.RED)

);

player.sendMessage(message);

}
```

For more complex use cases, `MinecraftServerAudiences` or `MinecraftClientAudiences` provide additional API.

### Commands

[Section titled “Commands”](#commands)

The platform provides custom argument types to specify `Key` and `Component` parameters in Brigadier commands.

Caution

See the platform-specific documentation for details on registration and syncing of these argument types.

As an example, here’s a simple command that will echo whatever is provided as input:

```java
// A potential method to be in the mod initializer class above

private static final String ARG_MESSAGE = "message";

void registerCommands(final CommandDispatcher dispatcher, final boolean isDedicated) {

dispatcher.register(literal("echo").then(argument(ARG_MESSAGE, component()).executes(ctx -> {

final Component message = component(ctx, ARG_MESSAGE);

((Audience) ctx.getSource()).sendMessage(Component.text("You said: ").append(message));

}));

}
```

## Working with native types

[Section titled “Working with native types”](#working-with-native-types)

Sadly, Adventure can’t provide API for every place chat components are used in the game. However, for areas not covered by the API in `Audience`,
it’s possible to convert components between native and Adventure types. See certain native types which implement
Adventure interfaces, and the methods on `MinecraftAudiences` for other available conversions.


================================================================================
Chapter Title: Fabric
Original Link: https://docs.papermc.io/adventure/platform/fabric/
================================================================================

Adventure supports Fabric on *Minecraft: Java Edition* 1.16 and up, for both server-side and client-side use. Each major version of Minecraft
will usually require a new release of the platform.

The platform supports all features, including localization and custom renderers.

When using at least version 5.3.0, this platform provides a *near-native* experience by directly implementing Adventure interfaces on Minecraft classes where possible.

Attention

Version 6.x of adventure-platform-fabric, utilizing a shared implementation with NeoForge (see [Modded (Fabric and NeoForge shared API)](https://docs.papermc.io/adventure/platform/modded))
is not published for Minecraft 1.20-1.21.1. This is to avoid conflicts with existing mods using 5.x.
Starting with Minecraft 1.21.2, both platforms have version 6.x published.

## Dependency

[Section titled “Dependency”](#dependency)

The Fabric platform is packaged as a mod, designed to be included in mods via jar-in-jar packaging.
As with the rest of the Adventure projects, releases are distributed on Maven Central, and snapshots on Sonatype OSS:

* [Gradle (Kotlin)](#tab-panel-15)
* [Gradle (Groovy)](#tab-panel-16)

build.gradle.kts

```java
repositories {

// for development builds

maven(url = "https://s01.oss.sonatype.org/content/repositories/snapshots/") {

name = "sonatype-oss-snapshots1"

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

modImplementation(include("net.kyori:adventure-platform-fabric:6.8.0")!!) // for Minecraft 1.21.11

}
```

build.gradle

```java
repositories {

// for development builds

maven {

name = 'sonatype-oss-snapshots1'

url = 'https://s01.oss.sonatype.org/content/repositories/snapshots/'

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

modImplementation include('net.kyori:adventure-platform-fabric:6.8.0') // for Minecraft 1.21.11

}
```

  

The Fabric platform requires *fabric-api-base* in order to provide the locale change event, *fabric-command-api-v2* for the callback click event,
and can optionally use [Colonel](https://gitlab.com/stellardrift/colonel) (or *fabric-networking-api-v1*) to allow the `Component` and `Key` argument
types to be used on clients without the mod installed. There are no other dependencies.

Attention

Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table below.

Historic Versions

| Minecraft Version | Adventure version | `adventure-platform-fabric` version |
| --- | --- | --- |
| 1.16.2-1.16.4 | 4.9.3 | 4.0.0 |
| 1.17.x | 4.9.3 | 4.1.0 |
| 1.18, 1.18.1 | 4.10.0 | 5.1.0 |
| 1.18.2 | 4.11.0 | 5.3.1 |
| 1.19 | 4.11.0 | 5.4.0 |
| 1.19.1-1.19.2 | 4.12.0 | 5.5.2 |
| 1.19.3 | 4.13.0 | 5.7.0 |
| 1.19.4 | 4.13.0 | 5.8.0 |
| 1.20-1.20.1 | 4.14.0 | 5.9.0 |
| 1.20.2 | 4.14.0 | 5.10.1 |
| 1.20.4 | 4.16.0 | 5.12.0 |
| 1.20.5-1.20.6 | 4.17.0 | 5.13.0 |
| 1.21-1.21.1 | 4.17.0 | 5.14.1 |

## Basic use

[Section titled “Basic use”](#basic-use)

The easiest way to get started with this platform is to work with the Minecraft game objects that directly implement Adventure interfaces (requires Loom 0.11 or newer).

This covers almost all cases where the default renderer is used.

The following Adventure interfaces are directly implemented:

`Audience`

* `net.minecraft.commands.CommandSourceStack`, `net.minecraft.server.MinecraftServer`, `net.minecraft.server.rcon.RconConsoleSource`,
* `net.minecraft.server.level.ServerPlayer`, `net.minecraft.client.player.LocalPlayer`

`Sound.Emitter`

* `net.minecraft.world.entity.Entity`

`Sound.Type`

* `net.minecraft.sounds.SoundEvent`

`Identified`

* `net.minecraft.world.entity.player.Player`

`ComponentLike`

* `net.minecraft.network.chat.Component`

`Key`

* `net.minecraft.resources.ResourceLocation`

`Keyed`

* `net.minecraft.resources.ResourceKey`

`HoverEventSource`

* `net.minecraft.world.entity.Entity`,
* `net.minecraft.world.item.ItemStack`

`SignedMessage`

* `net.minecraft.network.chat.PlayerChatMessage`

`SignedMessage.Signature`

* `net.minecraft.network.chat.MessageSignature`

Additionally, all `Key`s created will be `ResourceLocation` instances (on Loader 0.14.0+)

Using these injections, getting started is as simple as:

```java
void greet(final ServerPlayer player) {

Component message = Component.text()

.content("Hello ")

.append(player.get(Identity.DISPLAY_NAME)

.get()

.color(NamedTextColor.RED)

);

player.sendMessage(message);

}
```

For more complex use cases, `FabricServerAudiences` or `FabricClientAudiences` provide additional API.

## Server

[Section titled “Server”](#server)

The logical-server side of the Fabric platform can be accessed any time a server is available, through a `MinecraftServerAudiences` instance. By default, translatable components will be rendered with the global translator, but a custom renderer can be passed when initializing the platform.

All `AudienceProvider` interface methods are supported, except for the `permission` method. This will become supported as soon as Fabric gets a suitable permissions API.

To get started with Adventure, set up an audience provider like this:

```java
public class MyMod implements ModInitializer {

private volatile MinecraftServerAudiences adventure;

public MinecraftServerAudiences adventure() {

if (this.adventure == null) {

throw new IllegalStateException("Tried to access Adventure without a running server!");

}

return this.adventure;

}

@Override

public void onInitialize() {

// Register with the server lifecycle callbacks

// This will ensure any platform data is cleared between game instances

// This is important on the integrated server, where multiple server instances

// can exist for one mod initialization.

ServerLifecycleEvents.SERVER_STARTING.register(server -> this.adventure = MinecraftServerAudiences.of(server));

ServerLifecycleEvents.SERVER_STOPPED.register(server -> this.adventure = null);

}

}
```

From here, audiences can be acquired for players and any other `CommandSource`. Specialized serializer instances are also available, to allow using
game information in component serialization.

### Localization

[Section titled “Localization”](#localization)

As part of the platform’s translation support, the `PlayerLocales.CHANGED_EVENT` callback will be called any time a player on the server receives an
updated language from their client, and allows accessing the current locale for a player.

### Commands

[Section titled “Commands”](#commands)

The Fabric platform provides custom argument types to specify `Key` and `Component` parameters in Brigadier commands, and has helpers to easily get an
`Audience` from a `CommandSourceStack` (yarn: `ServerCommandSource`) instance.

Caution

If these custom argument types are used (pre-1.19), Vanilla clients will not be able to join unless the [Colonel](https://gitlab.com/stellardrift/colonel)
mod is installed on the server. Like the platform, it is small and easily included in your mod jar.

As an example, here’s a simple command that will echo whatever is provided as input:

```java
// A potential method to be in the mod initializer class above

private static final String ARG_MESSAGE = "message";

void registerCommands(final CommandDispatcher dispatcher, final boolean isDedicated) {

dispatcher.register(literal("echo").then(argument(ARG_MESSAGE, component()).executes(ctx -> {

final Component message = component(ctx, ARG_MESSAGE);

ctx.getSource().sendMessage(Component.text("You said: ").append(message));

}));

}
```

## Client

[Section titled “Client”](#client)

Special for the Fabric platform, purely client-side operations are supported. The setup is less involved than it is for the server,
since the client is a singleton, and there is only one subject that can be acted on: the client’s player.

This means that for most users the `MinecraftClientAudiences` object can be treated as a singleton. The only exception is users using a
custom renderer. This makes using Adventure audiences fairly simple, as this code example shows:

```java
void doThing() {

// Get the audience

final Audience client = MinecraftClientAudiences.of().audience();

// Do something. This will only work when the player is in game.

client.sendMessage(Component.text("meow", NamedTextColor.DARK_PURPLE));

}
```

The full functionality of the `Audience` interface is available, including localization!

## Working with native types

[Section titled “Working with native types”](#working-with-native-types)

Sadly, Adventure can’t provide API for every place chat components are used in the game. However, for areas not covered by the API in `Audience`,
it’s possible to convert components between native and Adventure types. See certain native types which implement
Adventure interfaces, and the methods on `FabricAudiences` for other available conversions.


================================================================================
Chapter Title: NeoForge
Original Link: https://docs.papermc.io/adventure/platform/neoforge/
================================================================================

Adventure supports NeoForge on *Minecraft: Java Edition* 1.21 and up, for both server-side and client-side use. Each major version of Minecraft will usually require
a new release of the platform.

The platform supports all features, including localization and custom renderers.

## Dependency

[Section titled “Dependency”](#dependency)

The NeoForge platform is packaged as a mod, designed to be included in mods via jar-in-jar packaging. As with the rest of the Adventure projects,
releases are distributed on Maven Central, and snapshots on Sonatype OSS:

* [Gradle (Kotlin)](#tab-panel-19)
* [Gradle (Groovy)](#tab-panel-20)

build.gradle.kts

```java
repositories {

// for development builds

maven(url = "https://s01.oss.sonatype.org/content/repositories/snapshots/") {

name = "sonatype-oss-snapshots1"

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

modImplementation(include("net.kyori:adventure-platform-neoforge:6.8.0")!!) // for Minecraft 1.21.11

}
```

build.gradle

```java
repositories {

// for development builds

maven {

name = 'sonatype-oss-snapshots1'

url = 'https://s01.oss.sonatype.org/content/repositories/snapshots/'

mavenContent { snapshotsOnly() }

}

// for releases

mavenCentral()

}

dependencies {

modImplementation include('net.kyori:adventure-platform-neoforge:6.8.0') // for Minecraft 1.21.11

}
```

  

Attention

Each major Minecraft release will require different platform versions. For older Minecraft versions, consult the table
at [Modded (Fabric and NeoForge shared API)](https://docs.papermc.io/adventure/platform/modded).

## Basic use

[Section titled “Basic use”](#basic-use)

See [Modded (Fabric and NeoForge shared API)](https://docs.papermc.io/adventure/platform/modded) for usage details common between NeoForge and Fabric.

## Server

[Section titled “Server”](#server)

The logical-server side of the modded platform can be accessed any time a server is available, through a `MinecraftServerAudiences`
instance. By default, translatable components will be rendered with the global translator, but a custom renderer can be passed when initializing the platform.

All `AudienceProvider` interface methods are supported.

To get started with Adventure, set up an audience provider like this:

```java
@Mod("my_mod")

public class MyMod {

private volatile MinecraftServerAudiences adventure;

public MinecraftServerAudiences adventure() {

if (this.adventure == null) {

throw new IllegalStateException("Tried to access Adventure without a running server!");

}

return this.adventure;

}

public MyMod() {

// Register with the server lifecycle callbacks

// This will ensure any platform data is cleared between game instances

// This is important on the integrated server, where multiple server instances

// can exist for one mod initialization.

NeoForge.EVENT_BUS.addListener((ServerStartingEvent e) ->

this.adventure = MinecraftServerAudiences.of(e.getServer())

);

NeoForge.EVENT_BUS.addListener((ServerStoppedEvent e) ->

this.adventure = null

);

}

}
```

From here, audiences can be acquired for players and any other `CommandSource`. Specialized serializer instances are also available, to allow using
game information in component serialization.

## Commands

[Section titled “Commands”](#commands)

The NeoForge platform includes a method to register the `KeyArgumentType` and `ComponentArgumentType`:

* `AdventureArgumentTypes.register();`

This should be called from the constructor of your `@Mod`-annotated class.
Registering the argument types on the server will require all clients that join to have the argument types
registered as well.

## Client

[Section titled “Client”](#client)

Special for the modded platform, purely client-side operations are supported. The setup is less involved than it is for the server, since the client is a singleton, and there
is only one subject that can be acted on: the client’s player.

This means that for most users the `MinecraftClientAudiences` object can be treated as a singleton. The only exception is users using a custom renderer. This makes using Adventure
audiences fairly simple, as this code example shows:

```java
void doThing() {

// Get the audience

final Audience client = MinecraftClientAudiences.of().audience();

// Do something. This will only work when the player is ingame.

client.sendMessage(Component.text("meow", NamedTextColor.DARK_PURPLE));

}
```

The full functionality of the `Audience` interface is available, including localization!


================================================================================
Chapter Title: ViaVersion
Original Link: https://docs.papermc.io/adventure/platform/viaversion/
================================================================================

On supported platforms (Sponge 7 and Bukkit), Adventure is able to enhance its functionality
by using the [ViaVersion](https://hangar.papermc.io/ViaVersion/ViaVersion) API
to send packets directly to the client. This allows, for instance, for a plugin on a Minecraft
1.7 server to send RGB chat messages and titles to clients on newer versions of Minecraft.

If you include the Sponge or Bukkit platforms, no further action is required: ViaVersion will
be detected and support for it will be enabled.


================================================================================
Chapter Title: Implementing platforms
Original Link: https://docs.papermc.io/adventure/platform/implementing/
================================================================================

Most users will be here to look at information about existing platform implementations, but for those who are looking to build their own platform integrations, look no further.

While at its core Adventure ‘just’ provides data structures and serializers, as the game evolves and more functionality is added there are more tunable options and platform hooks
necessary to produce the correct output for the applicable game version. This has led to the introduction of a variety of services that platforms can provide implementations of using
Java’s `ServiceLoader` mechanism. Some other behaviors are expected by convention. As there are not that many platforms that integrate with Adventure, this page is an attempt to
cover the common points. Please don’t be afraid to ask us questions, and together we can work on fleshing out this page.

## Services

[Section titled “Services”](#services)

### `ComponentSerializer` services

[Section titled “ComponentSerializer services”](#componentserializer-services)

Most of the serializers (Gson, legacy, etc.) have `Provider` SPI’s that allow customizing the default behaviors of serializers. These are most applicable for the Gson/other JSON
serializers where the data structures have changed over time, but the legacy serializer’s options can be worth referencing too. See the Javadoc for each serializer for more information.

For any `JSONComponentSerializer` subtype, we have tried to gather relevant tunable options within a single system, keyed by the game’s active
[data version](https://minecraft.wiki/w/Data_version). To handle hover events in pre-1.16 game versions, there’s the additional `LegacyHoverEventSerializer`
interface. We offer an implementation that uses `adventure-nbt` as a separate submodule, but platforms may wish to use a native NBT library for this instead.
Both of these options should be set on builders in the appropriate `Provider` implementation.

### Data component values

[Section titled “Data component values”](#data-component-values)

To handle storing platform-specific data on `show_item` hover events, we expose opaque data objects in-API. Platforms should provide logic to convert between different
implementations by providing an implementation of `DataComponentValueConverterRegistry.Provider`. For the most part this is just converting between platform-specific types
and the generic `TagSerializable` and `Removed` types, but platforms should make sure to include converters to `GsonDataComponentValue` (from both platform types
*and* the generic `TagSerializable` that requires parsing SNBT for a conversion to occur).

### Click callbacks

[Section titled “Click callbacks”](#click-callbacks)

As callbacks are a commonly desired feature, Adventure provides a ‘virtual’ click event type for callback functions. This action is not persistent between runs, and needs
platforms to register a command to trigger callbacks to execute. This is implemented via the `ClickCallback.Provider` SPI. This command should not be sent as part of the
command tree that clients receive to avoid spamming them.

Platforms implementing the click callback provider must register a command at the appropriate time, and maintain a registry of active callbacks that is added to any time a
callback command is requested. The platform is responsible for ensuring any execution conditions apply and implementing the effects of any `Option`s that may be set on the callback.

### Component logging

[Section titled “Component logging”](#component-logging)

`ComponentLogger`, as part of the `adventure-text-logger-slf4j` module, provides a logging interface that extends SLF4J and wraps any existing SLF4J logger (compatible with
v1 and v2). Platforms are responsible for providing the adapter that looks up the appropriate logger by name and serializes components to text.

This should involve performing any translations if necessary. The default behavior of the logger is to serialize to plain text, but platforms may want to look at the
`/serializer/ansi` serializer instead for colored output.

### Boss bars

[Section titled “Boss bars”](#boss-bars)

Boss bars are logistically somewhat complicated. As one of the few holders of mutable state in the library, they have to re-sync any state changes to their viewers.
In order to track viewers and link up to any internal state, the `BossBarImplementation.Provider` SPI allows platforms to provide their own implementation hooks per-bar.

## Conventional behaviors

[Section titled “Conventional behaviors”](#conventional-behaviors)

Some behaviors are expected by platforms beyond what is explicitly required by implementing certain interfaces. These are:

* When implementing `Audience`, any unsupported operations should fail silently.
* When sending components to a player, they should be passed through `GlobalTranslator` before sending to perform any translations (note: `GlobalTranslator` is only for
  custom translations, and should not contain vanilla resource pack translations - they have a different interpolation syntax than `GlobalTranslator` uses)
* There is no specific required list of Adventure modules to distribute with your platform, but we recommend `adventure-api`, `adventure-text-minimessage`,
  `adventure-text-logger-slf4j`, plus whatever serializers are required for the integration. We specifically do not recommend distributing the
  `adventure-text-serializer-legacy` module unless it is necessary for backwards compatibility within your platform.


================================================================================
Chapter Title: adventure
Original Link: https://docs.papermc.io/adventure/version-history/adventure
================================================================================

## v4.26.1

[Section titled “v4.26.1”](#v4.26.1)

Released on Dec 17, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.26.1)

Adventure 4.26.1 is *hopefully* the final release before the full release of 5.0. This release solely contains final changes and deprecations in preparation of the 5.0.

For full information about the 5.0 update, check out the following links:

* [Adventure 5.0 info issue](https://github.com/PaperMC/adventure/issues/1202)
* [Adventure 5.0 PR](https://github.com/PaperMC/adventure/pull/1253)
* [Migration docs PR](https://github.com/PaperMC/docs/pull/678)

Note: 4.26.0 was released on GitHub but never deployed and should be considered non existant.

## What's Changed

### ✨ Features

* Pre-5.0 update changes/deprecations by [@kezz](https://github.com/kezz) in [#1329](https://github.com/PaperMC/adventure/pull/1329)

### 📚 Documentation

* docs: Update documentation, discord and snapshot links by [@kezz](https://github.com/kezz) in [#1323](https://github.com/PaperMC/adventure/pull/1323)

**Full Changelog**: [v4.25.0...v4.26.1](https://github.com/PaperMC/adventure/compare/v4.25.0...v4.26.1)

---

## v4.26.0

[Section titled “v4.26.0”](#v4.26.0)

Released on Dec 17, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.26.0)

Adventure 4.26.0 is *hopefully* the final release before the full release of 5.0. This release solely contains final changes and deprecations in preparation of the 5.0.

For full information about the 5.0 update, check out the following links:

* [Adventure 5.0 info issue](https://github.com/PaperMC/adventure/issues/1202)
* [Adventure 5.0 PR](https://github.com/PaperMC/adventure/pull/1253)
* [Migration docs PR](https://github.com/PaperMC/docs/pull/678)

## What's Changed

### ✨ Features

* Pre-5.0 update changes/deprecations by [@kezz](https://github.com/kezz) in [#1329](https://github.com/PaperMC/adventure/pull/1329)

### 📚 Documentation

* docs: Update documentation, discord and snapshot links by [@kezz](https://github.com/kezz) in [#1323](https://github.com/PaperMC/adventure/pull/1323)

**Full Changelog**: [v4.25.0...v4.26.0](https://github.com/PaperMC/adventure/compare/v4.25.0...v4.26.0)

---

## v4.25.0

[Section titled “v4.25.0”](#v4.25.0)

Released on Oct 6, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.25.0)

## What's Changed

### ✨ Features

* Update for 1.21.9 by [@jpenilla](https://github.com/jpenilla) in [#1291](https://github.com/PaperMC/adventure/pull/1291)
* Add option to prepend https to click event urls by [@Emilxyz](https://github.com/Emilxyz) in [#1290](https://github.com/PaperMC/adventure/pull/1290)
* Allow passing parentStyle to Component#compact by [@indyteo](https://github.com/indyteo) in [#1288](https://github.com/PaperMC/adventure/pull/1288)
* Allow creation of a ClickEvent from an Action and Payload by [@Phoenix616](https://github.com/Phoenix616) in [#1322](https://github.com/PaperMC/adventure/pull/1322)
* Add `CompoundBinaryTag` contains methods by [@tal5](https://github.com/tal5) in [#1265](https://github.com/PaperMC/adventure/pull/1265)
* Add sequential (simple) head tag by [@Strokkur424](https://github.com/Strokkur424) in [#1320](https://github.com/PaperMC/adventure/pull/1320)
* Allow creating builders with an initial capacity by [@tal5](https://github.com/tal5) in [#1264](https://github.com/PaperMC/adventure/pull/1264)
* ObjectComponent serialization by [@Emilxyz](https://github.com/Emilxyz) in [#1293](https://github.com/PaperMC/adventure/pull/1293)

### 🐛 Fixes

* Provide the property directly in the properties DefaultOverideProvider by [@kezz](https://github.com/kezz) in [#1279](https://github.com/PaperMC/adventure/pull/1279)
* Correct `defaultValue` nullability by [@tal5](https://github.com/tal5) in [#1263](https://github.com/PaperMC/adventure/pull/1263)
* Fix invalid url extraction in legacy component serializer by [@derklaro](https://github.com/derklaro) in [#1280](https://github.com/PaperMC/adventure/pull/1280)

### 📚 Documentation

* Alongside this release, the old [adventure-docs](https://github.com/KyoriPowered/adventure-docs) repo has been archived and the documentation has been migrated to the [PaperMC docs](https://github.com/PaperMC/docs) repo.

### Other

* Check TagResolver#has in more places by [@kezz](https://github.com/kezz) in [#1297](https://github.com/PaperMC/adventure/pull/1297)

## New Contributors

* [@tal5](https://github.com/tal5) made their first contribution in [#1263](https://github.com/PaperMC/adventure/pull/1263)
* [@derklaro](https://github.com/derklaro) made their first contribution in [#1280](https://github.com/PaperMC/adventure/pull/1280)
* [@indyteo](https://github.com/indyteo) made their first contribution in [#1288](https://github.com/PaperMC/adventure/pull/1288)
* [@Phoenix616](https://github.com/Phoenix616) made their first contribution in [#1322](https://github.com/PaperMC/adventure/pull/1322)
* [@Strokkur424](https://github.com/Strokkur424) made their first contribution in [#1291](https://github.com/PaperMC/adventure/pull/1291)

**Full Changelog**: [v4.24.0...v4.25.0](https://github.com/PaperMC/adventure/compare/v4.24.0...v4.25.0)

---

## 🌏 Adventure 4.24.0

[Section titled “🌏 Adventure 4.24.0”](#v4.24.0)

Released on Jul 30, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.24.0)

## What's Changed

### ✨ Features

* feature(api): Add a method to close an open dialog by [@kezz](https://github.com/kezz) in [#1246](https://github.com/PaperMC/adventure/pull/1246)
* Implement #canTranslate in GlobalTranslatorImpl and call #canTranslate of its sources by [@ivi-kiwi](https://github.com/ivi-kiwi) in [#1252](https://github.com/PaperMC/adventure/pull/1252)
* Add a less verbose way of creating titles by [@LaserSlime](https://github.com/LaserSlime) in [#1272](https://github.com/PaperMC/adventure/pull/1272)
* feature(api): Property default override SPI and flattener nesting limit property by [@kezz](https://github.com/kezz) in [#1250](https://github.com/PaperMC/adventure/pull/1250)
* Uppercase hex colors created by asHexColor to avoid item desyncs in Minecraft by [@MrPowerGamerBR](https://github.com/MrPowerGamerBR) in [#1277](https://github.com/PaperMC/adventure/pull/1277)

### 🐛 Fixes

* Add `equals` to `VirtualComponent` by [@Seggan](https://github.com/Seggan) in [#1247](https://github.com/PaperMC/adventure/pull/1247)
* fix: component flattener not popping styles in correct order by [@diogotcorreia](https://github.com/diogotcorreia) in [#1255](https://github.com/PaperMC/adventure/pull/1255)
* fix(api): fix removing mutated source from GlobalTranslator by [@Emilxyz](https://github.com/Emilxyz) in [#1276](https://github.com/PaperMC/adventure/pull/1276)
* Avoid interpreting the "byte" suffix as a binary radix by [@IllusionTheDev](https://github.com/IllusionTheDev) in [#1241](https://github.com/PaperMC/adventure/pull/1241)

### 📚 Documentation

* docs: Remove wiki.vg link from NBT javadoc by [@kezz](https://github.com/kezz) in [#1251](https://github.com/PaperMC/adventure/pull/1251)

### Other

* chore: Deprecate non-named UTF8ResourceBundleControl getter by [@kezz](https://github.com/kezz) in [00ebf2e](https://github.com/PaperMC/adventure/commit/00ebf2e198280bbff8bc56724c8d080018b597e6)

## New Contributors

* [@Seggan](https://github.com/Seggan) made their first contribution in [#1247](https://github.com/PaperMC/adventure/pull/1247)
* [@diogotcorreia](https://github.com/diogotcorreia) made their first contribution in [#1255](https://github.com/PaperMC/adventure/pull/1255)
* [@Emilxyz](https://github.com/Emilxyz) made their first contribution in [#1276](https://github.com/PaperMC/adventure/pull/1276)
* [@ivi-kiwi](https://github.com/ivi-kiwi) made their first contribution in [#1252](https://github.com/PaperMC/adventure/pull/1252)
* [@LaserSlime](https://github.com/LaserSlime) made their first contribution in [#1272](https://github.com/PaperMC/adventure/pull/1272)
* [@IllusionTheDev](https://github.com/IllusionTheDev) made their first contribution in [#1241](https://github.com/PaperMC/adventure/pull/1241)
* [@MrPowerGamerBR](https://github.com/MrPowerGamerBR) made their first contribution in [#1277](https://github.com/PaperMC/adventure/pull/1277)

**Full Changelog**: [v4.23.0...v4.24.0](https://github.com/PaperMC/adventure/compare/v4.23.0...v4.24.0)

---

## 🌏 Adventure 4.23.0

[Section titled “🌏 Adventure 4.23.0”](#v4.23.0)

Released on Jun 18, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.23.0)

This is a hotfix release to resolve some issues in the recently released v4.22.0.

## What's Changed

### 🐛 Fixes

* fix: Ensure TagStringIO accepts hetergeneous lists in all reader methods by [@kezz](https://github.com/kezz) in [#1244](https://github.com/PaperMC/adventure/pull/1244)
* fix: Make custom click events hold NBT payloads by [@kezz](https://github.com/kezz) in [#1243](https://github.com/PaperMC/adventure/pull/1243)
* fix(key): Ensure keys with invalid namespaces throw the correct exception by [@kezz](https://github.com/kezz) in [#1245](https://github.com/PaperMC/adventure/pull/1245)

**Full Changelog**: [v4.22.0...v4.23.0](https://github.com/PaperMC/adventure/compare/v4.22.0...v4.23.0)

---

## 🌏 Adventure 4.22.0

[Section titled “🌏 Adventure 4.22.0”](#v4.22.0)

Released on Jun 17, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.22.0)

## What's Changed

### ✨ Features

* feature(api): Rewrite ComponentFlattener to remove recursion and add a configurable maximum nesting depth by [@kezz](https://github.com/kezz) in [#1237](https://github.com/PaperMC/adventure/pull/1237)
* 1.21.6 by [@kezz](https://github.com/kezz) in [#1238](https://github.com/PaperMC/adventure/pull/1238)
* feat(nbt): TagStringIO Enhancements by [@kermandev](https://github.com/kermandev) in [#1239](https://github.com/PaperMC/adventure/pull/1239)
* Improved support for hetergeneous lists by [@mworzala](https://github.com/mworzala) in [#1242](https://github.com/PaperMC/adventure/pull/1242)

### 🐛 Fixes

* fix(api): Always fire bossBarNameChanged by [@kezz](https://github.com/kezz) in [#1230](https://github.com/PaperMC/adventure/pull/1230)
* Typo fix in PrideTag.java by [@Stxellxa](https://github.com/Stxellxa) in [#1233](https://github.com/PaperMC/adventure/pull/1233)
* fix(api): Don't throw an exception if a PointersSupplier has no parent by [@kezz](https://github.com/kezz) in [#1232](https://github.com/PaperMC/adventure/pull/1232)

### 📚 Documentation

* chore(audience): update javadoc for playSound by [@Timongcraft](https://github.com/Timongcraft) in [#1235](https://github.com/PaperMC/adventure/pull/1235)

### Other

* Render translatable arguments and children by [@TonytheMacaroni](https://github.com/TonytheMacaroni) in [#1226](https://github.com/PaperMC/adventure/pull/1226)

## New Contributors

* [@Stxellxa](https://github.com/Stxellxa) made their first contribution in [#1233](https://github.com/PaperMC/adventure/pull/1233)
* [@Timongcraft](https://github.com/Timongcraft) made their first contribution in [#1235](https://github.com/PaperMC/adventure/pull/1235)
* [@kermandev](https://github.com/kermandev) made their first contribution in [#1239](https://github.com/PaperMC/adventure/pull/1239)
* [@mworzala](https://github.com/mworzala) made their first contribution in [#1242](https://github.com/PaperMC/adventure/pull/1242)

**Full Changelog**: [v4.21.0...v4.22.0](https://github.com/PaperMC/adventure/compare/v4.21.0...v4.22.0)

---

## 🌏 Adventure 4.21.0

[Section titled “🌏 Adventure 4.21.0”](#v4.21.0)

Released on Apr 30, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.21.0)

Adventure 4.21.0 adds preliminary support for new component features in 1.21.5, and some minor bugfixes. We recommend all users update.

## What's Changed

### ✨ Features

* Use DecorationMap for style builder by [@TonytheMacaroni](https://github.com/TonytheMacaroni) in [#1209](https://github.com/PaperMC/adventure/pull/1209)
* Add NumberBinaryTag#numberValue by [@GliczDev](https://github.com/GliczDev) in [#1188](https://github.com/PaperMC/adventure/pull/1188)
* feat(nbt): Add stream API for compound/list tags by [@zml2008](https://github.com/zml2008) in [#1208](https://github.com/PaperMC/adventure/pull/1208)
* 1.21.5 component changes by [@Gerrygames](https://github.com/Gerrygames) in [#1168](https://github.com/PaperMC/adventure/pull/1168)
* feature(minimessage): Set the target to hold the locale of the translation by default by [@kezz](https://github.com/kezz) in [#1216](https://github.com/PaperMC/adventure/pull/1216)
* feat(nbt): update number parsing for 1.21.5 by [@kennytv](https://github.com/kennytv) in [#1167](https://github.com/PaperMC/adventure/pull/1167)
* feature(api): Skip style builder creation on merge by [@kezz](https://github.com/kezz) in [#1219](https://github.com/PaperMC/adventure/pull/1219)
* feat(nbt): Initial implementation of heterogeneous list handling by [@zml2008](https://github.com/zml2008) in [#1218](https://github.com/PaperMC/adventure/pull/1218)

### 🐛 Fixes

* fix(minimessage): rename `numeric` to `string` by [@tjalp](https://github.com/tjalp) in [#1211](https://github.com/PaperMC/adventure/pull/1211)

## New Contributors

* [@TonytheMacaroni](https://github.com/TonytheMacaroni) made their first contribution in [#1209](https://github.com/PaperMC/adventure/pull/1209)
* [@tjalp](https://github.com/tjalp) made their first contribution in [#1211](https://github.com/PaperMC/adventure/pull/1211)
* [@Gerrygames](https://github.com/Gerrygames) made their first contribution in [#1168](https://github.com/PaperMC/adventure/pull/1168)

**Full Changelog**: [v4.20.0...v4.21.0](https://github.com/PaperMC/adventure/compare/v4.20.0...v4.21.0)

---

## 🌏 Adventure 4.20.0

[Section titled “🌏 Adventure 4.20.0”](#v4.20.0)

Released on Apr 5, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.20.0)

Adventure 4.20.0 is a feature release focused on translation improvements. The [MiniMessage translator](https://docs.advntr.dev/minimessage/translator.html) allows easily expressing translation values in the MiniMessage format, and the whole translation system has had a revamp to be more flexible.

## What's Changed

### ✨ Features

* feature(api): Silly micro optimisations for the mm color tag by [@kezz](https://github.com/kezz) in [#1177](https://github.com/PaperMC/adventure/pull/1177)
* feature(minimessage): Check for colors before parsing phases by [@kezz](https://github.com/kezz) in [#1180](https://github.com/PaperMC/adventure/pull/1180)
* feature(api): Improve handling of component children and component translating by [@kezz](https://github.com/kezz) in [#1181](https://github.com/PaperMC/adventure/pull/1181)
* feature: MiniMessageTranslator by [@kezz](https://github.com/kezz) in [#972](https://github.com/PaperMC/adventure/pull/972)
* feature(api, minimessage): Replace TranslationRegistry with a generic TranslationStore by [@kezz](https://github.com/kezz) in [#1182](https://github.com/PaperMC/adventure/pull/1182)
* feature(minimessage): Add context argument and unit tests by [@kezz](https://github.com/kezz) in [#1185](https://github.com/PaperMC/adventure/pull/1185)
* Add TagStringIO#asString for any tag by [@GliczDev](https://github.com/GliczDev) in [#1192](https://github.com/PaperMC/adventure/pull/1192)
* feat(text-serializer-commons): split into new module by [@zml2008](https://github.com/zml2008) in [#1193](https://github.com/PaperMC/adventure/pull/1193)

### ⚙️ Fixes

* fix(minimessage): Carry over target into context deserialize calls by [@kezz](https://github.com/kezz) in [#1179](https://github.com/PaperMC/adventure/pull/1179)

## New Contributors

* [@GliczDev](https://github.com/GliczDev) made their first contribution in [#1192](https://github.com/PaperMC/adventure/pull/1192)

**Full Changelog**: [v4.19.0...v4.20.0](https://github.com/PaperMC/adventure/compare/v4.19.0...v4.20.0)

---

## 🌏 Adventure 4.19.0

[Section titled “🌏 Adventure 4.19.0”](#v4.19.0)

Released on Feb 16, 2025
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.19.0)

Adventure 4.19.0 is a small feature release, primarily to introduce an option controlling MiniMessage's emission of virtual components.

## What's Changed

### ✨ Features

* feature(api): Replace text ignoring hover events by [@kezz](https://github.com/kezz) in [#1153](https://github.com/PaperMC/adventure/pull/1153)
* Configurable virtual component emission by [@lynxplay](https://github.com/lynxplay) in [#1164](https://github.com/PaperMC/adventure/pull/1164)

### 🐛 Fixes

* fix(api): add missing ScopedComponent overrides by [@zml2008](https://github.com/zml2008) in [#1161](https://github.com/PaperMC/adventure/pull/1161)

**Full Changelog**: [v4.18.0...v4.19.0](https://github.com/PaperMC/adventure/compare/v4.18.0...v4.19.0)

---

## 🌏 Adventure 4.18.0

[Section titled “🌏 Adventure 4.18.0”](#v4.18.0)

Released on Dec 22, 2024
- [GitHub](https://github.com/PaperMC/adventure/releases/tag/v4.18.0)

Adventure 4.18 has a few new features to improve expressiveness, plus support for the new shadow colour style attribute added in Minecraft 1.21.4.

## What's Changed

### ✨ Features

* feat(minimessage): Pride tag by [@kezz](https://github.com/kezz) in [#1079](https://github.com/PaperMC/adventure/pull/1079)
* feat(nbt): add isEmpty to CompoundBinaryTag/ListBinaryTag by [@RealBauHD](https://github.com/RealBauHD) in [#1088](https://github.com/PaperMC/adventure/pull/1088)
* feat(mini-message): add Formatter#joining by [@tahmid-23](https://github.com/tahmid-23) in [#938](https://github.com/PaperMC/adventure/pull/938)
* feat: shadow colors by [@kashike](https://github.com/kashike) in [#1124](https://github.com/PaperMC/adventure/pull/1124)
* feat(api): virtual components by [@kashike](https://github.com/kashike) in [#842](https://github.com/PaperMC/adventure/pull/842)

### 🐛 Fixes

* ensure numbers where we expected booleans parse correctly. by [@456dev](https://github.com/456dev) in [#1108](https://github.com/PaperMC/adventure/pull/1108)
* fix(text-serializer-gson): correctly handle removed data components by [@zml2008](https://github.com/zml2008) in [#1145](https://github.com/PaperMC/adventure/pull/1145)

## New Contributors

* [@456dev](https://github.com/456dev) made their first contribution in [#1108](https://github.com/PaperMC/adventure/pull/1108)
* [@tahmid-23](https://github.com/tahmid-23) made their first contribution in [#938](https://github.com/PaperMC/adventure/pull/938)

**Full Changelog**: [v4.17.0...v4.18.0](https://github.com/PaperMC/adventure/compare/v4.17.0...v4.18.0)

---


================================================================================
Chapter Title: adventure-platform
Original Link: https://docs.papermc.io/adventure/version-history/adventure-platform
================================================================================

## v4.4.1

[Section titled “v4.4.1”](#v4.4.1)

Released on Jul 30, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.4.1)

This is a patch release that adds initial support for 1.21.6/1.21.7.

## What's Changed

* Bukkit - Update MinecraftComponentSerializer for 1.21.6/7 by [@bloodmc](https://github.com/bloodmc) in [#212](https://github.com/PaperMC/adventure-platform/pull/212)

## New Contributors

* [@bloodmc](https://github.com/bloodmc) made their first contribution in [#212](https://github.com/PaperMC/adventure-platform/pull/212)

**Full Changelog**: [v4.4.0...v4.4.1](https://github.com/PaperMC/adventure-platform/compare/v4.4.0...v4.4.1)

---

## v4.4.0

[Section titled “v4.4.0”](#v4.4.0)

Released on May 10, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.4.0)

This release bumps the Adventure version used in order to support 1.21.5 on legacy platforms.

## What's Changed

### Other

* Support getLocale returning a Locale by [@Pablete1234](https://github.com/Pablete1234) in [#202](https://github.com/PaperMC/adventure-platform/pull/202)
* 1.21.5 support for platform-bukkit by [@MiniDigger](https://github.com/MiniDigger) in [#206](https://github.com/PaperMC/adventure-platform/pull/206)

## New Contributors

* [@Pablete1234](https://github.com/Pablete1234) made their first contribution in [#202](https://github.com/PaperMC/adventure-platform/pull/202)

**Full Changelog**: [v4.3.4...v4.4.0](https://github.com/PaperMC/adventure-platform/compare/v4.3.4...v4.4.0)

---

## v4.3.4

[Section titled “v4.3.4”](#v4.3.4)

Released on Aug 7, 2024
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.3.4)

This is a minor bugfix release that aims to fix some issues in certain environments.

## What's Changed

### 🐛 Fixes

* Fixed MinecraftComponentSerializer not working due to relocation by [@re-ovo](https://github.com/re-ovo) in [#177](https://github.com/PaperMC/adventure-platform/pull/177)
* Fix removed ResourceLocation constructor by [@56738](https://github.com/56738) in [#188](https://github.com/PaperMC/adventure-platform/pull/188)

## New Contributors

* [@re-ovo](https://github.com/re-ovo) made their first contribution in [#177](https://github.com/PaperMC/adventure-platform/pull/177)

**Full Changelog**: [v4.3.3...v4.3.4](https://github.com/PaperMC/adventure-platform/compare/v4.3.3...v4.3.4)

---

## v4.3.3

[Section titled “v4.3.3”](#v4.3.3)

Released on Jun 2, 2024
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.3.3)

This is a patch release to add support for Minecraft 1.20.5/1.20.6, for those who still choose to support legacy plataforms.

## What's Changed

### ✨ Features

* Bukkit 1.20.5 support by [@56738](https://github.com/56738) in [#163](https://github.com/PaperMC/adventure-platform/pull/163)
* BungeeCord: BossBar compatibilty with BungeeCord 1.20-R0.2 and newer by [@bivashy](https://github.com/bivashy) in [#153](https://github.com/PaperMC/adventure-platform/pull/153)

### 🐛 Fixes

* Fix tab list header/footer on Paper 1.20.6 by [@jpenilla](https://github.com/jpenilla) in [#171](https://github.com/PaperMC/adventure-platform/pull/171)
* Set player locale when creating Audience by [@CubBossa](https://github.com/CubBossa) in [#160](https://github.com/PaperMC/adventure-platform/pull/160)

### Other

* fix snapshot badge by [@powercasgamer](https://github.com/powercasgamer) in [#166](https://github.com/PaperMC/adventure-platform/pull/166)
* Fix javadoc generation by [@56738](https://github.com/56738) in [#168](https://github.com/PaperMC/adventure-platform/pull/168)

## New Contributors

* [@powercasgamer](https://github.com/powercasgamer) made their first contribution in [#166](https://github.com/PaperMC/adventure-platform/pull/166)
* [@bivashy](https://github.com/bivashy) made their first contribution in [#153](https://github.com/PaperMC/adventure-platform/pull/153)
* [@CubBossa](https://github.com/CubBossa) made their first contribution in [#160](https://github.com/PaperMC/adventure-platform/pull/160)

**Full Changelog**: [v4.3.2...v4.3.3](https://github.com/PaperMC/adventure-platform/compare/v4.3.2...v4.3.3)

---

## v4.3.2

[Section titled “v4.3.2”](#v4.3.2)

Released on Dec 21, 2023
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.3.2)

This is a patch release to add support for 1.20.3 and 1.20.4 on the Bukkit platform.

## What's Changed

* Fix MinecraftComponentSerializer on 1.20.3 by [@56738](https://github.com/56738) in [#144](https://github.com/PaperMC/adventure-platform/pull/144)

**Full Changelog**: [v4.3.1...v4.3.2](https://github.com/PaperMC/adventure-platform/compare/v4.3.1...v4.3.2)

---

## v4.3.1

[Section titled “v4.3.1”](#v4.3.1)

Released on Sep 29, 2023
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.3.1)

This is a bugfix release to add support for Minecraft 1.20.2 on the Bukkit platform.

## What's Changed

* Fix CraftBukkitFacet on 1.20.2 by [@56738](https://github.com/56738) in [#140](https://github.com/PaperMC/adventure-platform/pull/140)

## New Contributors

* [@56738](https://github.com/56738) made their first contribution in [#140](https://github.com/PaperMC/adventure-platform/pull/140)

**Full Changelog**: [v4.3.0...v4.3.1](https://github.com/PaperMC/adventure-platform/compare/v4.3.0...v4.3.1)

---

## v4.3.0

[Section titled “v4.3.0”](#v4.3.0)

Released on Mar 16, 2023
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.3.0)

This release adds full support for 1.19.4 on the Bukkit platform (though most functionality should work even on 4.2.0).

## What's Changed

* fix: 1.19.4 bound chat types by [@Machine-Maker](https://github.com/Machine-Maker) in [#128](https://github.com/PaperMC/adventure-platform/pull/128)

## New Contributors

* [@neziw](https://github.com/neziw) made their first contribution in [#124](https://github.com/PaperMC/adventure-platform/pull/124)

**Full Changelog**: [v4.2.0...v4.3.0](https://github.com/PaperMC/adventure-platform/compare/v4.2.0...v4.3.0)

---

## v4.2.0

[Section titled “v4.2.0”](#v4.2.0)

Released on Dec 9, 2022
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.2.0)

## What's Changed

* fix: CraftBukkit BossBar for 1.18+ by [@Machine-Maker](https://github.com/Machine-Maker) in [#94](https://github.com/PaperMC/adventure-platform/pull/94)
* Bump adventure to 4.12 and use sound seed when present by [@jpenilla](https://github.com/jpenilla) in [#112](https://github.com/PaperMC/adventure-platform/pull/112)
* 1.19.3 chat for bukkit by [@Machine-Maker](https://github.com/Machine-Maker) in [#113](https://github.com/PaperMC/adventure-platform/pull/113)
* Fix craftbukkit entity sound facet for 1.19.3 by [@Machine-Maker](https://github.com/Machine-Maker) in [#117](https://github.com/PaperMC/adventure-platform/pull/117)

**Full Changelog**: [v4.1.2...v4.2.0](https://github.com/PaperMC/adventure-platform/compare/v4.1.2...v4.2.0)

---

## v4.1.2

[Section titled “v4.1.2”](#v4.1.2)

Released on Aug 3, 2022
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.1.2)

## What's Changed

* Fix ViaFacet component type by [@kennytv](https://github.com/kennytv) in [#95](https://github.com/PaperMC/adventure-platform/pull/95)
* fix: CraftBukkit Chat facet for 1.19.1 by [@Machine-Maker](https://github.com/Machine-Maker) in [#98](https://github.com/PaperMC/adventure-platform/pull/98)
* fix: CraftBukkit EntitySound for 1.19+ by [@Machine-Maker](https://github.com/Machine-Maker) in [#99](https://github.com/PaperMC/adventure-platform/pull/99)

**Full Changelog**: [v4.1.1...v4.1.2](https://github.com/PaperMC/adventure-platform/compare/v4.1.1...v4.1.2)

---

## adventure-platform 4.1.1

[Section titled “adventure-platform 4.1.1”](#v4.1.1)

Released on Jun 12, 2022
- [GitHub](https://github.com/PaperMC/adventure-platform/releases/tag/v4.1.1)

## What's Changed

* fix: CraftBukkit Chat facet for 1.19 by [@Machine-Maker](https://github.com/Machine-Maker) in [#93](https://github.com/PaperMC/adventure-platform/pull/93)

## New Contributors

* [@Machine-Maker](https://github.com/Machine-Maker) made their first contribution in [#93](https://github.com/PaperMC/adventure-platform/pull/93)

**Full Changelog**: [v4.1.0...v4.1.1](https://github.com/PaperMC/adventure-platform/compare/v4.1.0...v4.1.1)

---


================================================================================
Chapter Title: adventure-platform-mod
Original Link: https://docs.papermc.io/adventure/version-history/adventure-platform-mod
================================================================================

## 🌍 adventure-platform-mod 6.8.0

[Section titled “🌍 adventure-platform-mod 6.8.0”](#v6.8.0)

Released on Dec 9, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.8.0)

This version of adventure-platform-mod adds support for Minecraft 1.21.11, distributing Adventure 4.25.0 for the Fabric and NeoForge platforms. Minecraft versions older than 1.21.11 are not supported by this release.

**Full Changelog**: [v6.7.0...v6.8.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.7.0...v6.8.0)

---

## 🌍 adventure-platform-mod 6.7.0

[Section titled “🌍 adventure-platform-mod 6.7.0”](#v6.7.0)

Released on Oct 6, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.7.0)

This version of adventure-platform-mod adds support for Minecraft 1.21.9, distributing Adventure 4.25.0 for the Fabric and NeoForge platforms. Minecraft versions older than 1.21.9 are not supported by this release.

**Full Changelog**: [v6.6.0...v6.7.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.6.0...v6.7.0)

---

## 🌍 adventure-platform-mod 6.6.0

[Section titled “🌍 adventure-platform-mod 6.6.0”](#v6.6.0)

Released on Jul 30, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.6.0)

This version of adventure-platform-mod updates the distributed version of Adventure to 4.24.0.

**Full Changelog**: [v6.5.1...v6.6.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.5.1...v6.6.0)

---

## 🌍 adventure-platform-mod 6.5.1

[Section titled “🌍 adventure-platform-mod 6.5.1”](#v6.5.1)

Released on Jul 23, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.5.1)

This version of adventure-platform-mod is a hotfix to address metadata not passing Maven Central validation.

**Full Changelog**: [v6.5.0...v6.5.1](https://github.com/PaperMC/adventure-platform-mod/compare/v6.5.0...v6.5.1)

---

## 🌍 adventure-platform-mod 6.5.0

[Section titled “🌍 adventure-platform-mod 6.5.0”](#v6.5.0)

Released on Jul 23, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.5.0)

This version of adventure-platform-mod adds support for Minecraft 1.21.6 through 1.21.8, distributing Adventure 4.23.0 for the Fabric and NeoForge platforms. Minecraft versions older than 1.21.6 are not supported by this release.

## What's Changed

### ✨ Features

* Minecraft 1.21.6 by [@jpenilla](https://github.com/jpenilla) in [#206](https://github.com/PaperMC/adventure-platform-mod/pull/206)

**Full Changelog**: [v6.4.0...v6.5.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.4.0...v6.5.0)

---

## 🌍 adventure-platform-mod 6.4.0

[Section titled “🌍 adventure-platform-mod 6.4.0”](#v6.4.0)

Released on May 10, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.4.0)

This version of adventure-platform-mod adds support for Minecraft 1.21.5, distributing Adventure 4.21.0 for the Fabric and NeoForge platforms.

## What's Changed

* Initial update for Minecraft 1.21.5 by [@jpenilla](https://github.com/jpenilla) in [#197](https://github.com/PaperMC/adventure-platform-mod/pull/197)

**Full Changelog**: [v6.3.0...v6.4.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.3.0...v6.4.0)

---

## 🌍 adventure-platform-mod 6.3.0

[Section titled “🌍 adventure-platform-mod 6.3.0”](#v6.3.0)

Released on Apr 5, 2025
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.3.0)

This release of adventure-platform-mod packages adventure 4.20.0 supporting Minecraft 1.21.4 for the Fabric and NeoForge platforms.

The only change in this release is to bump the packaged versions of Adventure and its dependencies.

**Full Changelog**: [v6.2.0...v6.3.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.2.0...v6.3.0)

---

## 🌍 adventure-platform-mod 6.2.0

[Section titled “🌍 adventure-platform-mod 6.2.0”](#v6.2.0)

Released on Dec 23, 2024
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.2.0)

This feature release of adventure-platform-mod bundles Adventure 4.18.0, compatible with Minecraft 1.21.2-1.21.4 on the Fabric and NeoForge platforms.

## What's Changed

### 🐛 Fixes

* Add dependencies to fabric-repack by [@jpenilla](https://github.com/jpenilla) in [#172](https://github.com/PaperMC/adventure-platform-mod/pull/172)
* fix(common): Add DCV converter for MM -> Gson by [@zml2008](https://github.com/zml2008) in [#178](https://github.com/PaperMC/adventure-platform-mod/pull/178)

### Other

* build: Replace hacky workarounds for run configs by [@jpenilla](https://github.com/jpenilla) in [#173](https://github.com/PaperMC/adventure-platform-mod/pull/173)

**Full Changelog**: [v6.1.0...v6.2.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.1.0...v6.2.0)

---

## 🌍 adventure-platform-mod 6.1.0

[Section titled “🌍 adventure-platform-mod 6.1.0”](#v6.1.0)

Released on Oct 28, 2024
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.1.0)

adventure-platform-mod 6.1.0 is a feature release bringing the platform interface to Minecraft 1.21.2-1.21.3, with Adventure 4.17.0 as before on both the Fabric and NeoForge mod loaders.

For Fabric users, this is the first published release in the 6.x series. See the [6.0.0 release notes](https://github.com/KyoriPowered/adventure-platform-mod/releases/tag/v6.0.0) for a summary of the changes.

## What's Changed

### ✨ Features

* 1.21.2 by [@zml2008](https://github.com/zml2008) in [#157](https://github.com/PaperMC/adventure-platform-mod/pull/157)
* Expose non-wrapping conversion outside of an active game by [@zml2008](https://github.com/zml2008) in [#166](https://github.com/PaperMC/adventure-platform-mod/pull/166)

**Full Changelog**: [v6.0.1...v6.1.0](https://github.com/PaperMC/adventure-platform-mod/compare/v6.0.1...v6.1.0)

---

## 🌍 adventure-platform-mod 6.0.1

[Section titled “🌍 adventure-platform-mod 6.0.1”](#v6.0.1)

Released on Oct 20, 2024
- [GitHub](https://github.com/PaperMC/adventure-platform-mod/releases/tag/v6.0.1)

adventure-platform-mod 6.0.1 is a patch release with Adventure 4.17.0 targeting Minecraft 1.21.1. As with 6.0.0, only `adventure-platform-neoforge` is released for this version.

## What's Changed

### 🐛 Fixes

* Fixes NPE in ServerPlayerAudience#sendResourcePacks by [@toxicity188](https://github.com/toxicity188) in [#161](https://github.com/PaperMC/adventure-platform-mod/pull/161)
* Implement equals and hashCode on WrappedComponent by [@jpenilla](https://github.com/jpenilla) in [#163](https://github.com/PaperMC/adventure-platform-mod/pull/163)

## New Contributors

* [@toxicity188](https://github.com/toxicity188) made their first contribution in [#161](https://github.com/PaperMC/adventure-platform-mod/pull/161)

**Full Changelog**: [v6.0.0...v6.0.1](https://github.com/PaperMC/adventure-platform-mod/compare/v6.0.0...v6.0.1)

---


================================================================================
Chapter Title: Overview
Original Link: https://docs.papermc.io/adventure/migration/
================================================================================

Moving to Adventure from other APIs is fairly straightforward. These guides
provide advice and replacements for tasks in other APIs.

* [Migrating from the BungeeCord Chat API](https://docs.papermc.io/adventure/migration/bungeecord-chat-api)
  + [Audiences](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#audiences)
  + [Decoration and styling](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#decoration-and-styling)
  + [Chat colors](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#chat-colors)
  + [Differences in `ComponentBuilder`](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#differences-in-componentbuilder)
  + [Immutability](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#immutability)
  + [Serializers](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#serializers)
  + [Backwards compatibility](https://docs.papermc.io/adventure/migration/bungeecord-chat-api#backwards-compatibility)
* [Migrating from text 3.x](https://docs.papermc.io/adventure/migration/text-3.x)
  + [A word of caution](https://docs.papermc.io/adventure/migration/text-3.x#a-word-of-caution)
  + [Breaking changes from text 3.x](https://docs.papermc.io/adventure/migration/text-3.x#breaking-changes-from-text-3x)
  + [Serializer](https://docs.papermc.io/adventure/migration/text-3.x#serializer)


================================================================================
Chapter Title: Migrating from the BungeeCord Chat API
Original Link: https://docs.papermc.io/adventure/migration/bungeecord-chat-api/
================================================================================

Adventure’s text API and the BungeeCord Chat API are designed along very different
methodologies. This page goes over some notable differences.

## Audiences

[Section titled “Audiences”](#audiences)

It is strongly recommended you read about [Audiences](https://docs.papermc.io/adventure/audiences) first. Unlike BungeeCord,
which limits functionality to specific user types, Adventure allows only the specific
operations that apply to an audience to be taken.

## Decoration and styling

[Section titled “Decoration and styling”](#decoration-and-styling)

The BungeeCord Chat API stores all decorations in the `BaseComponent`. Adventure separates
out styles into their own `Style` class.

BungeeCord allows you to merge the styles from one component into another. Adventure provides
equivalent methods that merge styles together, or allows you to replace the styles on one
component with another.

## Chat colors

[Section titled “Chat colors”](#chat-colors)

Adventure’s chat color and styling hierarchy differs from that of BungeeCord’s `ChatColor`
API. This is probably where the most stark contrast between the Adventure API and BungeeCord/Bukkit
will manifest.

### Replacement for `ChatColor`

[Section titled “Replacement for ChatColor”](#replacement-for-chatcolor)

Adventure’s equivalents for `ChatColor` are split over three types:

* Formatting types (such as `BOLD` or `ITALIC`) are in `TextDecoration`, and can be set
  on a component or a style with the `decoration` method. Decorations also use a tristate to
  specify if they are enabled, disabled, or not set (in which case the component inherits the
  setting from its parent component).
* Named colors (also called the legacy Mojang color codes) now exist in the `NamedTextColor`
  class.
* RGB colors are constructed using the `TextColor.color()` methods (this is equivalent to the
  `ChatColor.of()` method in the BungeeCord `ChatColor` 1.16 API.

### Legacy strings can’t be constructed

[Section titled “Legacy strings can’t be constructed”](#legacy-strings-cant-be-constructed)

The BungeeCord `ChatColor` API’s heritage is in the Bukkit API. The Bukkit `ChatColor` API in turn
dates from the early days of Minecraft (Beta 1.0), when the normal and accepted way of sending formatted
messages to the client was to concatenate magical strings that told the client what to format. A formatted
chat message would be sent to the client like this:

```java
player.sendMessage(ChatColor.GREEN + "Hi everyone, " + ChatColor.BOLD + "this message is in green and bold" + ChatColor.RESET + ChatColor.GREEN + "!");
```

This style of sending messages has persisted to this day, even as Mojang introduced rich chat components
into Minecraft 1.7.2. Bukkit preserved this backwards-compatible behavior, and BungeeCord introduced the
change as a result of being compatible with the Bukkit `ChatColor` class.

In Adventure, you can’t concatenate magical formatting codes. The equivalent of `ChatColor` in Adventure,
`TextColor`, instead returns descriptive text describing the color when its `toString()` is called. The
recommended replacement is to convert all legacy messages to components.

### `ChatColor.stripColor()`

[Section titled “ChatColor.stripColor()”](#chatcolorstripcolor)

`ChatColor.stripColor()` does not exist in Adventure. An equivalent would be to use
`PlainTextComponentSerializer.plainText().serialize(LegacyComponentSerializer.legacySection().deserialize(input))`.

### `ChatColor.translateAlternateColorCodes()`

[Section titled “ChatColor.translateAlternateColorCodes()”](#chatcolortranslatealternatecolorcodes)

`ChatColor.translateAlternateColorCodes()` does not exist in Adventure. Instead you should use
`LegacyComponentSerializer.legacy(altChar).deserialize(input)` when deserializing a legacy
string.

## Differences in `ComponentBuilder`

[Section titled “Differences in ComponentBuilder”](#differences-in-componentbuilder)

The BungeeCord `ComponentBuilder` treats each component independently and allows you
to manually carry over styles from a prior component. In Adventure, there are multiple
component builders. The closest equivalent for a BungeeCord `ComponentBuilder` is
to append components to a top-level empty component using `Component.text()`
as a base. To replicate the behavior of `ComponentBuilder`, consider doing the
following:

* Use the `Style` class to store common styles and the `mergeStyle` and `style`
  methods to merge and replace styles on a component.
* Use the Adventure `TextComponent` builder to create one component at a time and
  then append to a top-level text component builder that is empty.

As an example, this BungeeCord component:

```java
new ComponentBuilder("hello")

.color(ChatColor.GOLD)

.append(" world", FormatRetention.NONE)

.build()
```

becomes this Adventure equivalent:

```java
Component.text()

.append(Component.text("hello", NamedTextColor.GOLD)

.append(Component.text(" world"))

.build()
```

Likewise,

```java
new ComponentBuilder("hello")

.color(ChatColor.GOLD)

.bold(true)

.append(" world")

.build()
```

becomes

```java
Style style = Style.style(NamedTextColor.GOLD, TextDecoration.BOLD);

Component.text()

.append(Component.text("hello", style)

.append(Component.text(" world", style))

.build()
```

## Immutability

[Section titled “Immutability”](#immutability)

In the BungeeCord Chat API, all components are mutable. Adventure text components,
however, are immutable - any attempt to change a component results in a new component
being created that is a copy of the original component with the change you requested.

## Serializers

[Section titled “Serializers”](#serializers)

The BungeeCord Chat API includes three serializers. All three have equivalents in Adventure:

* The `TextComponent.fromLegacyText()` deserialization method is equivalent to the
  `deserialize` method of the [Legacy](https://docs.papermc.io/adventure/serializer/legacy) text serializer. Likewise, the
  `BaseComponent.toLegacyText()` serialization method is equivalent to the `serialize`
  method on the legacy text serializer.
* The `TextComponent.toPlainText()` serialization method is equivalent to the
  `serialize` method of the [Plain](https://docs.papermc.io/adventure/serializer/plain) text serializer. A component can be
  created from a plain-text string using `Component.text(string)`
* The Adventure equivalent of `ComponentSerializer` is the [Gson](https://docs.papermc.io/adventure/serializer/gson) text
  serializer.

## Backwards compatibility

[Section titled “Backwards compatibility”](#backwards-compatibility)

The `BungeeCordComponentSerializer` allows you to convert between Adventure [Components](https://docs.papermc.io/adventure/text)
and the native BungeeCord chat component API and back. This can be used when native platform support is
unavailable. The serializer is available in the `adventure-platform-text-serializer-bungeecord` artifact.


================================================================================
Chapter Title: Migrating from text 3.x
Original Link: https://docs.papermc.io/adventure/migration/text-3.x/
================================================================================

Adventure is an evolution of the text 3.x API. If you’ve worked with
the text API before, the switch to Adventure should be relatively quick.
For the most part, you’ll just need to depend on the Adventure API
and the relevant [Platform](https://docs.papermc.io/adventure/platform) you support and replace references
to classes in `net.kyori.text` to `net.kyori.adventure.text`, though see
below for major breaking changes.

## A word of caution

[Section titled “A word of caution”](#a-word-of-caution)

However, before you continue, it is strongly recommended you read about
[Audiences](https://docs.papermc.io/adventure/audiences). Unlike text, Adventure defines a standard interface for
sending content (including chat messages) to viewers. In addition, Adventure
defines interfaces for other game play mechanics that can be arbitrarily sent
to players.

## Breaking changes from text 3.x

[Section titled “Breaking changes from text 3.x”](#breaking-changes-from-text-3x)

### Factory methods renamed

[Section titled “Factory methods renamed”](#factory-methods-renamed)

In text 3.x, components could be constructed using the `<type>Component.of()` methods.
In Adventure, we’ve changed to using `Component.<type>(/*...*/)` style methods to allow
for easier static imports.

Similarly, `Style.of(/*...*/)` is changed to `Style.style(/*...*/)`.

### `.builder()`

[Section titled “.builder()”](#builder)

Builders are now created by calling the aforementioned factory methods with no parameters.
For example, `TextComponent.builder()` becomes `Component.text()`.

Note that the equivalent of `TextComponent.builder("hello")` is `Component.text().content("hello")`.

### `.append()` with a String argument

[Section titled “.append() with a String argument”](#append-with-a-string-argument)

Component builders in 3.x had a shorthand for appending a new text component: `builder.append("wow")`.
In Adventure you have to write it in full, `builder.append(Component.text("wow"))` in this case.

### `LegacyComponentSerializer`

[Section titled “LegacyComponentSerializer”](#legacycomponentserializer)

In text 3.x, you would deserialize a component that used a color code prefix that
differed from the section symbol normally used by using `LegacyComponentSerializer.legacy().deserialize(string, altChar)`.
In Adventure, the API to use is `LegacyComponentSerializer.legacy(altChar).deserialize(string)`.

To make a linking serializer you have to use the builder.
Change `LegacyComponentSerializer.legacyLinking(style)`
to `LegacyComponentSerializer.builder().extractUrl(style).build()`.

### `TextColor` renamed to `NamedTextColor`

[Section titled “TextColor renamed to NamedTextColor”](#textcolor-renamed-to-namedtextcolor)

In order to accommodate the new RGB colors introduced in 1.16, all the named text colors
were moved to the `NamedTextColor` class. References to the old `TextColor` class
should be updated to refer to `NamedTextColor`.

## Serializer

[Section titled “Serializer”](#serializer)

If you have a need to interoperate with clients using the old text 3.x API, you
can use the `adventure-text-serializer-legacy-text3` artifact, which includes a
`LegacyText3ComponentSerializer` that can convert from Adventure to text 3.x
components and back. Note that RGB colors will be downsampled.
