# PaperMC Documentation
> Generated: 2026-01-25 00:58:00
> Source: https://docs.papermc.io/paper/

---



================================================================================
Chapter Title: Getting started
Original Link: https://docs.papermc.io/paper/getting-started/
================================================================================

## Requirements

[Section titled “Requirements”](#requirements)

Tip

Paper requires at least **Java 21** to run, which [is easy to download and install](https://docs.papermc.io/misc/java-install).

| Paper Version | Recommended Java Version |
| --- | --- |
| 1.8 to 1.11 | Java 8 |
| 1.12 to 1.16.4 | Java 11 |
| 1.16.5 | Java 16 |
| 1.17.1-1.18.1+ | Java 21 |

## Downloading Paper

[Section titled “Downloading Paper”](#downloading-paper)

Paper provides runnable server JARs directly from our
[website’s downloads page](https://papermc.io/downloads).

Click on the build number to download a file.

## Running the server

[Section titled “Running the server”](#running-the-server)

To run the server you will need to either create a startup script
or run a command in your terminal.

You can generate a startup script using our [Startup Script Generator](https://docs.papermc.io/misc/tools/start-script-gen).
You can also obtain the optimized terminal command to run the server there.

If you’re just looking for a short command:

Terminal window

```java
java -Xms4G -Xmx4G -jar paper.jar --nogui
```

Ensure you navigated your terminal to the directory of your server
and that you have replaced `paper.jar` with the name of the JAR you have downloaded.

The amount of RAM can be set by changing the numbers in the `Xmx` and `Xms` arguments.
`--nogui` disables Vanilla’s GUI, so you don’t get double interfaces when using the command line.

To configure your server, see the [Global Configuration](https://docs.papermc.io/paper/reference/global-configuration) and
[Per World Configuration](https://docs.papermc.io/paper/reference/world-configuration) pages.

## Updating the server

[Section titled “Updating the server”](#updating-the-server)

Updating Paper is simple! See our [Update Tutorial](https://docs.papermc.io/paper/updating) for more information.

## Migrating to Paper

[Section titled “Migrating to Paper”](#migrating-to-paper)

### From Vanilla

[Section titled “From Vanilla”](#from-vanilla)

Migrating from Vanilla is easy, but there are some differences, namely in world saves. Paper (and
CraftBukkit and Spigot) separate out each dimension of a world (nether, the end, etc.) into separate
world folders.

Paper will handle this conversion for you automatically. No additional consideration is required.

### From CraftBukkit or Spigot

[Section titled “From CraftBukkit or Spigot”](#from-craftbukkit-or-spigot)

Paper is a drop in replacement for both CraftBukkit and Spigot, you don’t need to make any changes.

## Next steps

[Section titled “Next steps”](#next-steps)

Take a look at our [Next Steps](https://docs.papermc.io/paper/next-steps) guide to get your server up and running with the best performance and
features.


================================================================================
Chapter Title: Adding plugins
Original Link: https://docs.papermc.io/paper/adding-plugins/
================================================================================

Plugins are the most powerful way to extend the functionality of Paper beyond the configuration
files. Functionality added by plugins can range from making milk restore hunger or dead bushes grow,
to adding entirely new and original game modes or items.

Malicious Plugins

Ensure you fully trust the source of any plugin before installing it. Plugins are given **full and
unrestricted** access to not only your server but also the machine that it runs on. Because of this,
it is imperative that plugins only be installed from trusted sources. Be careful!

## Finding plugins

[Section titled “Finding plugins”](#finding-plugins)

Before installing a plugin, you’ll need to find what you want to install. The best place to find plugins is [Hangar](https://hangar.papermc.io), Paper’s plugin repository, but you can also find many plugins
on [SpigotMC](https://www.spigotmc.org/resources/),
[BukkitDev](https://dev.bukkit.org/bukkit-plugins), or the
[PaperMC Forums](https://forums.papermc.io/forums/paper-plugin-releases/), while other plugins may
release on [GitHub](https://github.com). One of the best ways to find plugins isn’t to browse any of
these sites directly but to search for plugins using a search engine. Searching for the function you
desire followed by `Minecraft plugin` will often yield good results.

Spigot and Bukkit Plugins

Paper is compatible with both Spigot and Bukkit plugins. It’s okay if a plugin does not explicitly
mention Paper compatibility. It’ll still work.

## Installing plugins

[Section titled “Installing plugins”](#installing-plugins)

1. Once you’ve found the plugin you’d like to install, download it. Ensure the file you have
   downloaded ends in `.jar`. Some plugins also distribute as `.zip` files, in which case you will
   need to extract the file and locate the `.jar` for your platform, often labeled `bukkit` or
   `paper`.
2. Once you have the plugin downloaded locally, locate the `plugins` folder from the root directory
   of your Paper server.
3. Drag and drop the plugin file (`.jar`) into the `plugins` folder. If you are using a shared
   hosting service, you may need to use their web panel or SFTP to upload the plugin; however, the
   procedure will be the same.
4. Restart your server. The plugin should load.
5. Check your work. Once the server has finished loading, run the `/plugins` command in-game or type
   `plugins` into the console. You should see your freshly installed plugin listed in green. If it
   is not listed or is colored red, continue to [troubleshooting](#troubleshooting). A plugin listed
   in red means that it is not currently enabled. For a freshly installed plugin, this often means
   that the plugin failed to load.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Check your logs

[Section titled “Check your logs”](#check-your-logs)

The first step to troubleshooting installing plugins is to check the log of your server. Your
server’s most recent logs will be stored to the `logs/latest.log` file. You may need to scroll near
the beginning of this file to see when plugins were loaded.

#### Missing dependencies

[Section titled “Missing dependencies”](#missing-dependencies)

If you see something like this:

```java
[00:00:00] [Server thread/WARN] Could not load 'plugins/MyAwesomePlugin-1.0.0.jar' in folder 'plugins'

[00:00:00] [Server thread/WARN] org.bukkit.plugin.UnknownDependencyException: Unknown/missing dependency plugins: [Vault]. Please download and install these plugins to run 'MyAwesomePlugin'.
```

This means that the plugin you tried to install is missing a dependency. A dependency, in this case,
is another plugin that you must install for the first to function. While you will get a big scary
error, the important line to look at is:

```java
[00:00:00] [Server thread/WARN] Unknown/missing dependency plugins: [Vault]. Please download and install these plugins to run 'MyAwesomePlugin'.
```

This is telling you that in order to load `MyAwesomePlugin`, you must first install `Vault`.

#### Invalid `plugin.yml`

[Section titled “Invalid plugin.yml”](#invalid-pluginyml)

If you see something closer to this:

```java
[00:00:00] [Server thread/WARN] Could not load 'plugins/MyAwesomePlugin-1.0.0.jar' in folder 'plugins'

[00:00:00] [Server thread/WARN] org.bukkit.plugin.InvalidDescriptionException: Invalid plugin.yml
```

This means that what you have downloaded isn’t a valid Paper plugin. This is generally caused by one
of the following:

1. The plugin you downloaded isn’t a plugin at all, but instead a mod for Forge, Fabric, or similar.
   These will not run on Paper.
2. The plugin failed to download completely. Especially when using tools such as `curl` or `wget`,
   you can easily download error pages rather than the plugin you intended. This may also be caused
   by a network issue. Attempt to download the plugin again. If you are using FTP (not SFTP or a web
   panel) to upload your plugin to a shared hosting service, ensure your FTP client is in `binary`
   and not `ASCII` mode. Consult the documentation for your FTP client for details.

#### Ambiguous plugin name

[Section titled “Ambiguous plugin name”](#ambiguous-plugin-name)

If you see something like this:

```java
[00:00:00] [Server thread/WARN] Ambiguous plugin name `Essentials' for files `plugins/EssentialsX-2.19.4.jar' and `plugins/Essentialsx-2.20.0-dev.jar' in `plugins'
```

This means you have two plugins with the same name, which is not supported. In this case, two
versions of EssentialsX are installed. Both the release `2.19.4`, and a development build of
`2.20.0`. Ensure you only have one version of each plugin installed at one time. Delete the older
version of the duplicate plugin, and restart your server.

To prevent accidentally installing two versions of one plugin while updating, you can use
the `update` folder as described in the [Update Guide](https://docs.papermc.io/paper/updating#step-2-update-plugins).

#### Something else

[Section titled “Something else”](#something-else)

If you see an error, but it isn’t similar to one of the above, attempt to read it yourself. While
the full error may be large and scary, you likely only have to read the first one or two lines to
understand what is going on. If you’re not sure, do not hesitate to reach out for support on our
[Discord](https://discord.gg/papermc) in the `#paper-help` channel.

### If nothing is logged

[Section titled “If nothing is logged”](#if-nothing-is-logged)

If nothing is logged, your server is likely not attempting to load any plugins. The conditions
needed for the server to load a plugin are as follows:

1. The file is at the root of the `plugins` folder, relative to its working directory. This is
   usually the same folder as the server JAR file. **Subdirectories of the `plugins` folder will not
   be checked.** All plugins must be in the root folder.
2. The file ends in `.jar`. If your plugin does not end in `.jar`, what you have downloaded may not
   be a plugin. Note that some plugins distribute multiple JARs as `.zip` files. If this is the
   case, you have to extract them before installing the plugin.

If both of these are true, and you still see no logs, please reach out for support on our
[Discord](https://discord.gg/papermc) server in the `#paper-help` channel. We will be happy to
assist you.


================================================================================
Chapter Title: Migrating to or from Paper
Original Link: https://docs.papermc.io/paper/migration/
================================================================================

It’s simple to migrate your server to or from Paper. The steps below will help you get started.

Backup your data before you start!

Before you begin, please ensure you have a full backup of your server.

See our [Backup Guide](https://docs.papermc.io/paper/updating#step-1-backup) for more information.

## Migrating to Paper

[Section titled “Migrating to Paper”](#migrating-to-paper)

### From CraftBukkit or Spigot

[Section titled “From CraftBukkit or Spigot”](#from-craftbukkit-or-spigot)

It’s easy to migrate from CraftBukkit or Spigot to Paper. Follow the steps below.

1. Stop your server if it is running, and create a full backup.
2. Download Paper from [our downloads page](https://papermc.io/downloads).
3. Rename the downloaded file to match the name specified in the [start command](https://docs.papermc.io/paper/getting-started#running-the-server).
4. Replace your existing JAR file with your freshly downloaded Paper JAR.
5. Start your new server.

Paper retains full compatibility with all Spigot plugins, allowing a seamless transition.

Note

Your new Paper server will still use [`bukkit.yml`](https://docs.papermc.io/paper/reference/bukkit-configuration)
and [`spigot.yml`](https://docs.papermc.io/paper/reference/spigot-configuration).
New configuration options can be found in [`config/paper-global.yml`](https://docs.papermc.io/paper/reference/global-configuration)
and [`config/paper-world-defaults.yml`](https://docs.papermc.io/paper/reference/world-configuration).

If you have any issues migrating from CraftBukkit or Spigot, do not hesitate to reach out for
support on [our Discord server](https://discord.gg/papermc) (`#paper-help` channel).

### From Vanilla

[Section titled “From Vanilla”](#from-vanilla)

When migrating to Paper from Vanilla, the way worlds are stored will automatically be changed.
Should you ever want to go back to Vanilla, follow the [Vanilla Migration Guide](#to-vanilla)
closely, as manual changes will be required.

1. Stop your Vanilla server if it is running, and create a full backup.
2. Download Paper from [our downloads page](https://papermc.io/downloads) and replace your Vanilla
   server JAR with your freshly downloaded Paper JAR.
3. Rename the downloaded file to match the name specified in the [start command](https://docs.papermc.io/paper/getting-started#running-the-server).
4. Start your new Paper server.

You have now successfully migrated to Paper. If you encounter any issues, do not hesitate to reach
out for support on [our Discord server](https://discord.gg/papermc) (`#paper-help` channel).

### From Fabric/Forge

[Section titled “From Fabric/Forge”](#from-fabricforge)

Because both Fabric and Forge use the Vanilla world directory structure, the same steps as the
[Vanilla Migration Guide](#from-vanilla) may be used, with one caveat. If your Fabric or Forge
server used mods that added new blocks, items, or other data to the game, Paper will be unable to
load these features.

Additionally, note that Paper does not support Fabric or Forge mods. You will need to find plugin
replacements. Any hybrids that attempt to support both mods and plugins are fundamentally flawed and
not recommended for use.

## Migrating from Paper

[Section titled “Migrating from Paper”](#migrating-from-paper)

### To Vanilla

[Section titled “To Vanilla”](#to-vanilla)

Because Paper stores worlds slightly differently than Vanilla, manual work is required to migrate.
If these steps are not taken, your nether and end will look like they have been reset. Don’t worry!
Even if this has happened, you haven’t lost any data. The Vanilla server just doesn’t know where to
find it.

Here is a chart to show the difference between how Vanilla and Paper store worlds.

| Server Software | Overworld | Nether | End |
| --- | --- | --- | --- |
| Vanilla | `/world` | `/world/DIM-1` | `/world/DIM1` |
| Paper | `/world` | `/world_nether/DIM-1` | `/world_the_end/DIM1` |

Follow these steps to migrate from Paper to Vanilla:

Note

These steps assume a `level-name` (as set in `server.properties`) of `world`. If this is not the
case for you, replace `world` with your `level-name` for all steps below.

1. Stop your Paper server, if it is running.
2. If you have already started your server with Vanilla, enter the `world` folder and delete both
   the `DIM-1` and `DIM1` folders. This step is only necessary should you have started your server
   with Vanilla.
3. Copy the `/world_nether/DIM-1` folder into the `/world` folder.
4. Copy the `/world_the_end/DIM1` folder into the `/world` folder.
5. Delete both the `/world_nether` and `/world_the_end` folders.
6. Replace your Paper JAR with a Vanilla server JAR.
7. Start your Vanilla server.

### To CraftBukkit or Spigot

[Section titled “To CraftBukkit or Spigot”](#to-craftbukkit-or-spigot)

Paper does **not** support migration to either CraftBukkit or Spigot! While you may find success
(both CraftBukkit and Spigot use the same directory structure as Paper), **do not** reach out for
support with issues you encounter and note that data loss is possible.

### To Fabric/Forge

[Section titled “To Fabric/Forge”](#to-fabricforge)

Because both Fabric and Forge use the same directory structure for world storage as Vanilla, follow
the [Vanilla Migration Guide](#to-vanilla) for this process. Note that neither Fabric nor Forge will
support Paper plugins! You will be required to find replacement mods.


================================================================================
Chapter Title: Next steps
Original Link: https://docs.papermc.io/paper/next-steps/
================================================================================

Now that you have your server up and running, there are a few things you should do to ensure that your server is running smoothly.

## Configuration

[Section titled “Configuration”](#configuration)

One of the first things you should do is ensure your server is configured to your specifications.
Paper is highly configurable, and you can change many settings to suit your needs. We outline where
you can find these settings in the [Configuration](https://docs.papermc.io/paper/reference/configuration) guide.

## Plugins

[Section titled “Plugins”](#plugins)

One of the main reasons to use Paper is to take advantage of the many plugins which make use of our
expansive API. We have our own plugin repository, [Hangar](https://hangar.papermc.io/), where you can
find many plugins to use on your server. We also have a guide on how to install plugins
[here](https://docs.papermc.io/paper/adding-plugins).

![Hangar](https://docs.papermc.io/_astro/hangar.BPr-gS9I_2p36KA.webp)

## Security

[Section titled “Security”](#security)

### Whitelisting

[Section titled “Whitelisting”](#whitelisting)

If you want to restrict who can join your server, you can use the whitelist feature. This allows you to
specify who can join your server, and stops anyone else from joining. You can use the whitelist from
the server console, or by editing the `whitelist.json` file in your server directory.

### Permissions

[Section titled “Permissions”](#permissions)

Permissions are a way to control what players can and cannot do on your server. You can use permissions
to restrict who can use certain commands, or who can access certain areas of your server. It is
common for plugins to use permissions to control who can use their features. You can use permission
plugins such as [LuckPerms](https://luckperms.net/) to manage the permissions which players will be granted.

## Backups

[Section titled “Backups”](#backups)

It’s important to keep backups of your server. If something goes wrong, you can restore your server to a
previous state. We cover how to do this in the [Updating](https://docs.papermc.io/paper/updating) guide.

## Optimization

[Section titled “Optimization”](#optimization)

Out of the box, Paper is optimized for performance. However, there are many things you can do to further
optimize your server. One of the most common things to do is to make sure that you are running the
correct startup flags for your server. We have a tool that allows you to automatically generate a
startup script with the correct flags for your server. You can find this tool
[here](https://docs.papermc.io/misc/tools/start-script-gen). Beyond this, a guide such as [this one](https://paper-chan.moe/paper-optimization/)
will help you to further optimize your server.

## Making your server public

[Section titled “Making your server public”](#making-your-server-public)

If you want to make your server public, you will need to port forward your server. This allows people
from outside your network to connect to your server. There is a guide made by
[NordVPN](https://nordvpn.com/blog/open-ports-on-router/) which explains what port forwarding is and how
to do it for your Paper server.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

If you encounter any issues with your server, you can follow our [Troubleshooting](https://docs.papermc.io/paper/basic-troubleshooting)
guide to help you diagnose and fix the issue. If you are unable to fix the issue, you can come and
ask for help in our [Discord](https://discord.gg/papermc) server!


================================================================================
Chapter Title: Aikar's flags
Original Link: https://docs.papermc.io/paper/aikars-flags/
================================================================================

## Recommended JVM startup flags

[Section titled “Recommended JVM startup flags”](#recommended-jvm-startup-flags)

Script Generator

**This page only serves as an explanation page.** If you want to generate a start script, please visit
our **[Script Generator](https://docs.papermc.io/misc/tools/start-script-gen)**.

Terminal window

```java
java -Xms10G -Xmx10G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar paper.jar --nogui
```

Do not allocate all of your available memory on a shared host!

When setting the `Xms` and `Xmx` values, if your host says you have 8GB of memory, **do not use 8GB**!

Minecraft (and Java) needs additional memory on top of that `Xmx` parameter. It is recommended to
**reduce your `Xmx` and `Xms` by about 1000-1500MB** to avoid running out of memory or `OOMKiller` killing
your server. This also leaves room for the operating system to use memory too.

Do you have 8GB of memory? Use 6500MB for safety.
*But you may also ask your host if they will cover this overhead for you and
give you 9500M instead. Some hosts will! Just ask.*

## Recommended memory

[Section titled “Recommended memory”](#recommended-memory)

**We recommend using at least 6-10GB**, no matter how few players! If you can’t afford 10GB of
memory, give as much as you can, but ensure you leave the operating system some memory too. G1GC
operates better with more memory.

However, more memory does not mean better performance above a certain point. Eventually you will hit
a point of diminishing returns. Going out and getting 32GB of RAM for a server will only waste your
money with minimal returns.

## Java GC logging

[Section titled “Java GC logging”](#java-gc-logging)

Are you having old gen issues with these flags? Add the following flags based on your Java version
to enable GC logging:

**Java 8-10**

Terminal window

```java
-Xloggc:gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps

-XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSize=1M
```

**Java 11+**

Terminal window

```java
-Xlog:gc*:logs/gc.log:time,uptime:filecount=5,filesize=1M
```

GC logging does not hurt your performance and can be left on at all times. The files will not take
up much space (5MB)

## Technical explanation of the flags

[Section titled “Technical explanation of the flags”](#technical-explanation-of-the-flags)

1. **-Xms matching -Xmx - why:** You should never run your server with the case that `Xmx` can run
   the system completely out of memory. Your server should always be expected to use the entire
   `Xmx`! You should then ensure the OS has extra memory on top of that `Xmx` for non-Minecraft/OS level
   things. Therefore, you should never run Minecraft with `Xmx` settings you can’t support if Java uses it
   all. Now, that means **if `Xms` is lower than `Xmx` you have unused memory**! Unused memory is
   wasted memory. G1 operates better with the more memory it’s given. G1 adaptively chooses how
   much memory to give to each region to optimize pause time. If you have more memory than it needs
   to reach an optimal pause time, G1 will simply push that extra into the old generation, and it
   will not hurt you. The fundamental idea of improving GC behavior is to ensure short-lived objects
   die young and never get promoted. With the more memory G1 has, the better assurance you will get
   that objects are not getting prematurely promoted to the old generation. G1 operates differently
   than previous collectors and is able to handle larger heaps more efficiently.

   If it does not need the memory given to it, it will not use it. The entire engine operates
   differently and does not suffer from too large of heaps, and this is industry-wide accepted
   information that under G1 to keep Xms and Xmx the same!
2. **UnlockExperimentalVMOptions:** needed for some the below options
3. **G1NewSizePercent:** These are the important ones. You now can specify percentages of an
   overall desired range for the new generation. With these settings, we tell G1 to not use its
   default 5% for new gen, and instead give it 40%! **Minecraft has an extremely high memory
   allocation rate**, ranging to at least 800MB/second on a 30 player server! And this is
   mostly short-lived objects (Block Position).

   Now, this means Minecraft **really** needs more focus on new gen to be able to even support this
   allocation rate. If your new gen is too small, you will be running new gen collections 1-2+
   times per second, which is awful. You will have so many pauses that TPS has risk of suffering,
   and the server will not be able to keep up with the cost of GCs. Then combine the fact that
   objects will now promote faster, resulting in your old gen growing faster. Given more new gen,
   we are able to slow down the intervals of young gen collections, resulting in more time for
   short-lived objects to die young and overall more efficient GC behavior.
4. **G1MixedGCLiveThresholdPercent:** Controls when to include regions in mixed GCs in the young
   GC collection, keeping old gen tidy without doing a normal old gen GC collection. When your
   memory is less than this percent, old gen won’t even be included in ‘mixed’ collections. Mixed
   are not as heavy as a full old collection, so having small incremental cleanups of old keeps
   memory usage light.

   Default is 65 to 85 depending on the Java version, we are setting that to 90 to ensure we reclaim garbage
   in old gen as fast as possible to retain as much free regions as we can.
5. **G1ReservePercent=20:** Minecraft memory allocation rate in up-to-date versions is really insane. We
   run the risk of a dreaded “to-space exhaustion” not having enough memory free to move data
   around. This ensures more memory is waiting to be used for this operation. Default is 10, so we
   are giving another 10 to it.
6. **MaxTenuringThreshold=1:** Minecraft has a really high allocation rate of memory. Of that
   memory, most is reclaimed in the eden generation. However, transient data will overflow into
   survivor. Initially played with completely removing survivor and had decent results, but does
   result in transient data making its way to old which is not good. Max Tenuring 1 ensures that we
   do not promote transient data to old generation, but anything that survives 2 passes of GC is
   just going to be assumed as longer-lived.

   Doing this greatly reduces pause times in young collections as copying data up to 15 times in
   survivor space for a tenured object really takes a lot of time for actually old memory. Ideally
   the GC engine would track average age for objects instead and tenure out data faster, but that
   is not how it works.

   Considering average GC rate is 10s to the upwards of minutes per young collection, this does not
   result in any ‘garbage’ being promoted, and just delays longer lived memory to be collected in
   mixed GCs.
7. **SurvivorRatio=32:** Because we drastically reduced MaxTenuringThreshold, we will be reducing
   use of survivor space drastically. This frees up more regions to be used by eden instead.
8. **AlwaysPreTouch:** AlwaysPreTouch gets the memory setup and reserved at process start ensuring
   it is contiguous, improving the efficiency of it more. This improves the operating systems
   memory access speed. Mandatory to use Transparent Huge Pages
9. **+DisableExplicitGC:** Many plugins think they know how to control memory, and try to invoke
   garbage collection. Plugins that do this trigger a full garbage collection, triggering a massive
   lag spike. This flag disables plugins from trying to do this, protecting you from their bad
   code.
10. **MaxGCPauseMillis=200:** This setting controls how much memory is used in between the minimum
    and maximum ranges specified for your new generation. This is a “goal” for how long you want
    your server to pause for collections. 200 is aiming for at most loss of 4 ticks. This will
    result in a short TPS drop, however the server can make up for this drop instantly, meaning it
    will have no meaningful impact on your TPS. 200ms is lower than players can recognize. In
    testing, having this value constrained to an even lower number results in G1 not recollecting
    memory fast enough and potentially running out of old gen triggering a full collection. Just
    because this number is 200 does not mean every collection will be 200. It means it can use up to
    200 if it really needs it, and we need to let it do its job when there is memory to collect.
11. **+ParallelRefProcEnabled:** Optimizes the GC process to use multiple threads for weak reference
    checking. Not sure why this isn’t default…
12. **G1RSetUpdatingPauseTimePercent=5:** Default is 10% of time spent during pause updating RSets,
    reduce this to 5% to make more of it concurrent to reduce pause durations.
13. **G1MixedGCCountTarget=4:** Default is 8. Because we are aiming to collect slower, with less old
    gen usage, try to reclaim old gen memory faster to avoid running out of old.
14. **G1HeapRegionSize=8M+:** Default is auto calculated. Super important for Minecraft, especially
    1.15, as with low memory situations, the default calculation will in most times be too low. Any
    memory allocation half of this size (4MB) will be treated as “Humongous” and promote straight to
    old generation and is harder to free. If you allow Java to use the default, you will be
    destroyed with a significant chunk of your memory getting treated as Humongous.
15. **+PerfDisableSharedMem:** Causes GC to write to file system which can cause major latency if
    disk IO is high - see <https://www.evanjones.ca/jvm-mmap-pause.html>

### Transparent huge pages

[Section titled “Transparent huge pages”](#transparent-huge-pages)

Controversial feature but may be usable if you can not configure your host for real HugeTLBFS. Try
adding `-XX:+UseTransparentHugePages` but it’s extremely important you also have `AlwaysPreTouch` set.
Otherwise, THP will likely hurt you. We have not measured how THP works for Minecraft or its impact with
`AlwaysPreTouch`, so this section is for the advanced users who want to experiment.


================================================================================
Chapter Title: Configuring Anti-Xray
Original Link: https://docs.papermc.io/paper/anti-xray/
================================================================================

> Originally written and maintained by [stonar96](https://github.com/stonar96).

Paper includes an obfuscation-based Anti-Xray with three modes, configurable on a per world basis.

Per World Configuration

If you aren’t already familiar with per world configuration, please take a moment to familiarize
yourself with the [Configuration Guide](https://docs.papermc.io/paper/reference/configuration).

This guide is a step-by-step walk-through for configuring Anti-Xray. For reference documentation,
refer to the Anti-Xray section of the
[Per-World Configuration Reference](https://docs.papermc.io/paper/reference/world-configuration#anticheat_anti_xray).

Anti-Xray has three different modes. `engine-mode: 1` replaces specified blocks (`hidden-blocks`) with
other “fake” blocks, `stone` (`deepslate` at y < 0), `netherrack`, or `end_stone` based on the
dimension. In contrast, `engine-mode: 2` will replace both `hidden-blocks` and `replacement-blocks`
with randomly generated `hidden-blocks`. `engine-mode: 3` works similarly to `engine-mode: 2`, but instead of
randomizing every block, it randomizes the block for each layer of a chunk.

The following images[1](#user-content-fn-1) show how each mode will look for a player using Xray with the recommended
configuration in both the overworld and nether.

![Overworld Anti-Xray Comparison](https://docs.papermc.io/_astro/anti-xray-overworld.CWzmAZnN_ZH414S.webp)
![Nether Anti-Xray Comparison](https://docs.papermc.io/_astro/anti-xray-nether.CUJUpqac_ZbC0JA.webp)

Especially on the client side, `engine-mode: 1` is much less computationally intensive, while
`engine-mode: 2` may better prevent Xray. With `engine-mode: 1`, only ores that are entirely covered
by solid blocks will be hidden. Ores exposed to air in caves or water from a lake will not be
hidden. With `engine-mode: 2`, fake ores obstruct the view of real blocks. If `air` is added to
`hidden-blocks`, `engine-mode: 2` will effectively hide all ores, even those exposed to air. `engine-mode: 3` can reduce network load when joining by a factor of ~2 and helps with chunk packet compression.

Anti-Xray Bypasses

**Range Extension**: While Anti-Xray alone will prevent the majority of users from Xraying on your
server, it is not by any means infallible. Because of how Anti-Xray is (and has to be) implemented,
it is possible to, on a default server, extend the range of real ores you can see by a not
insignificant amount. This can be mitigated by any competent anti-cheat plugin; however, this is not
included out of the box.

**Seed Reversing**: Another attack vector is the deterministic nature of Minecraft’s world
generation. If the client is able to obtain the world seed, it is able to know the real location of
every generated ore, completely bypassing Anti-Xray. This can be partially worked around by making
it harder for the client to reverse the world seed with the
[`feature-seeds` configuration](https://docs.papermc.io/paper/reference/world-configuration#feature_seeds), in conjunction
with the structure seed options in `spigot.yml`. Note that this is not a complete solution, and it
may still be possible for a client to obtain the server’s world seed. Using a different seed for
each world may also be beneficial.

**Ores Exposed to Air**: In `engine-mode: 1`, `engine-mode: 2` and `engine-mode: 3`, it is possible for a client
to view ores that are exposed to air. This can be mitigated in `engine-mode: 2` and `engine-mode: 3` by adding `air` to
the `hidden-blocks` list. However, doing this may cause client performance issues (FPS drops) for
some players.

## Recommended configuration

[Section titled “Recommended configuration”](#recommended-configuration)

The recommended configuration for `engine-mode: 1`, `engine-mode: 2` and `engine-mode: 3` is as follows:

Spacing

YAML cares about whitespace! The example configuration below is already formatted correctly. Ensure
formatting and indentation remains unchanged by using the “copy” button in the top right of each
example. Especially ensure that no tabulators are accidentally inserted. Check your editor’s options
for using spaces instead of tabulators for indentation. If your configuration file already contains
other important changes, it is recommended to make a backup before editing it.

### `engine-mode: 1`

[Section titled “engine-mode: 1”](#engine-mode-1)

Default World Configuration

Replace the existing `anticheat.anti-xray` block in `paper-world-defaults.yml` with the following:

paper-world-defaults.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 1

hidden-blocks:

# There's no chance to hide dungeon chests as they are entirely surrounded by air, but buried treasures will be hidden.

- chest

- coal_ore

- deepslate_coal_ore

- copper_ore

- deepslate_copper_ore

- raw_copper_block

- diamond_ore

- deepslate_diamond_ore

- emerald_ore

- deepslate_emerald_ore

- gold_ore

- deepslate_gold_ore

- iron_ore

- deepslate_iron_ore

- raw_iron_block

- lapis_ore

- deepslate_lapis_ore

- redstone_ore

- deepslate_redstone_ore

lava-obscures: false

# As of 1.18 some ores are generated much higher.

# Please adjust the max-block-height setting at your own discretion.

# https://minecraft.wiki/w/Ore might be helpful.

max-block-height: 64

# The replacement-blocks list is not used in engine-mode: 1. Changing this will have no effect.

replacement-blocks: []

update-radius: 2

use-permission: false
```

Nether Configuration

Copy and paste into your `paper-world.yml` within your nether world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_nether/paper-world.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 1

hidden-blocks:

- ancient_debris

- nether_gold_ore

- nether_quartz_ore

lava-obscures: false

max-block-height: 128

# The replacement-blocks list is not used in engine-mode: 1. Changing this will have no effect.

replacement-blocks: []

update-radius: 2

use-permission: false
```

End Configuration

Copy and paste into your `paper-world.yml` within your end world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_the\_end/paper-world.yml

```java
anticheat:

anti-xray:

enabled: false
```

### `engine-mode: 2`

[Section titled “engine-mode: 2”](#engine-mode-2)

Default World Configuration

Replace the existing `anticheat.anti-xray` block in `paper-world-defaults.yml` with the following:

paper-world-defaults.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 2

hidden-blocks:

# You can add air here such that many holes are generated.

# This works well against cave finders but may cause client FPS drops for all players.

- air

- copper_ore

- deepslate_copper_ore

- raw_copper_block

- diamond_ore

- deepslate_diamond_ore

- gold_ore

- deepslate_gold_ore

- iron_ore

- deepslate_iron_ore

- raw_iron_block

- lapis_ore

- deepslate_lapis_ore

- redstone_ore

- deepslate_redstone_ore

lava-obscures: false

# As of 1.18 some ores are generated much higher.

# Please adjust the max-block-height setting at your own discretion.

# https://minecraft.wiki/w/Ore might be helpful.

max-block-height: 64

replacement-blocks:

# Chest is a tile entity and can't be added to hidden-blocks in engine-mode: 2.

# But adding chest here will hide buried treasures, if max-block-height is increased.

- chest

- amethyst_block

- andesite

- budding_amethyst

- calcite

- coal_ore

- deepslate_coal_ore

- deepslate

- diorite

- dirt

- emerald_ore

- deepslate_emerald_ore

- granite

- gravel

- oak_planks

- smooth_basalt

- stone

- tuff

update-radius: 2

use-permission: false
```

Nether Configuration

Copy and paste into your `paper-world.yml` within your nether world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_nether/paper-world.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 2

hidden-blocks:

# See note about air and possible client performance issues above.

- air

- ancient_debris

- bone_block

- glowstone

- magma_block

- nether_bricks

- nether_gold_ore

- nether_quartz_ore

- polished_blackstone_bricks

lava-obscures: false

max-block-height: 128

replacement-blocks:

- basalt

- blackstone

- gravel

- netherrack

- soul_sand

- soul_soil

update-radius: 2

use-permission: false
```

End Configuration

Copy and paste into your `paper-world.yml` within your end world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_the\_end/paper-world.yml

```java
anticheat:

anti-xray:

enabled: false
```

### `engine-mode: 3`

[Section titled “engine-mode: 3”](#engine-mode-3)

Default World Configuration

Replace the existing `anticheat.anti-xray` block in `paper-world-defaults.yml` with the following:

paper-world-defaults.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 3

hidden-blocks:

# You can add air here such that many holes are generated.

# This works well against cave finders but may cause client FPS drops for all players.

- air

- copper_ore

- deepslate_copper_ore

- raw_copper_block

- diamond_ore

- deepslate_diamond_ore

- gold_ore

- deepslate_gold_ore

- iron_ore

- deepslate_iron_ore

- raw_iron_block

- lapis_ore

- deepslate_lapis_ore

- redstone_ore

- deepslate_redstone_ore

lava-obscures: false

# As of 1.18 some ores are generated much higher.

# Please adjust the max-block-height setting at your own discretion.

# https://minecraft.wiki/w/Ore might be helpful.

max-block-height: 64

replacement-blocks:

# Chest is a tile entity and can't be added to hidden-blocks in engine-mode: 2.

# But adding chest here will hide buried treasures, if max-block-height is increased.

- chest

- amethyst_block

- andesite

- budding_amethyst

- calcite

- coal_ore

- deepslate_coal_ore

- deepslate

- diorite

- dirt

- emerald_ore

- deepslate_emerald_ore

- granite

- gravel

- oak_planks

- smooth_basalt

- stone

- tuff

update-radius: 2

use-permission: false
```

Nether Configuration

Copy and paste into your `paper-world.yml` within your nether world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_nether/paper-world.yml

```java
anticheat:

anti-xray:

enabled: true

engine-mode: 3

hidden-blocks:

# See note about air and possible client performance issues above.

- air

- ancient_debris

- bone_block

- glowstone

- magma_block

- nether_bricks

- nether_gold_ore

- nether_quartz_ore

- polished_blackstone_bricks

lava-obscures: false

max-block-height: 128

replacement-blocks:

- basalt

- blackstone

- gravel

- netherrack

- soul_sand

- soul_soil

update-radius: 2

use-permission: false
```

End Configuration

Copy and paste into your `paper-world.yml` within your end world folder. See the
[Configuration Guide](https://docs.papermc.io/paper/reference/configuration) for more information.

world\_the\_end/paper-world.yml

```java
anticheat:

anti-xray:

enabled: false
```

## FAQ, common pitfalls and support

[Section titled “FAQ, common pitfalls and support”](#faq-common-pitfalls-and-support)

I can still see (some) ores / use X-ray

As described above, there are several reasons why you might still see (some) ores even though you
have enabled Anti-Xray:

* The ores are above the configured `max-block-height` value.
* Anti-Xray cannot hide ores exposed to air or other transparent blocks (in caves for example). In
  principle this is also the case for `engine-mode: 2` and `engine-mode: 3`, however, usually the fake ores obstruct the
  view of real blocks. Hiding those exposed ores too requires additional plugins.
* The `use-permission` option is enabled and you have the Anti-Xray bypass permission (`paper.antixray.bypass`) or you have
  operator status.
* The block type is missing in the configured block lists. This can be the result of using an
  outdated configuration file.
I have added fake blocks but X-ray doesn’t show them

If you use `engine-mode: 2` or `engine-mode: 3` and you have added fake blocks to the `hidden-blocks` list but you can’t
see them in-game using X-ray, this can have the following reasons:

* The added block types are tile entities. Anti-Xray can hide (replace) tile entities (such as
  chests), provided that they are not exposed to air or other transparent blocks. However, Anti-Xray
  can’t place tile entities as fake blocks into the chunk.
* The block is disabled in your client’s X-ray mod or not shown by your X-ray resource pack.
It doesn’t work below y = 0 or in certain other places.

* Your configuration file is probably outdated and missing important blocks in the
  `replacement-blocks` list, such as `deepslate` or biome-specific blocks, such as `basalt`. You
  might also want to check if the `hidden-blocks` list includes all important ores and their
  `deepslate` variants.
* If it doesn’t work above a certain y-level, check your `max-block-height` setting.
It still doesn’t work, further troubleshooting

* Make sure to always restart your server after making changes to the Anti-Xray configuration.
  Changes won’t be applied automatically.
* Do not use the `/reload` command. To apply Anti-Xray configuration changes a restart is required.
* After restarting the server, verify that the configuration is applied correctly by inspecting the
  config sections with timings or spark.
How and where do I ask for support if it still doesn’t work?

If the above bullet points don’t solve your problem or if you have further questions about
Anti-Xray, please don’t hesitate to ask us on the [PaperMC Discord](https://discord.gg/papermc)
using the #paper-help channel. Please try to provide as much detail as possible about your problem.
“It doesn’t work” isn’t very helpful when asking for support. Describe what you want to achieve,
what you have tried, what you expect and what you observe. Ideally include a timings or spark link
and a picture what you observe in-game.

## Footnotes

[Section titled “Footnotes”](#footnote-label)

1. Image design by `Oberfail`, initially posted in the
   [PaperMC Discord](https://discord.gg/papermc). [↩](#user-content-fnref-1)


================================================================================
Chapter Title: Basic troubleshooting
Original Link: https://docs.papermc.io/paper/basic-troubleshooting/
================================================================================

This guide will help you diagnose your server’s problem before reporting it to PaperMC or the plugin’s author.

Stop Your Server And Take A Backup

Before following this guide, stop your server first. Modifying server files while it is still running will corrupt them. Only a full server shutdown can prevent this.

Also, if you don’t follow this guide carefully or make a mistake while following it, you might corrupt your server. It is highly advised to back up your server before following this guide. Archiving your server folder as a .zip is good enough, or if you prefer, use backup software such as [borg](https://www.borgbackup.org/) or [kopia](https://kopia.io/). It would be ideal to create a test server by copying your production server’s file, but that’s not always possible.

If your server encounters a problem, it will either print an error message on the server console, create a crash report and close itself, or do both.
If your server crashes, the crash report will be saved in the crash-report directory. If your server didn’t crash, those error messages will be stored in the log directory along with other messages.

Note that the logs older than the latest will be compressed and not stored as plain text files.

The first thing you have to do is diagnose those messages.

Almost every problem you encounter will print error message lines, which are called a “stack trace”, on the server console. Examining the stack trace will help you find out what is causing problems on your server.

The stack trace starts with the error message, exception type, and exception message.

Both error messages and exception messages were put there by the developer of either your plugin or Paper. These messages tell you what problem your server experienced. An exception type like `java.lang.RuntimeException` tells you the type of the exception. This will help the developer (and you) understand the type of problem. A good starting point is to search the exception type and message in the [Paper Discord](https://discord.gg/papermc).

Many lines beginning with `at` may appear beneath the exception message. These are the body of the stack trace. These lines tell you where the problem starts. The top line of the body of the stack trace will tell you exactly where the problem occurred and, if possible, display where it came from.

Issues are often plugin-induced, and are the first possible thing you should check.

# Common issues

[Section titled “Common issues”](#common-issues)

## Plugin-induced issues

[Section titled “Plugin-induced issues”](#plugin-induced-issues)

If you find any plugin’s name in a stack trace in your logs, head to [Check Plugin Updates](#check-plugin-updates) and read from there. In most cases, the plugin, whose name is found on the stack trace, is causing the problem.

You can disable all of your plugins by renaming the plugins directory to something else, such as plugins-disabled, or by archiving the plugins directory and deleting it.

After that, try to run your server.

If the problem is resolved after removing the plugins, you know that it was a plugin that caused the issue.

### Binary search

[Section titled “Binary search”](#binary-search)

In case you’ve determined a plugin is causing issues but cannot narrow it down, try a binary search.

1. Split your plugins into two groups. The size of the two groups can be different, but it is ideal if the difference is minimal. Make sure that plugins that depend on each other are grouped together.
2. Disable one of the two groups of plugins. You can disable them by changing their extension from .jar to something else, such as .jar-disabled, or move them outside the plugins directory and into a temporary directory.
3. Run your server and check if the problem still exists. If the problem is resolved, the plugin that caused the issue is one of the disabled plugins. If the problem is not resolved, the plugin that is causing the issue is one of the active plugins.
4. Repeat from the start with the suspect plugin group.
   Repeat the steps above with groups that have the plugin that is causing the issue.

Library Plugin Dependencies

Some plugins that you install are not a typical plugin, but a library. These are installed like plugins, however tend to offer few user-facing features and are relied upon by other plugins for their functionality. If you disable a library, plugins that depend on it will not work properly. Common examples of these libraries are ProtocolLib, Vault providers, permission plugins, etc.

### Check plugin updates

[Section titled “Check plugin updates”](#check-plugin-updates)

There is a chance that your problem is already fixed in the latest release or latest build of the plugin.

Head to your plugin’s official download page and check if you are using the latest build or the latest release of the plugin. If not, update it to the latest version and try to run your server again to see if the problem is resolved.

### Update library plugins

[Section titled “Update library plugins”](#update-library-plugins)

Many plugins use library plugins like ProtocolLib, and you have to download them and put them in the plugins directory.

If you don’t update them to the latest version or latest build, you might experience problems related to plugins that use the library plugin.

Some library plugins tell their users to use their latest development build for support of the latest Minecraft version. You should look carefully at the requirements of your plugin.

### Check documentation

[Section titled “Check documentation”](#check-documentation)

If you misconfigured your plugin or your server, it can also cause problems on your server. Many plugins provide their own documentation about how to set them up properly. Read those documents carefully and check if there is something wrong with the plugin’s configuration.

If your problem is related to a plugin you use, and you still don’t know how to solve it, you can try to reach out to the plugin’s author. Many plugins have a way to contact their author, like a GitHub issue tracker, Discord support guild, Gitter, IRC, etc.

Below, we list other issues that may happen when running a server.

## Server does not start

[Section titled “Server does not start”](#server-does-not-start)

When this happens, always check your `latest.log` file in your `logs` folder, you may find your issue listed here. If logs are not generating, check your startup script, as described below:

### Checking your startup script

[Section titled “Checking your startup script”](#checking-your-startup-script)

The recommended way to start a server is via a startup script, that you can generate [here](https://docs.papermc.io/misc/tools/start-script-gen). Don’t double click the .jar!
If you’re on Windows and your terminal disappears quickly after you run, make sure there’s a line at the end of the file containing just `pause`.
In case you get an error similar to `Error: Unable to access jarfile server.jar`, make sure that the .jar name in your startup script is the same as the file you downloaded. Note that Windows, by default, hides extensions, so you may need re-enable that in the Folder and Search Options in the file explorer to see the correct name of the file, extension included.

### Failed to bind to port

[Section titled “Failed to bind to port”](#failed-to-bind-to-port)

This may happen in two cases:

1. A server is already running, check your task manager app for Java processes.
2. `server-ip`, in `server.properties`, is configured incorrectly. Note that this option is not a placeholder for your external IP, it controls which network interfaces your server will bind to. Most of the time, it should be left empty.

### Attempted to load chunk saved with newer version

[Section titled “Attempted to load chunk saved with newer version”](#attempted-to-load-chunk-saved-with-newer-version)

```java
java.lang.RuntimeException: Server attempted to load chunk saved with newer version of minecraft! 3955 > 3465

[18:23:38 WARN]:        at net.minecraft.world.level.chunk.storage.ChunkRegionLoader.loadChunk(ChunkRegionLoader.java:149)

[18:23:38 WARN]:        at io.papermc.paper.chunk.system.scheduling.ChunkLoadTask$ChunkDataLoadTask.runOffMain(ChunkLoadTask.java:338)

[18:23:38 WARN]:        at io.papermc.paper.chunk.system.scheduling.GenericDataLoadTask$ProcessOffMainTask.run(GenericDataLoadTask.java:307)

[18:23:38 WARN]:        at ca.spottedleaf.concurrentutil.executor.standard.PrioritisedThreadedTaskQueue$PrioritisedTask.executeInternal(PrioritisedThreadedTaskQueue.java:351)

[18:23:38 WARN]:        at ca.spottedleaf.concurrentutil.executor.standard.PrioritisedThreadedTaskQueue.executeTask(PrioritisedThreadedTaskQueue.java:118)

[18:23:38 WARN]:        at ca.spottedleaf.concurrentutil.executor.standard.PrioritisedThreadPool$PrioritisedThread.pollTasks(PrioritisedThreadPool.java:274)

[18:23:38 WARN]:        at ca.spottedleaf.concurrentutil.executor.standard.PrioritisedQueueExecutorThread.run(PrioritisedQueueExecutorThread.java:50)
```

That error means that your world was created or opened in a server version that’s newer than one you’re currently running. Downgrading your world is not supported, so make sure to use the latest supported version of Paper. Even if you haven’t joined the server, by loading your world in a newer version, it is upgraded automatically.

Forcing the server to try to load a newer world

The server will start if you use the `-DPaper.ignoreWorldDataVersion=true` flag. However, this is **highly not recommended, completely unsupported and may permanently corrupt your world**. If you’re going to attempt this, take a backup.

### Circular plugin loading

[Section titled “Circular plugin loading”](#circular-plugin-loading)

```java
[15:01:04] [Server thread/ERROR]: [SimpleProviderStorage] Circular plugin loading detected!

[15:01:04] [Server thread/ERROR]: [SimpleProviderStorage] Circular load order:

[15:01:04] [Server thread/ERROR]: [SimpleProviderStorage]   Plugin1 -> Plugin2 -> Plugin3 -> Plugin4 -> Plugin1

[15:01:04] [Server thread/ERROR]: [SimpleProviderStorage] Please report this to the plugin authors of the first plugin of each loop or join the PaperMC Discord server for further help.

[15:01:04] [Server thread/ERROR]: [SimpleProviderStorage] If you would like to still load these plugins, acknowledging that there may be unexpected plugin loading issues, run the server with -Dpaper.useLegacyPluginLoading=true
```

That means your plugins are configured in a way such that they want to start before (or after) each other, which is impossible — one has to go first. Plugins usually have reasons to want to start before each other, so when such a conflict happens, rather than picking randomly and risking issues, the server warns you about the issue and shuts down.
There’s often a problematic plugin involved, and to solve this, it’s preferable that you report the issue to its authors. Removing it should also fix the issue. As a last resort, you can use the `-Dpaper.useLegacyPluginLoading=true` startup flag, but it may cause hard to debug issues.

### Outdated version of Java

[Section titled “Outdated version of Java”](#outdated-version-of-java)

```java
Exception in thread "ServerMain" java.lang.UnsupportedClassVersionError: org/bukkit/craftbukkit/Main has been compiled by a more recent version of the Java Runtime (class file version 65.0), this version of the Java Runtime only recognizes class file versions up to 61.0

at java.base/java.lang.ClassLoader.defineClass1(Native Method)

at java.base/java.lang.ClassLoader.defineClass(ClassLoader.java:1017)

at java.base/java.security.SecureClassLoader.defineClass(SecureClassLoader.java:150)

at java.base/java.net.URLClassLoader.defineClass(URLClassLoader.java:524)

at java.base/java.net.URLClassLoader$1.run(URLClassLoader.java:427)

at java.base/java.net.URLClassLoader$1.run(URLClassLoader.java:421)

at java.base/java.security.AccessController.doPrivileged(AccessController.java:712)

at java.base/java.net.URLClassLoader.findClass(URLClassLoader.java:420)

at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:592)

at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:525)

at java.base/java.lang.Class.forName0(Native Method)

at java.base/java.lang.Class.forName(Class.java:467)

at io.papermc.paperclip.Paperclip.lambda$main$0(Paperclip.java:38)

at java.base/java.lang.Thread.run(Thread.java:842)
```

Your version of Java is outdated, check [our guide on updating it](https://docs.papermc.io/misc/java-install). To avoid possibly having to do more tweaks, uninstall your current version of Java, if any.
If you do have the correct version installed, your operating system may be not picking it up. Make sure you’ve closed and opened your terminal after installing it, and that Java is present in your `PATH` environment variable.

## Server crashes or exits unexpectedly

[Section titled “Server crashes or exits unexpectedly”](#server-crashes-or-exits-unexpectedly)

Update!

Always keep your server up to date (and take a backup before updating). Older versions are known to have on-demand crashes that can be triggered by players at any time.

### Unexpected graceful shutdown

[Section titled “Unexpected graceful shutdown”](#unexpected-graceful-shutdown)

If your server shuts down normally as if you typed `/stop` or pressed a stop button in your panel, enable `debug` in `server.properties`. The next time the server shuts down, you will get a stack trace that will help you debug.

### Watchdog dump (“DO NOT REPORT THIS TO PAPER”)

[Section titled “Watchdog dump (“DO NOT REPORT THIS TO PAPER”)”](#watchdog-dump-do-not-report-this-to-paper)

```java
[02:04:00] [Paper Watchdog Thread/ERROR]: --- DO NOT REPORT THIS TO PAPER - THIS IS NOT A BUG OR A CRASH  - 1.21.3-66-afb5b13 (MC: 1.21.3) ---

[02:04:00] [Paper Watchdog Thread/ERROR]: The server has not responded for 10 seconds! Creating thread dump

[02:04:00] [Paper Watchdog Thread/ERROR]: ------------------------------

[02:04:00] [Paper Watchdog Thread/ERROR]: Server thread dump (Look for plugins here before reporting to Paper!):

[02:04:00] [Paper Watchdog Thread/ERROR]: ------------------------------

[02:04:00] [Paper Watchdog Thread/ERROR]: Current Thread: Server thread

[02:04:00] [Paper Watchdog Thread/ERROR]: PID: 129 | Suspended: false | Native: true | State: RUNNABLE

[02:04:00] [Paper Watchdog Thread/ERROR]: Stack:

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.UnixFileDispatcherImpl.write0(Native Method)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.UnixFileDispatcherImpl.write(UnixFileDispatcherImpl.java:65)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.IOUtil.writeFromNativeBuffer(IOUtil.java:137)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.IOUtil.write(IOUtil.java:102)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.IOUtil.write(IOUtil.java:72)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.FileChannelImpl.write(FileChannelImpl.java:300)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.ChannelOutputStream.writeFully(ChannelOutputStream.java:68)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/sun.nio.ch.ChannelOutputStream.write(ChannelOutputStream.java:105)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/java.io.BufferedOutputStream.flushBuffer(BufferedOutputStream.java:125)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/java.io.BufferedOutputStream.implFlush(BufferedOutputStream.java:252)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/java.io.BufferedOutputStream.flush(BufferedOutputStream.java:240)

[02:04:00] [Paper Watchdog Thread/ERROR]: [email protected]/java.io.FilterOutputStream.close(FilterOutputStream.java:184)
```

That message shows up when your server is taking very long (10+ seconds) to finish the current tick — it’s not a bug or crash, it’s simply warning you of severe lag, that can eventually lead to a crash.
A good rule of thumb is checking the first lines of the stack trace, as that shows where the main thread was stuck at the time it was printed. Many times, that points to the root cause of the issue.
However, sometimes the issue may not be obvious or appear in the stack trace. If possible, analyze a [spark report](#spark-report) for more details, and, if you’re in doubt about how to proceed, feel free to visit the [Paper Discord](https://discord.gg/papermc) for help.

### Crash without logs

[Section titled “Crash without logs”](#crash-without-logs)

If you have access to a Linux shell, run `dmesg -T | grep -i killed`. That should show how your server process was killed.
A common cause (but not the only one), if it was killed due to OOM, is that your server panel is configured with a memory limit that’s too close to your `-Xmx`. Either reduce `-Xmx` (by 1-2GB is a good initial rule of thumb) or increase/disable the memory limits in your panel.
If you’re using a hosting company that only provides you with a panel, you likely won’t have the tools to get to the bottom of the problem. You should make a ticket with your host in this case.

## Performance and gameplay issues

[Section titled “Performance and gameplay issues”](#performance-and-gameplay-issues)

Unfortunately, Paper can’t replicate Vanilla behavior 100%, but it is a goal (except when it comes to exploits). If you’re still experiencing a bug that cannot be reproduced in vanilla **multiplayer**, please apply a [Vanilla-like configuration](https://docs.papermc.io/paper/vanilla) and check if there’s already an open issue in our GitHub. If not, feel free to create one.

### Strange entity/farm/redstone/spawning behavior

[Section titled “Strange entity/farm/redstone/spawning behavior”](#strange-entityfarmredstonespawning-behavior)

If you copied values of a pre-made configuration or optimization guide, now is a good time to revert the changes. Keep a copy of your current configs if you prefer, and delete the originals so they can re-generate to default values.

In case you’re still experiencing such issues with default configurations, try our [Vanilla-like configurations](https://docs.papermc.io/paper/vanilla) but do note that this comes at a performance cost.

Also, keep in mind that singleplayer does not behave the same as multiplayer, both when it comes to spawning and certain entity behavior. For example, mobs despawn if they’re over 128 blocks away from a player, and this becomes more apparent in multiplayer, especially if you’re making farms where monsters go to another dimension via a nether portal. If there are players in the target dimension and they’re all very far from the portal, the mob will instantly despawn — this is intended Vanilla behavior.

### Dupes not working

[Section titled “Dupes not working”](#dupes-not-working)

Paper has some [unsupported settings](https://docs.papermc.io/paper/reference/global-configuration#unsupported_settings) that allow certain dupes. However, a few of them cannot be re-introduced because that would break other aspects of the server. Paper also will not re-add dupes that no longer exist in the game.

## Performance issues

[Section titled “Performance issues”](#performance-issues)

### Spark report

[Section titled “Spark report”](#spark-report)

Paper has the [spark](https://spark.lucko.me/) profiler built-in, in order to diagnose the root cause of performance issues.
For example, you can generate a report for 300 seconds by running `/spark profiler start --timeout 300`
If you want to diagnose lag spikes that last more than, for example, 100 ms, you can run `/spark profiler start --only-ticks-over 100 --timeout 300`

Look into the [spark docs](https://spark.lucko.me/docs) for a more in-depth guide on how to use it and read reports. If you’re still unsure about what’s the cause of your problem, you can send us the link via the [Paper Discord](https://discord.gg/papermc).

### High RAM usage

[Section titled “High RAM usage”](#high-ram-usage)

Unless you’re experiencing out of memory crashes or bad garbage collection (GC) times, high memory usage is expected.

Java programs store objects in memory, in an area where we call the heap. The heap grows over time, you can set its initial value with `-Xms` and the maximum value with `-Xmx`.

It’s normal that the Java process will use the RAM it’s given, sometimes using a little more than `-Xmx`. This number won’t go down over time, as the garbage collector (GC) rarely returns RAM to the operating system in servers. This is by itself not a problem, in fact it’s beneficial: by having more heap memory to work with, GC will have to worry less about disposing of garbage, as that takes valuable processing time. This is not a memory leak and will not cause out of memory crashes, which are commonly caused by not leaving enough RAM for your OS or improperly configured memory limits in a container.

There are several different memory metrics that can be measured. For example, imagine a server in a 16GB container, running with `-Xms1G -Xmx14G`. In this case:

* **Container memory limit:** 16GB
* **Maximum heap:** 14GB
* **Current heap size:** Starts at 1GB and expands quickly. Will be between 1-14GB at any given point
* **Current heap usage:** will be smaller than the number above, and will grow and shrink in a sawtooth pattern under normal conditions

Keep in mind that different tools choose different metrics out of these to display, so the usage meter in your panel, at a glance, might not look like what a plugin will display.

### Low CPU usage

[Section titled “Low CPU usage”](#low-cpu-usage)

Paper is able to make use of multiple cores, but this does not necessarily mean that you will have several cores at near 100% usage. A major source of load in the server comes from the tick loop, which uses a single thread. Thus, at a certain point, more cores will not give you a performance benefit, so it’s advisable to go for a CPU with high single-threaded performance and allocate a sufficient amount of threads to your server (at least 4). In servers with a high core count, this situation can translate to a low CPU usage relative to the total amount of cores.

However, if your server (especially if large) is really adamant on using only a single core, check your panel’s CPU allocation setting. In certain panels, a number like `4` doesn’t mean it’ll use 4 cores, but instead that it will use the one core with ID 4.


================================================================================
Chapter Title: Profiling
Original Link: https://docs.papermc.io/paper/profiling/
================================================================================

Profiling is a way to diagnose performance problems with your server.
A profiler measures certain characteristics of a running server, e.g. how often a method is called
and how much time it takes up in a single tick, how long and often the garbage collector runs and much more.

Caution

*For profiling to be effective, the issue you are diagnosing must be actively occurring.*

If you need help with analyzing a performance issue, please bring a spark report to the
[PaperMC Discord server](https://discord.gg/PaperMC) (#paper-help) for assistance.

## spark

[Section titled “spark”](#spark)

Starting with 1.21, Paper bundles the [spark](https://spark.lucko.me/) profiler, which is the preferred way
to profile Paper.

To start profiling your server, run this command:

```java
/spark profiler start --timeout 600
```

After 10 minutes, this will return a URL to a profiler report, which you can analyze yourself or provide
to a developer of a plugin or the Paper support chats.

This is only a fraction of what spark can do, so if you want to learn about the different features of spark
or learn to analyze reports yourself, check out spark’s documentation [here](https://spark.lucko.me/docs/).

Tip

If you want to use a version of spark newer than the bundled one, simply place a standalone spark plugin JAR
into the `plugins` directory and set the [`paper.preferSparkPlugin`](https://docs.papermc.io/paper/reference/system-properties#paperprefersparkplugin)
system property to `true`.

If you want to use PlaceholderAPI [placeholders](https://spark.lucko.me/docs/misc/Placeholders)
from the bundled spark version, you need to install the [spark expansion](https://api.extendedclip.com/expansions/spark/)
from PAPI’s eCloud (`/papi ecloud download spark` and `/papi reload`).

## Timings

[Section titled “Timings”](#timings)

Paper also bundles the [Timings v2](https://timings.aikar.co/) profiler, however Timings has been unmaintained
for multiple years and its reports are difficult to read for beginners. It has been deprecated in favor of
spark and turned off by default in 1.21, see [this discussion](https://github.com/PaperMC/Paper/discussions/10565)
for more information.


================================================================================
Chapter Title: Updating
Original Link: https://docs.papermc.io/paper/updating/
================================================================================

Updating Paper is an important part of running every server. With new features and fixes coming
every day, we recommend updating at least once per week to keep your server patched for the latest
bugs. Installing updates is very simple, but it’s important to know how to do it correctly.

Don’t replace any JAR in a running server

Unless you know exactly what and why you’re doing what you’re doing, it’s never a good idea to
replace any JAR in a running server, be that plugins, or Paper itself.

## Step 1. Backup

[Section titled “Step 1. Backup”](#step-1-backup)

Tip

If you are using a shared host, your host may provide a built-in way to back up. Consult their
documentation before continuing.

This is the most important step, and yet the most frequently skipped. While it is unlikely that
updating Paper itself will cause any issues requiring you to restore from a backup, plugin
malfunctions or other accidents might! Updating is a great time to work in a backup. Having
functioning backups is essential to every server, big or small. The main things to back up are:

* The world folders
* Server Configuration Files
* Plugin Configuration Files & Plugin JARs

You should aim to have backups from multiple times, and keep them in a safe place. A common approach
is to keep rolling backups, so you always have a certain number of backups from a set amount of time.

## Step 2. Update plugins

[Section titled “Step 2. Update plugins”](#step-2-update-plugins)

Just like it’s important to update Paper, it’s equally important to keep plugins up to date. You
never know what plugin authors may be working on, be it bugfixes or new features.

A little known feature of Paper servers is the `update` folder. Here’s how you use it.

1. Create a folder called `update` within the `plugins` folder.
2. One by one, download plugins you would like to update and put them in the `update` folder.
3. Restart your server, do not remove or modify any plugins outside the `update` folder.

By doing this, you are able to update all of your plugins at the same time without having the server
off, or replacing plugin JARs while the server is running. You do not need to restart your server
before updating Paper itself. This feature allows you to update both Paper and plugins all at the
same time, without needing any additional downtime.

## Step 3. Update Paper

[Section titled “Step 3. Update Paper”](#step-3-update-paper)

Tip

If you are using a shared host, your host may provide a built-in way to update! Consult their
documentation before continuing.

Updating Paper itself is very simple.

1. Download a new JAR from [our downloads page](https://papermc.io/downloads).
2. Stop your server. It is not recommended and may cause issues to replace your Paper JAR while the server is running.
3. Rename the downloaded file to match the name specified in the [start command](https://docs.papermc.io/paper/getting-started#running-the-server).
4. Replace your old Paper JAR file with the new renamed one.
5. Start your server. Watch the startup log to ensure everything goes to plan. If there are any
   plugin conflicts or issues, you will see them here.

To minimize downtime caused by updates, some server owners will, rather than replacing their server
JAR, upload a new one and set their start script to use the new one on the next restart. Both of
these are valid update strategies.

Automatic Updates

While it may be convenient to install updates automatically (and Paper’s [downloads service](https://docs.papermc.io/misc/downloads-service) allows you
to with ease), doing so is not recommended by Paper due to the possibility of plugin conflicts or
other issues that you may not know about. Always be present during updates, and keep a careful watch
on your server’s log after the fact.

If you do choose to automatically install updates, ensure you have a functioning backup strategy in
place!


================================================================================
Chapter Title: Vanilla-like experience
Original Link: https://docs.papermc.io/paper/vanilla/
================================================================================

Due to the way the Bukkit API is implemented in Paper, the gameplay experience between Vanilla and Paper can have inconsistencies.
This can be furthered by efforts to fix bugs present in Vanilla Minecraft.
Whilst many people may not notice the inconsistencies, there are situations where they become problematic.
One example is that technical players may struggle getting their machines to work like they should.
This page aims to provide a starting point for players who want to get as close to Vanilla as possible.

Note

This page is inspired by [Earthcomputer’s collection](https://gist.github.com/Earthcomputer/2296da33b8cc91dba81b48103c0e1fe3) of Vanilla breaking changes.

Caution

This guide will only help you to get as close to Vanilla as possible.
Unfortunately, it currently is not possible to get a 100% Vanilla experience in Paper.

## server.properties

[Section titled “server.properties”](#serverproperties)

pause-when-empty-seconds=60[#](#server_properties_pause_when_empty_seconds) 

How many seconds have to pass after no player has been online before the server is paused. This is disabled by default because it is incompatible with what plugins expect and might do with no players online.

## paper-world-defaults.yml

[Section titled “paper-world-defaults.yml”](#paper-world-defaultsyml)

chunks: 

delay-chunk-unloads-by: 0s[#](#paper_world_defaults_chunks_delay_chunk_unloads_by) 

Delays chunk unloads by the specified time. Formatted as a duration with a single unit e.g. 10h or 25m. Supports d, h, m, and s.

max-auto-save-chunks-per-tick: 200[#](#paper_world_defaults_chunks_max_auto_save_chunks_per_tick) 

The maximum number of chunks the auto-save system will save in a single tick

collisions: 

allow-player-cramming-damage: true[#](#paper_world_defaults_collisions_allow_player_cramming_damage) 

Allows players to take damage from cramming when colliding with more entities than set in the maxEntityCramming game rule

max-entity-collisions: 2147483647[#](#paper_world_defaults_collisions_max_entity_collisions) 

Instructs the server to stop processing collisions after this value is reached

entities: 

behavior: 

cooldown-failed-beehive-releases: false[#](#paper_world_defaults_entities_behavior_cooldown_failed_beehive_releases) 

Adds a cooldown to bees being released after a failed release, which can occur if the hive is blocked or it being night.

only-merge-items-horizontally: true[#](#paper_world_defaults_entities_behavior_only_merge_items_horizontally) 

Prevents merging items that are not on the same y level, preventing potential visual artifacts.

phantoms-do-not-spawn-on-creative-players: false[#](#paper_world_defaults_entities_behavior_phantoms_do_not_spawn_on_creative_players) 

Disables spawning of phantoms on players in creative mode

phantoms-only-attack-insomniacs: false[#](#paper_world_defaults_entities_behavior_phantoms_only_attack_insomniacs) 

Prevents phantoms from attacking players who have slept

stuck-entity-poi-retry-delay: disabled[#](#paper_world_defaults_entities_behavior_stuck_entity_poi_retry_delay) 

The delay before retrying POI acquisition when entity navigation is stuck. This will reduce pathfinding performance impact. Measured in ticks.

spawning: 

max-arrow-despawn-invulnerability: disabled[#](#paper_world_defaults_entities_spawning_max_arrow_despawn_invulnerability) 

Workaround for MC-125757, makes all arrows advance their despawn timer as if they were stuck in the ground, after a delay (in ticks).

count-all-mobs-for-spawning: true[#](#paper_world_defaults_entities_spawning_count_all_mobs_for_spawning) 

Determines whether spawner mobs and other misc mobs are counted towards the global mob limit

duplicate-uuid: 

mode: NOTHING[#](#paper_world_defaults_entities_spawning_duplicate_uuid_mode) 

Specifies the method the server uses to resolve entities with duplicate UUIDs. This can be one of the following values:

* **SAFE\_REGEN**: Regenerate a UUID for the entity, or delete it if they are close.
* **DELETE**: Delete the entity.
* **NOTHING**: Does nothing, not printing logs.
* **WARN**: Does nothing, printing logs

filter-bad-tile-entity-nbt-from-falling-blocks: false[#](#paper_world_defaults_entities_spawning_filter_bad_tile_entity_nbt_from_falling_blocks) 

Instructs the server to remove certain NBT data from falling blocks. **Note**: Some adventure maps may require this to be turned off to function correctly, but we do not recommend turning it off on a public server

filtered-entity-tag-nbt-paths: [][#](#paper_world_defaults_entities_spawning_filtered_entity_tag_nbt_paths) 

A list of NBT tags that will be removed from the “entity\_data” component on items which spawn entities. The format of these strings follows the same format used to select NBT tags in Vanilla commands. If the spawning was directly caused by a player and the player has the minecraft.nbt.place permission, the filter list will be ignored. The defaults are set to prevent entities from spawning or moving to a place other than the location they were placed. For example, if Pos wasn’t included, a spawn egg could place an entity at any location. **Note**: Some adventure maps may require this to be an empty list to function correctly, but we do not recommend turning it off on a public server

per-player-mob-spawns: false[#](#paper_world_defaults_entities_spawning_per_player_mob_spawns) 

Determines whether the mob limit (in bukkit.yml) is counted per player or for the entire server. Enabling this setting results in roughly the same number of mobs, but with a more even distribution that prevents one player from using the entire mob cap and provides a more single-player like experience

hopper: 

cooldown-when-full: false[#](#paper_world_defaults_hopper_cooldown_when_full) 

Instructs the server to apply a short cooldown when the hopper is full, instead of constantly trying to pull new items

maps: 

item-frame-cursor-limit: 2147483647[#](#paper_world_defaults_maps_item_frame_cursor_limit) 

The number of cursors (markers) allowed per map. A large number of cursors may be used to lag clients

misc: 

allow-remote-ender-dragon-respawning: true[#](#paper_world_defaults_misc_allow_remote_ender_dragon_respawning) 

Disables an optimization which verifies that end crystals placed in the end are placed on the portal frame before any attempt is made at respawning the ender dragon. Enabling this setting allows remote ender dragon respawning to work again.

scoreboards: 

use-vanilla-world-scoreboard-name-coloring: true[#](#paper_world_defaults_scoreboards_use_vanilla_world_scoreboard_name_coloring) 

Instructs the server to use the Vanilla scoreboard for player nickname coloring. Useful when playing on adventure maps made for the Vanilla server and client

unsupported-settings: 

**Unsupported settings**

The following settings are provided by Paper but are not officially supported. Use them at your own risk and they may be removed at any time.

disable-world-ticking-when-empty: true[#](#paper_world_defaults_unsupported_settings_disable_world_ticking_when_empty) 

Stops the ticking of the world when there are no players or force loaded chunks present in the world.

fix-invulnerable-end-crystal-exploit: false[#](#paper_world_defaults_unsupported_settings_fix_invulnerable_end_crystal_exploit) 

If set to false, the creation of invulnerable end crystals will be allowed. Fixes [MC-108513](https://bugs.mojang.com/browse/MC-108513)

## paper-global.yml

[Section titled “paper-global.yml”](#paper-globalyml)

commands: 

suggest-player-names-when-null-tab-completions: false[#](#paper_global_commands_suggest_player_names_when_null_tab_completions) 

Instructs the server to return a list of players when tab-completing when there are no other completions available

time-command-affects-all-worlds: true[#](#paper_global_commands_time_command_affects_all_worlds) 

Whether the /time command should act on all worlds or just the sender’s current world

item-validation: 

book: 

author: 2147483647[#](#paper_global_item_validation_book_author) 

The maximum length of a book’s author in characters

page: 2147483647[#](#paper_global_item_validation_book_page) 

The maximum length of a book’s page in characters

title: 2147483647[#](#paper_global_item_validation_book_title) 

The maximum length of a book’s title in characters

book-size: 

page-max: disabled[#](#paper_global_item_validation_book_size_page_max) 

The max number of bytes a single page in a book can contribute to the allowed byte total for a book, or “disabled” to disable non-vanilla restrictions on the book size.

display-name: 2147483647[#](#paper_global_item_validation_display_name) 

The maximum length of an item’s display name in characters

lore-line: 2147483647[#](#paper_global_item_validation_lore_line) 

The maximum length of a lore line in characters

resolve-selectors-in-books: true[#](#paper_global_item_validation_resolve_selectors_in_books) 

Whether to resolve selectors in books. With this enabled, players given creative mode will be able to crash the server in yet another way

misc: 

fix-far-end-terrain-generation: false[#](#paper_global_misc_fix_far_end_terrain_generation) 

Whether to fix MC-159283 which causes unusual ring-shaped terrain patterns in the outer End islands at extremely far distances.

max-joins-per-tick: 2147483647[#](#paper_global_misc_max_joins_per_tick) 

Sets the maximum amount of players that may join the server in a single tick. If more players join, they will be postponed until later ticks to join but not kicked. This is not related to connection throttling found in bukkit.yml

packet-limiter: 

all-packets: 

interval: -1[#](#paper_global_packet_limiter_all_packets_interval) 

The interval, in seconds, for which max-packet-rate should apply

overrides: 

Override the **action**, **interval**, and **max-packet-rate** configuration for any individual serverbound packet. You can find the identifiers for packets on the [wiki](https://minecraft.wiki/w/Java_Edition_protocol/Packets).

minecraft:place\_recipe: 

interval: -1[#](#paper_global_packet_limiter_overrides_minecraft:place_recipe_interval) 

The interval, in seconds, for which max-packet-rate should apply

spam-limiter: 

incoming-packet-threshold: disabled[#](#paper_global_spam_limiter_incoming_packet_threshold) 

Sets the threshold at which the server will consider incoming packets spam and ignore them

unsupported-settings: 

**Unsupported settings**

The following settings are provided by Paper but are not officially supported. Use them at your own risk and they may be removed at any time.

allow-headless-pistons: true[#](#paper_global_unsupported_settings_allow_headless_pistons) 

Whether the server should allow the creation of headless pistons. These are often used to break permanent blocks

allow-permanent-block-break-exploits: true[#](#paper_global_unsupported_settings_allow_permanent_block_break_exploits) 

Whether unbreakable blocks can be broken with Vanilla exploits. This includes bedrock, end portal frames, end portal blocks, and more

allow-piston-duplication: true[#](#paper_global_unsupported_settings_allow_piston_duplication) 

Whether to allow duplication of TNT, carpets, and rails. This does not control sand duplication

allow-unsafe-end-portal-teleportation: true[#](#paper_global_unsupported_settings_allow_unsafe_end_portal_teleportation) 

This setting allows for exploits related to end portal teleportation to be possible, for example sand duplication. This setting is not recommended to be enabled, but is provided for those who wish to use it.

oversized-item-component-sanitizer: 

dont-sanitize: [#](#paper_global_unsupported_settings_oversized_item_component_sanitizer_dont_sanitize)

- minecraft:container
- minecraft:charged\_projectiles
- minecraft:bundle\_contents

This setting defines which item data components shouldn’t be sanitized in oversized item obfuscation. Changing this re-enables exploits, but may be needed for certain resource packs. Possible values: `minecraft:container`, `minecraft:charged_projectiles`, `minecraft:bundle_contents`

perform-username-validation: false[#](#paper_global_unsupported_settings_perform_username_validation) 

Whether the server should validate usernames. While this may allow users with special characters in their name to join, it can also cause issues with commands and plugins

skip-tripwire-hook-placement-validation: true[#](#paper_global_unsupported_settings_skip_tripwire_hook_placement_validation) 

This setting allows for exploits related to tripwire hook duping to be enabled.

update-equipment-on-player-actions: false[#](#paper_global_unsupported_settings_update_equipment_on_player_actions) 

This setting controls if equipment should be updated when handling certain player actions. If set to false this will allow players to exploit attributes by e.g. switching equipment before using it.

## spigot.yml

[Section titled “spigot.yml”](#spigotyml)

world-settings: 

default: 

entity-activation-range: 

animals: 0[#](#spigot_world_settings_default_entity_activation_range_animals) 

The entity activation range for animals.

monsters: 0[#](#spigot_world_settings_default_entity_activation_range_monsters) 

The entity activation range for monsters.

raiders: 0[#](#spigot_world_settings_default_entity_activation_range_raiders) 

The entity activation range for raiders.

misc: 0[#](#spigot_world_settings_default_entity_activation_range_misc) 

The entity activation range for misc entities.

water: 0[#](#spigot_world_settings_default_entity_activation_range_water) 

The entity activation range for water mobs.

villagers: 0[#](#spigot_world_settings_default_entity_activation_range_villagers) 

The entity activation range for villagers.

flying-monsters: 0[#](#spigot_world_settings_default_entity_activation_range_flying_monsters) 

The entity activation range for flying monsters.

max-tnt-per-tick: -1[#](#spigot_world_settings_default_max_tnt_per_tick) 

How many TNT to process per server tick. Set to 0 or less to disable.

## Further considerations

[Section titled “Further considerations”](#further-considerations)

* `settings.timeout-time` in `spigot.yml` mirrors the watchdog setting in the `server.properties` file. Keep in mind that the `spigot.yml` setting is in seconds while the default setting is in milliseconds.
* `watchdog` in `paper-global.yml` controls the watchdog early warning. While this is only a warning, you might want to disable it as it can get annoying.


================================================================================
Chapter Title: Configuration
Original Link: https://docs.papermc.io/paper/reference/configuration/
================================================================================

Note

Many of our files have been comprehensively documented. If this is the case, they will offer a link to their page.
If this is not the case, they offer a brief explanation to what they are.

* Directorylogs/ all logs for the server
  + latest.log the most recent log
  + <yyyy-MM-dd>-<run-id>.log.gz old logs compressed with gzip
* Directoryconfig/
  + [paper-global.yml](https://docs.papermc.io/paper/reference/global-configuration)
  + [paper-world-defaults.yml](https://docs.papermc.io/paper/reference/world-configuration)
* Directoryplugins/ you can place your plugin JARs here
  + Directory.paper-remapped/ used to store remapped plugin JARs, learn more [here](https://forums.papermc.io/threads/important-dev-psa-future-removal-of-cb-package-relocation.1106/)
    - …
  + DirectorybStats/
    - config.yml stores configuration for bStats plugin metrics
  + Directoryspark/ plugin folder for the bundled spark profiler
    - [config.json](https://spark.lucko.me/docs/Configuration)  the main spark config file
* Directory<world>/
  + [paper-world.yml](#per-world-values)  stores [configuration values](https://docs.papermc.io/paper/reference/world-configuration) that apply only to the world <world>
* [banned-ips.json](https://docs.papermc.io/paper/reference/vanilla-data-files#banned-ipsjson)  stores IP addresses banned from the server
* [banned-players.json](https://docs.papermc.io/paper/reference/vanilla-data-files#banned-playersjson)  stores players banned from the server
* [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration)
* [commands.yml](https://docs.papermc.io/paper/reference/bukkit-commands-configuration)
* [eula.txt](https://docs.papermc.io/paper/reference/vanilla-data-files#eulatxt)  stores the EULA consent status
* [help.yml](https://docs.papermc.io/paper/reference/bukkit-help-configuration)  stores configuration for the `/help` command
* [ops.json](https://docs.papermc.io/paper/reference/vanilla-data-files#opsjson)  stores information about players with operator status
* [permissions.yml](https://docs.papermc.io/paper/reference/bukkit-permissions-configuration)  stores additional permission definitions
* [server.properties](https://docs.papermc.io/paper/reference/server-properties)
* [spigot.yml](https://docs.papermc.io/paper/reference/spigot-configuration)
* usercache.json caches players’ Mojang API data, e.g. their head textures
* [whitelist.json](https://docs.papermc.io/paper/reference/vanilla-data-files#whitelistjson)  stores information about whitelisted players

## Per-world configuration

[Section titled “Per-world configuration”](#per-world-configuration)

One of the most powerful yet least understood features of the Paper configuration is setting
configuration options per world. While you can not override every config option per world,
everything stored within `paper-world-defaults.yml` can be.

### Default values

[Section titled “Default values”](#default-values)

Paper sets no per-world overrides out of the box, storing all default values in
`config/paper-world-defaults.yml`. Everything in this file can be overridden per world but isn’t by
default. Changing something in `paper-world-defaults.yml` will change the value for all worlds where
you have not manually overridden it.

### Per-world values

[Section titled “Per-world values”](#per-world-values)

To set a value for a specific world, edit `paper-world.yml` within the world folder. For example, if
you wanted to enable `lootables.auto-replenish` for a world named `resource`, you would edit
`paper-world.yml` within the `resource` folder like so:

resource/paper-world.yml

```java
_version: 28

lootables:

auto-replenish: true
```

Nothing but `_version` is set in `paper-world.yml` configuration files by default. In order to
override the default for an option, you must manually add it by copying from
`paper-world-defaults.yml`.

### Inheritance

[Section titled “Inheritance”](#inheritance)

All configuration not explicitly defined for a world is inherited from `paper-world-defaults.yml`.
This means that there is no need to repeat yourself between the `paper-world-defaults.yml` and each
individual `paper-world.yml`. You **do not need to and should not** copy the entire
`paper-world-default.yml` file into each `paper-world.yml` file you want to modify. Only copy the
exact value you want to change.

For a more complex real-world example: setting both different `spawn-limits` and `auto-replenish`
in two worlds.

paper-world-defaults.yml

```java
lootables:

auto-replenish: true

entities:

spawning:

spawn-limits:

ambient: 70

axolotls: 10

creature: 15

monster: 5

underground_water_creature: 5

water_ambient: 5

water_creature: 20
```

world\_nether/paper-world.yml

```java
entities:

spawning:

spawn-limits:

monster: 90
```

resource\_world/paper-world.yml

```java
lootables:

auto-replenish: false

entities:

spawning:

spawn-limits:

axolotls: 8

creature: 15

monster: 2
```

This example demonstrates the concept of inheritance. For each world, this is the effective
configuration which will be applied:

| Configuration Key | world | world\_nether | world\_the\_end | resource\_world |
| --- | --- | --- | --- | --- |
| `lootables.auto-replenish` | `true` | `true` | `true` | `false` |
| `entities.spawning.spawn-limits.ambient` | `15` | `15` | `15` | `15` |
| `entities.spawning.spawn-limits.axolotls` | `5` | `5` | `5` | `8` |
| `entities.spawning.spawn-limits.creature` | `10` | `10` | `10` | `15` |
| `entities.spawning.spawn-limits.monster` | `70` | `90` | `70` | `2` |
| `entities.spawning.spawn-limits.underground_water_creature` | `5` | `5` | `5` | `5` |
| `entities.spawning.spawn-limits.water_ambient` | `20` | `20` | `20` | `20` |
| `entities.spawning.spawn-limits.water_creature` | `5` | `5` | `5` | `5` |

Notice that `world_the_end/paper-world.yml` was never modified. Because of this, it inherits all the
configuration options from `config/paper-world-defaults.yml`. Additionally, `auto-replenish` was
only disabled in `resource_world/paper-world.yml` because in `config/paper-world-defaults.yml`,
`auto-replenish` is set to `true`.


================================================================================
Chapter Title: Global configuration
Original Link: https://docs.papermc.io/paper/reference/global-configuration/
================================================================================

Note

The below YAML shows you the structure and default values for the global configuration (`config/paper-global.yml`).

Click on a leaf node to view the description for that setting.

anticheat: 

obfuscation: 

items: 

all-models: 

also-obfuscate: [][#](#anticheat_obfuscation_items_all_models_also_obfuscate) 

Controls additional data components which should be hidden for all items from other players. It’s generally not recommended to configure this unless you know what you are doing, as you may change how items look to other players.

dont-obfuscate: [#](#anticheat_obfuscation_items_all_models_dont_obfuscate)

- minecraft:lodestone\_tracker

Controls which data components should not be hidden for all items from other players. This is because they may slightly change the item’s appearance, so hiding it isn’t warranted. In this example, lodestone trackers may reveal critical locations, but hiding the location causes the compass to shake around for other players. It’s up to your digression whether you think this tradeoff is important.

sanitize-count: true[#](#anticheat_obfuscation_items_all_models_sanitize_count) 

Controls whether the item’s count should be hidden from other players.

enable-item-obfuscation: false[#](#anticheat_obfuscation_items_enable_item_obfuscation) 

Controls whether unnecessary item information (such as enchantments, lore, etc.) that can give cheat clients an advantage should be sent to other players’ clients. This may break resource packs that rely on information such as enchantments, lore or item names when observing other players. The hidden data components can be extended or reduced via `also-obfuscate` and `dont-obfuscate` respectively.

model-overrides: 

minecraft:elytra: 

also-obfuscate: [][#](#anticheat_obfuscation_items_model_overrides_minecraft:elytra_also_obfuscate) 

Controls the components that should also be obfuscated for items with the item model of `minecraft:elytra`. This may be useful if you want to hide certain components not important to other players.

dont-obfuscate: [#](#anticheat_obfuscation_items_model_overrides_minecraft:elytra_dont_obfuscate)

- minecraft:damage

Controls the components that should not be obfuscated for items with the item model of `minecraft:elytra`. This defaults to `minecraft:damage` as elytras with 1 durability have a special texture.

sanitize-count: true[#](#anticheat_obfuscation_items_model_overrides_minecraft:elytra_sanitize_count) 

Controls whether the item count of items with the model `minecraft:elytra` should be hidden from other players.

block-updates: 

disable-chorus-plant-updates: false[#](#block_updates_disable_chorus_plant_updates) 

Whether to disable any form of block updates for chorus plants on the server. Disabling block updates leads to chorus plants no longer updating their block state, allowing for technically invalid chorus plant configurations to remain in the world, which might be useful for mapmakers.

disable-mushroom-block-updates: false[#](#block_updates_disable_mushroom_block_updates) 

Whether to disable any form of block updates for mushroom blocks on the server. Disabling block updates leads to mushroom blocks no longer updating their block state, allowing for technically invalid mushroom block configurations to remain in the world, which might be useful for mapmakers.

disable-noteblock-updates: false[#](#block_updates_disable_noteblock_updates) 

Whether to disable any form of block updates for note blocks on the server. Disabling block updates leads to note blocks no longer updating their block state, allowing for technically invalid note blocks to remain in the world, which might be useful for mapmakers.

disable-tripwire-updates: false[#](#block_updates_disable_tripwire_updates) 

Whether to disable any form of block updates for tripwires on the server. Disabling block updates leads to tripwires no longer updating their block state, allowing for technically invalid tripwires to remain in the world, which might be useful for mapmakers.

chunk-loading-advanced: 

auto-config-send-distance: true[#](#chunk_loading_advanced_auto_config_send_distance) 

Set to true if the server will match the chunk send radius that clients have configured in their view distance settings if the client is less-than the server’s send distance.

player-max-concurrent-chunk-generates: 0[#](#chunk_loading_advanced_player_max_concurrent_chunk_generates) 

Specifies the maximum amount of concurrent chunk generations that an individual player can have. Set to 0 to let the server configure it automatically per player, or set it to -1 to disable the limit.

player-max-concurrent-chunk-loads: 0[#](#chunk_loading_advanced_player_max_concurrent_chunk_loads) 

Specifies the maximum amount of concurrent chunk loads that an individual player can have. Set to 0 to let the server configure it automatically per player, or set it to -1 to disable the limit.

chunk-loading-basic: 

player-max-chunk-generate-rate: -1.0[#](#chunk_loading_basic_player_max_chunk_generate_rate) 

The maximum rate at which chunks will generate for any individual player. Set to -1 to disable this limit.

player-max-chunk-load-rate: 100[#](#chunk_loading_basic_player_max_chunk_load_rate) 

The maximum rate at which chunks will load for any individual player. Note that this setting also affects chunk generations, since a chunk load is always first issued to test if a chunk is already generated. Set to -1 to disable this limit.

player-max-chunk-send-rate: 75[#](#chunk_loading_basic_player_max_chunk_send_rate) 

The maximum rate in chunks per second that the server will send to any individual player. Set to -1 to disable this limit.

chunk-system: 

io-threads: -1[#](#chunk_system_io_threads) 

Sets the number of threads to be used for read and write operations with chunks. If any value below zero is set, only one thread will be used.

worker-threads: -1[#](#chunk_system_worker_threads) 

Sets the number of threads to be used for parallel chunk generation. If a value below zero is set, the server will automatically determine the optimal number of threads based on the available physical CPU cores (**not logical cores**). For systems with 3 or fewer physical cores, only 1 thread will be used. In all other cases, the number of threads is capped at half of the physical cores.

collisions: 

enable-player-collisions: true[#](#collisions_enable_player_collisions) 

Sets whether the server should allow players to collide with one another. This option can be broken by plugins interacting with the scoreboard. If you are having trouble with this option, try without plugins installed

send-full-pos-for-hard-colliding-entities: true[#](#collisions_send_full_pos_for_hard_colliding_entities) 

Collisions with boats and minecarts are often subject to client/server disagreement, which may cause glitchy behavior for players. This setting attempts to mitigate this desync by sending precise locations for entities involved in collisions. Having this enabled will use more bandwidth; however, in the majority of cases, this is a worthy tradeoff

commands: 

ride-command-allow-player-as-vehicle: false[#](#commands_ride_command_allow_player_as_vehicle) 

Allow mounting entities to a player in the Vanilla `/ride` command.

suggest-player-names-when-null-tab-completions: true[#](#commands_suggest_player_names_when_null_tab_completions) 

Instructs the server to return a list of players when tab-completing when there are no other completions available

time-command-affects-all-worlds: false[#](#commands_time_command_affects_all_worlds) 

Whether the /time command should act on all worlds or just the sender’s current world

console: 

enable-brigadier-completions: true[#](#console_enable_brigadier_completions) 

Enables Mojang’s Brigadier (advanced) command completions in the server console

enable-brigadier-highlighting: true[#](#console_enable_brigadier_highlighting) 

Enables Mojang’s Brigadier highlighting in the server console

has-all-permissions: false[#](#console_has_all_permissions) 

Whether the console command sender has all permissions

item-validation: 

book: 

author: 8192[#](#item_validation_book_author) 

The maximum length of a book’s author in characters

page: 16384[#](#item_validation_book_page) 

The maximum length of a book’s page in characters

title: 8192[#](#item_validation_book_title) 

The maximum length of a book’s title in characters

book-size: 

page-max: 2560[#](#item_validation_book_size_page_max) 

The max number of bytes a single page in a book can contribute to the allowed byte total for a book, or “disabled” to disable non-vanilla restrictions on the book size.

total-multiplier: 0.98[#](#item_validation_book_size_total_multiplier) 

Each page has this multiple of bytes from the last page as its contribution to the allowed byte total for a book (with the first page being having a multiplier of 1.0)

display-name: 8192[#](#item_validation_display_name) 

The maximum length of an item’s display name in characters

lore-line: 8192[#](#item_validation_lore_line) 

The maximum length of a lore line in characters

resolve-selectors-in-books: false[#](#item_validation_resolve_selectors_in_books) 

Whether to resolve selectors in books. With this enabled, players given creative mode will be able to crash the server in yet another way

logging: 

deobfuscate-stacktraces: true[#](#logging_deobfuscate_stacktraces) 

Whether to remap Spigot mapped stacktraces to Mojang mappings in logging. Has no impact on Mojang mapped servers

messages: 

kick: 

authentication-servers-down: <lang:multiplayer.disconnect.authservers\_down>[#](#messages_kick_authentication_servers_down) 

Message sent to players when Mojang’s authentication servers are unreachable. Formatted using [MiniMessage](https://docs.papermc.io/adventure/minimessage/).

connection-throttle: Connection throttled! Please wait before reconnecting.[#](#messages_kick_connection_throttle) 

Message sent to players when they are throttled for connecting too frequently. Formatted using [MiniMessage](https://docs.papermc.io/adventure/minimessage/).

flying-player: <lang:multiplayer.disconnect.flying>[#](#messages_kick_flying_player) 

Message sent to players who are detected flying. Formatted using [MiniMessage](https://docs.papermc.io/adventure/minimessage/).

flying-vehicle: <lang:multiplayer.disconnect.flying>[#](#messages_kick_flying_vehicle) 

Message sent to players who are detected riding a flying vehicle. Formatted using [MiniMessage](https://docs.papermc.io/adventure/minimessage/).

no-permission: <red>I'm sorry, but you do not have permission to perform this command. Please contact the server administrators if you believe that this is in error.[#](#messages_no_permission) 

Default message sent to players when they have insufficient permissions for an action, formatted with [MiniMessage](https://docs.papermc.io/adventure/minimessage/). Plugins may override this for their commands

use-display-name-in-quit-message: false[#](#messages_use_display_name_in_quit_message) 

Whether the server should use the player’s display name (set by plugins) or actual name in quit messages

misc: 

chat-threads: 

chat-executor-core-size: -1[#](#misc_chat_threads_chat_executor_core_size) 

Sets the core number of threads in the chat thread pool. Values smaller than 0 will have the same effect as 0.

chat-executor-max-size: -1[#](#misc_chat_threads_chat_executor_max_size) 

Limits the number of allowed threads in the chat thread pool. Values Smaller or equal to 0 result in no limit.

client-interaction-leniency-distance: default[#](#misc_client_interaction_leniency_distance) 

Defines the leniency distance added on the server to the interaction range of a player when validating interact packets.

compression-level: default[#](#misc_compression_level) 

Sets the compression level. A value of “default” defaults to -1, resulting in no compression.

enable-nether: true[#](#misc_enable_nether) 

Whether the nether dimension is enabled and will be loaded.

fix-far-end-terrain-generation: true[#](#misc_fix_far_end_terrain_generation) 

Whether to fix MC-159283 which causes unusual ring-shaped terrain patterns in the outer End islands at extremely far distances.

load-permissions-yml-before-plugins: true[#](#misc_load_permissions_yml_before_plugins) 

Loads bukkit’s permission.yml file before plugins, allowing them to check information set there immediately on enable

max-joins-per-tick: 5[#](#misc_max_joins_per_tick) 

Sets the maximum amount of players that may join the server in a single tick. If more players join, they will be postponed until later ticks to join but not kicked. This is not related to connection throttling found in bukkit.yml

prevent-negative-villager-demand: false[#](#misc_prevent_negative_villager_demand) 

Fixes MC-163962. Prevents the villager demand from going negative, but may introduce parity issues with Vanilla.

region-file-cache-size: 256[#](#misc_region_file_cache_size) 

The maximum size of the region file cache

send-full-pos-for-item-entities: false[#](#misc_send_full_pos_for_item_entities) 

Whether to send the full position for item entities

strict-advancement-dimension-check: false[#](#misc_strict_advancement_dimension_check) 

Disables the attempts to translate worlds that use the same generation as the Overworld, The Nether, or The End to general dimensions rather than the specific dimension key of the world.

use-alternative-luck-formula: false[#](#misc_use_alternative_luck_formula) 

Use an [alternative luck formula](https://gist.github.com/aikar/40281f6c73ec9b6fef7588e6461e1ba9) allowing luck to be applied to items that have no quality defined. Makes major changes to fishing formulas

use-dimension-type-for-custom-spawners: false[#](#misc_use_dimension_type_for_custom_spawners) 

Whether phantoms, wandering traders, etc. should be able to spawn in custom overworlds. Defaults to false in order to match Vanilla behavior

xp-orb-groups-per-area: default[#](#misc_xp_orb_groups_per_area) 

The amount of equal value experience orb groups that can exist in a given area. By default, the server uses 40. Experience orbs that do not share the same value will not be merged by Vanilla’s merging algorithm.

packet-limiter: 

all-packets: 

action: KICK[#](#packet_limiter_all_packets_action) 

The action to take once the limit has been violated. Possible values are DROP which will ignore packets over the limit, and KICK which will kick players for exceeding the limit

interval: 7.0[#](#packet_limiter_all_packets_interval) 

The interval, in seconds, for which max-packet-rate should apply

max-packet-rate: 500.0[#](#packet_limiter_all_packets_max_packet_rate) 

The number of packets allowed per player within the interval

kick-message: <red><lang:disconnect.exceeded\_packet\_rate>[#](#packet_limiter_kick_message) 

The message players are kicked with for sending too many packets. Formatted using [MiniMessage](https://docs.papermc.io/adventure/minimessage/).

overrides: 

Override the **action**, **interval**, and **max-packet-rate** configuration for any individual serverbound packet. You can find the identifiers for packets on the [wiki](https://minecraft.wiki/w/Java_Edition_protocol/Packets).

minecraft:place\_recipe: 

action: KICK[#](#packet_limiter_overrides_minecraft:place_recipe_action) 

The action to take once the limit has been violated. Possible values are DROP which will ignore packets over the limit, and KICK which will kick players for exceeding the limit

interval: 7.0[#](#packet_limiter_overrides_minecraft:place_recipe_interval) 

The interval, in seconds, for which max-packet-rate should apply

max-packet-rate: 500.0[#](#packet_limiter_overrides_minecraft:place_recipe_max_packet_rate) 

The number of packets allowed per player within the interval

player-auto-save: 

max-per-tick: -1[#](#player_auto_save_max_per_tick) 

How many players should be saved at most in a single tick. A value of -1 will set a recommended value based on player-auto-save.rate of either 10 or 20

rate: -1[#](#player_auto_save_rate) 

How often player data should be saved in ticks. A value of -1 will use ticks-per.autosave in bukkit.yml

proxies: 

bungee-cord: 

online-mode: true[#](#proxies_bungee_cord_online_mode) 

Instructs the server how to handle player UUIDs and data when behind BungeeCord. Always set to match your proxy’s online-mode setting

proxy-protocol: false[#](#proxies_proxy_protocol) 

Whether the server should process [PROXY Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) messages. This is completely unrelated to Velocity or BungeeCord. Only enable this if you are using HAProxy or similar

velocity: 

enabled: false[#](#proxies_velocity_enabled) 

Whether the server should accept Velocity Modern Forwarding

online-mode: true[#](#proxies_velocity_online_mode) 

Instructs the server how to handle player UUIDs and data when behind Velocity. Always set to match your proxy’s online-mode setting

secret: ""[#](#proxies_velocity_secret) 

The secret string that is shared by your Velocity proxy and this server. This needs to match your proxy’s secret as defined in the forwarding.secret file

scoreboards: 

save-empty-scoreboard-teams: true[#](#scoreboards_save_empty_scoreboard_teams) 

Some scoreboard plugins leave hundreds of empty scoreboard teams around, dramatically slowing down login times. This sets whether the server should remove those empty teams automatically

track-plugin-scoreboards: false[#](#scoreboards_track_plugin_scoreboards) 

Whether the server should track plugin scoreboards with only dummy objectives. This is a breaking change; however, it provides a much more sensible default value. Enabling this with plugins using many scoreboards will incur a performance degradation

spam-limiter: 

incoming-packet-threshold: 300[#](#spam_limiter_incoming_packet_threshold) 

Sets the threshold at which the server will consider incoming packets spam and ignore them

recipe-spam-increment: 1[#](#spam_limiter_recipe_spam_increment) 

The number that the recipe spam counter increases by when a player presses a recipe

recipe-spam-limit: 20[#](#spam_limiter_recipe_spam_limit) 

The number that the recipe spam counter can reach until the server kicks the player for spam

tab-spam-increment: 1[#](#spam_limiter_tab_spam_increment) 

The number that the internal tab spam counter increases by when a player presses tab in the chat window

tab-spam-limit: 500[#](#spam_limiter_tab_spam_limit) 

The number that the internal tab spam counter can reach until the server kicks the player for spam

spark: 

enable-immediately: false[#](#spark_enable_immediately) 

Whether the bundled spark profiler should be enabled as soon as possible. This can be useful for profiling the server during startup. By default, spark is enabled once the server has finished starting up (when the **Done (X.XXXs)! For help, type “help”** message is sent in the console).

enabled: true[#](#spark_enabled) 

Whether the bundled spark profiler should be enabled.

unsupported-settings: 

**Unsupported settings**

The following settings are provided by Paper but are not officially supported. Use them at your own risk and they may be removed at any time.

allow-headless-pistons: false[#](#unsupported_settings_allow_headless_pistons) 

Whether the server should allow the creation of headless pistons. These are often used to break permanent blocks

allow-permanent-block-break-exploits: false[#](#unsupported_settings_allow_permanent_block_break_exploits) 

Whether unbreakable blocks can be broken with Vanilla exploits. This includes bedrock, end portal frames, end portal blocks, and more

allow-piston-duplication: false[#](#unsupported_settings_allow_piston_duplication) 

Whether to allow duplication of TNT, carpets, and rails. This does not control sand duplication

allow-unsafe-end-portal-teleportation: false[#](#unsupported_settings_allow_unsafe_end_portal_teleportation) 

This setting allows for exploits related to end portal teleportation to be possible, for example sand duplication. This setting is not recommended to be enabled, but is provided for those who wish to use it.

compression-format: ZLIB[#](#unsupported_settings_compression_format) 

Allows the server to customize the format of saved region files. This supports ZLIB, GZIP, LZ4 and NONE, where None namely allows for compression to be disabled

oversized-item-component-sanitizer: 

dont-sanitize: [][#](#unsupported_settings_oversized_item_component_sanitizer_dont_sanitize) 

This setting defines which item data components shouldn’t be sanitized in oversized item obfuscation. Changing this re-enables exploits, but may be needed for certain resource packs. Possible values: `minecraft:container`, `minecraft:charged_projectiles`, `minecraft:bundle_contents`

perform-username-validation: true[#](#unsupported_settings_perform_username_validation) 

Whether the server should validate usernames. While this may allow users with special characters in their name to join, it can also cause issues with commands and plugins

skip-tripwire-hook-placement-validation: false[#](#unsupported_settings_skip_tripwire_hook_placement_validation) 

This setting allows for exploits related to tripwire hook duping to be enabled.

skip-vanilla-damage-tick-when-shield-blocked: false[#](#unsupported_settings_skip_vanilla_damage_tick_when_shield_blocked) 

Whether the server should skip damage ticks when entities are blocking damage via a shield. While Vanilla does process a damage tick, this behavior was a long standing bug in Paper. Enabling this option means that the damage tick will be skipped, which may result in rapid damage on shields due to the missing invulnerability.

update-equipment-on-player-actions: true[#](#unsupported_settings_update_equipment_on_player_actions) 

This setting controls if equipment should be updated when handling certain player actions. If set to false this will allow players to exploit attributes by e.g. switching equipment before using it.

update-checker: 

enabled: true[#](#update_checker_enabled) 

Whether Paper should check for updates automatically on startup. See [here](https://docs.papermc.io/paper/misc/update-checker/) for more information.

watchdog: 

early-warning-delay: 10000[#](#watchdog_early_warning_delay) 

The number of milliseconds before the watchdog thread starts printing thread dumps after the server starts hanging

early-warning-every: 5000[#](#watchdog_early_warning_every) 

The interval in milliseconds between printed thread dumps while the server is hanging


================================================================================
Chapter Title: World configuration
Original Link: https://docs.papermc.io/paper/reference/world-configuration/
================================================================================

Note

The below YAML shows you the structure and default values for the world configuration (`config/paper-world-defaults.yml` and `<worldfolder>/paper-world.yml`).

Click on a leaf node to view the description for that setting.

anticheat: 

anti-xray: 

enabled: false[#](#anticheat_anti_xray_enabled) 

Controls the on/off state for the Anti-Xray system

engine-mode: 1[#](#anticheat_anti_xray_engine_mode) 

Sets the Anti-Xray engine mode. 1 replaces specified blocks (hidden-blocks) with other “fake” blocks, stone (deepslate at y < 0), netherrack, or end\_stone based on the dimension. In contrast, 2 will replace both hidden-blocks and replacement-blocks with randomly generated hidden-blocks. Similarly to engine mode 2, mode 3 will replace each chunk layer with a random block from the hidden-blocks list.

hidden-blocks: [#](#anticheat_anti_xray_hidden_blocks)

- copper\_ore
- deepslate\_copper\_ore
- raw\_copper\_block
- gold\_ore
- deepslate\_gold\_ore
- iron\_ore
- deepslate\_iron\_ore
- raw\_iron\_block
- coal\_ore
- deepslate\_coal\_ore
- lapis\_ore
- deepslate\_lapis\_ore
- mossy\_cobblestone
- obsidian
- chest
- diamond\_ore
- deepslate\_diamond\_ore
- redstone\_ore
- deepslate\_redstone\_ore
- clay
- emerald\_ore
- deepslate\_emerald\_ore
- ender\_chest

With engine-mode: 1, these blocks will be replaced by stone (deepslate at y < 0), netherrack, or end\_stone, based on the dimension. All types of air are ignored on this list.
With engine-mode: 2, these blocks will be randomly placed in the world, replacing both hidden-blocks and replacement-blocks. Tile entities, such as chests or spawners, are not allowed on this list. Individual blocks may be added multiple times, increasing their chance of being placed.
engine-mode: 3 is very similar to 2, but these blocks will be randomly placed where each vertical chunk layer will take the same block from the list.

lava-obscures: false[#](#anticheat_anti_xray_lava_obscures) 

Whether to obfuscate blocks touching lava. Does not work well with non-stone-like ore textures. This is because lava, while being mostly opaque, does not cover blocks fully at the surface

max-block-height: 64[#](#anticheat_anti_xray_max_block_height) 

Sets the maximum height (y coordinate, starting from the bottom of the world) to which anti-xray will operate. Only integer multiples of 16 are accepted. All other values will be rounded down. The [Minecraft Wiki page about Ore](https://minecraft.wiki/w/Ore) may be helpful in determining the best value for you

replacement-blocks: [#](#anticheat_anti_xray_replacement_blocks)

- stone
- oak\_planks
- deepslate

With engine-mode: 1, replacement blocks are not used. Changing this list will have no effect.
With engine-mode: 2, both replacement-blocks and hidden-blocks are randomly replaced by hidden-blocks. While tile entities are ignored in the hidden-blocks list, they may be added to the replacement-blocks list. All types of air blocks are ignored here.
With engine-mode: 3, the behavior is the same as engine-mode: 2, but the replacement-blocks list is used to determine which blocks are used for each vertical chunk layer.

update-radius: 2[#](#anticheat_anti_xray_update_radius) 

Radius for block updates which will be sent containing real block data when the client interacts with a block. Only values 0, 1, and 2 are accepted. Values smaller than 0 will be rounded up to 0, while values larger than 2 will be rounded down to 2. 0 is only designed for testing purposes. Do not use it in production

use-permission: false[#](#anticheat_anti_xray_use_permission) 

Whether to allow players with the paper.antixray.bypass permission to bypass anti-xray. Checking this permission is disabled by default as legacy permission plugins may struggle with the number of checks made. This should only be used with modern permission plugins

chunks: 

auto-save-interval: default[#](#chunks_auto_save_interval) 

Configures the world saving interval in ticks. Overrides ticks-per.autosave in bukkit.yml for this world. By default it will use the global ticks-per.autosave in bukkit.yml

delay-chunk-unloads-by: 10s[#](#chunks_delay_chunk_unloads_by) 

Delays chunk unloads by the specified time. Formatted as a duration with a single unit e.g. 10h or 25m. Supports d, h, m, and s.

entity-per-chunk-save-limit: 

experience\_orb: -1[#](#chunks_entity_per_chunk_save_limit_experience_orb) 

Limits the number of experience\_orb’s that will be saved/loaded per chunk. A value of -1 disables the limit for a specific entity.

<entity-type>: amount[#](#chunks_entity_per_chunk_save_limit__entity_type_) 

Limits the number of any type of entity that will be saved/loaded per chunk. A value of -1 disables the limit for a specific entity. **Any entity may be added to the list**, beyond the enumerated defaults

fixed-chunk-inhabited-time: -1[#](#chunks_fixed_chunk_inhabited_time) 

If 0 or greater, set the chunk inhabited time to a fixed number. Fixed in this instance means static or unchanging. This is **not** fixing a bug. The timer is increased when chunks are kept loaded because of player activity

flush-regions-on-save: false[#](#chunks_flush_regions_on_save) 

Sets whether the server will flush chunks to disk when they are saved. This may have a performance impact

max-auto-save-chunks-per-tick: 24[#](#chunks_max_auto_save_chunks_per_tick) 

The maximum number of chunks the auto-save system will save in a single tick

prevent-moving-into-unloaded-chunks: false[#](#chunks_prevent_moving_into_unloaded_chunks) 

Sets whether the server will prevent players from moving into unloaded chunks or not

collisions: 

allow-player-cramming-damage: false[#](#collisions_allow_player_cramming_damage) 

Allows players to take damage from cramming when colliding with more entities than set in the maxEntityCramming game rule

allow-vehicle-collisions: true[#](#collisions_allow_vehicle_collisions) 

Whether vehicles should also be able to collide while only-players-collide is enabled

fix-climbing-bypassing-cramming-rule: false[#](#collisions_fix_climbing_bypassing_cramming_rule) 

Sets whether climbing should bypass the entity cramming limit(maxEntityCramming game rule). If set to true, climbing entities will also be counted towards the entity cramming limit so that they can take suffocation damage

max-entity-collisions: 8[#](#collisions_max_entity_collisions) 

Instructs the server to stop processing collisions after this value is reached

only-players-collide: false[#](#collisions_only_players_collide) 

Only calculate collisions if a player is one of the two entities colliding

command-blocks: 

force-follow-perm-level: true[#](#command_blocks_force_follow_perm_level) 

Require that command blocks meet both the Bukkit permission requirements and the Vanilla permission level. Otherwise, only 1 of those is required.

permissions-level: 2[#](#command_blocks_permissions_level) 

Default Vanilla permission level for command blocks.

entities: 

armor-stands: 

do-collision-entity-lookups: true[#](#entities_armor_stands_do_collision_entity_lookups) 

Instructs armor stand entities to do entity collision checks

tick: true[#](#entities_armor_stands_tick) 

Disable to prevent armor stands from ticking. Can improve performance with many armor stands

behavior: 

allow-spider-world-border-climbing: true[#](#entities_behavior_allow_spider_world_border_climbing) 

Whether spiders should be able to climb on the world border, as if it were a regular wall.

baby-zombie-movement-modifier: 0.5[#](#entities_behavior_baby_zombie_movement_modifier) 

Modifies the speed that baby zombies move at, where 0.5 is 50% faster than the mob base speed, and -0.4 would be 40% slower

cooldown-failed-beehive-releases: true[#](#entities_behavior_cooldown_failed_beehive_releases) 

Adds a cooldown to bees being released after a failed release, which can occur if the hive is blocked or it being night.

disable-chest-cat-detection: false[#](#entities_behavior_disable_chest_cat_detection) 

Allows you to open chests even if they have a cat sitting on top of them

disable-creeper-lingering-effect: false[#](#entities_behavior_disable_creeper_lingering_effect) 

Disables creepers randomly leaving behind a lingering area effect cloud

disable-player-crits: false[#](#entities_behavior_disable_player_crits) 

Instructs the server to disable critical hits in PvP, treating them as normal hits instead

door-breaking-difficulty: 

vindicator: [#](#entities_behavior_door_breaking_difficulty_vindicator)

- NORMAL
- HARD

A list of difficulties (PEACEFUL, EASY, NORMAL, HARD) at which vindicators will attempt to break doors.

<entity-type>: [#](#entities_behavior_door_breaking_difficulty__entity_type_)

- HARD

A list of difficulties (PEACEFUL, EASY, NORMAL, HARD) at which zombie-like entities (husks, zombies, zombie villagers and zombified piglins) will attempt to break doors.

ender-dragons-death-always-places-dragon-egg: false[#](#entities_behavior_ender_dragons_death_always_places_dragon_egg) 

Controls whether ender dragons should always drop dragon eggs on death

experience-merge-max-value: -1[#](#entities_behavior_experience_merge_max_value) 

Instructs the server to put a maximum value on experience orbs, preventing them all from merging down into 1 single orb. A value of -1 instructs the server to use no max value, allowing them to merge down into a single orb. This is especially noticeable when defeating boss monsters

mobs-can-always-pick-up-loot: 

skeletons: false[#](#entities_behavior_mobs_can_always_pick_up_loot_skeletons) 

Instructs the server to allow skeletons to pick up loot. If set to false, the probability that a skeleton picks up items depends on the world’s difficulty (Vanilla behavior)

zombies: false[#](#entities_behavior_mobs_can_always_pick_up_loot_zombies) 

Instructs the server to allow zombies to pick up loot. If set to false, the probability that a zombie picks up items depends on the world’s difficulty (Vanilla behavior)

nerf-pigmen-from-nether-portals: false[#](#entities_behavior_nerf_pigmen_from_nether_portals) 

Removes AI from pigmen spawned via nether portals

only-merge-items-horizontally: false[#](#entities_behavior_only_merge_items_horizontally) 

Prevents merging items that are not on the same y level, preventing potential visual artifacts.

parrots-are-unaffected-by-player-movement: false[#](#entities_behavior_parrots_are_unaffected_by_player_movement) 

Makes parrots “sticky” so they do not fall off a player’s shoulder when they move. Use crouch to shake them off

phantoms-do-not-spawn-on-creative-players: true[#](#entities_behavior_phantoms_do_not_spawn_on_creative_players) 

Disables spawning of phantoms on players in creative mode

phantoms-only-attack-insomniacs: true[#](#entities_behavior_phantoms_only_attack_insomniacs) 

Prevents phantoms from attacking players who have slept

phantoms-spawn-attempt-max-seconds: 119[#](#entities_behavior_phantoms_spawn_attempt_max_seconds) 

Sets the maximum number of seconds between phantom spawn attempts

phantoms-spawn-attempt-min-seconds: 60[#](#entities_behavior_phantoms_spawn_attempt_min_seconds) 

Sets the minimum number of seconds between phantom spawn attempts

piglins-guard-chests: true[#](#entities_behavior_piglins_guard_chests) 

If piglins should attempt to guard chests when angered

pillager-patrols: 

disable: false[#](#entities_behavior_pillager_patrols_disable) 

Disables Pillager patrols and associated AI

spawn-chance: 0.2[#](#entities_behavior_pillager_patrols_spawn_chance) 

Modify the spawn changes for patrols

spawn-delay: 

ticks: 12000[#](#entities_behavior_pillager_patrols_spawn_delay_ticks) 

Delay in ticks between spawn chance

per-player: false[#](#entities_behavior_pillager_patrols_spawn_delay_per_player) 

Sets the delay to be independent for each player

start: 

day: 5[#](#entities_behavior_pillager_patrols_start_day) 

Days between raid spawns

per-player: false[#](#entities_behavior_pillager_patrols_start_per_player) 

Sets the start to be independent for each player

player-insomnia-start-ticks: 72000[#](#entities_behavior_player_insomnia_start_ticks) 

Number of ticks a player must stay awake before phantoms can start spawning.
Default (72000) is 3 Minecraft days, -1 disables phantom spawning.

should-remove-dragon: false[#](#entities_behavior_should_remove_dragon) 

Sets whether to remove the dragon if it exists without a portal

spawner-nerfed-mobs-should-jump: false[#](#entities_behavior_spawner_nerfed_mobs_should_jump) 

Determines if spawner nerfed mobs should attempt to float (jump) in water

stuck-entity-poi-retry-delay: 200[#](#entities_behavior_stuck_entity_poi_retry_delay) 

The delay before retrying POI acquisition when entity navigation is stuck. This will reduce pathfinding performance impact. Measured in ticks.

zombie-villager-infection-chance: default[#](#entities_behavior_zombie_villager_infection_chance) 

Sets the chance for villager conversion to zombie villager. Set to “default” for default behavior based on game difficulty. Set to 0.0 to always have villagers die when killed by zombies. Set to 100.0 to always convert villagers to zombie villagers

zombies-target-turtle-eggs: true[#](#entities_behavior_zombies_target_turtle_eggs) 

Sets whether zombies and zombified piglins should target turtle eggs. Setting this to false may help with performance, as they won’t search for nearby eggs

entities-target-with-follow-range: false[#](#entities_entities_target_with_follow_range) 

Sets whether the server should use follow range when targeting entities

markers: 

tick: true[#](#entities_markers_tick) 

Disable to prevent markers from ticking. This may affect how they behave as passengers of other entities

mob-effects: 

immune-to-wither-effect: true[#](#entities_mob_effects_immune_to_wither_effect) 

If the specified entity should be immune to the wither effect

spiders-immune-to-poison-effect: true[#](#entities_mob_effects_spiders_immune_to_poison_effect) 

If spiders should be immune to poison

sniffer: 

boosted-hatch-time: default[#](#entities_sniffer_boosted_hatch_time) 

The boosted hatch time, in ticks, a sniffer egg requires to hatch. Boosted hatching occurs when planted on specific blocks.

hatch-time: default[#](#entities_sniffer_hatch_time) 

The non-boosted hatch time, in ticks, a sniffer egg requires to hatch.

spawning: 

all-chunks-are-slime-chunks: false[#](#entities_spawning_all_chunks_are_slime_chunks) 

Instructs the server to treat all chunks like slime chunks, allowing them to spawn in any chunk. This may actually decrease your chances of running into a Slime as they now have a much larger potential spawn area

alt-item-despawn-rate: 

enabled: false[#](#entities_spawning_alt_item_despawn_rate_enabled) 

Determines if items will have different despawn rates

items: 

cobblestone: 300[#](#entities_spawning_alt_item_despawn_rate_items_cobblestone) 

Sets a custom despawn rate for cobblestone of 300 ticks

<item-type>: amount[#](#entities_spawning_alt_item_despawn_rate_items__item_type_) 

Determines how long each respective item despawns in ticks. The item ids are the same as those used in the /give command. They can be viewed by enabling advanced item tooltips in-game by pressing **F3 + H**; the item id will appear at the bottom of the tooltip that appears when you hover over an item

max-arrow-despawn-invulnerability: 200[#](#entities_spawning_max_arrow_despawn_invulnerability) 

Workaround for MC-125757, makes all arrows advance their despawn timer as if they were stuck in the ground, after a delay (in ticks).

count-all-mobs-for-spawning: false[#](#entities_spawning_count_all_mobs_for_spawning) 

Determines whether spawner mobs and other misc mobs are counted towards the global mob limit

creative-arrow-despawn-rate: default[#](#entities_spawning_creative_arrow_despawn_rate) 

The rate, in ticks, at which arrows shot from players in creative mode are despawned

despawn-range-shape: ELLIPSOID[#](#entities_spawning_despawn_range_shape) 

The shape of the despawn range. Can be one of the following values:

* **ELLIPSOID**: The despawn range is an ellipsoid, with the horizontal and vertical despawn ranges being separate. This is the default Minecraft behavior.
* **CYLINDER**: The vertical despawn range is checked separately from the horizontal despawn range, but the horizontal despawn range is a circle.

despawn-ranges: 

<mob\_category>: 

hard: default[#](#entities_spawning_despawn_ranges__mob_category__hard) 

The horizontal and vertical number of blocks away from a player in which each monster type (set individually) will be forcibly despawned.

soft: default[#](#entities_spawning_despawn_ranges__mob_category__soft) 

The horizontal and vertical number of blocks away from a player in which each monster type (set individually) will be randomly selected to be despawned.

<mob\_category>: 

hard: 

horizontal: default[#](#entities_spawning_despawn_ranges__mob_category___hard_horizontal) 

The horizontal number of blocks away from a player in which each entity type (set individually) will be forcibly despawned.

vertical: default[#](#entities_spawning_despawn_ranges__mob_category___hard_vertical) 

The vertical number of blocks away from a player in which each entity type (set individually) will be forcibly despawned.

soft: 

horizontal: default[#](#entities_spawning_despawn_ranges__mob_category___soft_horizontal) 

The horizontal number of blocks away from a player in which each entity type (set individually) will be randomly selected to be despawned.

vertical: default[#](#entities_spawning_despawn_ranges__mob_category___soft_vertical) 

The vertical number of blocks away from a player in which each entity type (set individually) will be randomly selected to be despawned.

despawn-time: 

<entity-type>: disabled[#](#entities_spawning_despawn_time__entity_type_) 

A server-introduced despawn time after which the entity is forcefully despawned. If disabled or not specified, the entity will simply despawn according to Vanilla rules.

disable-mob-spawner-spawn-egg-transformation: false[#](#entities_spawning_disable_mob_spawner_spawn_egg_transformation) 

Whether to block players from changing the type of mob spawners with a spawn egg

duplicate-uuid: 

mode: SAFE\_REGEN[#](#entities_spawning_duplicate_uuid_mode) 

Specifies the method the server uses to resolve entities with duplicate UUIDs. This can be one of the following values:

* **SAFE\_REGEN**: Regenerate a UUID for the entity, or delete it if they are close.
* **DELETE**: Delete the entity.
* **NOTHING**: Does nothing, not printing logs.
* **WARN**: Does nothing, printing logs

safe-regen-delete-range: 32[#](#entities_spawning_duplicate_uuid_safe_regen_delete_range) 

If multiple entities with duplicate UUIDs are within this many blocks, saferegen will delete all but 1 of them

filter-bad-tile-entity-nbt-from-falling-blocks: true[#](#entities_spawning_filter_bad_tile_entity_nbt_from_falling_blocks) 

Instructs the server to remove certain NBT data from falling blocks. **Note**: Some adventure maps may require this to be turned off to function correctly, but we do not recommend turning it off on a public server

filtered-entity-tag-nbt-paths: [#](#entities_spawning_filtered_entity_tag_nbt_paths)

- Pos
- Motion
- sleeping\_pos

A list of NBT tags that will be removed from the “entity\_data” component on items which spawn entities. The format of these strings follows the same format used to select NBT tags in Vanilla commands. If the spawning was directly caused by a player and the player has the minecraft.nbt.place permission, the filter list will be ignored. The defaults are set to prevent entities from spawning or moving to a place other than the location they were placed. For example, if Pos wasn’t included, a spawn egg could place an entity at any location. **Note**: Some adventure maps may require this to be an empty list to function correctly, but we do not recommend turning it off on a public server

iron-golems-can-spawn-in-air: false[#](#entities_spawning_iron_golems_can_spawn_in_air) 

Sets whether iron golems can spawn in the air. Iron farms may break depending on this setting

monster-spawn-max-light-level: default[#](#entities_spawning_monster_spawn_max_light_level) 

When set to “default”, the Vanilla default will be used (=0). Set to 15 or greater to revert to pre-1.18 behavior

non-player-arrow-despawn-rate: default[#](#entities_spawning_non_player_arrow_despawn_rate) 

The rate, in ticks, at which arrows shot from non-player entities are despawned. The default value instructs the server to use the same default arrow despawn rate from spigot.yml that is used for all arrows

per-player-mob-spawns: true[#](#entities_spawning_per_player_mob_spawns) 

Determines whether the mob limit (in bukkit.yml) is counted per player or for the entire server. Enabling this setting results in roughly the same number of mobs, but with a more even distribution that prevents one player from using the entire mob cap and provides a more single-player like experience

scan-for-legacy-ender-dragon: true[#](#entities_spawning_scan_for_legacy_ender_dragon) 

Determines if the server attempts to start the ender dragon fight. Setting this to false will make the ender dragon not spawn in the end, even with a new world

skeleton-horse-thunder-spawn-chance: default[#](#entities_spawning_skeleton_horse_thunder_spawn_chance) 

Sets the chance that a “Skeleton Trap” (4 skeleton horsemen) will spawn in a thunderstorm. Takes a double between 0 and 1, where 0 is 0% chance

slime-spawn-height: 

slime-chunk: 

maximum: 40[#](#entities_spawning_slime_spawn_height_slime_chunk_maximum) 

Sets the maximum Y position for natural Slime spawn in Slime Chunks

surface-biome: 

minimum: 50[#](#entities_spawning_slime_spawn_height_surface_biome_minimum) 

Sets the minimum Y position for natural Slime spawn in Surface Biomes

maximum: 70[#](#entities_spawning_slime_spawn_height_surface_biome_maximum) 

Sets the maximum Y position for natural Slime spawn in Surface Biomes

spawn-limits: 

ambient: -1[#](#entities_spawning_spawn_limits_ambient) 

The constant used to determine how many ambient mobs will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_ambient), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

axolotls: -1[#](#entities_spawning_spawn_limits_axolotls) 

The constant used to determine how many axolotls will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_axolotls), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

creature: -1[#](#entities_spawning_spawn_limits_creature) 

The constant used to determine how many animals will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_animals), except that it can be configured per world, and the name.
A value of -1 will use the value in bukkit.yml

monster: -1[#](#entities_spawning_spawn_limits_monster) 

The constant used to determine how many monsters will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_monsters), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

underground\_water\_creature: -1[#](#entities_spawning_spawn_limits_underground_water_creature) 

The constant used to determine how many underground water creatures will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_water_underground_creature), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

water\_ambient: -1[#](#entities_spawning_spawn_limits_water_ambient) 

The constant used to determine how many water ambient mobs will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_water_ambient), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

water\_creature: -1[#](#entities_spawning_spawn_limits_water_creature) 

The constant used to determine how many water animals will be naturally spawned per world. This is identical to the value set in [bukkit.yml](https://docs.papermc.io/paper/reference/bukkit-configuration#spawn_limits_water_animals), except that it can be configured per world.
A value of -1 will use the value in bukkit.yml

ticks-per-spawn: 

ambient: -1[#](#entities_spawning_ticks_per_spawn_ambient) 

Determines how many ticks there are between attempts to spawn ambient mobs (bats).
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_ambient_spawns).

axolotls: -1[#](#entities_spawning_ticks_per_spawn_axolotls) 

Determines how many ticks there are between attempts to spawn axolotls.
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_axolotl_spawns).

creature: -1[#](#entities_spawning_ticks_per_spawn_creature) 

Determines how many ticks there are between attempts to spawn passive creatures (animals).
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_animal_spawns).

monster: -1[#](#entities_spawning_ticks_per_spawn_monster) 

Determines how many ticks there are between attempts to spawn hostile monsters.
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_monster_spawns).

underground\_water\_creature: -1[#](#entities_spawning_ticks_per_spawn_underground_water_creature) 

Determines how many ticks there are between attempts to spawn underground water creatures (glow squid).
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_water_underground_creature_spawns).

water\_ambient: -1[#](#entities_spawning_ticks_per_spawn_water_ambient) 

Determines how many ticks there are between attempts to spawn ambient water mobs (tropical fish).
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_water_ambient_spawns).

water\_creature: -1[#](#entities_spawning_ticks_per_spawn_water_creature) 

Determines how many ticks there are between attempts to spawn water creatures (squid, dolphins).
Default (-1) uses
[bukkit.yml spawn rate](https://docs.papermc.io/paper/reference/bukkit-configuration#ticks_per_water_spawns).

wandering-trader: 

spawn-chance-failure-increment: 25[#](#entities_spawning_wandering_trader_spawn_chance_failure_increment) 

How much the spawn chance will be increased on every failed wandering trader spawn

spawn-chance-max: 75[#](#entities_spawning_wandering_trader_spawn_chance_max) 

The maximum chance that a wandering trader will be spawned

spawn-chance-min: 25[#](#entities_spawning_wandering_trader_spawn_chance_min) 

The minimum chance that a wandering trader will be spawned

spawn-day-length: 24000[#](#entities_spawning_wandering_trader_spawn_day_length) 

Time between wandering trader spawn attempts in ticks

spawn-minute-length: 1200[#](#entities_spawning_wandering_trader_spawn_minute_length) 

The length of the wandering trader spawn minute in ticks

wateranimal-spawn-height: 

maximum: default[#](#entities_spawning_wateranimal_spawn_height_maximum) 

The maximum height at which water animals will spawn. **Note**: The default value defers to Minecraft’s default setting, which as of 1.12 is the sea level of the world (usually Y: 64)

minimum: default[#](#entities_spawning_wateranimal_spawn_height_minimum) 

The minimum height at which water animals will spawn. **Note**: The default value defers to Minecraft’s default setting, which as of 1.12 is the sea level of the world (usually Y: 64)

tracking-range-y: 

animal: default[#](#entities_tracking_range_y_animal) 

Controls how far vertically in blocks animals are tracked (sent to) the player.

display: default[#](#entities_tracking_range_y_display) 

Controls how far vertically in blocks display entities are tracked (sent to) the player.

enabled: false[#](#entities_tracking_range_y_enabled) 

Enables separate ranges for tracking ranges in the vertical (Y) direction.

misc: default[#](#entities_tracking_range_y_misc) 

Controls how far vertically in blocks miscellaneous are tracked (sent to) the player.

monster: default[#](#entities_tracking_range_y_monster) 

Controls how far vertically in blocks monsters are tracked (sent to) the player.

other: default[#](#entities_tracking_range_y_other) 

Controls how far vertically in blocks other entities are tracked (sent to) the player.

player: default[#](#entities_tracking_range_y_player) 

Controls how far vertically in blocks players are tracked (sent to) the player.

environment: 

disable-explosion-knockback: false[#](#environment_disable_explosion_knockback) 

Instructs the server to completely block any knockback that occurs as a result of an explosion

disable-ice-and-snow: false[#](#environment_disable_ice_and_snow) 

Disables ice and snow formation. This also causes cauldrons to no longer be filled by rain or snow

disable-thunder: false[#](#environment_disable_thunder) 

Disables thunderstorms

fire-tick-delay: 30[#](#environment_fire_tick_delay) 

Sets the minimum delay between fire ticks

frosted-ice: 

delay: 

max: 40[#](#environment_frosted_ice_delay_max) 

Maximum RNG value to apply frosted-ice effects at

min: 20[#](#environment_frosted_ice_delay_min) 

Minimum RNG value to apply frosted-ice effects at

enabled: true[#](#environment_frosted_ice_enabled) 

Instructs the server to enable (and tick) frosted ice blocks

generate-flat-bedrock: false[#](#environment_generate_flat_bedrock) 

Instructs the server to generate bedrock as a single flat layer

locate-structures-outside-world-border: false[#](#environment_locate_structures_outside_world_border) 

If the server should be able to locate structures in chunks that are outside the world border.

max-block-ticks: 65536[#](#environment_max_block_ticks) 

The maximum number of block ticks that can be processed in a single tick. This is a safety measure to prevent the server from hanging when there is a large amount of block updates.

max-fluid-ticks: 65536[#](#environment_max_fluid_ticks) 

The maximum number of fluid ticks that can be processed in a single tick. This is a safety measure to prevent the server from hanging when there is a large number of fluid updates.

nether-ceiling-void-damage-height: disabled[#](#environment_nether_ceiling_void_damage_height) 

Sets the level above which players in the nether will take void damage. This is a Vanilla-friendly way to restrict players from using the nether ceiling as a buildable area. Setting to disabled disables this feature

optimize-explosions: false[#](#environment_optimize_explosions) 

Instructs the server to cache entity lookups during an explosion, rather than recalculating throughout the process. This speeds up explosions significantly

portal-create-radius: 16[#](#environment_portal_create_radius) 

The maximum range the server will try to create a portal around when generating a new portal

portal-search-radius: 128[#](#environment_portal_search_radius) 

The maximum range the server will use to look for an existing nether portal. If it can’t find one in that range, it will generate a new one

portal-search-vanilla-dimension-scaling: true[#](#environment_portal_search_vanilla_dimension_scaling) 

Whether to apply Vanilla dimension scaling to portal-search-radius

treasure-maps: 

enabled: true[#](#environment_treasure_maps_enabled) 

If villagers should trade treasure maps and treasure maps from chests should lead to a feature

find-already-discovered: 

loot-tables: default[#](#environment_treasure_maps_find_already_discovered_loot_tables) 

Overrides the loot table-configured check for undiscovered structures. default allows loot tables to individually determine if the map should allow discovered locations in its search. All Vanilla loot tables default to skipping discovered locations so changing this to false would override that behavior and force them to search discovered locations

villager-trade: false[#](#environment_treasure_maps_find_already_discovered_villager_trade) 

Instructs the server to target the first treasure location found for maps obtained via trading with villagers

void-damage-amount: 4[#](#environment_void_damage_amount) 

The amount of void damage dealt per void damage attempt. May be set to `disabled` to completely disable void damage in the world.

void-damage-min-build-height-offset: -64[#](#environment_void_damage_min_build_height_offset) 

The offset from a world’s minimum build height at which entities should receive void damage.

water-over-lava-flow-speed: 5[#](#environment_water_over_lava_flow_speed) 

Sets the speed at which water flows while over lava

feature-seeds: 

generate-random-seeds-for-all: false[#](#feature_seeds_generate_random_seeds_for_all) 

Enables autofilling random seeds for all available features you haven’t already set a seed to. Using this in a controlled environment is also a good way of receiving a full list of features you can set seeds for

<feature-namespace>: -1[#](#feature_seeds__feature_namespace_) 

Sets the population seed for the specified feature. If set to -1, the Vanilla population seed stays unchanged and will not be overridden by the autofill option

fishing-time-range: 

maximum: 600[#](#fishing_time_range_maximum) 

The maximum number of RNG ticks before catching a fish

minimum: 100[#](#fishing_time_range_minimum) 

The minimum number of RNG ticks needed to catch a fish

fixes: 

disable-unloaded-chunk-enderpearl-exploit: false[#](#fixes_disable_unloaded_chunk_enderpearl_exploit) 

Prevent enderpearls from storing the thrower when in an unloaded chunk

falling-block-height-nerf: disabled[#](#fixes_falling_block_height_nerf) 

The height at which falling blocks will be removed from the server. A value of disabled will disable this feature

fix-items-merging-through-walls: false[#](#fixes_fix_items_merging_through_walls) 

Whether items should be prevented from merging through walls. Enabling this will incur a performance degradation. This is only necessary when merge-radius.item (spigot.yml) is large enough to merge items through walls

prevent-tnt-from-moving-in-water: false[#](#fixes_prevent_tnt_from_moving_in_water) 

Instructs the server to keep Primed TNT entities from moving in flowing water

split-overstacked-loot: true[#](#fixes_split_overstacked_loot) 

When set to false, loot tables will not attempt to split items with a stack size higher than the maximum into items of smaller stack sizes. This will prevent overstacked items from being lost or causing a chunk to become uninhabitable (due to players getting constantly kicked because of oversized packets) when a shulker box is broken in survival

tnt-entity-height-nerf: disabled[#](#fixes_tnt_entity_height_nerf) 

The height at which Primed TNT entities will be removed from the server. A value of disabled will disable this feature

hopper: 

cooldown-when-full: true[#](#hopper_cooldown_when_full) 

Instructs the server to apply a short cooldown when the hopper is full, instead of constantly trying to pull new items

disable-move-event: false[#](#hopper_disable_move_event) 

Completely disables the InventoryMoveItemEvent for hoppers. Dramatically improves hopper performance but will break protection plugins and any others that depend on this event

ignore-occluding-blocks: false[#](#hopper_ignore_occluding_blocks) 

Determines if hoppers will ignore containers inside occluding blocks, like a hopper minecart inside a sand block. Enabling this will improve performance for hoppers checking where to insert items

lootables: 

auto-replenish: false[#](#lootables_auto_replenish) 

Instructs the server to automatically replenish lootable containers. This feature is useful for long-term worlds in which players are not expected to constantly explore to generate new chunks. Breaking such lootable containers disables replenishing after their initial looting.

max-refills: -1[#](#lootables_max_refills) 

Sets the maximum number of times a lootable may be refilled. **Note**: The default value will allow a lootable to refill an infinite number of times

refresh-max: 2d[#](#lootables_refresh_max) 

The maximum amount of time that can pass before a lootable is refilled. Formatted as a duration with a single unit e.g. 10h or 25m. Supports d, h, m, and s.

refresh-min: 12h[#](#lootables_refresh_min) 

The minimum amount of time that must pass before a lootable will be eligible to be refilled. Formatted as a duration with a single unit e.g. 10h or 25m. Supports d, h, m, and s.

reset-seed-on-fill: true[#](#lootables_reset_seed_on_fill) 

Resets the loot seed each time the lootable is refilled, effectively randomizing the new loot items on each refill

restrict-player-reloot: true[#](#lootables_restrict_player_reloot) 

Prevents the same players from coming back and re-looting the same containers over and over

restrict-player-reloot-time: disabled[#](#lootables_restrict_player_reloot_time) 

Per-player cooldown between reloots. Formatted as a duration with a single unit e.g. 10h or 25m. Supports d, h, m, and s.

retain-unlooted-shulker-box-loot-table-on-non-player-break: true[#](#lootables_retain_unlooted_shulker_box_loot_table_on_non_player_break) 

Configures if breaking a shulker box via non-player means, e.g. a piston, should retain the shulker box’s loot table if the shulker box has not been looted yet. Setting this option to `false` prevents players from moving shulker boxes with potentially refilling loot tables to new locations by breaking them via the likes of pistons.

maps: 

item-frame-cursor-limit: 128[#](#maps_item_frame_cursor_limit) 

The number of cursors (markers) allowed per map. A large number of cursors may be used to lag clients

item-frame-cursor-update-interval: 10[#](#maps_item_frame_cursor_update_interval) 

The interval in ticks at which cursors on maps in item frames are updated. Setting this to a number less than 1 will disable updates altogether

max-growth-height: 

bamboo: 

max: 16[#](#max_growth_height_bamboo_max) 

Maximum height bamboo will naturally grow to

min: 11[#](#max_growth_height_bamboo_min) 

Minimum height bamboo will naturally grow to

cactus: 3[#](#max_growth_height_cactus) 

Maximum height cactus blocks will naturally grow to

reeds: 3[#](#max_growth_height_reeds) 

Maximum height sugar cane/reeds blocks will naturally grow to

misc: 

allow-remote-ender-dragon-respawning: false[#](#misc_allow_remote_ender_dragon_respawning) 

Disables an optimization which verifies that end crystals placed in the end are placed on the portal frame before any attempt is made at respawning the ender dragon. Enabling this setting allows remote ender dragon respawning to work again.

alternate-current-update-order: HORIZONTAL\_FIRST\_OUTWARD[#](#misc_alternate_current_update_order) 

Controls the order in which Alternate Current updates wires and neighboring blocks. Only has an effect when using the “ALTERNATE\_CURRENT” redstone implementation. This can be one of the following values:

* **HORIZONTAL\_FIRST\_OUTWARD**
* **HORIZONTAL\_FIRST\_INWARD**
* **VERTICAL\_FIRST\_OUTWARD**
* **VERTICAL\_FIRST\_INWARD**

disable-end-credits: false[#](#misc_disable_end_credits) 

Instructs the server to never send the end game credits when leaving the End

disable-relative-projectile-velocity: false[#](#misc_disable_relative_projectile_velocity) 

Instructs the server to ignore shooter velocity when calculating the velocity of a fired arrow

disable-sprint-interruption-on-attack: false[#](#misc_disable_sprint_interruption_on_attack) 

Determines if the server will interrupt a sprinting player if they are attacked. When set to true, you may be subject to a Vanilla bug where sprinting is stopped and started when attacking players.

legacy-ender-pearl-behavior: false[#](#misc_legacy_ender_pearl_behavior) 

Determines if the server uses legacy (pre-1.21.2) ender pearl behavior. If enabled, ender pearls will no longer load chunks and will be saved with the launching player instead of being saved as independent entities in the world.

max-leash-distance: default[#](#misc_max_leash_distance) 

Configure the maximum distance of a leash. If the distance to the leashed entity is greater, the leash will break.

redstone-implementation: VANILLA[#](#misc_redstone_implementation) 

Specifies the redstone implementation that the server uses. Alternative implementations can greatly reduce the lag caused by redstone dust by optimizing power calculations and reducing the number of block and shape updates emitted. The following implementations are available:

* **VANILLA**: The Vanilla redstone implementation.
* **EIGENCRAFT**: The Eigencraft redstone implementation by theosib.
* **ALTERNATE\_CURRENT**: The Alternate Current redstone implementation by Space Walker.

**Note:** Both the Eigencraft and Alternate Current implementations change the behavior of redstone dust. You can read about how behavior is changed in each implementation’s respective documentation:

* Eigencraft: No official documentation available. However, [theosib’s comments](https://bugs.mojang.com/browse/MC-81098?focusedCommentId=420777#comment-420777) on the Mojira bug tracker give an overview of the Eigencraft implementation.
* [Alternate Current](https://github.com/SpaceWalkerRS/alternate-current/blob/main/README.md)

show-sign-click-command-failure-msgs-to-player: false[#](#misc_show_sign_click_command_failure_msgs_to_player) 

Whether commands executed by sign click should show failure messages to players

update-pathfinding-on-block-update: true[#](#misc_update_pathfinding_on_block_update) 

Controls whether the pathfinding of mobs is updated when a block is updated in the world. Disabling this option can improve the server performance significantly, while there is almost no noticeable effect on the game mechanics. This is recommended when there are lots of entities loaded, and you have automated farms or redstone clocks

scoreboards: 

allow-non-player-entities-on-scoreboards: true[#](#scoreboards_allow_non_player_entities_on_scoreboards) 

Instructs the server to always treat non-player entities as if they are never on a team. Disabling this may slightly decrease the amount of time the server spends calculating entity collisions

use-vanilla-world-scoreboard-name-coloring: false[#](#scoreboards_use_vanilla_world_scoreboard_name_coloring) 

Instructs the server to use the Vanilla scoreboard for player nickname coloring. Useful when playing on adventure maps made for the Vanilla server and client

spawn: 

allow-using-signs-inside-spawn-protection: false[#](#spawn_allow_using_signs_inside_spawn_protection) 

Allows players to use signs while inside spawn protection

tick-rates: 

behavior: 

villager: 

validatenearbypoi: -1[#](#tick_rates_behavior_villager_validatenearbypoi) 

Sets the tick rate of the validatenearbypoi behavior. of Villager entities

<entity-type>: 

<behavior-name>: -1[#](#tick_rates_behavior__entity_type___behavior_name_) 

Sets the behavior tick rate of an entity. -1 uses Vanilla. See timings for the names. Might change between updates!

container-update: 1[#](#tick_rates_container_update) 

The rate, in ticks, at which the server updates containers and inventories. Higher values than 1 can cause item desync/ghosting or make block breaking progress appear to reset randomly. It can also create visual artifacts mimicking server lag to clients, despite this not being the case.

dry-farmland: 1[#](#tick_rates_dry_farmland) 

Controls how frequently dry farmland blocks are ticked.
Higher values slow down the rate at which farmland checks for moisture updates.
Default (1) uses Vanilla behavior, -1 disables dry farmland random ticks.

grass-spread: 1[#](#tick_rates_grass_spread) 

Sets the delay, in ticks, at which the server attempts to spread grass. Higher values will result in a slower spread

mob-spawner: 1[#](#tick_rates_mob_spawner) 

How often mob spawners should tick to calculate available spawn areas and spawn new entities into the world. A value of -1 will disable all spawners

sensor: 

villager: 

secondarypoisensor: 40[#](#tick_rates_sensor_villager_secondarypoisensor) 

Sets the tick rate of the secondarypoisensor sensor of Villager entities

<entity-type>: 

<sensor-name>: -1[#](#tick_rates_sensor__entity_type___sensor_name_) 

Sets the sensor tick rate of an entity. -1 uses Vanilla. See timings for the names. Might change between updates!

wet-farmland: 1[#](#tick_rates_wet_farmland) 

Controls how frequently wet farmland blocks are ticked.
Higher values slow down the rate at which farmland checks for moisture updates.
Default (1) uses Vanilla behavior, -1 disables wet farmland random ticks.

unsupported-settings: 

**Unsupported settings**

The following settings are provided by Paper but are not officially supported. Use them at your own risk and they may be removed at any time.

disable-world-ticking-when-empty: false[#](#unsupported_settings_disable_world_ticking_when_empty) 

Stops the ticking of the world when there are no players or force loaded chunks present in the world.

fix-invulnerable-end-crystal-exploit: true[#](#unsupported_settings_fix_invulnerable_end_crystal_exploit) 

If set to false, the creation of invulnerable end crystals will be allowed. Fixes [MC-108513](https://bugs.mojang.com/browse/MC-108513)


================================================================================
Chapter Title: bukkit.yml
Original Link: https://docs.papermc.io/paper/reference/bukkit-configuration/
================================================================================

Note

The below YAML shows you the structure and default values for `bukkit.yml`.

Click on a leaf node to view the description for that setting.

settings: 

allow-end: true[#](#settings_allow_end) 

Whether to load end-type dimensions.

warn-on-overload: true[#](#settings_warn_on_overload) 

Allows disabling the “Can’t keep up!” message.

permissions-file: permissions.yml[#](#settings_permissions_file) 

File to load server permissions from. Use of this feature has mostly been replaced by permission plugins.

update-folder: update[#](#settings_update_folder) 

Path to replace new plugin versions with. See [Updating Plugins](https://docs.papermc.io/paper/updating#step-2-update-plugins) for more information.

plugin-profiling: false[#](#settings_plugin_profiling) 

This option does not operate, as it is disabled by a Paper patch.

connection-throttle: 4000[#](#settings_connection_throttle) 

How long of a delay to enforce between connections from an IP address. Measured in milliseconds since last attempt.

query-plugins: true[#](#settings_query_plugins) 

Whether to send plugins in the GS4 Query protocol response.

deprecated-verbose: default[#](#settings_deprecated_verbose) 

Whether to warn for use of deprecated events. If “default”, the warning is printed if annotated with `@Warning(true)`. Ignored if system property [paper.alwaysPrintWarningState](https://docs.papermc.io/paper/reference/system-properties#paperalwaysprintwarningstate) is true.
Valid values are “true”, “false”, or “default”.

shutdown-message: Server closed[#](#settings_shutdown_message) 

The kick message for the player when the server shuts down.
The message is formatted with legacy ”§” style formatting.

minimum-api: none[#](#settings_minimum_api) 

Minimum plugin [api-version](https://docs.papermc.io/paper/dev/plugin-yml#api-version). A string containing the server version, from `1.13` to `1.21.11`. If below this, or not specified, the plugin is prevented from loading.

use-map-color-cache: true[#](#settings_use_map_color_cache) 

Whether to build and save mappings from RGB colors to the closest map palette color.

world-container: N/A[#](#settings_world_container) 

Specifies the path to the folder where world files are saved. By default, this is the folder where the server JAR file is located. Note: Worlds must be manually moved to this folder for the server to recognize them.

spawn-limits: 

monsters: 70[#](#spawn_limits_monsters) 

Set the spawn-limits for monsters. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_monster).

animals: 10[#](#spawn_limits_animals) 

Set the spawn-limits for animals. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_creature).

water-animals: 5[#](#spawn_limits_water_animals) 

Set the spawn-limits for water animals. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_water_creature).

water-ambient: 20[#](#spawn_limits_water_ambient) 

Set the spawn-limits for water ambient mobs. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_water_ambient).

water-underground-creature: 5[#](#spawn_limits_water_underground_creature) 

Set the spawn-limits for water underground creatures. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_underground_water_creature).

axolotls: 5[#](#spawn_limits_axolotls) 

Set the spawn-limits for axolotls. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_axolotls).

ambient: 15[#](#spawn_limits_ambient) 

Set the spawn-limits for ambient mobs. This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_spawn_limits_ambient).

chunk-gc: 

period-in-ticks: 600[#](#chunk_gc_period_in_ticks) 

How long chunks loaded by plugins should last for. Capped by Paper to be 20 ticks (1 second).

ticks-per: 

animal-spawns: 400[#](#ticks_per_animal_spawns) 

Number of ticks between each passive creature (animal) spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_creature).

monster-spawns: 1[#](#ticks_per_monster_spawns) 

Number of ticks between each hostile monster spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_monster).

water-spawns: 1[#](#ticks_per_water_spawns) 

Number of ticks between each water creature spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_water_creature).

water-ambient-spawns: 1[#](#ticks_per_water_ambient_spawns) 

Number of ticks between each ambient water mob spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_water_ambient).

water-underground-creature-spawns: 1[#](#ticks_per_water_underground_creature_spawns) 

Number of ticks between each underground water creatures spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_underground_water_creature).

axolotl-spawns: 1[#](#ticks_per_axolotl_spawns) 

Number of ticks between each axolotl spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_axolotls).

ambient-spawns: 1[#](#ticks_per_ambient_spawns) 

Number of ticks between each ambient mob spawn attempt. Set to -1 to use [the Vanilla default](https://minecraft.wiki/w/Mob_spawning#Spawn_cycle). This can be overridden by the [Paper world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_ticks_per_spawn_ambient).

autosave: 6000[#](#ticks_per_autosave) 

Number of ticks between each full auto-save. Set to -1 to disable auto-save.

aliases: now-in-commands.yml[#](#aliases) 

Static value from converting old versions to the new commands.yml format.

worlds: 

<world>: 

biome-provider: N/A[#](#worlds__world__biome_provider) 

The biome provider to use for this world. Plugins must register a `BiomeProvider` to be used here. The format is *plugin-name:extra-parameters* or *plugin-name* if no extra parameters are needed. The plugin name is as defined in the `plugin.yml` or `paper-plugin.yml`.

generator: N/A[#](#worlds__world__generator) 

The generator to use for this world. Plugins must register a `ChunkGenerator` to be used here. The format is *plugin-name:extra-parameters* or *plugin-name* if no extra parameters are needed. The plugin name is as defined in the `plugin.yml` or `paper-plugin.yml`.


================================================================================
Chapter Title: spigot.yml
Original Link: https://docs.papermc.io/paper/reference/spigot-configuration/
================================================================================

Note

The below YAML shows you the structure and default values for `spigot.yml`

Click on a leaf node to view the description for that setting.

Note

To override a per-world option, create a new key under `world-settings` with the level-name (name of the folder).

settings: 

debug: false[#](#settings_debug) 

Enables debug logging, by setting the log level to ALL.

save-user-cache-on-stop-only: false[#](#settings_save_user_cache_on_stop_only) 

If false, the server saves the user-cache on every update.

sample-count: 12[#](#settings_sample_count) 

How many players to display the names of in the player-count hover. The selected players, and their positions in the list, are randomized.

timeout-time: 60[#](#settings_timeout_time) 

Time in seconds since the last server-tick that the server is deemed not-responding by the server, and is stopped/restarted by the watchdog.

restart-on-crash: true[#](#settings_restart_on_crash) 

Whether to call `restart-script` when the server is killed by the watchdog. Note: this setting doesn’t restart the server if it gets killed externally, like by the OS.

restart-script: ./start.sh[#](#settings_restart_script) 

The script file that is run when the server restarts.

* On Windows this is passed to `cmd /c start {restart-script}`. Normally, this means specifying a Batch (\*.bat) file to be run. See Microsoft’s [documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start) for specific options.
* On other platforms, this is passed to `sh {restart-script}`. The option is interpreted as an absolute or relative path to a shell script (\*.sh). See your operating system’s documentation for more information (e.g. [Man Pages](https://man.archlinux.org/man/sh.1p#command_file)).

For more information on Spigot’s restart system, read [this](https://gist.github.com/Prof-Bloodstone/6367eb4016eaf9d1646a88772cdbbac5)

log-villager-deaths: true[#](#settings_log_villager_deaths) 

Whether to log villager deaths and witch transformations to console and latest.log

log-named-deaths: true[#](#settings_log_named_deaths) 

Whether to log deaths of entities with custom names to console and latest.log

bungeecord: false[#](#settings_bungeecord) 

Whether to enable Bungeecord support, enabling:

* Receiving forwarded player-data and source ips.
* Support for binding to unix domain sockets.

attribute: 

maxAbsorption: 

max: 2048.0[#](#settings_attribute_maxAbsorption_max) 

Overrides the maximum for the maxAbsorption attribute.

maxHealth: 

max: 1024.0[#](#settings_attribute_maxHealth_max) 

Overrides the maximum for the maxHealth attribute.

movementSpeed: 

max: 1024.0[#](#settings_attribute_movementSpeed_max) 

Overrides the maximum for the movementSpeed attribute.

attackDamage: 

max: 2048.0[#](#settings_attribute_attackDamage_max) 

Overrides the maximum for the attackDamage attribute.

netty-threads: 4[#](#settings_netty_threads) 

Sets number of netty threads.

player-shuffle: 0[#](#settings_player_shuffle) 

How often to shuffle the list of player connections, in ticks, 0 or less to disable. This prevents players from strategically re-logging to increase their position in the tick order. This can have a performance impact if enabled with low values.

user-cache-size: 1000[#](#settings_user_cache_size) 

How many players to keep in the user cache.

moved-too-quickly-multiplier: 10.0[#](#settings_moved_too_quickly_multiplier) 

Controls how fast a client can move in one packet. If triggered, the server logs to console and prevents the move.

moved-wrongly-threshold: 0.0625[#](#settings_moved_wrongly_threshold) 

Controls how far the client can move per move-packet, defined as the distance in blocks squared. If triggered, the server logs to console and prevents the move.

advancements: 

disable-saving: false[#](#advancements_disable_saving) 

Prevents saving of Advancements.

disabled: [#](#advancements_disabled)

- minecraft:story/disabled

A list of strings, each being:

* A namespace-including Advancement key, For example, “minecraft:adventure/avoid\_vibration” would disable the Sneak 100 advancement. [The Minecraft Wiki](https://minecraft.wiki/w/Advancement#List_of_advancements) has a list of all the Vanilla advancements, which need the “minecraft:” namespace prepended to them.
* The literal string ”\*”, which disables *all* Advancements.
* An Advancement key’s namespace, which disables all advancements inside it. For example, “minecraft” would disable all Vanilla advancements.

if an advancement is disabled without all of it’s children also being disabled console errors occur on load.

messages: 

whitelist: You are not whitelisted on this server![#](#messages_whitelist) 

The kick message for a player when:

* The player is unable to join as the whitelist is active.
* The player was kicked after they are removed from the whitelist, with enforce-whitelist enabled.
* The player was kicked after the whitelist enables, with enforce-whitelist enabled

The message is formatted with legacy ”&” style formatting, and “\n” for newlines.

unknown-command: Unknown command. Type "/help" for help.[#](#messages_unknown_command) 

NOTE: This setting no longer has any effect. The functionality should instead be replaced by a plugin.

server-full: The server is full![#](#messages_server_full) 

The kick message for a player when they can’t join, as the server doesn’t have any open slots (current-players >= max players)
The message is formatted with legacy ”&” style formatting, and “\n” for newlines.

outdated-client: Outdated client! Please use {0}[#](#messages_outdated_client) 

The kick for a player when they can’t join, as the server version is newer than the client version.
The message is formatted with legacy ”&” style formatting, and “\n” for newlines. Additionally, it replaces {0} with the current server version

outdated-server: Outdated server! I'm still on {0}[#](#messages_outdated_server) 

The kick for a player when they can’t join, as the server version is older than the client version.
The message is formatted with legacy ”&” style formatting, and “\n” for newlines. Additionally, it replaces {0} with the current server version

restart: Server is restarting[#](#messages_restart) 

The kick message for players on the server when it starts restarting, or if a player tries to join while the server is still restarting.
The message is formatted with legacy ”&” style formatting, and “\n” for newlines.

world-settings: 

default: 

below-zero-generation-in-existing-chunks: true[#](#world_settings_default_below_zero_generation_in_existing_chunks) 

Whether to allow conversion of existing chunks to full (post 1.18) height.

merge-radius: 

exp: -1[#](#world_settings_default_merge_radius_exp) 

The range, in blocks, that exp orbs will combine at on initial spawn. This behavior is not present in Vanilla and doesn’t impact the usual merge range once spawned. Set to 0 or less to disable.

item: 0.5[#](#world_settings_default_merge_radius_item) 

The range, in blocks, that items will combine within.

ticks-per: 

hopper-check: 1[#](#world_settings_default_ticks_per_hopper_check) 

The ticks between checks to pull items.

hopper-transfer: 8[#](#world_settings_default_ticks_per_hopper_transfer) 

The ticks between hopper item movements.

hopper-amount: 1[#](#world_settings_default_hopper_amount) 

How many items a hopper should move at a time, limited to stack size.

hopper-can-load-chunks: false[#](#world_settings_default_hopper_can_load_chunks) 

Whether to prevent hoppers from loading chunks.

hunger: 

combat-exhaustion: 0.1[#](#world_settings_default_hunger_combat_exhaustion) 

How much exhaustion to give from attacking.

jump-sprint-exhaustion: 0.2[#](#world_settings_default_hunger_jump_sprint_exhaustion) 

How much exhaustion to give from sprint jumping.

jump-walk-exhaustion: 0.05[#](#world_settings_default_hunger_jump_walk_exhaustion) 

How much exhaustion to give from jump walking.

other-multiplier: 0.0[#](#world_settings_default_hunger_other_multiplier) 

The exhaustion multiplier for normal walking and crouching.

regen-exhaustion: 6.0[#](#world_settings_default_hunger_regen_exhaustion) 

How much exhaustion to give from regenerating health.

sprint-multiplier: 0.1[#](#world_settings_default_hunger_sprint_multiplier) 

The exhaustion multiplier for sprinting on the ground.

swim-multiplier: 0.01[#](#world_settings_default_hunger_swim_multiplier) 

The exhaustion multiplier for when “swimming”. This occurs when the player is:

* actually swimming
* walking underwater (eyes below surface)
* walking on water (eyes above surface)

enable-zombie-pigmen-portal-spawns: true[#](#world_settings_default_enable_zombie_pigmen_portal_spawns) 

Whether to allow zombified piglins to spawn inside nether portals. This setting does not affect portal travel for any mobs.

zombie-aggressive-towards-villager: true[#](#world_settings_default_zombie_aggressive_towards_villager) 

Whether zombies try to seek out and attack villagers.

dragon-death-sound-radius: 0[#](#world_settings_default_dragon_death_sound_radius) 

The number of blocks that the dragon death sound is audible. Set to 0 to use the Vanilla default (64 blocks). This setting has no effect if the gamerule globalSoundEvents is set to true, which is the default.

end-portal-sound-radius: 0[#](#world_settings_default_end_portal_sound_radius) 

The number of blocks that the end portal opening sound is audible. Set to 0 to use the Vanilla default (64 blocks). This setting has no effect if the gamerule globalSoundEvents is set to true, which is the default.

hanging-tick-frequency: 100[#](#world_settings_default_hanging_tick_frequency) 

How often to tick hanging entities, in ticks.

wither-spawn-sound-radius: 0[#](#world_settings_default_wither_spawn_sound_radius) 

The number of blocks that the wither spawn sound is audible. Set to 0 to use the Vanilla default (64 blocks). This setting has no effect if the gamerule globalSoundEvents is set to true, which is the default.

item-despawn-rate: 6000[#](#world_settings_default_item_despawn_rate) 

The default time in ticks it takes an item to despawn. Per-item rates are found in Paper’s [per-world config](https://docs.papermc.io/paper/reference/world-configuration#entities_spawning_alt_item_despawn_rate).

mob-spawn-range: 8[#](#world_settings_default_mob_spawn_range) 

The range, in chunks, from the player, that mobs can spawn.

arrow-despawn-rate: 1200[#](#world_settings_default_arrow_despawn_rate) 

The number of ticks before an arrow despawns.

trident-despawn-rate: 1200[#](#world_settings_default_trident_despawn_rate) 

The number of ticks before a trident despawns.

seed-village: 10387312[#](#world_settings_default_seed_village) 

The per-structure seed for villages.

seed-desert: 14357617[#](#world_settings_default_seed_desert) 

The per-structure seed for desert structures.

seed-igloo: 14357618[#](#world_settings_default_seed_igloo) 

The per-structure seed for igloos.

seed-jungle: 14357619[#](#world_settings_default_seed_jungle) 

The per-structure seed for jungle structures.

seed-swamp: 14357620[#](#world_settings_default_seed_swamp) 

The per-structure seed for swamp structures.

seed-monument: 10387313[#](#world_settings_default_seed_monument) 

The per-structure seed for monuments.

seed-shipwreck: 165745295[#](#world_settings_default_seed_shipwreck) 

The per-structure seed for shipwrecks.

seed-ocean: 14357621[#](#world_settings_default_seed_ocean) 

The per-structure seed for the ocean structures.

seed-outpost: 165745296[#](#world_settings_default_seed_outpost) 

The per-structure seed for outposts.

seed-endcity: 10387313[#](#world_settings_default_seed_endcity) 

The per-structure seed for end cities.

seed-slime: 987234911[#](#world_settings_default_seed_slime) 

The per-structure seed for slime chunks.

seed-nether: 30084232[#](#world_settings_default_seed_nether) 

The per-structure seed for the nether structures.

seed-mansion: 10387319[#](#world_settings_default_seed_mansion) 

The per-structure seed for mansions.

seed-fossil: 14357921[#](#world_settings_default_seed_fossil) 

The per-structure seed for fossils.

seed-portal: 34222645[#](#world_settings_default_seed_portal) 

The per-structure seed for portals.

seed-ancientcity: 20083232[#](#world_settings_default_seed_ancientcity) 

The per-structure seed for ancient cities.

seed-trailruins: 83469867[#](#world_settings_default_seed_trailruins) 

The per-structure seed for trail ruins.

seed-trialchambers: 94251327[#](#world_settings_default_seed_trialchambers) 

The per-structure seed for trial chambers.

seed-buriedtreasure: 10387320[#](#world_settings_default_seed_buriedtreasure) 

The per-structure seed for buried treasure.

seed-mineshaft: default[#](#world_settings_default_seed_mineshaft) 

The per-structure seed for mineshafts.

seed-stronghold: default[#](#world_settings_default_seed_stronghold) 

The per-structure seed for strongholds.

thunder-chance: 100000[#](#world_settings_default_thunder_chance) 

The chance of lightning occurring during a thunderstorm, as a probability of 1/<thunder-chance> per chunk, every tick.

entity-activation-range: 

animals: 32[#](#world_settings_default_entity_activation_range_animals) 

The entity activation range for animals.

monsters: 32[#](#world_settings_default_entity_activation_range_monsters) 

The entity activation range for monsters.

raiders: 64[#](#world_settings_default_entity_activation_range_raiders) 

The entity activation range for raiders.

misc: 16[#](#world_settings_default_entity_activation_range_misc) 

The entity activation range for misc entities.

water: 16[#](#world_settings_default_entity_activation_range_water) 

The entity activation range for water mobs.

villagers: 32[#](#world_settings_default_entity_activation_range_villagers) 

The entity activation range for villagers.

flying-monsters: 32[#](#world_settings_default_entity_activation_range_flying_monsters) 

The entity activation range for flying monsters.

wake-up-inactive: 

animals-every: 1200[#](#world_settings_default_entity_activation_range_wake_up_inactive_animals_every) 

How often an inactive animal outside of range will be woken up, in ticks. This is a minimum due to being limited to animals-max-per-tick.

animals-for: 100[#](#world_settings_default_entity_activation_range_wake_up_inactive_animals_for) 

How long to wake an inactive animal up for, in ticks.

animals-max-per-tick: 4[#](#world_settings_default_entity_activation_range_wake_up_inactive_animals_max_per_tick) 

A limit of how many inactive animals can be woken up on the same tick.

flying-monsters-every: 200[#](#world_settings_default_entity_activation_range_wake_up_inactive_flying_monsters_every) 

How often an inactive flying monster outside of range will be woken up, in ticks. This is a minimum due to being limited to flying-monsters-max-per-tick.

flying-monsters-for: 100[#](#world_settings_default_entity_activation_range_wake_up_inactive_flying_monsters_for) 

How long to wake an inactive flying monster up for, in ticks.

flying-monsters-max-per-tick: 8[#](#world_settings_default_entity_activation_range_wake_up_inactive_flying_monsters_max_per_tick) 

A limit of how many inactive flying monsters can be woken up on the same tick.

monsters-every: 400[#](#world_settings_default_entity_activation_range_wake_up_inactive_monsters_every) 

How often an inactive monster outside of range will be woken up, in ticks. This is a minimum due to being limited to monsters-max-per-tick.

monsters-for: 100[#](#world_settings_default_entity_activation_range_wake_up_inactive_monsters_for) 

How long to wake an inactive monster up for, in ticks.

monsters-max-per-tick: 8[#](#world_settings_default_entity_activation_range_wake_up_inactive_monsters_max_per_tick) 

A limit of how many inactive monsters can be woken up on the same tick.

villagers-every: 600[#](#world_settings_default_entity_activation_range_wake_up_inactive_villagers_every) 

How often an inactive villager outside of range will be woken up, in ticks. This is a minimum due to being limited to villagers-max-per-tick

villagers-for: 100[#](#world_settings_default_entity_activation_range_wake_up_inactive_villagers_for) 

How long to wake an inactive villager up for, in ticks.

villagers-max-per-tick: 4[#](#world_settings_default_entity_activation_range_wake_up_inactive_villagers_max_per_tick) 

A limit of how many inactive villagers can be woken up on the same tick.

villagers-work-immunity-after: 100[#](#world_settings_default_entity_activation_range_villagers_work_immunity_after) 

The time in ticks a villager has to be inactive and working to be woken up.

villagers-work-immunity-for: 20[#](#world_settings_default_entity_activation_range_villagers_work_immunity_for) 

How long a villager should be woken up for, in ticks, after villagers-work-immunity-after.

villagers-active-for-panic: true[#](#world_settings_default_entity_activation_range_villagers_active_for_panic) 

Whether to activate villagers when they want to panic.

tick-inactive-villagers: true[#](#world_settings_default_entity_activation_range_tick_inactive_villagers) 

Whether to keep ticking villagers that are outside of their activation range.

ignore-spectators: false[#](#world_settings_default_entity_activation_range_ignore_spectators) 

Whether spectators activate entities within range.

nerf-spawner-mobs: false[#](#world_settings_default_nerf_spawner_mobs) 

Disable most AI for spawner spawned mobs.

unload-frozen-chunks: false[#](#world_settings_default_unload_frozen_chunks) 

Experimental option that controls whether chunks can unload whilst ticks are frozen via /tick freeze.

entity-tracking-range: 

players: 128[#](#world_settings_default_entity_tracking_range_players) 

Controls how far in blocks players are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

animals: 96[#](#world_settings_default_entity_tracking_range_animals) 

Controls how far in blocks animals are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

monsters: 96[#](#world_settings_default_entity_tracking_range_monsters) 

Controls how far in blocks monsters are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

misc: 96[#](#world_settings_default_entity_tracking_range_misc) 

Controls how far in blocks misc entities are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

display: 128[#](#world_settings_default_entity_tracking_range_display) 

Controls how far in blocks display entities are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

other: 64[#](#world_settings_default_entity_tracking_range_other) 

Controls how far in blocks other entities are tracked (sent to) the player. This is scaled by the [entity-broadcast-range-percentage](https://docs.papermc.io/paper/reference/server-properties#entity_broadcast_range_percentage).

growth: 

cactus-modifier: 100[#](#world_settings_default_growth_cactus_modifier) 

The growth modifier percentage for cactus, where Vanilla speed is 100%. This option is unable to disable growth at 0, instead defaulting to 100%
The maximum effectiveness is 1600%.

cane-modifier: 100[#](#world_settings_default_growth_cane_modifier) 

The growth modifier percentage for sugarcane, where Vanilla speed is 100%. This option is unable to disable growth at 0%, instead defaulting to 100%
The maximum effectiveness is 1600%.

melon-modifier: 100[#](#world_settings_default_growth_melon_modifier) 

The growth modifier percentage for melons, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

mushroom-modifier: 100[#](#world_settings_default_growth_mushroom_modifier) 

The growth modifier percentage for mushrooms, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 2500%

pumpkin-modifier: 100[#](#world_settings_default_growth_pumpkin_modifier) 

The growth modifier percentage for pumpkins, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

sapling-modifier: 100[#](#world_settings_default_growth_sapling_modifier) 

The growth modifier percentage for saplings, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 700%

beetroot-modifier: 100[#](#world_settings_default_growth_beetroot_modifier) 

The growth modifier percentage for beetroot, where Vanilla speed is 100%. This option is unable to disable growth at 0%, instead defaulting to 100%
The maximum effectiveness is 5100%.

carrot-modifier: 100[#](#world_settings_default_growth_carrot_modifier) 

The growth modifier percentage for carrots, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%.

potato-modifier: 100[#](#world_settings_default_growth_potato_modifier) 

The growth modifier percentage for potatoes, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

torchflower-modifier: 100[#](#world_settings_default_growth_torchflower_modifier) 

The growth modifier percentage for torchflowers, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

wheat-modifier: 100[#](#world_settings_default_growth_wheat_modifier) 

The growth modifier percentage for wheat, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

netherwart-modifier: 100[#](#world_settings_default_growth_netherwart_modifier) 

The growth modifier percentage for netherwart, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 1000%

vine-modifier: 100[#](#world_settings_default_growth_vine_modifier) 

The growth modifier percentage for vines, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 400%

cocoa-modifier: 100[#](#world_settings_default_growth_cocoa_modifier) 

The growth modifier percentage for cocoa beans, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 500%

bamboo-modifier: 100[#](#world_settings_default_growth_bamboo_modifier) 

The growth modifier percentage for bamboo, where Vanilla speed is 100%. This option is unable to disable growth at 0%, instead defaulting to 100%
The maximum effectiveness is 300%.

sweetberry-modifier: 100[#](#world_settings_default_growth_sweetberry_modifier) 

The growth modifier percentage for sweet-berries, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 500%

kelp-modifier: 100[#](#world_settings_default_growth_kelp_modifier) 

The growth modifier percentage for kelp, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is roughly 715%

twistingvines-modifier: 100[#](#world_settings_default_growth_twistingvines_modifier) 

The growth modifier percentage for twisting-vines, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 1000%

weepingvines-modifier: 100[#](#world_settings_default_growth_weepingvines_modifier) 

The growth modifier percentage for weeping-vines, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 1000%

cavevines-modifier: 100[#](#world_settings_default_growth_cavevines_modifier) 

The growth modifier percentage for cave-vines, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 1000%

glowberry-modifier: 100[#](#world_settings_default_growth_glowberry_modifier) 

The growth modifier percentage for glow-berries, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is roughly 910%

pitcherplant-modifier: 100[#](#world_settings_default_growth_pitcherplant_modifier) 

The growth modifier percentage for pitcherplants, where Vanilla speed is 100%. This option is unable to disable growth, instead defaulting to 100%
The maximum effectiveness is 5100%

max-tick-time: 

tile: 50[#](#world_settings_default_max_tick_time_tile) 

This option does not operate, as it is disabled by a Paper patch.

entity: 50[#](#world_settings_default_max_tick_time_entity) 

This option does not operate, and is non-functional upstream.

max-tnt-per-tick: 100[#](#world_settings_default_max_tnt_per_tick) 

How many TNT to process per server tick. Set to 0 or less to disable.

view-distance: default[#](#world_settings_default_view_distance) 

Overrides the view distance. Set to -1 or “default” to use the value in [server.properties](https://docs.papermc.io/paper/reference/server-properties#view_distance)

simulation-distance: default[#](#world_settings_default_simulation_distance) 

Overrides the simulation distance. Set to -1 or “default” to use the value in [server.properties](https://docs.papermc.io/paper/reference/server-properties#simulation_distance).

verbose: false[#](#world_settings_default_verbose) 

Whether to log world settings when the configuration file is loaded. This normally occurs on startup, `/spigot reload`, and `/reload`.

players: 

disable-saving: false[#](#players_disable_saving) 

Prevents saving player data.

config-version: ""[#](#config_version) 

Internal constant for upgrading configuration: **Do Not Touch**.

stats: 

disable-saving: false[#](#stats_disable_saving) 

Whether to prevent saving stats.

forced-stats: {}[#](#stats_forced_stats) 

An Object, where:

* The Keys inside are any “Resource location” from [The Minecraft Wiki](https://minecraft.wiki/w/Statistics#List_of_custom_statistic_names).
* The Value for each key is an integer to force the related stat to.

commands: 

tab-complete: 0[#](#commands_tab_complete) 

How many characters need to be typed before commands tab-complete.  
< 0 — Tab-completion is disabled.   
 = 0 — Always tab-complete all available commands.   
 > 0 — Only tab-complete commands after n characters are typed. This behaves as 0 due to client changes.

send-namespaced: true[#](#commands_send_namespaced) 

Whether to send commands with a namespace (like minecraft:give) to the client.

log: true[#](#commands_log) 

Whether to log commands executed by players, in chat or on signs. This *currently* logs in the format “<playername> issued server command: <command>”.

replace-commands: [#](#commands_replace_commands)

- setblock
- summon
- testforblock
- tellraw

List of Vanilla commands that should override any plugin commands.

spam-exclusions: [#](#commands_spam_exclusions)

- /skill

Any chat message or command that prefix matches an entry in this list will be excluded from the built-in spam filter.
Commands need a ”/” to be counted as commands.

silent-commandblock-console: false[#](#commands_silent_commandblock_console) 

Whether to log Vanilla command feedback to the Console.

enable-spam-exclusions: false[#](#commands_enable_spam_exclusions) 

Whether to apply spam exclusions from [`commands.spam-exclusions`](#commands_spam_exclusions).


================================================================================
Chapter Title: commands.yml
Original Link: https://docs.papermc.io/paper/reference/bukkit-commands-configuration/
================================================================================

Note

The below YAML shows you the structure and default values for the legacy `commands.yml`.

Click on a leaf node to view the description for that setting.

Caution

The aliases defined in this legacy file do not support modern features, such as:

* Tab completion
* Permissions

command-block-overrides: [#](#command_block_overrides)

- <command to override>

Which Vanilla commands should be prioritized over those provided by Bukkit or plugins. Useful for compatibility with adventure maps built for Vanilla command blocks.
Use the literal ”\*” to always use the Vanilla version in command blocks.
By default, no commands are overridden.

ignore-vanilla-permissions: false[#](#ignore_vanilla_permissions) 

Whether to use Vanilla permission levels when executing commands.

aliases: 

icanhasbukkit: [#](#aliases_icanhasbukkit)

- version $1-

A built-in alias. Set aliases to an empty list ([]) to persistently remove.

<alias name>: [#](#aliases__alias_name_)

- <commands to run>

A list of strings which are target commands. Alternatively, a string, which is a single target command.
A target command is a command that is run, when the alias is run.
Replacements:

* `$sender` is replaced with the command sender”s name (Added by Paper).
* `$<n>` is replaced by the n”th argument, 1-indexed.
* `$$<n>` is replaced by the n”th argument, 1-indexed, failing if the n”th argument is not present.
* `$<n>-` is replaced by the n”th argument and everything that follows, 1-indexed.
* `$$<n>-` is replaced by the n”th argument and everything that follows, 1-indexed, failing if the n”th argument is not present.

Each alias registered cannot (easily) be overridden by a plugin.


================================================================================
Chapter Title: permissions.yml
Original Link: https://docs.papermc.io/paper/reference/bukkit-permissions-configuration/
================================================================================

Note

The below YAML shows you the structure for `permissions.yml`.

Click on a leaf node to view the description for that setting.

Caution

This is NOT a replacement for a permissions plugin.

This file is used to define metadata about permissions themselves, including a description and a default value.

<permission>: 

default: op[#](#_permission__default) 

Who this permission is granted to by default.

“true”: all players.

“false”: no players.

“op”: only operators (also aliased as “isop”, “operator”, “isoperator”, “admin”, and “isadmin”).

“!op”: all players except operators (also aliased as “notop”, “!operator”, “notoperator”, “!admin”, “notadmin”).

children: 

A list (not shown) or a map (shown below) of child permissions.

<permission>: true[#](#_permission__children__permission_) 

A child permission of this permission.

The value is either a boolean, where false inverts the whether the permission would be granted to this.

or a top level permission entry,
except the default is this parent permissions default value,
and any child permissions of the newly created permission are bubbled up to the top level.

description: ""[#](#_permission__description_) 

The description of the permission.


================================================================================
Chapter Title: help.yml
Original Link: https://docs.papermc.io/paper/reference/bukkit-help-configuration/
================================================================================

Note

The below YAML shows you the structure for `help.yml`.

Click on a leaf node to view the description for that setting.

general-topics: 

<topic name>: 

A custom help “topic” to show when the user types “`/help <topic>`”.

shortText: ""[#](#general_topics__topic_name__shortText) 

The first line of the help entry, used as a summary in index pages.

This is formatted with legacy ”&” style formatting.

fullText: ""[#](#general_topics__topic_name__fullText) 

The remaining lines of this help entry.

This is formatted with legacy ”&” style formatting.

permission: ""[#](#general_topics__topic_name__permission) 

The permission required to view this help entry.

If this is empty/not set, the entry does not require a permission.

index-topics: 

<topic name>: 

A composite help topic index.

If the topic name is the special value “Default”,
it will override the automatically generated index used for /help with no arguments.

shortText: ""[#](#index_topics__topic_name__shortText) 

The short text used in other index topics.

This is not displayed when showing this topic itself.

This is formatted with legacy ”&” style formatting.

preamble: ""[#](#index_topics__topic_name__preamble) 

Information to show before the index.

This is formatted with legacy ”&” style formatting.

permission: ""[#](#index_topics__topic_name__permission) 

A custom permission required to view this help entry.

If this is empty/not set, the entry does not require a permission.

commands: [][#](#index_topics__topic_name__commands) 

What to show in the index.

This is a list of commands, or other help topics.

They will be displayed in the order they are listed here
in “topic name: short text” format.

Each entry is a maximum of 1 minimum-width chat line (55 chars).

amended-topics: 

<topic name>: 

shortText: ""[#](#amended_topics__topic_name__shortText) 

A replacement for the short text of the topic.

If this is empty/not set, the original short text is used.

If this contains the literal string `<text>`, it will be replaced with the original short text.

This is formatted with legacy ”&” style formatting.

fullText: ""[#](#amended_topics__topic_name__fullText) 

A replacement for the full text of the topic.

If this is empty/not set, the original full text is used.

If this contains the literal string `<text>`, it will be replaced with the original full text.

This is formatted with legacy ”&” style formatting.

permission: ""[#](#amended_topics__topic_name__permission) 

Overrides the permission required to view this help entry.

If this is empty/not set, the original permission is NOT used, instead no permission is required.

ignore-plugins: [][#](#ignore_plugins) 

A list of plugins to ignore when generating help topics for registered commands.

If “All” is included, all plugins are ignored.

If the special plugin name “Bukkit” is included, all commands registered by Bukkit are ignored.

command-topics-in-master-index: true[#](#command_topics_in_master_index) 

Whether to allow command topics (topics starting with a `/`) to be shown in the main index.

This is the index shown when the user types “`/help`” or “`/help <page>`”.
Command alias topics are always hidden.


================================================================================
Chapter Title: server.properties
Original Link: https://docs.papermc.io/paper/reference/server-properties/
================================================================================

Note

The below page shows the settings and default values for the `server.properties` file.

Click on a property to learn more about it.

accept-transfers=false[#](#accept_transfers) 

Whether this server accepts transfers from other servers using the transfer command/packet. If this is set to false, the server will disconnect the client.

allow-flight=false[#](#allow_flight) 

Means that users will not be kicked if they fly whilst in Survival mode. This is likely to occur through hacking however there can be false positives.

broadcast-console-to-ops=true[#](#broadcast_console_to_ops) 

Send console command output to all online operators.

broadcast-rcon-to-ops=true[#](#broadcast_rcon_to_ops) 

Send rcon command output to all online operators.

bug-report-link=[#](#bug_report_link) 

A URL value used for the Report Server Bugs button in the Server Links client menu.

debug=false[#](#debug) 

Enables the server’s debug mode.

difficulty=easy[#](#difficulty) 

Defines the difficulty of the server. (Allowed values: “peaceful”, “easy”, “normal”, “hard”)

enable-code-of-conduct=false[#](#enable_code_of_conduct) 

Whether the server will look for code of conduct files in the codeofconduct subfolder in the server folder.
Each file in the folder should have the form <language\_code>.txt. The server will then show the code of conduct matching the player’s language. If the language doesn’t exist, then en\_us will be used. If neither exist, an arbitrary available entry will be used instead.

enable-jmx-monitoring=false[#](#enable_jmx_monitoring) 

Exposes an MBean with the Object name “net.minecraft.server:type=Server” and two attributes “averageTickTime” and “tickTimes” exposing the tick times in milliseconds. In order for enabling JMX on the Java runtime you also need to add a couple of JVM flags to the startup as documented [here](https://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html)

enable-query=false[#](#enable_query) 

Enables GameSpy4 protocol server listener. Used to get information about server.

enable-rcon=false[#](#enable_rcon) 

Enables remote access to the server console.

enable-status=true[#](#enable_status) 

Makes the server appear on the server list and also enables listener for getting server information. If turned off, server will appear offline but players will still be able to connect.

enforce-secure-profile=true[#](#enforce_secure_profile) 

If set to true, players without a Mojang-signed public key will not be able to connect to the server.

enforce-whitelist=false[#](#enforce_whitelist) 

If set to true, the server will kick players who are not on the whitelist.

entity-broadcast-range-percentage=100[#](#entity_broadcast_range_percentage) 

Controls how close entities need to be before being sent to clients. Higher values means they”ll be rendered from farther away, potentially causing more lag. This is expressed the percentage of the default value. For example, setting to 50 will make it half as usual. This mimics the function on the client video settings (not unlike Render Distance, which the client can customize so long as it”s under the server”s setting). This must be between 10 and 1000 percent.

force-gamemode=false[#](#force_gamemode) 

Force players to join in the default game mode. This will reset their previous game mode when they reconnect.

function-permission-level=2[#](#function_permission_level) 

Sets the default permission level for functions. (Allowed values: 1, 2, 3, 4)

gamemode=survival[#](#gamemode) 

Defines the mode of gameplay. (Allowed values: “survival”, “creative”, “adventure”, “spectator”)

generate-structures=true[#](#generate_structures) 

Defines whether structures (such as villages) will be generated.

generator-settings={}[#](#generator_settings) 

The settings used to customize world generation. Follow [its format](https://minecraft.wiki/w/Java_Edition_level_format#generatorOptions_tag_format) and write the corresponding JSON string.

hardcore=false[#](#hardcore) 

If set to true, players will be set to spectator mode if they die.

hide-online-players=false[#](#hide_online_players) 

Hides the player list sent with the status request packets.

initial-disabled-packs=[#](#initial_disabled_packs) 

Comma-separated list of datapacks to not be auto-enabled on world creation.

initial-enabled-packs=vanilla[#](#initial_enabled_packs) 

Comma-separated list of datapacks to be enabled during world creation. Feature packs need to be explicitly enabled.

level-name=world[#](#level_name) 

The name of the world. This will be the name of the folder in which the world is saved.

level-seed=[#](#level_seed) 

The seed used to generate the world. Leave blank to default to random.

level-type=minecraft:normal[#](#level_type) 

Defines the type of the world generator. (Allowed values: “normal”, “flat”, “large\_biomes”, “amplified”, “single\_biome\_surface”, “buffet”, “default\_1\_1”, “customized”)

log-ips=true[#](#log_ips) 

Whether player IP addresses should be logged by the server. This does not impact the ability of plugins to log the IP addresses of players

management-server-enabled=false[#](#management_server_enabled) 

Whether the [Minecraft Server Management Protocol](https://minecraft.wiki/w/Minecraft_Server_Management_Protocol) is enabled.

management-server-host=localhost[#](#management_server_host) 

Controls the host that the Minecraft Server Management Protocol is started.

management-server-port=0[#](#management_server_port) 

Controls the port that the Minecraft Server Management Protocol is started on.

management-server-secret=[#](#management_server_secret) 

Allows for clients to supply an Authorization header with a server specific secret, which is forty alphanumeric characters long (A-Z, a-z, and 0-9).
The secret is automatically generated if the property is left empty.

management-server-tls-enabled=true[#](#management_server_tls_enabled) 

Controls whether the Minecraft Server Management Protocol uses TLS (Transport Layer Security).

management-server-tls-keystore=[#](#management_server_tls_keystore) 

Controls the path to the keystore file used for TLS.
A server will not start when TLS is enabled and no keystore is provided.

management-server-tls-keystore-password=[#](#management_server_tls_keystore_password) 

Controls the password to the keystore file used for TLS.
The password can be done through an environment variable (MINECRAFT\_MANAGEMENT\_TLS\_KEYSTORE\_PASSWORD), a Java Virtual Machine argument (-Dmanagement.tls.keystore.password=), or through this server property.

max-chained-neighbor-updates=1000000[#](#max_chained_neighbor_updates) 

Limits the number of consecutive neighbor updates before skipping subsequent updates. Negative values will disable the limit.

max-players=20[#](#max_players) 

The maximum number of players that can play on the server at the same time.

max-tick-time=60000[#](#max_tick_time) 

The maximum number of milliseconds a single tick may take before the server watchdog stops the server with the message. If a single server tick took 60.00 seconds (should be max 0.05) it will be considered to be crashed and the server will forcibly shutdown via calling System.exit(1). Setting this to -1 will disable watchdog entirely.

max-world-size=29999984[#](#max_world_size) 

The maximum allowed size of the world radius, in blocks. This only affects the chunks that are generated when the world is initially created, and not the world border (Limited to 29999984).

motd=A Minecraft Server[#](#motd) 

The message of the day, displayed in the server list.

network-compression-threshold=256[#](#network_compression_threshold) 

The number of bytes of a packet before it is compressed. Setting to a negative disables compression.

online-mode=true[#](#online_mode) 

If set to true, the server checks all connecting players against Minecraft”s account database. This requires all connected players to have a valid Minecraft account and makes it impossible for cracked players to connect.

op-permission-level=4[#](#op_permission_level) 

Sets the default permission level for ops when using /op. (Allowed values: 0, 1, 2, 3, 4)

pause-when-empty-seconds=-1[#](#pause_when_empty_seconds) 

How many seconds have to pass after no player has been online before the server is paused. This is disabled by default because it is incompatible with what plugins expect and might do with no players online.

player-idle-timeout=0[#](#player_idle_timeout) 

If non-zero, players are kicked from the server if they are idle for more than that many minutes. (Default: 0). The following packets stop this timer: “Click Window”, “Enchant Item”, “Update Sign”, “Player Digging”, “Player Block Placement”, “Held Item Change”, “Animation (swing arm)”, “Entity Action”, “Client Status”, “Chat Message”, “Use Entity”.

prevent-proxy-connections=false[#](#prevent_proxy_connections) 

If the ISP/AS sent from the server is different from the one from Mojang Studios” authentication server, the player not allowed to join the server.

query.port=25565[#](#query.port) 

The port for the query server. This is used to get information about the server.

rate-limit=0[#](#rate_limit) 

Sets the maximum allowed number of packets that can be sent before getting kicked. Setting this to 0 disables the limit.

rcon.password=[#](#rcon.password) 

The password for the rcon server.

rcon.port=25575[#](#rcon.port) 

The port to start the rcon server on.

region-file-compression=deflate[#](#region_file_compression) 

Specifies the compression type used to compress region files. Possible values are: “deflate”, “lz4” and “none”. If set to “none”, region files will take up significantly more disk space, but it might make sense together with filesystem-level compression.

require-resource-pack=false[#](#require_resource_pack) 

If true, a player must have the given resource pack to connect. They will be kicked if they do not have it.

resource-pack=[#](#resource_pack) 

The URL to the server’s resource pack.

resource-pack-id=[#](#resource_pack_id) 

The UUID of the server resource pack to use.

resource-pack-prompt=[#](#resource_pack_prompt) 

The message that is displayed when the client is prompted to download the resource pack.

resource-pack-sha1=[#](#resource_pack_sha1) 

The hash of the resource pack, used for verification. This is recommended to be set to ensure players are downloading the correct pack.

server-ip=[#](#server_ip) 

The IP address to bind to. Leave blank to bind to all interfaces.

server-port=25565[#](#server_port) 

The port to listen on for connections.

simulation-distance=10[#](#simulation_distance) 

Sets the maximum distance from players that living entities may be located in order to be updated by the server, measured in chunks in each direction of the player (radius, not diameter). If entities are outside this radius, then they will not be ticked by the server nor will they be visible to players. Must be between 3 and 32 inclusive.

spawn-protection=16[#](#spawn_protection) 

Used to determine the side length of the spawn protection. The formula of 2x+1 is used. A value of 1 will result in a side length of 3 **blocks**. Setting this to 0 will disable spawn protection. There must be at least 1 operator to be enabled.

status-heartbeat-interval=0[#](#status_heartbeat_interval) 

Controls the intervals in which the management server sends heartbeat notifications to connected clients. It is disabled by default.

sync-chunk-writes=true[#](#sync_chunk_writes) 

Enables synchronous writing of chunk data. Has no effect on Paper by default, unless the corresponding system property is also set to true.
See [the system properties reference](https://docs.papermc.io/paper/reference/system-properties#paperenable-sync-chunk-writes).

text-filtering-config=[#](#text_filtering_config) 

The path to the text filtering configuration file. Leave blank to disable text filtering.

text-filtering-version=0[#](#text_filtering_version) 

The version of the configuration format used for [`text-filtering-config`](#text_filtering_config).
Valid values are 0 and 1.

use-native-transport=true[#](#use_native_transport) 

Provides a performance boost for Linux servers.

view-distance=10[#](#view_distance) 

Sets the amount of world data the server sends the client, measured in chunks in each direction of the player (radius, not diameter). It determines the server-side viewing distance (Default: 10, Min: 3, Max: 32).

white-list=false[#](#white_list) 

Enables a whitelist on the server. If enabled, the server will only allow selected users to connect.


================================================================================
Chapter Title: Vanilla data files
Original Link: https://docs.papermc.io/paper/reference/vanilla-data-files/
================================================================================

## `eula.txt`

[Section titled “eula.txt”](#eulatxt)

`eula.txt` is a simple config file that allows you to accept the [EULA](https://aka.ms/MinecraftEULA),
which is required to run the Minecraft server.

#By changing the setting below to TRUE you are indicating your agreement to our EULA (<https://aka.ms/MinecraftEULA>).

#<date>

eula=false[#](#eula_eula) 

Whether to accept the Minecraft EULA. This must be set to “true” to run the server.

## `banned-ips.json`

[Section titled “banned-ips.json”](#banned-ipsjson)

`banned-ips.json` is a JSON file that stores IP addresses that are not allowed to connect to the server.

Caution

This is a data file used by the server, not a configuration file.

We do not recommend editing this file directly, and this is provided for reference only.

Instead, use the `/ban-ip`, `/pardon-ip`, and `/banlist ips` commands to manage banned-ips.json.

{

This is a single entry in the root array found in banned-ips.json.

"ip": an IPv4 or IPv6 address,[#](#banned_ips_ip) 

The IP address representing the banned user.

For IPv4 the expected format is “x.x.x.x”,

For IPv6 the expected format follows [RFC5952 Section 4](https://datatracker.ietf.org/doc/html/rfc5952#section-4),

For anything else, “<unknown>” may be present (but its use is discouraged).

"created": the ban creation time,[#](#banned_ips_created) 

A timestamp of when the user was banned.
The expected format is “yyyy-MM-dd HH:mm:ss Z”.

"source": "(Unknown)",[#](#banned_ips_source) 

A string representing the source of the ban.

"expires": "forever",[#](#banned_ips_expires) 

A timestamp of when the ban expires, or “forever” if it does not expire.

The expected format is “yyyy-MM-dd HH:mm:ss Z”.

"reason": "Banned by an operator."[#](#banned_ips_reason) 

The reason for the ban.

}

## `banned-players.json`

[Section titled “banned-players.json”](#banned-playersjson)

`banned-players.json` is a JSON file that stores players that are not allowed to connect to the server.

Caution

This is a data file used by the server, not a configuration file.

We do not recommend editing this file directly, and this is provided for reference only.

Instead, use the `/ban`, `/pardon`, and `/banlist players` commands to manage banned-players.json.

{

This is a single entry in the root array found in banned-players.json.

"uuid": the UUID of the banned user,[#](#banned_players_uuid) 

The UUID representing the banned user.

"name": the name of the banned user,[#](#banned_players_name) 

The name of the banned user.

"created": the ban creation time,[#](#banned_players_created) 

A timestamp of when the user was banned.
The expected format is “yyyy-MM-dd HH:mm:ss Z”.

"source": "(Unknown)",[#](#banned_players_source) 

A string representing the source of the ban.

"expires": "forever",[#](#banned_players_expires) 

A timestamp of when the ban expires, or “forever” if it does not expire.

The expected format is “yyyy-MM-dd HH:mm:ss Z”.

"reason": "Banned by an operator."[#](#banned_players_reason) 

The reason for the ban.

}

## `ops.json`

[Section titled “ops.json”](#opsjson)

`ops.json` is a JSON file that stores player’s operator status information.

In Vanilla, this is used as a rudimentary permissions system, and to allow certain player to bypass the player limit.

Caution

This is a data file used by the server, not a configuration file.

We do not recommend editing this file directly, and this is provided for reference only.

Instead, use the `/op`, `/deop` commands to manage ops.json.

{

This is a single entry in the root array found in ops.json.

"uuid": the UUID of the operator,[#](#ops_uuid) 

The UUID representing the operator.

"name": the name of the operator,[#](#ops_name) 

The name of the operator.

"level": 0,[#](#ops_level) 

The level of the operator permissions.

The expected format is an integer between 0 and 4.

"bypassesPlayerLimit": false[#](#ops_bypassesPlayerLimit) 

Whether this operator bypasses the player limit.

}

## `whitelist.json`

[Section titled “whitelist.json”](#whitelistjson)

`whitelist.json` is a JSON file that stores players that are allowed to connect to the server.

It is used in conjunction with the [`white-list`](https://docs.papermc.io/paper/reference/server-properties#white_list) option in `server.properties`.

Caution

This is a data file used by the server, not a configuration file.

We do not recommend editing this file directly, and this is provided for reference only.

Instead, use the `/whitelist` command to manage whitelist.json.

{

This is a single entry in the root array found in whitelist.json.

"uuid": the UUID of the player on the whitelist,[#](#whitelist_uuid) 

The UUID of the player on the whitelist.

"name": the name of the player on the whitelist[#](#whitelist_name) 

The name of the player on the whitelist.

}


================================================================================
Chapter Title: Paper plugins
Original Link: https://docs.papermc.io/paper/reference/paper-plugins/
================================================================================

This documentation page serves to explain all the new semantics and possible confusions that Paper plugins may introduce.

Note

Developers can get more information on Paper plugins [here](https://docs.papermc.io/paper/dev/getting-started/paper-plugins).

## What are they?

[Section titled “What are they?”](#what-are-they)

Paper plugins are plugins which are loaded by Paper’s new plugin loading framework. Paper plugins are used by developers to
take advantage of modern systems Mojang provides, for example, datapacks.

![Plugin List](https://docs.papermc.io/_astro/plugin-list.xu6gSgcJ_16YTyX.webp)

## What is the difference?

[Section titled “What is the difference?”](#what-is-the-difference)

When enabled, Paper plugins are **identical** to Bukkit plugins. This allows plugins to still fully communicate and support each other, meaning that even if a
plugin is a Bukkit or Paper plugin, they are both able to depend on each other just fine.

Paper plugins only support being loaded by Paper’s Plugin Loader and may use new API unavailable to Bukkit plugins.

### How do I add Paper plugins?

[Section titled “How do I add Paper plugins?”](#how-do-i-add-paper-plugins)

Paper plugins are added the same as Bukkit plugins, therefore, you can follow [this guide](https://docs.papermc.io/paper/adding-plugins).

### Cyclic plugin loading

[Section titled “Cyclic plugin loading”](#cyclic-plugin-loading)

With the introduction of Paper plugins, Paper introduces a new plugin loader that fixes some odd issues.
However, as a result, this now causes [cyclic loading](https://docs.papermc.io/paper/dev/getting-started/paper-plugins#cyclic-plugin-loading) between plugins to no longer be supported.

If Paper detects a loop, your server will be shut down with an error.

Legacy

If your server **requires** this circular loading, you can enable this by adding the [`-Dpaper.useLegacyPluginLoading=true`](https://docs.papermc.io/paper/reference/system-properties#paperuselegacypluginloading) startup flag.
Please note that this may not be supported in the future.


================================================================================
Chapter Title: Commands
Original Link: https://docs.papermc.io/paper/reference/commands/
================================================================================

This page explains all commands which are added by Paper.

## Bukkit commands

[Section titled “Bukkit commands”](#bukkit-commands)

These commands are located under the `bukkit:` namespace.

### version (aliases: ver, about)

[Section titled “version (aliases: ver, about)”](#version-aliases-ver-about)

The version command displays the version information about the server, the output may look like this:

![](https://docs.papermc.io/_astro/version-command-output.CXwsIEmE_ZIMbhf.webp)

You can also use this command to display version information about specific plugins.

![](https://docs.papermc.io/_astro/plugin-version-command-output.DeCQ1chK_1YJfMx.webp)

### plugins (alias: pl)

[Section titled “plugins (alias: pl)”](#plugins-alias-pl)

The plugins command displays the list of all loaded plugins. Paper differentiates between two types of
plugins: **Paper plugins** and **Bukkit plugins**. The difference is generally only relevant to plugin
developers ([guide to paper-plugin.yml](https://docs.papermc.io/paper/dev/getting-started/paper-plugins)). Plugins are marked
as **green** if no issues occurred whilst enabling them and their functionality can be assumed working.
Plugins marked **red** failed to load or were disabled. Check the startup logs for more information if
that happens.

Bukkit plugins furthermore have the possibility of being loaded **with legacy support** enabled. These
are marked with a **yellow star** in front of their name. That usually means the plugin was made for a
very old version of the game or the plugin author simply forgot to specify a target Minecraft version
for their plugin.

You can click on the plugins’ names to display version information about that plugin. The click action
is equivalent to running `/version <plugin_name>`.

![](https://docs.papermc.io/_astro/plugins-command-output.lz1W5qbT_ZsjqxE.webp)

### help (alias: ?)

[Section titled “help (alias: ?)”](#help-alias)

The help command displays descriptions for all registered commands. It acts
as a quick reference to both built-in commands and any plugin-added commands.

### reload (alias: spigot reload)

[Section titled “reload (alias: spigot reload)”](#reload-alias-spigot-reload)

Deprecation

The reload command is deprecated for removal. You should instead restart your server
if you wish to update your plugins, as the reload is known for causing issues with plugins.

If you are looking to reload the Paper configs, you can use [/paper reload](#reload).

## Performance profiling

[Section titled “Performance profiling”](#performance-profiling)

The `/mspt` and `/tps` commands, whilst working fine, are superseded by the `/spark` command,
and you should therefore switch to the `/spark` command instead.

### spark

[Section titled “spark”](#spark)

The only command you should rely on for performance information is the `/spark` command.
The spark subcommands are documented [in the dedicated spark wiki](https://spark.lucko.me/docs/Command-Usage).

### tps

[Section titled “tps”](#tps)

The tps command is a simple command to get the TPS (ticks per second, how often the game loop
is run per second. The higher, the better. Target TPS is 20.0) from the past 1, 5, and 15 minutes.

### mspt

[Section titled “mspt”](#mspt)

The mspt command is another simple command to get the average, min, and max MSPT (milliseconds per tick, how much time
a tick takes. The lower, the better. MSPT should be below 50 for 20 TPS) of the server from the last 5, 10, and 60 seconds.

### timings

[Section titled “timings”](#timings)

Deprecation

The timings command is deprecated for removal. You should instead use the [spark command](#spark) as a replacement.

More information can be viewed here: <https://github.com/PaperMC/Paper/discussions/10565>.

## restart

[Section titled “restart”](#restart)

The `/restart` command is part of Spigot’s restart mechanism, which makes the server restart when it crashes
or the command is run manually.

Note

For help setting up the restart script, see
[this gist by Prof\_Bloodstone](https://gist.github.com/Prof-Bloodstone/6367eb4016eaf9d1646a88772cdbbac5).

## paper

[Section titled “paper”](#paper)

This section is dedicated to the subcommands of the in-game `/paper` command.

### chunkinfo

[Section titled “chunkinfo”](#chunkinfo)

The `/paper chunkinfo [<worldname>]` command is used for displaying information about loaded chunks in a world.
You can specify the world to get info about with the `[<worldname>]` argument. If you set it to `*` or leave it
out, it will list information for all worlds.

The output differentiates between multiple types of loaded chunks. Here is a quick rundown of each type.
A more complete documentation may be found in the [Minecraft wiki](https://minecraft.wiki/w/Chunk).

* `Total` As the name suggests, this number describes **all chunks** currently loaded.
* `Inactive` More commonly referred to as “inaccessible”, are chunks which are not ticked, but where chunk generation occurs.
* `Full` Usually called **border chunks**. No ticking is happening, but entities and blocks are loaded and accessible.
* `Block Ticking` All game aspects work as expected, except that entities are not spawned naturally or ticked, but still accessible. Also called **lazy chunks**.
* `Entity Ticking` The chunk is being ticked fully.

### debug

[Section titled “debug”](#debug)

The `/paper debug <chunks>` command is used to dump information about all currently loaded chunks to a file. The content
of this file is generally irrelevant for most server admins and is intended to be used by developers.

### dumpitem

[Section titled “dumpitem”](#dumpitem)

The `/paper dumpitem [all]` command can be used to retrieve the data component representation of your currently held
item. Simply running `/paper dumpitem` will yield the item data, which you can use to represent this item in
commands which expect an item argument. `/paper dumpitem all` yields the **full data component representation**,
including default data components you do not have to explicitly declare.

### dumplisteners

[Section titled “dumplisteners”](#dumplisteners)

The `/paper dumplisteners toFile|<className>` command is primarily intended for developers trying to figure out why
their event handlers might not be working as expected. Using `/paper dumplisteners toFile` will write all
currently registered event handlers to a file, whilst `/paper dumplisteners <className>` will print the registered
event handlers only for the specific event.

### dumpplugins

[Section titled “dumpplugins”](#dumpplugins)

The `/paper dumpplugins` command is intended for developers trying to figure out issues with their dependencies or
loading order in relation to other plugins. It can also be used to debug bootstrapper providers, general load order,
and listing class loaders for the plugins.

### entity

[Section titled “entity”](#entity)

The `/paper entity list [<filter>] [<world>]` command can be used to list all currently ticking entities.

The `[<filter>]` argument is used to filter the listed entities types and acts similar to a **regular expression**:

* You can use `*` to list **all** entities, which is the default value for this argument.
* You can list individual entities by providing `minecraft:<entity_type>` as the argument. The namespace here is very important.
* To list multiple entities, you can use the `*` as a greedy wildcard expression. For example, to list all entities,
  whose names start with **e**, you could use `minecraft:e*`.
* You can also use the `?` single-character wildcard expression. For example, to list `pig` and `piglin`, but **not**
  `piglin_brute`, you can provide `minecraft:pig???` as the filter.

The `[<world>]` argument declares the world you want to check the entities in. This defaults to the current world
of a player or to the overworld for the console.

The output will look similar to this:

```java
Total Ticking: -78, Total Non-Ticking: 92

10 (3) : minecraft:pig

1 (0) : minecraft:piglin

* First number is ticking entities, second number is non-ticking entities
```

The comment at the end already clearly describes the purpose of the numbers.

### fixlight

[Section titled “fixlight”](#fixlight)

The `/paper fixlight` command is a simple command to trigger a full re-calculation of the light map of all currently
loaded chunks. This can be used to fix any lighting issues which commonly occur with plugins like WorldEdit.

### heap

[Section titled “heap”](#heap)

The `/paper heap` is a developer debug command to dump the current JVM heap to a `.hprof` file, which can be analyzed
to detect to amount of memory used by certain objects. The output file can be rather big, so having a bit of free
space on your disk is recommended before running this command (as a general rule, the file is usually smaller
than the currently used memory. You can check the memory consumption using the `/spark healthreport` command).

### holderinfo

[Section titled “holderinfo”](#holderinfo)

The `/paper holderinfo [<world>]` command is used to gather the number of different chunks currently held in memory.

The `[<world>]` argument can be used to define the world to get the chunk holder information for. Leave blank to
default to `*`, which prints the information for all chunks.

In general, the types have the following meanings:

* `Total` The total amount of in-memory chunk holders.
* `Unloadable` The number of chunks that are safe to be unloaded.
* `Null` Chunks, which have received the unload signal, but whose scheduling locks are still held.
* `ReadOnly` The number of chunk holders, which are readable, but not writable to.
* `Proto` A “prototype” chunk, which is a fully working chunk loaded in memory, but which is not currently placed in the world.
* `Full` Represents the number of chunks currently placed in the world.

### mobcaps

[Section titled “mobcaps”](#mobcaps)

Not to be confused with the [playermobcaps](#playermobcaps) subcommand, the `/paper mobcaps [<world>]` command displays
the **global** mob caps for all players in a world. The `[<world>]` argument defaults to the overworld and
can be set to retrieve the mob caps for other worlds as well. The command also lists the number of
chunks in which mobs can spawn.

### playermobcaps

[Section titled “playermobcaps”](#playermobcaps)

The `/paper playermobcaps [<player>]` command is used to list the local mob caps for a specific player. The `[<player>]`
argument defaults to the player, who ran the command, if one exists.

### reload

[Section titled “reload”](#reload)

The `/paper reload` command is an unsupported command which allows for runtime Paper-config reloading. If you get any issues
after using this command, please make sure to reproduce this on a freshly-started server before asking for help or
reporting it. Do not that this command **does not** reload non-Paper configs, like the `spigot.yml`.

### syncloadinfo

[Section titled “syncloadinfo”](#syncloadinfo)

The `/paper syncloadinfo [clear]` command requires the `-Dpaper.debug-sync-loads=true` JVM flag to be explicitly set
before running the command. The command was historically used for debugging purposes during Paper development, but
the mechanism behind the command is currently unused, meaning that the written file will **always** look
like this:

```java
{

"worlds": []

}
```

Outside of checking for whether the command is allowed to be run, the JVM flag is otherwise unused.

### version

[Section titled “version”](#version)

The `/paper version` command is an alias to the standard `/version` command.


================================================================================
Chapter Title: System properties
Original Link: https://docs.papermc.io/paper/reference/system-properties/
================================================================================

These system properties and environment variables can be set when you start your server allowing for the configuration of various settings.

Danger Ahead

Setting flags for the JVM can alter how it operates and the same goes for the Paper server.
If you are unsure about what a flag does, it is recommended that you **do not use it**.

## How they work

[Section titled “How they work”](#how-they-work)

System properties are set when you start your server. For example, if you are using a `.bat` or a `.sh` file to start your server, you can add the system properties to the file. For example:

Terminal window

```java
java -Dcom.mojang.eula.agree=true -jar paper.jar
```

Note

Some of Paper’s system properties contain a `.` character in their name. When using PowerShell, these will require wrapping in quotes.
i.e. `"-Dcom.mojang.eula.agree=true"`

Where a `-D` is used to set a system property, and the system property is `com.mojang.eula.agree` with a value of `true`. Otherwise, just add them to the start command.

Note

Where a system property is stated as `unset`, setting it as `true` will work to enable it.

[Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are another way to pass values to Paper.
They can be set in various ways, depending on your operating system and how you start Paper.

In most cases, you will not need to use these, unless you are running Paper in a (Docker) container or such.

## List of system properties

[Section titled “List of system properties”](#list-of-system-properties)

#### paper.playerconnection.keepalive

[Section titled “paper.playerconnection.keepalive”](#paperplayerconnectionkeepalive)

* **default**: `30`
* **description**: Controls how long the player connection will wait before closing when not receiving any keepalives, in seconds.

#### timings.bypassMax

[Section titled “timings.bypassMax”](#timingsbypassmax)

* **default**: `unset`
* **description**: Allows for bypassing the max amount of data to send to the Aikar’s Timings API. Setting this will not permit bypassing the limit unless the API is configured to allow it.

#### LetMeReload

[Section titled “LetMeReload”](#letmereload)

* **default**: `unset`
* **description**: This disables the reload confirmation message when using the `/reload` command.

#### paper.disableChannelLimit

[Section titled “paper.disableChannelLimit”](#paperdisablechannellimit)

* **default**: `unset`
* **description**: Disables the plugin channel limit for the server. This will disable the limit of 128 plugin channels per player.

#### net.kyori.adventure.text.warnWhenLegacyFormattingDetected

[Section titled “net.kyori.adventure.text.warnWhenLegacyFormattingDetected”](#netkyoriadventuretextwarnwhenlegacyformattingdetected)

* **default**: `false`
* **description**: Enables or disables the warning when legacy formatting is detected in a chat component.

#### Paper.DisableClassPrioritization

[Section titled “Paper.DisableClassPrioritization”](#paperdisableclassprioritization)

* **default**: `unset`
* **description**: Disables the class prioritization system - mostly an issue when failing to relocate or shade properly.

#### Paper.disableFlushConsolidate

[Section titled “Paper.disableFlushConsolidate”](#paperdisableflushconsolidate)

* **default**: `unset`
* **description**: Disables the netty flush consolidation system.

#### Paper.debugDynamicMissingKeys

[Section titled “Paper.debugDynamicMissingKeys”](#paperdebugdynamicmissingkeys)

* **default**: `unset`
* **description**: Enables debug logging for missing keys in NBT objects.

#### disable.watchdog

[Section titled “disable.watchdog”](#disablewatchdog)

* **default**: `unset`
* **description**: Disables the watchdog warning system.

#### paper.explicit-flush

[Section titled “paper.explicit-flush”](#paperexplicit-flush)

* **default**: `unset`
* **description**: Enables explicit flushing of the network channel.

#### Paper.enable-sync-chunk-writes

[Section titled “Paper.enable-sync-chunk-writes”](#paperenable-sync-chunk-writes)

* **default**: `unset`
* **description**: Syncs writes on each write call. This has a performance impact, particularly on hard drives.

#### paper.debug-sync-loads

[Section titled “paper.debug-sync-loads”](#paperdebug-sync-loads)

* **default**: `unset`
* **description**: Enables debug logging for sync chunk loads.

#### Paper.ignoreWorldDataVersion

[Section titled “Paper.ignoreWorldDataVersion”](#paperignoreworlddataversion)

* **default**: `unset`
* **description**: Ignores the world data version when loading a world. This is not recommended and will likely cause issues.

#### Paper.bypassHostCheck

[Section titled “Paper.bypassHostCheck”](#paperbypasshostcheck)

* **default**: `unset`
* **description**: Bypasses the host pattern matching attempt for the client when connecting to the server.

#### paper.ticklist-warn-on-excessive-delay

[Section titled “paper.ticklist-warn-on-excessive-delay”](#paperticklist-warn-on-excessive-delay)

* **default**: `unset`
* **description**: Enables the warning when a tick list is scheduled with an excessive delay.

#### debug.rewriteForIde

[Section titled “debug.rewriteForIde”](#debugrewriteforide)

* **default**: `unset`
* **description**: Removes the NMS revision from the stack trace to allow for easier debugging in IDEs.
  It also remaps plugin CB calls to remove the version information.

#### convertLegacySigns

[Section titled “convertLegacySigns”](#convertlegacysigns)

* **default**: `unset`
* **description**: Converts legacy signs to the new format.

#### paper.maxCustomChannelName

[Section titled “paper.maxCustomChannelName”](#papermaxcustomchannelname)

* **default**: `64`
* **description**: Sets the largest size that a plugin channel name can take.

#### Paper.maxSignLength

[Section titled “Paper.maxSignLength”](#papermaxsignlength)

* **default**: `80`
* **description**: Sets the maximum line length for signs.

#### Paper.minPrecachedDatafixVersion

[Section titled “Paper.minPrecachedDatafixVersion”](#paperminprecacheddatafixversion)

* **default**: `Minecraft world version + 1`
* **description**: If you are expecting to convert a large number of chunks you might consider setting this to only convert from a point onwards.

#### Paper.WorkerThreadCount

[Section titled “Paper.WorkerThreadCount”](#paperworkerthreadcount)

* **default**: half of available physical (**not logical**) cores or `1` if 3 or fewer cores are available
* **description**: Sets the number of worker threads to use for chunk loading. See [here](https://docs.papermc.io/paper/reference/global-configuration#chunk_system_worker_threads) for more info.

#### Paper.excessiveTELimit

[Section titled “Paper.excessiveTELimit”](#paperexcessivetelimit)

* **default**: `750`
* **description**: Splits tile entities into multiple packets if there are more than this many.

#### io.papermc.paper.suppress.sout.nags

[Section titled “io.papermc.paper.suppress.sout.nags”](#iopapermcpapersuppresssoutnags)

* **default**: `unset`
* **description**: Suppresses the nag message about using `System.out`/`System.err` in a plugin.

#### paper.strict-thread-checks

[Section titled “paper.strict-thread-checks”](#paperstrict-thread-checks)

* **default**: `unset`
* **description**: This sets the status of the AsyncCatcher so that it will always log an error if code is not run on the main thread.

#### Paper.skipServerPropertiesComments

[Section titled “Paper.skipServerPropertiesComments”](#paperskipserverpropertiescomments)

* **default**: `unset`
* **description**: Skips the comments in the `server.properties` file.

#### Paper.debugInvalidSkullProfiles

[Section titled “Paper.debugInvalidSkullProfiles”](#paperdebuginvalidskullprofiles)

* **default**: `unset`
* **description**: Enables debug logging for invalid skull profiles. This logs any invalid skulls in the world with the appropriate location information.

#### paper.alwaysPrintWarningState

[Section titled “paper.alwaysPrintWarningState”](#paperalwaysprintwarningstate)

* **default**: `unset`
* **description**: Always prints the warning state for the particular level.

#### Paper.parseYamlCommentsByDefault

[Section titled “Paper.parseYamlCommentsByDefault”](#paperparseyamlcommentsbydefault)

* **default**: `true`
* **description**: Sets whether to parse comments in YAML files by default.

#### paperclip.patchonly:

[Section titled “paperclip.patchonly:”](#paperclippatchonly)

* **default**: `false`
* **description**: If the server is started via the Paperclip patch utility (the default distribution on the downloads page) then this sets whether it should only patch the Vanilla server and download libraries without starting the server.

#### Paper.IgnoreJavaVersion

[Section titled “Paper.IgnoreJavaVersion”](#paperignorejavaversion)

* **default**: `false`
* **description**: Allows you to bypass the Java version check. See [here](https://docs.papermc.io/paper/faq#unsupported-java-detected-what-do-i-do) for more info.

#### paper.disableStartupVersionCheck

[Section titled “paper.disableStartupVersionCheck”](#paperdisablestartupversioncheck)

* **default**: `unset`
* **description**: If set, disables the automatic update checking on startup. See [here](https://docs.papermc.io/paper/misc/update-checker) for more info.

#### paper.useLegacyPluginLoading

[Section titled “paper.useLegacyPluginLoading”](#paperuselegacypluginloading)

* **default**: `false`
* **description**: Allows cyclic plugin loading. See [here](https://docs.papermc.io/paper/reference/paper-plugins#cyclic-plugin-loading) for more info.

#### Paper.DisableCommandConverter

[Section titled “Paper.DisableCommandConverter”](#paperdisablecommandconverter)

* **default**: `false`
* **description**: Disables Paper’s automatic upgrading of commands, including items with custom data defined in command blocks and other places that may contain commands, to the new component format introduced in version 1.20.5.

#### paper.disableOldApiSupport

[Section titled “paper.disableOldApiSupport”](#paperdisableoldapisupport)

* **default**: `false`
* **description**: Disables plugin compatibility measures that can otherwise result in a considerable delay of class loading (also known as “Commodore” plugin rewriting). This generally requires all of your plugins to be compiled against a recent API version.

#### paper.disablePluginRemapping

[Section titled “paper.disablePluginRemapping”](#paperdisablepluginremapping)

* **default**: `false`
* **description**: Disables plugin remapping introduced in 1.20.5. For more information see the [userdev](https://docs.papermc.io/paper/dev/userdev#1205-and-beyond) documentation and the official [announcement](https://discord.com/channels/289587909051416579/976631292747735080/1232740079097876570).

#### paper.preferSparkPlugin

[Section titled “paper.preferSparkPlugin”](#paperprefersparkplugin)

* **default**: `false`
* **description**: Whether the bundled spark profiler should be disabled in favor of a standalone plugin. If the spark plugin is not found, the bundled version will be loaded regardless of the setting, unless it is [explicitly disabled](https://docs.papermc.io/paper/reference/global-configuration#spark_enabled).

#### paper.disableWorldSymlinkValidation

[Section titled “paper.disableWorldSymlinkValidation”](#paperdisableworldsymlinkvalidation)

* **default**: `false`
* **description**: Disables the folder walk and symlink validation when loading a world. Significantly improves world loading speed on massive worlds (>1TB). This does not disable symlink verification of datapacks.

#### paper.disableGameRuleLimits

[Section titled “paper.disableGameRuleLimits”](#paperdisablegamerulelimits)

* **default**: `false`
* **description**: Disables limits on certain game rule values, e.g. `minecartMaxSpeed` and `spawnChunkRadius`.

#### minecraft.api.session.host

[Section titled “minecraft.api.session.host”](#minecraftapisessionhost)

* **default**: `https://sessionserver.mojang.com`
* **description**: Allows specifying of a custom session server URL e.g. for caching. [`minecraft.api.services.host`](#minecraftapiserviceshost) needs to be set too for this to apply.

#### minecraft.api.services.host

[Section titled “minecraft.api.services.host”](#minecraftapiserviceshost)

* **default**: `https://api.minecraftservices.com`
* **description**: Allows specifying of a custom services API URL e.g. for caching. [`minecraft.api.session.host`](#minecraftapisessionhost) needs to be set too for this to apply.

#### com.mojang.eula.agree

[Section titled “com.mojang.eula.agree”](#commojangeulaagree)

* **default**: `false`
* **description**: Setting this to true indicates that you have agreed with [Mojang’s EULA](https://aka.ms/MinecraftEULA), skipping `eula.txt` checks.

#### org.bukkit.plugin.java.LibraryLoader.centralURL

[Section titled “org.bukkit.plugin.java.LibraryLoader.centralURL”](#orgbukkitpluginjavalibraryloadercentralurl)

* **default**: `https://maven-central.storage-download.googleapis.com/maven2`
* **description**: Sets the default central repository URL, from which plugins’ dependencies declared using the [`libraries`](https://docs.papermc.io/paper/dev/plugin-yml#libraries) plugin.yml field are resolved. This is overridden by the [`PAPER_DEFAULT_CENTRAL_REPOSITORY`](#paper_default_central_repository) environment variable, if it is set.

Caution

If you wish to configure this with Maven Central, use a mirror, as using Maven Central directly as a CDN is against the Maven Central Terms of Service, and you may hit rate limits.

By default, this uses Google’s NA mirror of Maven Central. You may also use region-specific mirrors listed [here](https://storage-download.googleapis.com/maven-central/index.html).

#### paper.debugEntitiesWithInvalidIds

[Section titled “paper.debugEntitiesWithInvalidIds”](#paperdebugentitieswithinvalidids)

* **default**: `false`
* **description**: Enables logging the full entity NBT when an entity with a missing or otherwise invalid entity id is attempted to be loaded. (Whenever ‘Skipping Entity with id’ is logged to the console.)

#### paper.maxChatCommandInputSize

[Section titled “paper.maxChatCommandInputSize”](#papermaxchatcommandinputsize)

* **default**: `256`
* **description**: The maximum length a chat command may have. A Vanilla client cannot send more than 256 characters.

## List of environment variables

[Section titled “List of environment variables”](#list-of-environment-variables)

#### PAPER\_VELOCITY\_SECRET

[Section titled “PAPER\_VELOCITY\_SECRET”](#paper_velocity_secret)

* **default**: `unset`
* **description**: Overrides the [`proxies.velocity.secret`](https://docs.papermc.io/paper/reference/global-configuration#proxies_velocity_secret) global configuration option.

#### PAPER\_DEFAULT\_CENTRAL\_REPOSITORY

[Section titled “PAPER\_DEFAULT\_CENTRAL\_REPOSITORY”](#paper_default_central_repository)

* **default**: `https://maven-central.storage-download.googleapis.com/maven2`
* **description**: Sets the default central repository URL, from which plugins’ dependencies declared using the [`libraries`](https://docs.papermc.io/paper/dev/plugin-yml#libraries) plugin.yml field are resolved. This overrides the [`org.bukkit.plugin.java.LibraryLoader.centralURL`](#orgbukkitpluginjavalibraryloadercentralurl) system property, if it is set.

Caution

If you wish to configure this with Maven Central, use a mirror, as using Maven Central directly as a CDN is against the Maven Central Terms of Service, and you may hit rate limits.

By default, this uses Google’s NA mirror of Maven Central. You may also use region-specific mirrors listed [here](https://storage-download.googleapis.com/maven-central/index.html).


================================================================================
Chapter Title: Permissions
Original Link: https://docs.papermc.io/paper/reference/permissions/
================================================================================

This page lists all permissions that are included in the default Paper server.

## Vanilla command permissions

[Section titled “Vanilla command permissions”](#vanilla-command-permissions)

The following is a list of permissions for Vanilla commands.

| Command | Aliases | Permission Node | Players Have Permission By Default? |
| --- | --- | --- | --- |
| [advancement](https://minecraft.wiki/w/Commands/advancement) |  | minecraft.command.advancement | No |
| [attribute](https://minecraft.wiki/w/Commands/attribute) |  | minecraft.command.attribute | No |
| [ban](https://minecraft.wiki/w/Commands/ban) |  | minecraft.command.ban | No |
| [ban-ip](https://minecraft.wiki/w/Commands/ban-ip) |  | minecraft.command.ban-ip | No |
| [banlist](https://minecraft.wiki/w/Commands/banlist) |  | minecraft.command.banlist | No |
| [bossbar](https://minecraft.wiki/w/Commands/bossbar) |  | minecraft.command.bossbar | No |
| [clear](https://minecraft.wiki/w/Commands/clear) |  | minecraft.command.clear | No |
| [clone](https://minecraft.wiki/w/Commands/clone) |  | minecraft.command.clone | No |
| [damage](https://minecraft.wiki/w/Commands/damage) |  | minecraft.command.damage | No |
| [data](https://minecraft.wiki/w/Commands/data) |  | minecraft.command.data | No |
| [datapack](https://minecraft.wiki/w/Commands/datapack) |  | minecraft.command.datapack | No |
| [debug](https://minecraft.wiki/w/Commands/debug) |  | minecraft.command.debug | No |
| [defaultgamemode](https://minecraft.wiki/w/Commands/defaultgamemode) |  | minecraft.command.defaultgamemode | No |
| [deop](https://minecraft.wiki/w/Commands/deop) |  | minecraft.command.deop | No |
| [dialog](https://minecraft.wiki/w/Commands/dialog) |  | minecraft.command.dialog | No |
| [difficulty](https://minecraft.wiki/w/Commands/difficulty) |  | minecraft.command.difficulty | No |
| [effect](https://minecraft.wiki/w/Commands/effect) |  | minecraft.command.effect | No |
| [enchant](https://minecraft.wiki/w/Commands/enchant) |  | minecraft.command.enchant | No |
| [execute](https://minecraft.wiki/w/Commands/execute) |  | minecraft.command.execute | No |
| [fetchprofile](https://minecraft.wiki/w/Commands/fetchprofile) |  | minecraft.command.fetchprofile | No |
| [fill](https://minecraft.wiki/w/Commands/fill) |  | minecraft.command.fill | No |
| [fillbiome](https://minecraft.wiki/w/Commands/fillbiome) |  | minecraft.command.fillbiome | No |
| [forceload](https://minecraft.wiki/w/Commands/forceload) |  | minecraft.command.forceload | No |
| [function](https://minecraft.wiki/w/Commands/function) |  | minecraft.command.function | No |
| [gamemode](https://minecraft.wiki/w/Commands/gamemode) |  | minecraft.command.gamemode | No |
| [gamerule](https://minecraft.wiki/w/Commands/gamerule) |  | minecraft.command.gamerule | No |
| [give](https://minecraft.wiki/w/Commands/give) |  | minecraft.command.give | No |
| [help](https://minecraft.wiki/w/Commands/help) |  | minecraft.command.help | Yes |
| [item](https://minecraft.wiki/w/Commands/item) |  | minecraft.command.item | No |
| [jfr](https://minecraft.wiki/w/Commands/jfr) |  | minecraft.command.jfr | No |
| [kick](https://minecraft.wiki/w/Commands/kick) |  | minecraft.command.kick | No |
| [kill](https://minecraft.wiki/w/Commands/kill) |  | minecraft.command.kill | No |
| [list](https://minecraft.wiki/w/Commands/list) |  | minecraft.command.list | Yes |
| [locate](https://minecraft.wiki/w/Commands/locate) |  | minecraft.command.locate | No |
| [loot](https://minecraft.wiki/w/Commands/loot) |  | minecraft.command.loot | No |
| [me](https://minecraft.wiki/w/Commands/me) |  | minecraft.command.me | Yes |
| [msg](https://minecraft.wiki/w/Commands/msg) | /w, /tell | minecraft.command.msg | Yes |
| [op](https://minecraft.wiki/w/Commands/op) |  | minecraft.command.op | No |
| [pardon](https://minecraft.wiki/w/Commands/pardon) |  | minecraft.command.pardon | No |
| [pardon-ip](https://minecraft.wiki/w/Commands/pardon-ip) |  | minecraft.command.pardon-ip | No |
| [particle](https://minecraft.wiki/w/Commands/particle) |  | minecraft.command.particle | No |
| [perf](https://minecraft.wiki/w/Commands/perf) |  | minecraft.command.perf | No |
| [place](https://minecraft.wiki/w/Commands/place) |  | minecraft.command.place | No |
| [playsound](https://minecraft.wiki/w/Commands/playsound) |  | minecraft.command.playsound | No |
| [publish](https://minecraft.wiki/w/Commands/publish) |  | minecraft.command.publish | No |
| [random](https://minecraft.wiki/w/Commands/random) |  | minecraft.command.random | Yes without sequence argument, No with sequence argument. |
| [recipe](https://minecraft.wiki/w/Commands/recipe) |  | minecraft.command.recipe | No |
| [reload](https://minecraft.wiki/w/Commands/reload) |  | minecraft.command.reload | No |
| [return](https://minecraft.wiki/w/Commands/return) |  | minecraft.command.return | No |
| [ride](https://minecraft.wiki/w/Commands/ride) |  | minecraft.command.ride | No |
| [rotate](https://minecraft.wiki/w/Commands/rotate) |  | minecraft.command.rotate | No |
| [save-all](https://minecraft.wiki/w/Commands/save-all) |  | minecraft.command.save-all | No |
| [save-off](https://minecraft.wiki/w/Commands/save-off) |  | minecraft.command.save-off | No |
| [save-on](https://minecraft.wiki/w/Commands/save-on) |  | minecraft.command.save-on | No |
| [say](https://minecraft.wiki/w/Commands/say) |  | minecraft.command.say | No |
| [schedule](https://minecraft.wiki/w/Commands/schedule) |  | minecraft.command.schedule | No |
| [scoreboard](https://minecraft.wiki/w/Commands/scoreboard) |  | minecraft.command.scoreboard | No |
| [seed](https://minecraft.wiki/w/Commands/seed) |  | minecraft.command.seed | No |
| [setblock](https://minecraft.wiki/w/Commands/setblock) |  | minecraft.command.setblock | No |
| [setidletimeout](https://minecraft.wiki/w/Commands/setidletimeout) |  | minecraft.command.setidletimeout | No |
| [setworldspawn](https://minecraft.wiki/w/Commands/setworldspawn) |  | minecraft.command.setworldspawn | No |
| [spawnpoint](https://minecraft.wiki/w/Commands/spawnpoint) |  | minecraft.command.spawnpoint | No |
| [spectate](https://minecraft.wiki/w/Commands/spectate) |  | minecraft.command.spectate | No |
| [spreadplayers](https://minecraft.wiki/w/Commands/spreadplayers) |  | minecraft.command.spreadplayers | No |
| [stop](https://minecraft.wiki/w/Commands/stop) |  | minecraft.command.stop | No |
| [stopsound](https://minecraft.wiki/w/Commands/stopsound) |  | minecraft.command.stopsound | No |
| [summon](https://minecraft.wiki/w/Commands/summon) |  | minecraft.command.summon | No |
| [tag](https://minecraft.wiki/w/Commands/tag) |  | minecraft.command.tag | No |
| [team](https://minecraft.wiki/w/Commands/team) |  | minecraft.command.team | No |
| [teammsg](https://minecraft.wiki/w/Commands/teammsg) | /tm | minecraft.command.teammsg | Yes |
| [teleport](https://minecraft.wiki/w/Commands/teleport) | /tp | minecraft.command.teleport | No |
| [tellraw](https://minecraft.wiki/w/Commands/tellraw) |  | minecraft.command.tellraw | No |
| [test](https://minecraft.wiki/w/Commands/test) |  | minecraft.command.test | No |
| [tick](https://minecraft.wiki/w/Commands/tick) |  | minecraft.command.tick | No |
| [time](https://minecraft.wiki/w/Commands/time) |  | minecraft.command.time | No |
| [title](https://minecraft.wiki/w/Commands/title) |  | minecraft.command.title | No |
| [transfer](https://minecraft.wiki/w/Commands/transfer) |  | minecraft.command.transfer | No |
| [trigger](https://minecraft.wiki/w/Commands/trigger) |  | minecraft.command.trigger | Yes |
| [version](https://minecraft.wiki/w/Commands/version) |  | minecraft.command.version | No |
| [waypoint](https://minecraft.wiki/w/Commands/waypoint) |  | minecraft.command.waypoint | No |
| [weather](https://minecraft.wiki/w/Commands/weather) |  | minecraft.command.weather | No |
| [whitelist](https://minecraft.wiki/w/Commands/whitelist) |  | minecraft.command.whitelist | No |
| [worldborder](https://minecraft.wiki/w/Commands/worldborder) |  | minecraft.command.worldborder | No |
| [xp](https://minecraft.wiki/w/Commands/xp) | /experience | minecraft.command.xp | No |

## Bukkit command permissions

[Section titled “Bukkit command permissions”](#bukkit-command-permissions)

The following is a list of permissions for Bukkit commands.

| Command | Aliases | Permission Node | Players Have Permission By Default? |
| --- | --- | --- | --- |
| help | /? | bukkit.command.help | Yes |
| plugins | /pl | bukkit.command.plugins | Yes |
| reload | /rl | bukkit.command.reload | No |
| restart |  | bukkit.command.restart | No |
| timings |  | bukkit.command.timings | No |
| version | /ver, /about | bukkit.command.version | Yes |

## Paper command permissions

[Section titled “Paper command permissions”](#paper-command-permissions)

The following is a list of permissions for Paper commands.

| Command | Aliases | Permission Node | Players Have Permission By Default? |
| --- | --- | --- | --- |
| paper |  | bukkit.command.paper | No |

## Vanilla permissions

[Section titled “Vanilla permissions”](#vanilla-permissions)

The following is a list of all additional Vanilla permissions.

| Permission Node | Description | Players Have Permission By Default? |
| --- | --- | --- |
| minecraft | Gives the user the ability to use all vanilla utilities and commands. | No |
| minecraft.admin.command\_feedback | Receive command broadcasts when sendCommandFeedback is true. | No |
| minecraft.nbt.place | Gives the user the ability to place restricted blocks with NBT in creative. | No |
| minecraft.nbt.copy | Gives the user the ability to copy NBT in creative. | Yes |
| minecraft.debugstick | Gives the user the ability to use the debug stick in creative. | No |
| minecraft.debugstick.always | Gives the user the ability to use the debug stick in all game modes. | No |
| minecraft.commandblock | Gives the user the ability to use command blocks. | No |
| minecraft.command.selector | Gives the user the ability to use [target selectors](https://minecraft.wiki/w/Target_selectors) in command arguments. | No |

## Bukkit permissions

[Section titled “Bukkit permissions”](#bukkit-permissions)

The following is a list of all additional Bukkit permissions.

| Permission Node | Description | Players Have Permission By Default? |
| --- | --- | --- |
| bukkit.broadcast | Allows the user to receive all broadcast messages | No |
| bukkit.broadcast.admin | Allows the user to receive administrative broadcasts | No |
| bukkit.broadcast.user | Allows the user to receive user broadcasts | Yes |

## Paper permissions

[Section titled “Paper permissions”](#paper-permissions)

The following is a list of all additional Paper permissions.

| Permission Node | Description | Players Have Permission By Default? |
| --- | --- | --- |
| bukkit.command.paper.heap | Allows the user to run the heap sub command | No |
| bukkit.command.paper.entity | Allows the user to run the entity sub command | No |
| bukkit.command.paper.reload | Allows the user to run the reload sub command | No |
| bukkit.command.paper.version | Allows the user to run the version sub command | No |
| bukkit.command.paper.dumpplugins | Allows the user to run the dumpplugins sub command | No |
| bukkit.command.paper.syncloadinfo | Allows the user to run the syncloadinfo sub command | No |
| bukkit.command.paper.dumpitem | Allows the user to run the dumpitem sub command | No |
| bukkit.command.paper.mobcaps | Allows the user to run the mobcaps sub command | No |
| bukkit.command.paper.dumplisteners | Allows the user to run the dumplisteners sub command | No |
| bukkit.command.paper.fixlight | Allows the user to run the fixlight sub command | No |
| bukkit.command.paper.debug | Allows the user to run the debug sub command | No |
| paper.antixray.bypass | Allows the user to bypass anti-xray if use-permission is enabled | No |
| paper.bypass-visibility.tab-completion | Allows the user to see hidden players in command tab completions | No |


================================================================================
Chapter Title: Update checker
Original Link: https://docs.papermc.io/paper/misc/update-checker/
================================================================================

Since 1.21.11, Paper includes a built-in update checker that notifies server administrators on startup when a new version of Paper is available.

## How it works

[Section titled “How it works”](#how-it-works)

When the server starts, Paper will check its current version against the latest available version in the stable channel on the PaperMC servers.
If a newer version is found, a notification message will be printed to the console and server logs.

Additionally, you can manually check for updates at any time by running the `version` command in the server console (or in-game with appropriate `bukkit.command.version` permission).

## What is sent

[Section titled “What is sent”](#what-is-sent)

The update checker sends the following information to the PaperMC servers:

* Current Paper version
* Your server’s client IP (as for any http request)

This information is not currently stored or analyzed by PaperMC, though requests pass through CloudFlare.

## Configuration

[Section titled “Configuration”](#configuration)

The update checker can be disabled in the `paper-global.yml` configuration file. The relevant section is as follows:

config/paper-global.yml

```java
update-checker:

enabled: false
```

Alternatively you can disable the update checker by adding the following JVM argument when starting your server:

Terminal window

```java
-Dpaper.disableStartupVersionCheck
```


================================================================================
Chapter Title: Bug fixes
Original Link: https://docs.papermc.io/paper/misc/paper-bug-fixes/
================================================================================

Paper fixes many gameplay and technical issues within Minecraft. The most prevalent fixes are to TNT duplication and bedrock breaking.

## Vanilla bug fixes

[Section titled “Vanilla bug fixes”](#vanilla-bug-fixes)

Paper fixes many Vanilla bugs that were not intended by Mojang. These bugs are patched to fix behavior or prevent abuse and
instability on the server. Some of our fixes are configurable, as we understand that some servers may want to keep the
Vanilla behavior. You will find these configuration options in the [global configuration](https://docs.papermc.io/paper/reference/global-configuration)
and the [world configuration](https://docs.papermc.io/paper/reference/world-configuration).

### What is intended behavior vs a bug?

[Section titled “What is intended behavior vs a bug?”](#what-is-intended-behavior-vs-a-bug)

When an issue is reported to us, we check Mojang’s issue tracker. If the problem has been reported there, then we
check to see if it:

1. Has been confirmed as a bug
2. Has an assigned priority to it

If it meets these two criteria then we will accept changes to fix the bug, as it can take a long time for Mojang to fix
them (sometimes years). If an issue gets declined by Mojang, we normally do not “fix” it as it is intended behavior.

## Duplication bugs

[Section titled “Duplication bugs”](#duplication-bugs)

Because TNT duping is considered a form of automated mining and not a resource dupe, we have provided an option to
restore it. This, undesirably, also re-enables carpet and rail duping, which normally we would not provide a config for,
but it’s the same bug for those, so we have no choice. However, the config option is as follows:

config/paper-global.yml

```java
unsupported-settings:

allow-piston-duplication: true
```

We also allow you to restore the ability to duplicate gravity blocks, such as sand, using end portals. This is not
recommended, as it can cause issues with the server, but we do provide a config option to restore this functionality:

config/paper-global.yml

```java
unsupported-settings:

allow-unsafe-end-portal-teleportation: true
```

## Block breaking

[Section titled “Block breaking”](#block-breaking)

We also fix the ability to break Bedrock and End Portal frames. We do also provide a config option to restore this
functionality, but it is not recommended:

config/paper-global.yml

```java
unsupported-settings:

allow-permanent-block-break-exploits: true
```

## Afterword

[Section titled “Afterword”](#afterword)

We will not support you if you have issues whilst these settings are enabled, as they can cause unintended side effects.
These settings are also not guaranteed to be supported in the future and may have their behavior changed, or removed, at any time.

For legacy reasoning behind not having configuration options for many duplication bugs, see:
[#3724](https://github.com/PaperMC/Paper/issues/3724)


================================================================================
Chapter Title: Frequently asked questions
Original Link: https://docs.papermc.io/paper/faq/
================================================================================

## Unsupported Java detected, what do I do?!

[Section titled “Unsupported Java detected, what do I do?!”](#unsupported-java-detected-what-do-i-do)

Unsupported, early-access, or internal versions of Java are often missing features, have known issues or be straight up broken.
As such, we cannot provide support for servers running such versions.
You should install a supported version of Java as explained [here](https://docs.papermc.io/misc/java-install).

If you still wish to continue, knowing that you are on your own and will receive NO support, you can disable the check with a system property, as explained [here](https://docs.papermc.io/paper/reference/system-properties#paperignorejavaversion).


================================================================================
Chapter Title: Project setup
Original Link: https://docs.papermc.io/paper/dev/project-setup/
================================================================================

As the Paper team primarily uses [IntelliJ IDEA](https://www.jetbrains.com/idea/), this guide will be focused on that IDE.
However, the steps below should apply to other IDEs as well, with some minor changes.

The Paper team uses [Gradle](https://gradle.org/) as its build system, and its tools are implemented for Gradle.
Most of the code below can be altered to work with other build systems, such as Maven, but this guide will only cover Gradle.

Follow the guide [here](https://docs.gradle.org/current/userguide/migrating_from_maven.html) to learn how to migrate from Maven to Gradle.

## Creating a new project

[Section titled “Creating a new project”](#creating-a-new-project)

Open your IDE and select the option to create a new project.
In IntelliJ, you will get the option to select the type of project you want to create - select `New Project`.
Select `Gradle - Kotlin DSL` and click `Create`.

You will land into the `build.gradle.kts` file where you can add your dependencies.

### Adding Paper as a dependency

[Section titled “Adding Paper as a dependency”](#adding-paper-as-a-dependency)

To add Paper as a dependency, you will need to add the Paper repository to your `build.gradle.kts` or `pom.xml` file as well as the dependency itself.

* [Gradle (Kotlin)](#tab-panel-77)
* [Gradle (Groovy)](#tab-panel-78)
* [Maven](#tab-panel-79)

build.gradle.kts

```java
repositories {

maven {

name = "papermc"

url = uri("https://repo.papermc.io/repository/maven-public/")

}

}

dependencies {

compileOnly("io.papermc.paper:paper-api:1.21.11-R0.1-SNAPSHOT")

}

java {

toolchain.languageVersion.set(JavaLanguageVersion.of(21))

}
```

build.gradle

```java
repositories {

maven {

name = 'papermc'

url = 'https://repo.papermc.io/repository/maven-public/'

}

}

dependencies {

compileOnly 'io.papermc.paper:paper-api:1.21.11-R0.1-SNAPSHOT'

}
```

pom.xml

```java
<project>

<repositories>

<repository>

<id>papermc</id>

<url>https://repo.papermc.io/repository/maven-public/</url>

</repository>

</repositories>

<dependencies>

<dependency>

<groupId>io.papermc.paper</groupId>

<artifactId>paper-api</artifactId>

<version>1.21.11-R0.1-SNAPSHOT</version>

<scope>provided</scope>

</dependency>

</dependencies>

</project>
```

  

### Setting up the `src` directory

[Section titled “Setting up the src directory”](#setting-up-the-src-directory)

Note

If your IDE creates a `src` directory automatically, you can skip this step.

To set up the `src` directory, you will need to create a new directory called `src` and then create a new directory called `main` inside of it.
Inside of `main`, create two new directories called `java` and `resources`.

It should look like this:

* Directoryexample-plugin/
  + build.gradle.kts
  + settings.gradle.kts
  + Directorysrc/
    - Directorymain/
      * Directoryjava/
        + …
      * Directoryresources/
        + …

### Setting up the `java` directory

[Section titled “Setting up the java directory”](#setting-up-the-java-directory)

You will place your Java source files in the `java` directory. You first need to create some packages to organize your code.
For this example, we will create three packages called `io.papermc.testplugin` and then create a class called `ExamplePlugin` inside of it.

* Directoryexample-plugin/
  + build.gradle.kts
  + settings.gradle.kts
  + Directorysrc/
    - Directorymain/
      * Directoryjava/
        + Directoryio/
          - Directorypapermc/
            * Directorytestplugin/
              + ExamplePlugin.java
      * Directoryresources/
        + …

### Packages

[Section titled “Packages”](#packages)

You can see here that the `ExamplePlugin` class is inside the `io.papermc.testplugin` package.
A package is a way to organize your code - essentially, it’s a folder. Java packages are used to group related classes.
Oracle has a guide on [packages](https://docs.oracle.com/javase/tutorial/java/package/packages.html) if you want to learn more.

When [naming](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html) your packages, you should use your domain name in reverse order. For example, if your domain name is `papermc.io`,
your package name should be `io.papermc`. If you do not have a domain name, you could use something like your GitHub username.
If you were Linus Torvalds, your package would be `io.github.torvalds`.

This is then followed by the name of your project.
For example, if your project was called `ExamplePlugin`, your package would be `io.github.torvalds.exampleplugin`.
This allows for a unique package name for every plugin.

### The *main* class

[Section titled “The main class”](#the-main-class)

The main class is the entry point to your plugin and will be the only class that extends
[`JavaPlugin`](https://jd.papermc.io/paper/org/bukkit/plugin/java/JavaPlugin.html) in your plugin.
This is an example of what your `ExamplePlugin` class could look like:

ExamplePlugin.java

```java
package io.papermc.testplugin;

import net.kyori.adventure.text.Component;

import org.bukkit.Bukkit;

import org.bukkit.event.EventHandler;

import org.bukkit.event.Listener;

import org.bukkit.event.player.PlayerJoinEvent;

import org.bukkit.plugin.java.JavaPlugin;

public class ExamplePlugin extends JavaPlugin implements Listener {

@Override

public void onEnable() {

Bukkit.getPluginManager().registerEvents(this, this);

}

@EventHandler

public void onPlayerJoin(PlayerJoinEvent event) {

event.getPlayer().sendMessage(Component.text("Hello, " + event.getPlayer().getName() + "!"));

}

}
```

### Setting up the `resources`

[Section titled “Setting up the resources”](#setting-up-the-resources)

The `resources` directory is where you will place your plugin’s `plugin.yml` file. See the [Plugin YML](https://docs.papermc.io/paper/dev/plugin-yml) page for more information.

## Using the Minecraft Development IntelliJ plugin

[Section titled “Using the Minecraft Development IntelliJ plugin”](#using-the-minecraft-development-intellij-plugin)

Alternatively, you can use the [Minecraft Development IntelliJ plugin](https://plugins.jetbrains.com/plugin/8327-minecraft-development)
to create a new project.

Note

This tutorial only works with IntelliJ IDEA. If you are using another IDE, please follow the manual project setup guide described above.

### Installing the Minecraft Development plugin

[Section titled “Installing the Minecraft Development plugin”](#installing-the-minecraft-development-plugin)

The first thing you need to do is install the [Minecraft Development](https://plugins.jetbrains.com/plugin/8327-minecraft-development) plugin.
You can do this by going to `File > Settings > Plugins` and searching for `Minecraft Development` under the `Marketplace` section.

![](https://docs.papermc.io/_astro/installing-plugin.C20qTP_2_1dCgj5.webp)

Once you have installed the plugin, you will need to restart IntelliJ.
To do that you can click the `Restart IDE` button that appears after installing the plugin.

![](https://docs.papermc.io/_astro/restart-ide.F2xwJWmT_1mxKOL.webp)

### Creating a new project

[Section titled “Creating a new project”](#creating-a-new-project-1)

Once you have installed the plugin, you can create a new project by going to `File > New > Project...` and selecting `Minecraft` from the list of options.

![](https://docs.papermc.io/_astro/new-project-paper.D5YNPCqf_I8H4.webp)

You will be asked to provide some information about your project.

| Field | Explanation |
| --- | --- |
| **Name** | The name of your project. |
| **Location** | The location of your project. This is where the project files will be stored. |
| **Platform Type** | The platform type you are developing for. This should be `Plugin`. |
| **Platform** | The platform you are developing for. This should be `Paper`. |
| **Minecraft Version** | The version of Minecraft you are developing for. |
| **Plugin Name** | The name of your plugin. |
| **Main Class** | The main class of your plugin. This should be the class that extends `JavaPlugin`. |
| **Optional Settings** | Here you can define things like authors, website, description, etc. These are optional and not required for the plugin to work. |
| **Build System** | The build system you want to use. Paper recommends using Gradle but you can use Maven if you prefer. |
| **Paper Manifest** | Whether you want to use the new Paper plugins or not. For now this is not recommended as it is still in development. |
| **Group ID** | The group ID of your project. This is used for Maven and Gradle. This is usually your domain name in reverse. If you don’t know what you should put here, you can use something like `io.github.<yourname>` or if you don’t have GitHub you can use `me.<yourname>`. |
| **Artifact ID** | The artifact ID of your project. This is used for Maven and Gradle. This is usually the name of your project. This is usually the same as the `Name` field. |
| **Version** | The version of your project. This is used for Maven and Gradle. This is usually `1.0-SNAPSHOT` and does not really matter for now. |
| **JDK** | The JDK you want to use. This can be anything from Java 21 and above. |

Now you can click on the `Create` button and IntelliJ will create the project for you.
If everything went well, you should see something like this:

![](https://docs.papermc.io/_astro/paper-plugin-overview.93vGrB36_ZU0iII.webp)

## Plugin remapping

[Section titled “Plugin remapping”](#plugin-remapping)

As of 1.20.5, Paper ships with a Mojang-mapped runtime instead of reobfuscating the server to Spigot mappings.
If you are using Spigot/Bukkit plugins, your plugin will be assumed to be Spigot-mapped.
This means that the server will have to deobfuscate and remap the plugin JAR when it’s loaded for the first time.

Note

`paperweight-userdev` already sets this attribute automatically. For more information see the [userdev](https://docs.papermc.io/paper/dev/userdev) documentation.

### Mojang mappings

[Section titled “Mojang mappings”](#mojang-mappings)

To tell the server that your plugin is Mojang-mapped, you need to add the following code to your build script:

Paper plugins

If you are using Paper plugins, this step is not needed as plugins will be assumed to be Mojang-mapped.

* [Gradle (Kotlin)](#tab-panel-80)
* [Gradle (Groovy)](#tab-panel-81)
* [Maven](#tab-panel-82)

build.gradle.kts

```java
tasks.jar {

manifest {

attributes["paperweight-mappings-namespace"] = "mojang"

}

}

// if you have shadowJar configured

tasks.shadowJar {

manifest {

attributes["paperweight-mappings-namespace"] = "mojang"

}

}
```

build.gradle

```java
jar {

manifest {

attributes(

'paperweight-mappings-namespace': 'mojang'

)

}

}

// if you have shadowJar configured

shadowJar {

manifest {

attributes(

'paperweight-mappings-namespace': 'mojang'

)

}

}
```

pom.xml

```java
<plugin>

<groupId>org.apache.maven.plugins</groupId>

<artifactId>maven-jar-plugin</artifactId>

<version>3.4.1</version>

<configuration>

<archive>

<manifestEntries>

<paperweight-mappings-namespace>mojang</paperweight-mappings-namespace>

</manifestEntries>

</archive>

</configuration>

</plugin>
```

 

### Spigot mappings

[Section titled “Spigot mappings”](#spigot-mappings)

If you explicitly want to tell the server that your plugin is Spigot-mapped, you need to add the following code to your build script:

* [Gradle (Kotlin)](#tab-panel-83)
* [Gradle (Groovy)](#tab-panel-84)
* [Maven](#tab-panel-85)

build.gradle.kts

```java
tasks.jar {

manifest {

attributes["paperweight-mappings-namespace"] = "spigot"

}

}

// if you have shadowJar configured

tasks.shadowJar {

manifest {

attributes["paperweight-mappings-namespace"] = "spigot"

}

}
```

build.gradle

```java
jar {

manifest {

attributes(

'paperweight-mappings-namespace': 'spigot'

)

}

}

// if you have shadowJar configured

shadowJar {

manifest {

attributes(

'paperweight-mappings-namespace': 'spigot'

)

}

}
```

pom.xml

```java
<plugin>

<groupId>org.apache.maven.plugins</groupId>

<artifactId>maven-jar-plugin</artifactId>

<version>3.4.1</version>

<configuration>

<archive>

<manifestEntries>

<paperweight-mappings-namespace>spigot</paperweight-mappings-namespace>

</manifestEntries>

</archive>

</configuration>

</plugin>
```

 

## Conclusion

[Section titled “Conclusion”](#conclusion)

You should now have a project set up with Paper as a dependency.
All you have left to do now is to compile your plugin and run it on a Paper server.

Note

If you want to streamline the process of testing a plugin, you can use the [Run-Task](https://github.com/jpenilla/run-task) Gradle plugin.
It will automatically download a Paper server and run it for you.

Note

If you are using IntelliJ, you can use the Gradle GUI `Build` menu to compile your plugin - found on the top right of your IDE.
The output JAR of your plugin will be in the `build/libs` directory.


================================================================================
Chapter Title: How plugins work
Original Link: https://docs.papermc.io/paper/dev/how-do-plugins-work/
================================================================================

Plugins are a way to extend the functionality of a Minecraft server. They are written in JVM-based languages such as
Java, Kotlin, Groovy or Scala. Plugins are loaded from the `plugins` folder in the server directory. Plugins will be
loaded from a `.jar` file. Each plugin has a main class that is specified in the plugin’s `plugin.yml` file. This
class must extend JavaPlugin, and is the entry point for the plugin and is where the plugin’s lifecycle methods are
defined.

Caution

We do not recommend writing code inside your main class’s constructor as there are no guarantees about what
API is available at that point. Instead, you should use the `onLoad` method to initialize your plugin. Also,
do not call your plugin’s constructor directly. This will cause issues with your plugin.

## Plugin lifecycle

[Section titled “Plugin lifecycle”](#plugin-lifecycle)

Plugins are loaded and unloaded at runtime. When a plugin is loaded, it is initialized and enabled. When a plugin is
unloaded, it is disabled and finalized.

### Initialization

[Section titled “Initialization”](#initialization)

When a plugin is loaded, it is initialized. This means that the plugin is loaded into memory and its `onLoad`
method is called. This method is used to initialize the plugin and set up any resources that it needs. Most of the
Bukkit API is not available at this point, so it is not safe to interact with it.

### Enabling

[Section titled “Enabling”](#enabling)

When a plugin is enabled, its `onEnable` method is called. This method is used to set up any resources that the plugin
needs to run. This method is called when the plugin is initialized but before the server has started ticking, so it is
safe to register event listeners and other resources that the plugin needs to run, however often not safe to interact
with a lot of APIs.

This is when you can also open database connections, start threads, and other things that are not safe to do in the
`onLoad` method.

### Disabling

[Section titled “Disabling”](#disabling)

When a plugin is disabled, its `onDisable` method is called. This method is used to clean up any resources that the
plugin has allocated. This method is called before all plugins are unloaded, and is meant for any cleanup that needs to
be done before the plugin is unloaded. This may include saving data to disk or closing connections to databases.

## Event listeners

[Section titled “Event listeners”](#event-listeners)

Events are a way for plugins to listen to things that happen in the server and run code when they are fired. For
example, [`PlayerJoinEvent`](https://jd.papermc.io/paper/org/bukkit/event/player/PlayerJoinEvent.html) is fired when a player
joins the server. This is a more performant way to run code when something happens, as opposed to constantly checking.
See our [event listener page](https://docs.papermc.io/paper/dev/event-listeners) for more.

Some events are cancellable. This means that when the event is fired, it can be cancelled which negates or stops the
effect of the event. For example, [`PlayerMoveEvent`](https://jd.papermc.io/paper/org/bukkit/event/player/PlayerMoveEvent.html)
is cancellable. This means that when it is cancelled, the player will not move. This is useful for things like anti-cheat,
where you want to cancel the event if the player is moving too fast.

It is important to think about how “hot” an event is when writing event listeners. A “hot” event is an event that is fired
very often. For example, `PlayerMoveEvent` is fired every time a player moves. This means that if you have a lot of
expensive code in your event listener, it will be run every time a player moves. This can cause a lot of lag. It is
important to keep event listeners as lightweight as possible. One possible way is to quickly check if the event should
be handled, and if not, return. For example, if you only want to handle the event if the player is moving from one block
to another, you can check if the player’s location has changed blocks. If it hasn’t, you can return from the listener.

## Commands

[Section titled “Commands”](#commands)

Commands are a way for players, the console, RCON and command blocks to run code on the server. Commands are registered
by plugins and can be run by command senders. For example, the `/help` command is registered by the server and can be
run by players. Commands can be run by players by typing them in the chat or by running them from a command block.

Commands can have arguments. For example, the `/give` command takes an argument for the player to give the item to and
an argument for the item to give. Arguments are separated by spaces. For example, the command `/give Notch diamond` will
give the player named Notch a diamond. Note here that the arguments are `["Notch", "diamond"]`.

### Permissions

[Section titled “Permissions”](#permissions)

Permissions are a way to control who can run commands and who can listen to events. Permissions
are registered by plugins and can be checked by other plugins. Permissions can be granted to players and groups.
Permissions can have a hierarchical nature, if defined so by the plugin in their `plugin.yml`. For example, a
plugin can define `example.command.help` as a sub-permission of `example.command`. This means that if a player
has the `example.command` permission, they will also have the `example.command.help` permission.

Note

Permission plugins can allow the usage of wildcard permissions using the `*` character to grant any permission
or sub-permission available, allowing hierarchical permissions even if not set by the plugin itself. For example,
granting `example.command.*` through a permission plugin with wildcard support will grant access to all permissions
starting with `example.command.` itself.

It is **not** recommended to use wildcard permissions, especially `*` (All permissions), as it can be a huge
security risk, as well as potentially causing unwanted side effects to a player. Use with caution.

## Configuration

[Section titled “Configuration”](#configuration)

Plugins can have configuration files. These files are used to store data that the plugin needs to run. For example, a
plugin that adds a new block to the game might have a configuration file that stores the block’s ID. Configuration files
should be stored in the plugin’s data folder, within the `plugins` folder. The server offers a YAML configuration API
that can be used to read and write configuration files. See [here](https://docs.papermc.io/paper/dev/plugin-configurations) for more information.

## Scheduling tasks

[Section titled “Scheduling tasks”](#scheduling-tasks)

Plugins can schedule tasks to run at a later time. This is useful for things like running code after a certain amount
of time has passed. For example, a plugin might want to run code after 5 seconds. This can be done by scheduling a task
to run after 100 ticks - one second is 20 ticks during normal operation. It is important to note that tasks might be
delayed if the server is lagging. For example, if the server is only running at 10 ticks per second, a task that is
scheduled to run after 100 ticks will take 10 seconds.

In Java, typically you could use [`Thread#sleep()`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Thread.html#sleep(long)) to delay
the execution of code. However, if the code is running on the main thread, this will cause the server to pause for the
delay. Instead, you should use the `Scheduler` API to schedule tasks to run later.
Learn more about the `Scheduler` API [here](https://docs.papermc.io/paper/dev/scheduler).

## Components

[Section titled “Components”](#components)

Since Minecraft 1.7 and the introduction of “components”, plugins can now send messages to players that contain
rich text. This means that plugins can send messages that contain things like colors, bold text, and clickable links.
Colors were always possible, but only through the use of legacy color codes.

Paper implements a library called `Adventure` that makes it easy to create and send messages to players. Learn more
about the `Adventure` API [here](https://docs.papermc.io/adventure/) from their docs or our docs
[here](https://docs.papermc.io/paper/dev/component-api/introduction).


================================================================================
Chapter Title: Paper pluginsExperimental
Original Link: https://docs.papermc.io/paper/dev/getting-started/paper-plugins/
================================================================================

Paper plugins allow developers to take advantage of more modern concepts introduced by Mojang, such as datapacks, to
expand the field of what the Paper API is able to introduce.

Experimental

This is experimental and may be subject to change.

* [Bootstrapper](#bootstrapper)
* [Loader](#loaders)
* [Differences](#differences)

## How do I use them?

[Section titled “How do I use them?”](#how-do-i-use-them)

Similarly to Bukkit plugins, you have to introduce a `paper-plugin.yml` file into your JAR resources folder.
This will not act as a drop-in replacement for `plugin.yml`, as some things, as outlined in this guide, need to be declared differently.

It should be noted that you still have the ability to include both `paper-plugin.yml` and `plugin.yml` in the same JAR.

Here is an example configuration:

```java
name: Paper-Test-Plugin

version: '1.0'

main: io.papermc.testplugin.TestPlugin

description: Paper Test Plugin

api-version: '1.21.11'

bootstrapper: io.papermc.testplugin.TestPluginBootstrap

loader: io.papermc.testplugin.TestPluginLoader
```

### Dependency declaration

[Section titled “Dependency declaration”](#dependency-declaration)

Paper plugins change how to declare dependencies in your `paper-plugin.yml`:

```java
dependencies:

bootstrap:

# Let's say that RegistryPlugin registers some data that your plugin needs to use

# We don't need this during runtime, so it's not required in the server section.

# However, can be added to both if needed

RegistryPlugin:

load: BEFORE

required: true

join-classpath: true # Defaults to true

server:

# Add a required "RequiredPlugin" dependency, which will load AFTER your plugin.

RequiredPlugin:

load: AFTER

required: true

# This means that your plugin will not have access to their classpath

join-classpath: false
```

With Paper plugins, dependencies are split into two sections:

* `bootstrap` - These are dependencies that you will be using in the [bootstrap](#bootstrapper).
* `server` - These are dependencies that are used for the core functionality of your plugin, whilst the server is running.

Let’s take a look at a dependency:

```java
RegistryPlugin:

load: BEFORE # Defaults to OMIT

required: true # Defaults to true

join-classpath: true # Defaults to true
```

* `load` (`BEFORE`|`AFTER`|`OMIT`): Whether this plugin should load before or after **your** plugin. Note: `OMIT` has undefined ordering behavior.
* `required`: Whether this plugin is required for your plugin to load.
* `join-classpath`: Whether your plugin should have access to their classpath. This is used for plugins that need to access other plugins internals directly.

Cyclic Loading

Note that in certain cases, plugins may be able to introduce cyclic loading loops, which will prevent the server from starting.
Please read the [cyclic loading guide](#cyclic-plugin-loading) for more information.

Here are a couple of examples:

```java
# Suppose we require ProtocolLib to be loaded for our plugin

ProtocolLib:

load: BEFORE

required: true

# Now, we are going to register some details for a shop plugin

# So the shop plugin should load after our plugin

SuperShopsXUnlimited:

load: AFTER

required: false

# Now, we are going to need to access a plugins classpath

# So that we can properly interact with it.

SuperDuperTacoParty:

required: true

join-classpath: true
```

## What is it used for?

[Section titled “What is it used for?”](#what-is-it-used-for)

Paper plugins lay down the framework for some future API. Our goals are to open more modern API that better aligns
with Vanilla. Paper plugins allow us to do just that by making a new way to load plugin resources before the server
has started by using [bootstrappers](#bootstrapper).

## Bootstrapper

[Section titled “Bootstrapper”](#bootstrapper)

Paper plugins are able to identify their own bootstrapper by implementing
[`PluginBootstrap`](https://jd.papermc.io/paper/io/papermc/paper/plugin/bootstrap/PluginBootstrap.html)
and adding the class of your implementation to the bootstrapper field in the `paper-plugin.yml`.

TestPluginBootstrap.java

```java
public class TestPluginBootstrap implements PluginBootstrap {

@Override

public void bootstrap(BootstrapContext context) {

}

@Override

public JavaPlugin createPlugin(PluginProviderContext context) {

return new TestPlugin("My custom parameter");

}

}
```

A bootstrapper also allows you to change the way your plugin is initialized, allowing you to pass values into your plugin constructor.
Currently, bootstrappers do not offer much new API and are highly experimental. This may be subject to change once more API is introduced.

## Loaders

[Section titled “Loaders”](#loaders)

Paper plugins are able to identify their own plugin loader by implementing
[`PluginLoader`](https://jd.papermc.io/paper/io/papermc/paper/plugin/loader/PluginLoader.html)
and adding the class of your implementation to the loader field in the `paper-plugin.yml`.

The goal of the plugin loader is the creation of an expected/dynamic environment for the plugin to load into.
This, as of right now, only applies to creating the expected classpath for the plugin, e.g. supplying external libraries to the plugin.

TestPluginLoader.java

```java
public class TestPluginLoader implements PluginLoader {

@Override

public void classloader(PluginClasspathBuilder classpathBuilder) {

classpathBuilder.addLibrary(new JarLibrary(Path.of("dependency.jar")));

MavenLibraryResolver resolver = new MavenLibraryResolver();

resolver.addDependency(new Dependency(new DefaultArtifact("com.example:example:version"), null));

resolver.addRepository(new RemoteRepository.Builder("paper", "default", "https://repo.papermc.io/repository/maven-public/").build());

classpathBuilder.addLibrary(resolver);

}

}
```

Currently, you are able to add two different library types:
[`JarLibrary`](https://jd.papermc.io/paper/io/papermc/paper/plugin/loader/library/impl/JarLibrary.html) and
[`MavenLibraryResolver`](https://jd.papermc.io/paper/io/papermc/paper/plugin/loader/library/impl/MavenLibraryResolver.html).

Danger

If you wish to resolve libraries from Maven Central, use a mirror, as using Maven Central directly as a CDN is against the Maven Central Terms of Service, and users of your plugin may hit rate limits.

You should use Paper’s default mirror, configured by the [`PAPER_DEFAULT_CENTRAL_REPOSITORY`](https://docs.papermc.io/paper/reference/system-properties#paper_default_central_repository) environment variable and [`org.bukkit.plugin.java.LibraryLoader.centralURL`](https://docs.papermc.io/paper/reference/system-properties#orgbukkitpluginjavalibraryloadercentralurl) system property:

```java
resolver.addRepository(new RemoteRepository.Builder("central", "default", MavenLibraryResolver.MAVEN_CENTRAL_DEFAULT_MIRROR).build());
```

Using the Maven Central repository (i.e. `*.maven.org` or `*.maven.apache.org`) will cause a warning to be shown in the console.

## Differences

[Section titled “Differences”](#differences)

### Bukkit serialization system

[Section titled “Bukkit serialization system”](#bukkit-serialization-system)

Paper plugins still support the serialization system (`org.bukkit.configuration.serialization`) that Bukkit uses. However, custom classes will not be
automatically registered for serialization. In order to use [`ConfigurationSection#getObject`](https://jd.papermc.io/paper/org/bukkit/configuration/ConfigurationSection.html#getObject(java.lang.String,java.lang.Class)),
you **must** call [`ConfigurationSerialization#registerClass(Class)`](https://jd.papermc.io/paper/org/bukkit/configuration/serialization/ConfigurationSerialization.html#registerClass(java.lang.Class))
before you attempt to fetch objects from configurations.

### Classloading isolation

[Section titled “Classloading isolation”](#classloading-isolation)

Paper plugins are not able to access each other unless given explicit access by depending on another plugin, etc. This
helps prevent Paper plugins from accidentally accessing each other’s dependencies, and in general helps ensure that
plugins are only able to access what they explicitly depend on.

Paper plugins have the ability to bypass this, being able to access OTHER plugins’ classloaders by adding a `join-classpath` option to their `paper-plugin.yml`.

```java
Plugin:

join-classpath: true # Means you have access to their classpath
```

Note, other Paper plugins will still be unable to access your classloader.

### Load order logic split

[Section titled “Load order logic split”](#load-order-logic-split)

In order to better take advantage of classloading isolation, Paper plugins do **not** use the `dependencies` field to determine load order.
This was done for a variety of reasons, mostly to allow better control and allow plugins to properly share classloaders.

See [declaring dependencies](#dependency-declaration) for more information on how to declare the load order of your plugin.

### Commands

[Section titled “Commands”](#commands)

Paper plugins do not use the `commands` field to register commands. This means that you do not need to include all
of your commands in the `paper-plugin.yml` file. Instead, you can register commands using the
[Brigadier Command API](https://docs.papermc.io/paper/dev/command-api/basics/introduction).

### Cyclic plugin loading

[Section titled “Cyclic plugin loading”](#cyclic-plugin-loading)

Cyclic loading describes the phenomenon when a plugin loading causes a loop that eventually cycles back to the original plugin.
Unlike Bukkit plugins, Paper plugins will not attempt to resolve cyclic loading issues.

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/getting-started/paper-plugins-0.svg)

However, if Paper detects a loop that cannot be resolved, you will get an error that looks like this:

```java
[ERROR]: [LoadOrderTree] =================================

[ERROR]: [LoadOrderTree] Circular plugin loading detected:

[ERROR]: [LoadOrderTree] 1) Paper-Test-Plugin1 -> Paper-Test-Plugin -> Paper-Test-Plugin1

[ERROR]: [LoadOrderTree]    Paper-Test-Plugin1 loadbefore: [Paper-Test-Plugin]

[ERROR]: [LoadOrderTree]    Paper-Test-Plugin loadbefore: [Paper-Test-Plugin1]

[ERROR]: [LoadOrderTree] Please report this to the plugin authors of the first plugin of each loop or join the PaperMC Discord server for further help.

[ERROR]: [LoadOrderTree] =================================
```

It is up to you to resolve these cyclical loading issues.


================================================================================
Chapter Title: plugin.yml
Original Link: https://docs.papermc.io/paper/dev/plugin-yml/
================================================================================

The `plugin.yml` file is the main configuration file for your plugin.
It contains information about your plugin, such as its name, version, and description.
It also contains information about the plugin’s dependencies, permissions, and commands.

The `plugin.yml` file is located in the `resources` directory of your project.

* Directoryexample-plugin/
  + build.gradle.kts
  + settings.gradle.kts
  + Directorysrc/
    - Directorymain/
      * Directoryjava/
        + …
      * Directoryresources/
        + **plugin.yml**

## Example

[Section titled “Example”](#example)

Here is an example of a `plugin.yml` file:

```java
name: ExamplePlugin

version: 1.0.0

main: io.papermc.testplugin.ExamplePlugin

description: An example plugin

author: PaperMC

website: https://papermc.io

api-version: '1.21.11'
```

## Fields

[Section titled “Fields”](#fields)

Note

The fields in this section are not in any particular order.
If they have an asterisk (\*) next to them, that means they are required.

### name\*

[Section titled “name\*”](#name)

The name of your plugin. This is what will be displayed in the plugin list and log messages.
This will be overridden in the logs if the prefix is set.

* `name: ExamplePlugin`

### version\*

[Section titled “version\*”](#version)

The current version of the plugin. This is shown in plugin info messages and server logs.

* `version: 1.0.0`

### main\*

[Section titled “main\*”](#main)

The main class of your plugin. This is the class that extends `JavaPlugin` and is the entry point to your plugin.

* `main: io.papermc.testplugin.ExamplePlugin`

This is the package path and class name of your main class.

### description

[Section titled “description”](#description)

A short description of your plugin and what it does. This will be shown in the plugin info commands.

* `description: An example plugin`

### author / authors

[Section titled “author / authors”](#author--authors)

The author(s) of the plugin. This can be a single author or a list of authors.

* `author: PaperMC`
* `authors: [PaperMC, SpigotMC, Bukkit]`
  These will be shown in the plugin info commands.

### contributors

[Section titled “contributors”](#contributors)

The contributors to the plugin that aren’t the managing author(s).

* `contributors: [PaperMC, SpigotMC, Bukkit]`
  These will be shown in the plugin info commands.

### website

[Section titled “website”](#website)

The website of the plugin. This is useful for linking to a GitHub repository or a plugin page.

* `website: https://papermc.io`
  This will be shown in the plugin info commands.

### api-version

[Section titled “api-version”](#api-version)

The version of the Paper API that your plugin is using. This doesn’t include the minor version until 1.20.5. From 1.20.5 and onward, a minor version is supported.
Servers with a version lower than the version specified here will refuse to load the plugin.
The valid versions are 1.13 - 1.21.11.

* `api-version: '1.21.11'`

Note

If this is not specified, the plugin will be loaded as a legacy plugin and a warning will be printed to the console.

### load

[Section titled “load”](#load)

This tells the server when to load the plugin. This can be `STARTUP` or `POSTWORLD`. Will default to `POSTWORLD` if not specified.

* `load: STARTUP`

### prefix

[Section titled “prefix”](#prefix)

The prefix of the plugin. This is what will be displayed in the log instead of the plugin name.

* `prefix: EpicPaperMCHypePlugin`

### libraries

[Section titled “libraries”](#libraries)

This is a list of libraries that your plugin depends on. These libraries will be downloaded from the Maven Central repository and added to the classpath.
This removes the need to shade and relocate the libraries.

```java
libraries:

- com.google.guava:guava:30.1.1-jre

- com.google.code.gson:gson:2.8.6
```

Note

The central repository is configurable using the [`PAPER_DEFAULT_CENTRAL_REPOSITORY`](https://docs.papermc.io/paper/reference/system-properties#paper_default_central_repository) environment variable and [`org.bukkit.plugin.java.LibraryLoader.centralURL`](https://docs.papermc.io/paper/reference/system-properties#orgbukkitpluginjavalibraryloadercentralurl) system property.

### permissions

[Section titled “permissions”](#permissions)

This is a list of permissions that your plugin uses. This is useful for plugins that use permissions to restrict access to certain features.

```java
permissions:

permission.node:

description: "This is a permission node"

default: op

children:

permission.node.child: true

another.permission.node:

description: "This is another permission node"

default: notop
```

The description is the description of the permission node. This is what will be displayed in the permissions list.
The default is the default value of the permission node. This can be `op`/`notop` or `true`/`false`.
This defaults to the value of `default-permission` if not specified, which in turn defaults to `op`.
Each permission node can have children. When set to `true`, it will inherit the parent permission.

### default-permission

[Section titled “default-permission”](#default-permission)

The default value that permissions that don’t have a `default` specified will have. This can be `op`/`notop` or `true`/`false`.

* `default-permission: true`

### paper-plugin-loader

[Section titled “paper-plugin-loader”](#paper-plugin-loader)

A fully qualified class name of a Paper plugin [loader](https://docs.papermc.io/paper/dev/getting-started/paper-plugins#loaders) class, if you want to use one.

* `paper-plugin-loader: com.example.paperplugin.MyPluginLoader`

Experimental

[Paper plugins](https://docs.papermc.io/paper/dev/getting-started/paper-plugins) (and therefore plugin loaders) are experimental and may be subject to change.

### paper-skip-libraries

[Section titled “paper-skip-libraries”](#paper-skip-libraries)

If `true`, Paper will skip resolution of libraries defined in the [`libraries` section](#libraries).
This is useful for delegating library loading to a Paper plugin [loader](https://docs.papermc.io/paper/dev/getting-started/paper-plugins#loaders).

* `paper-skip-libraries: false`

Experimental

[Paper plugins](https://docs.papermc.io/paper/dev/getting-started/paper-plugins) (and therefore plugin loaders) are experimental and may be subject to change.

## Commands

[Section titled “Commands”](#commands)

This is a list of commands that your plugin uses. This is useful for plugins that use commands to provide features.

```java
commands:

command:

description: "This is a command"

usage: "/command <arg>"

aliases: [cmd, command]

permission: permission.node

permission-message: "You do not have permission to use this command"
```

* `description` is the description of the command. This gives a brief description of what the command does.
* `usage` is the usage of the command. This is what will be displayed when the player uses `/help <command>`.
* `aliases` are a list of aliases that the command can be used with. This is useful for shortening the command.
* `permission` is the permission node that the player needs to use the command. Note: Players will only see commands they have permission to use.
* `permission-message` is the message that will be displayed when the player does not have permission to use the command.

## Dependencies

[Section titled “Dependencies”](#dependencies)

Dependency Loops

If a plugin is specified as a dependency, it will be loaded before your plugin.
Be careful as these can cause plugin load issues if cyclical dependencies appear. A cyclical dependency can be illustrated as follows:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/getting-started/plugin-yml-0.svg)

Where `Plugin A` and `Plugin B` are plugins that depend on each other.

### depend

[Section titled “depend”](#depend)

A list of plugins that your plugin depends on to **load**. They are specified by their plugin name.

Note

If the plugin is not found, your plugin will not load.

* `depend: [Vault, WorldEdit]`

### softdepend

[Section titled “softdepend”](#softdepend)

A list of plugins that your plugin depends on to have **full functionality**. They are specified by their plugin name.

* `softdepend: [Vault, WorldEdit]`

### loadbefore

[Section titled “loadbefore”](#loadbefore)

A list of plugins that your plugin should be loaded **before**. They are specified by their plugin name.
This is useful if you want to load your plugin before another plugin for the other plugin to use your plugin’s API.

* `loadbefore: [Vault, FactionsUUID]`

### provides

[Section titled “provides”](#provides)

This can be used to tell the server that this plugin will provide the functionality of some library or other plugin (like an alias system).
Plugins that (soft)depend on the other plugin will treat your plugin as if the other plugin exists when resolving dependencies or using
[`PluginManager#getPlugin(String)`](https://jd.papermc.io/paper/org/bukkit/plugin/PluginManager.html#getPlugin(java.lang.String)).

* `provides: [SomeOtherPlugin]`


================================================================================
Chapter Title: paperweight-userdev
Original Link: https://docs.papermc.io/paper/dev/userdev/
================================================================================

**paperweight** is the name of Paper’s custom build tooling. The **paperweight-userdev** Gradle plugin part of that
provides access to internal code (also known as NMS) during development.

Note

This guide is written using the Gradle Kotlin DSL and assumes you have some basic knowledge of Gradle.
If you want to see a fully-functioning plugin that uses **paperweight-userdev**,
check out this [example plugin](https://github.com/PaperMC/paperweight-test-plugin).

## Why this is useful

[Section titled “Why this is useful”](#why-this-is-useful)

This is the only supported way of accessing server internals, as redistributing the server JAR is against the
Minecraft EULA and general license assumption. Even if you manually depended on the patched server, you would be
hindering other people working on your project and would be missing deployed API javadocs/sources in your IDE.

On top of that, Spigot and pre-1.20.5 Paper versions still use Spigot mappings, which are a mix of obfuscated fields/methods
and mapped as well as custom named classes. This can make it hard to work with in a development environment. This plugin lets you use
fully deobfuscated types, names, and fields during development, and then remaps your plugin, so it can still be used with the obfuscated
server. However, this does not apply to reflection. Look at something like [this library](https://github.com/jpenilla/reflection-remapper) to be able to
use non-obfuscated names in reflection if you want to support obfuscated servers.

1.20.5 Mojang-mapped runtime

As of Minecraft version 1.20.5, Paper ships with a Mojang-mapped runtime instead of re-obfuscating the server to Spigot mappings.
See [here](#1205-and-beyond) for more details.

## Adding the plugin

[Section titled “Adding the plugin”](#adding-the-plugin)

Add the plugin to your `build.gradle.kts` file.

build.gradle.kts

```java
plugins {

id("io.papermc.paperweight.userdev") version "2.0.0-beta.19"

}
```

Gradle Version

Please make sure you are using the latest stable version of Gradle.
For more information on upgrading Gradle, check out the [Gradle Wrapper documentation](https://docs.gradle.org/current/userguide/gradle_wrapper.html).

The latest version of `paperweight-userdev` supports dev bundles for Minecraft 1.17.1 and newer, so it’s best practice to keep it up to date!
Only the latest version of `paperweight-userdev` is officially supported, and we will ask you to update first if you are having problems with old versions.
Furthermore, if you are having issues with `paperweight-userdev`, you should ask in the
[`#build-tooling-help`](https://discord.com/channels/289587909051416579/1078993196924813372) channel in our dedicated [Discord server](https://discord.gg/PaperMC)!

Snapshots

**paperweight-userdev** SNAPSHOT (pre-release) versions are only available through Paper’s Maven repository.

settings.gradle.kts

```java
pluginManagement {

repositories {

gradlePluginPortal()

maven("https://repo.papermc.io/repository/maven-public/")

}

}
```

## Adding the dev bundle dependency

[Section titled “Adding the dev bundle dependency”](#adding-the-dev-bundle-dependency)

If you try to load your Gradle project now, you will receive an error saying you have to declare
a dev bundle dependency. You can do that by adding to your `dependencies` block in your `build.gradle.kts`
file.

build.gradle.kts

```java
dependencies {

// Other Dependencies

paperweight.paperDevBundle("1.21.11-R0.1-SNAPSHOT")

}
```

Tip

You should remove any dependency on the Paper API, as the dev bundle includes that.

Configuring the Java toolchain for userdev setup

A given dev bundle may not always support the Java toolchain Gradle is configured to use
(whether configured explicitly or inherited from the Gradle runtime).
If you are getting an error during the execution of `paperweightUserdevSetup` (especially patch application failures),
you can try setting paperweight’s `javaLauncher` property to a different Java version.

For example, with 1.17.1:

build.gradle.kts

```java
paperweight {

javaLauncher = javaToolchains.launcherFor {

// Example scenario:

// Paper 1.17.1 was originally built with JDK 16 and the bundle

// has not been updated to work with 21+ (but we want to compile with a 25 toolchain)

languageVersion = JavaLanguageVersion.of(17)

}

}
```

Among others, the [multi-project branch of the PaperMC/paperweight-test-plugin](https://github.com/PaperMC/paperweight-test-plugin/tree/multi-project)
makes use of this feature.

## Gradle tasks

[Section titled “Gradle tasks”](#gradle-tasks)

### `reobfJar`

[Section titled “reobfJar”](#reobfjar)

This task creates a plugin JAR that is re-obfuscated to Spigot’s runtime mappings.
This means it will work on standard Paper servers.

The output will be inside the `build/libs` folder. The JAR whose filename includes `-dev`
is Mojang-mapped (not re-obfuscated) and will not work on most servers.

Shadow

If you have the shadow Gradle plugin applied in your build script, **paperweight-userdev** will
detect that and use the shaded JAR as the input for the `reobfJar` task.

The `-dev-all.jar` file in `build/libs` is the shaded, but not re-obfuscated JAR.

You can make the `reobfJar` task run on the default `build` task with:

build.gradle(.kts)

```java
tasks.assemble {

dependsOn(tasks.reobfJar)

}
```

## 1.20.5 and beyond

[Section titled “1.20.5 and beyond”](#1205-and-beyond)

As of 1.20.5, Paper ships with a Mojang-mapped runtime instead of re-obfuscating the server to Spigot mappings.
Additionally, CraftBukkit classes will no longer be relocated into a versioned package.
This requires plugins to be deobfuscated before loading when necessary.

Most of this process is done automatically by paperweight, but there are some important things to know when using server internals (or “NMS”) from now on.

### Default mappings assumption

[Section titled “Default mappings assumption”](#default-mappings-assumption)

* By default, all Spigot/Bukkit plugins will be assumed to be Spigot-mapped if they do not specify their mappings namespace in the manifest.
  The other way around, all Paper plugins will be assumed to be Mojang-mapped if they do not specify their mappings namespace in the manifest.
* Spigot-mapped plugins will need to be deobfuscated on first load, Mojang-mapped plugins will not.

### Compiling to Mojang mappings

[Section titled “Compiling to Mojang mappings”](#compiling-to-mojang-mappings)

Note

This is the preferred option, as the one-time plugin remapping process during server startup will be skipped and it
may allow you to keep version compatibility across smaller updates without changes or additional modules.
However, this makes your plugin incompatible with Spigot servers.

If you want your main output to use Mojang mappings, you need to remove all `dependsOn(reobfJar)` lines and add the following code to your build script:

build.gradle.kts

```java
paperweight.reobfArtifactConfiguration = io.papermc.paperweight.userdev.ReobfArtifactConfiguration.MOJANG_PRODUCTION
```

### Compiling to Spigot mappings

[Section titled “Compiling to Spigot mappings”](#compiling-to-spigot-mappings)

If you want your main output to use Spigot mappings, add the following code to your build script:

build.gradle.kts

```java
paperweight.reobfArtifactConfiguration = io.papermc.paperweight.userdev.ReobfArtifactConfiguration.REOBF_PRODUCTION
```

This is useful for plugins that have loaders for both Spigot and Paper and want to keep compatibility with both.

Note

If you are using Gradle with the Groovy DSL, you should instead access the fields via static methods like `getMOJANG_PRODUCTION()`.


================================================================================
Chapter Title: Introduction
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/introduction/
================================================================================

Paper’s command system is built on top of Minecraft’s Brigadier command system. This system provides a powerful and flexible way to define commands and arguments.
It offers many advantages above the previously widely used Bukkit command system:

* Less parsing or error checking required by the developer for arguments.
* Better user experience with client error checking.
* Integration with reload events, allowing the definition of commands usable in datapacks.
* Easier creation of subcommands.

Note

To see a comparison between the new Brigadier system and the old Bukkit system, [click here](https://docs.papermc.io/paper/dev/command-api/misc/comparison-bukkit-brigadier).

## Guide

[Section titled “Guide”](#guide)

Tip

If the Brigadier API seems too complicated, you can start with
[basic commands](https://docs.papermc.io/paper/dev/command-api/misc/basic-command). They
provide a simple way of creating commands, with only a small learning curve.

The following sites are worth-while to look through first when learning about Brigadier:

* [The Command Tree](https://docs.papermc.io/paper/dev/command-api/basics/command-tree)
* [Arguments and Literals](https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals)
* [Command Executors](https://docs.papermc.io/paper/dev/command-api/basics/executors)
* [Command Registration](https://docs.papermc.io/paper/dev/command-api/basics/registration)
* [Command Requirements](https://docs.papermc.io/paper/dev/command-api/basics/requirements)
* [Argument Suggestions](https://docs.papermc.io/paper/dev/command-api/basics/argument-suggestions)
* [Custom Arguments](https://docs.papermc.io/paper/dev/command-api/basics/custom-arguments)

For a reference of more advanced arguments, you should look here:

* [Minecraft Arguments](https://docs.papermc.io/paper/dev/command-api/arguments/minecraft)

Future pages

The following pages will be added to the documentation in the future:

* **Tutorial: Creating Utility Commands**
* **The Command Dispatcher**
* **Forks and Redirects**
* **Tutorial: Extending the vanilla execute command**

## Additional support

[Section titled “Additional support”](#additional-support)

For support regarding the command API, you can always ask in our [Discord server](https://discord.gg/PaperMC) under the
[`#paper-dev`](https://discord.com/channels/289587909051416579/555462289851940864) channel!


================================================================================
Chapter Title: Command trees
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/command-tree/
================================================================================

What is a command tree and in what way does it have anything to do with Brigadier? If you are confused, this is the page for you! Here we will take an
extensive look at everything you need to know to understands command tree!

Note

This is meant as a full-on course about the structure of Brigadier commands. This site provides no information about executing branches or general arguments, only literals.
It is suggested that you look in here if you are new to Brigadier programming.

## What is a tree?

[Section titled “What is a tree?”](#what-is-a-tree)

When talking about trees, the first that comes to mind is a tree in the wild. One that may look like this:

![Command tree](https://docs.papermc.io/_astro/tree.CnyuCtZh_1lfeob.webp)

So, what does this have to do with commands? Imagine a command that looks like this:

A Generic Command

```java
/customplugin reload

/customplugin tphere

/customplugin killall
```

For the sake of simplicity, we will refer to `/customplugin` (without any arguments) as our “command” or “tree” root. Each argument after our “root” is referred to as a “branch”.
You can visualize this on our generic tree like this:

![Described command tree](https://docs.papermc.io/_astro/tree-descriptions.BsJtCvOK_Z2nHUb9.webp)

Having to draw a tree each time like this is exhausting and usually does not get to the point though. We can visualize trees using a **tree diagram**. This would look like this:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-0.svg)

It is way easier to understand the root/branch relationship of elements now. The root node is the node that is at the top of our hierarchy. In this case, that is the ‘customplugin’ node.
The other elements have an arrow pointing **at** them, meaning they are a **branch** of our root node, also called a child. Family trees follow a similar structure, as you can see here:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-1.svg)

It is important to remember that this tree-like structure is not only important for Brigadier. It is a fairly often used concept. Paper’s included [Adventure API](https://docs.papermc.io/paper/dev/component-api/introduction)
also operates using a tree. Why is this important for using Brigadier though? Well, it allows for explicit command declaration. Being at a node, you know exactly where you are. That means you do not have
to, like in standard Bukkit way, first check whether the amount of arguments is 2 and the first argument is `tphere`. Because you are at that exact `tphere` node, you can just start writing
your logic. If you want to learn more about the execute logic of Brigadier commands, it is suggested that you check out [command executors](https://docs.papermc.io/paper/dev/command-api/basics/executors).

## How can we visualize a tree in-code?

[Section titled “How can we visualize a tree in-code?”](#how-can-we-visualize-a-tree-in-code)

We can define our root like this:

```java
LiteralArgumentBuilder<CommandSourceStack> root = Commands.literal("customplugin");
```

This method returns a `LiteralArgumentBuilder<CommandSourceStack>`, which is a class that allows us to add branches to it using the `.then(...)` method, like this:

```java
LiteralArgumentBuilder<CommandSourceStack> root = Commands.literal("customplugin");

root.then(Commands.literal("reload"));

root.then(Commands.literal("tphere"));

root.then(Commands.literal("killall"));
```

Each of these `.then(...)` methods adds a new branch to our root. You may have noticed the repeated use of `Commands.literal(String)` here. It does not only define the root of the tree
of our command, but also our “subcommands” (`reload`, `tphere`, and `killall`). Each “child” literal is referred to as a subcommand of its parent.

## Creating a more advanced command

[Section titled “Creating a more advanced command”](#creating-a-more-advanced-command)

But what if we want a more complex command? Let’s say we want to define the following command:

Advanced Command

```java
/advanced

┣━┳ killall

┃ ┣━━ entities

┃ ┣━━ players

┃ ┗━━ zombies

┗━┳ eat

┣━━ ice-cream

┗━━ main-dish
```

Which allows for the following command executions in-game:

```java
/advanced killall entities

/advanced killall players

/advanced killall zombies

/advanced eat ice-cream

/advanced eat main-dish
```

As this is a fairly complicated command, we can visualize it as a tree graph first in order to we have a better understanding on what is going on:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-2.svg)

Having defined our target command, how can we go about this now? There is a few possible ways, but the simplest one is defining **furthest from root** first. That means we are first
defining the last branches of our entire tree. So those, which have no subcommands:

```java
LiteralArgumentBuilder<CommandSourceStack> entities = Commands.literal("entities");

LiteralArgumentBuilder<CommandSourceStack> players = Commands.literal("players");

LiteralArgumentBuilder<CommandSourceStack> zombies = Commands.literal("zombies");

LiteralArgumentBuilder<CommandSourceStack> iceCream = Commands.literal("ice-cream");

LiteralArgumentBuilder<CommandSourceStack> mainDish = Commands.literal("main-dish");
```

This grants us the deepest elements in our tree.

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-3.svg)

Now, we can define the next layer of literals: So the `killall` and `eat` ones:

```java
LiteralArgumentBuilder<CommandSourceStack> killall = Commands.literal("killall");

LiteralArgumentBuilder<CommandSourceStack> eat = Commands.literal("eat");
```

Visualized in our tree graph:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-4.svg)

With these defined, we can add our child elements to their parent element, like this:

```java
killall.then(entities);

killall.then(players);

killall.then(zombies);

eat.then(iceCream);

eat.then(mainDish);
```

Which gives us this, somewhat tree-like structure:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-5.svg)

Finally, we can create our **root node** and add our `killall` and `eat` subcommands to it:

```java
LiteralArgumentBuilder<CommandSourceStack> advancedCommandRoot = Commands.literal("advanced");

advancedCommandRoot.then(killall);

advancedCommandRoot.then(eat);
```

And this returns the final command tree:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/command-api/basics/command-tree-6.svg)

And we are done!

## Chaining ‘then’ method calls together

[Section titled “Chaining ‘then’ method calls together”](#chaining-then-method-calls-together)

You might have noticed that it feels unnecessarily verbose to have to store every child node in its own variable. But here is where the `.then()` argument
comes to rescue. It returns the same element as it was called on. That means if we were to run this code:

```java
LiteralArgumentBuilder<CommandSourceStack> value = killall.then(entities);

if (value == killall) {

logger.info("The return value is the same as killall");

}
```

We would always have “The return value is the same as killall” printed out. And we can take advantage of that by chaining the `then(...)` calls together, like this:

```java
killall.then(entities).then(players).then(zombies);
```

Due to this being hard to read, we should give each branch a new line:

```java
killall

.then(entities)

.then(players)

.then(zombies);
```

With this, we also do not have to store every single literal in its own variable, instead we can directly pass them into the `.then(...)` method:

```java
killall

.then(Commands.literal("entities"))

.then(Commands.literal("players"))

.then(Commands.literal("zombies"));
```

The same can be done for the `eat` subcommand:

```java
eat

.then(Commands.literal("ice-cream"))

.then(Commands.literal("main-dish"));
```

Taking even more advantage of the builder pattern of the `then` method, we can put these chained branches directly on the initial creation of our subcommand. Like this:

```java
LiteralArgumentBuilder<CommandSourceStack> eat = Commands.literal("eat")

.then(Commands.literal("ice-cream"))

.then(Commands.literal("main-dish"));

LiteralArgumentBuilder<CommandSourceStack> killall = Commands.literal("killall")

.then(Commands.literal("entities"))

.then(Commands.literal("players"))

.then(Commands.literal("zombies"));

LiteralArgumentBuilder<CommandSourceStack> advancedCommandRoot = Commands.literal("advanced");

advancedCommandRoot.then(eat);

advancedCommandRoot.then(killall);
```

Now then, you might have noticed that our root node also registers its branches using the `.then(...)` method, meaning we can also combine those:

```java
LiteralArgumentBuilder<CommandSourceStack> advancedCommandRoot = Commands.literal("advanced")

.then(Commands.literal("eat")

.then(Commands.literal("ice-cream"))

.then(Commands.literal("main-dish"))

)

.then(Commands.literal("killall")

.then(Commands.literal("entities"))

.then(Commands.literal("players"))

.then(Commands.literal("zombies"))

);
```

Which results in the finished command!

Caution

You have to be extremely careful when nesting branches, as the command turns into a completely different one when you misplace a bracket.


================================================================================
Chapter Title: Arguments and literals
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals/
================================================================================

Note

In the [command tree docs](https://docs.papermc.io/paper/dev/command-api/basics/command-tree) we have looked at the structure of Brigadier commands and how to build up a command tree.
If you haven’t finished reading that yet, we strongly recommend doing that before reading about arguments and literals.

## Introduction

[Section titled “Introduction”](#introduction)

Each `.then(...)` method of an `ArgumentBuilder<CommandSourceStack, ?>` takes in another `ArgumentBuilder<CommandSourceStack, ?>` object. This abstract ArgumentBuilder
has two implementations: `RequiredArgumentBuilder` and `LiteralArgumentBuilder`. When using Brigadier with Paper, we create these objects by running either `Commands.literal(String)`
for the `LiteralArgumentBuilder` or `Commands.argument(String, ArgumentType<T>)` for the `RequiredArgumentBuilder`.

As an explanation to what the difference is, you can picture it like this:

* An argument is a variable input by the user. It is semi-unpredictable, but will always return a valid entry of the object that it is backing.
* A literal is a non-variable input by the user. It is mainly used as a way to define predictable input, since each literal is a new branch on our command tree.

## Literals

[Section titled “Literals”](#literals)

In code, literals generally cannot be accessed. Yet, due to the nature of our command tree, we can always know on what literal branch we currently are:

```java
Commands.literal("plant")

.then(Commands.literal("tree")

.executes(ctx -> {

/* Here we are on /plant tree */

})

)

.then(Commands.literal("grass")

.executes(ctx -> {

/* Here we are on /plant grass */

}));
```

Tip

You may notice the usage of the `executes` method. This method declares logic to our branches. If a branch has no `executes` method defined, it will not be executable.
For more information about execution logic, [click here](https://docs.papermc.io/paper/dev/command-api/basics/executors).

## Arguments

[Section titled “Arguments”](#arguments)

Arguments are slightly more complex. They also define a new branch in a tree, but they are not directly predictable. Each argument is created using `Commands.argument(String, ArgumentType<T>)`.
That method returns a `RequiredArgumentBuilder`. The T type parameter declares the return type of the argument, which you can then use inside your `executes` method. That means that
if you put in an `ArgumentType<Integer>`, you can retrieve the value of that argument as an integer, requiring no manual parsing! There are a few build-in, primitive argument types
that we can use for arguments:

| Name | Return value | Possible Input | Description |
| --- | --- | --- | --- |
| BoolArgumentType.bool() | Boolean | true/false | Only allows a boolean value |
| IntegerArgumentType.integer() | Integer | 253, -123, 0 | Any valid integer |
| LongArgumentType.longArg() | Long | 25418263123783 | Any valid long |
| FloatArgumentType.floatArg() | Float | 253.2, -25.0 | Any valid float |
| DoubleArgumentType.doubleArg() | Double | 4123.242, -1.1 | Any valid double |
| StringArgumentType.word() | String | letters-and+1234567 | A single word. May only contain letters and numbers and these characters: `+`, `-`, `_`, and `.` |
| StringArgumentType.string() | String | ”with spaces” | A single word, or, if quoted, any valid string with spaces |
| StringArgumentType.greedyString() | String | unquoted spaces | The literal written input. May contain any characters. Has to be the last argument |

### Boolean argument type and argument parsing

[Section titled “Boolean argument type and argument parsing”](#boolean-argument-type-and-argument-parsing)

A boolean argument is used for retrieving, well, a boolean. An example usage for that might be a `/serverflight` command which allows for enabling and disabling server flight
with `/serverflight true` and `/serverflight false`:

ServerFlightCommand.java

```java
Commands.literal("serverflight")

.then(Commands.argument("allow", BoolArgumentType.bool())

.executes(ctx -> {

boolean allowed = ctx.getArgument("allow", boolean.class);

/* Toggle server flying */

})

);
```

Here, you can see how one would access an argument in-code. The first parameter for the `Commands.argument(String, ArgumentType)` method takes in the node name. This is not required
by literals, as their name is the same as their value. But here we need a way to access the argument. The parameter of the executes-lambda has a method called
`T getArgument(String, Class<T>)`. The first parameter is the name of the method we want to retrieve. The second parameter is the return value of the argument. As we are using
a boolean argument, we put in `boolean.class` and retrieve the argument value as such.

### Number arguments

[Section titled “Number arguments”](#number-arguments)

All of the number arguments (like `IntegerArgumentType.integer()`) have three overloads:

| Overload | Description |
| --- | --- |
| `IntegerArgumentType.integer()` | Any value between Integer.MIN\_VALUE and Integer.MAX\_VALUE |
| `IntegerArgumentType.integer(int min)` | Any value between min and Integer.MAX\_VALUE |
| `IntegerArgumentType.integer(int min, int max)` | Any value between min and max |

This is particularly useful for filtering out too high or too low input. As an example, we can define a `/flyspeed` command. As the
[`Player#setFlySpeed(float value)`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#setFlySpeed(float)) method only
accepts floats between -1 and 1, where -1 is an inverse direction, it would make sense to limit the values between 0 and 1 for in-bounds, non-negative speed values.
This can be achieved with the following command tree:

FlightSpeedCommand.java

```java
Commands.literal("flyspeed")

.then(Commands.argument("speed", FloatArgumentType.floatArg(0, 1.0f))

.executes(ctx -> {

float speed = ctx.getArgument("speed", float.class);

/* Set player's flight speed */

return Command.SINGLE_SUCCESS;

})

);
```

Tip

Some arguments can have special ways of being retrieved. Most notably, all of the Brigadier-provided arguments (the ones mentioned on this page)
have a resolver to get their own argument value. For the float argument, this would look like this:

```java
float speed = FloatArgumentType.getFloat(ctx, "speed");
```

It generally does not matter whether you use `ctx.getArgument` or `FloatArgumentType.getFloat`, since it goes through the same logic, but in future documentation,
primitive values might be retrieved using their own parsers.

These parsers for Brigadier-native arguments exist. All of these take in `(CommandContext<?> context, String name)` as method parameters:

* `BoolArgumentType.getBool`
* `IntegerArgumentType.getInteger`
* `LongArgumentType.getLong`
* `FloatArgumentType.getFloat`
* `DoubleArgumentType.getDouble`
* `StringArgumentType.getString`

Now, if we input a valid float between 0 and 1, the command would execute correctly:
![](https://docs.papermc.io/_astro/valid-float.Dl02CkKx_1b5Vw8.webp)

But if we input a too small or too big float, it would throw an error **on the client**:
![](https://docs.papermc.io/_astro/small-float.DhEDVkML_13sg8V.webp)
![](https://docs.papermc.io/_astro/big-float.DsjpNbva_1alKgH.webp)

This is the main advantage of native arguments: The client itself performs simple error checking on the arguments, which makes user experience whilst running a command
way better, as they can see invalid input without sending the command to the server.

### String arguments

[Section titled “String arguments”](#string-arguments)

There is three string arguments: `word`, `string`, and `greedyString`.

The `word` string argument is the simplest one of these. It only accepts a single word consisting of alphanumerical characters and these special characters: `+`, `-`, `_`, and `.`.

* ✅ `.this_is_valid_input.`
* ❌ `this is invalid input`
* ❌ `"also_invalid"`
* ✅ `-10_numbers_are_valid`
* ❌ `@_@`

The `string` argument is slightly more complicated. If unquoted, it follows the same rules as the `word` argument. Only alphanumerical characters and the mentioned special characters.
But if you put your string into quotes, you can enter any combination of unicode characters you want to. Quotes `"` can be escaped using a backslash `\`.

* ✅ `this_is-valid-input`
* ✅ `"\"quotes\""`
* ❌ `this is invalid input`
* ✅ `"this is valid input again"`
* ✅ `"also_valid"`
* ✅ `"紙の神"`

The `greedyString` argument is the only argument which does not perform any parsing. Due to its “greedy” nature, it does not allow any arguments after its declaration. That also means, that
any input is completely valid and it requires no quotes. In fact, quotes are counted as literal characters.

* ✅ `this_is_valid_input`
* ✅ `this is valid as well input`
* ✅ `"this is valid input again"`
* ✅ `also_valid`
* ✅ `紙の神`

Here you can see the arguments in action:
![](https://docs.papermc.io/_astro/string-arguments.DCrPKkcP_Z2tMrue.webp)

## Further reference

[Section titled “Further reference”](#further-reference)

### Minecraft arguments

[Section titled “Minecraft arguments”](#minecraft-arguments)

Apart from these built-in Brigadier arguments, countless custom arguments are defined by Paper as well. These can be accessed in a static context with the `ArgumentTypes` class. You
can read more about these [here](https://docs.papermc.io/paper/dev/command-api/arguments/minecraft).

### Custom arguments

[Section titled “Custom arguments”](#custom-arguments)

Sometimes you want to define your own, custom arguments. For that you can implement the `CustomArgumentType<T, N>` interface.
You can read more about these [here](https://docs.papermc.io/paper/dev/command-api/basics/custom-arguments).


================================================================================
Chapter Title: Executors
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/executors/
================================================================================

Tip

This page requires knowledge about [Command Trees](https://docs.papermc.io/paper/dev/command-api/basics/command-tree) and [Arguments and Literals](https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals). If you haven’t read
through those articles, it is highly recommend to check those out beforehand!

This page is dedicated to the `executes(...)` method from the `ArgumentBuilder` class.

## Examining the executes method

[Section titled “Examining the executes method”](#examining-the-executes-method)

The `executes` method is defined as following:

ArgumentBuilder.java

```java
public T executes(Command<S> command);
```

The `Command<S>` interface is declared as a `FunctionalInterface`. That means that instead of putting in a class that implements it, we can just pass in a lambda statement.

Command.java

```java
@FunctionalInterface

public interface Command<S> {

int SINGLE_SUCCESS = 1;

int run(CommandContext<S> ctx) throws CommandSyntaxException;

}
```

Our lambda has one parameter and returns an integer. That is essentially that `run` method defined in that interface. The one parameter, `CommandContext<S>` is the one where
we get all the information about the sender who executed that command and all the command arguments. It has quite a few methods, but the main ones of use for us are
`S getSource()` and `V getArgument(String, Class<V>)`. We have taken a brief look at the `getArgument(...)` in the [Arguments and Literals](https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals) chapter, but
in a nutshell, this is the method that we can retrieve arguments from. There will be more specific examples later on.

You should mainly notice the generic parameter S by the `getSource()` method. That is the type of the source of the command. For the executes method, this type is always a
`CommandSourceStack`. That class itself has three methods: `Location getLocation()`, `CommandSender getSender()`, and `@Nullable Entity getExecutor()`.
The most used method from that is `getSender()`, as that is the command sender who has actually run the command. For the target of a command, you should use `getExecutor()`,
which is relevant, if the command was ran via `/execute as <entity> run <our_command>`. It is not necessarily required, but is seen as good practice.

## Example: Flyspeed command

[Section titled “Example: Flyspeed command”](#example-flyspeed-command)

In the [Arguments and Literals](https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals) chapter, we have briefly declared the structure for a `/flyspeed` command with the use of a ranged float argument.
But that command does not actually set the flyspeed of the executing player. In order to do that, we’d have to append an executor onto it, like this:

FlightSpeedCommand.java

```java
Commands.literal("flyspeed")

.then(Commands.argument("speed", FloatArgumentType.floatArg(0, 1.0f))

.executes(ctx -> {

float speed = FloatArgumentType.getFloat(ctx, "speed"); // Retrieve the speed argument

CommandSender sender = ctx.getSource().getSender(); // Retrieve the command sender

Entity executor = ctx.getSource().getExecutor(); // Retrieve the command executor, which may or may not be the same as the sender

// Check whether the executor is a player, as you can only set a player's flight speed

if (!(executor instanceof Player player)) {

// If a non-player tried to set their own flight speed

sender.sendPlainMessage("Only players can fly!");

return Command.SINGLE_SUCCESS;

}

// Set the player's speed

player.setFlySpeed(speed);

if (sender == executor) {

// If the player executed the command themselves

player.sendPlainMessage("Successfully set your flight speed to " + speed);

return Command.SINGLE_SUCCESS;

}

// If the speed was set by a different sender (Like using /execute)

sender.sendRichMessage("Successfully set <playername>'s flight speed to " + speed, Placeholder.component("playername", player.name()));

player.sendPlainMessage("Your flight speed has been set to " + speed);

return Command.SINGLE_SUCCESS;

})

);
```

### Explanation

[Section titled “Explanation”](#explanation)

There is a lot to unpack, so let’s break it down, top to bottom:

The first lines define a `/flyspeed` command root, with a float argument named “speed”, which only allows values between 0 and 1.
We then add an executes clause to our argument branch and retrieves the speed argument by running `FloatArgumentType.getFloat`.

Note the highlighted lines. We first retrieve the `CommandSourceStack` from our `CommandContext<CommandSourceStack>` and then finally retrieve its sender and executor.
A `CommandSender` is an interface, which declares the `sendMessage(...)`, `getServer()`, and `getName()` methods. It is implemented by all entities, including players,
and the ConsoleCommandSender, which is used if a console executes a command.

Next up we check whether our executor object is also instance of a `Player` interface. If executor were null, this would be false, which is why we require no null check.
If the expression evaluates as true, we get a new `player` variable, which represents an actual player on the server that the command was executed by.

Next up, we set the player’s flight speed using the value retrieved from the player-provided float argument and send them a message to confirm the operation.
It is always recommended to send a confirmation message whether the command was successful, because otherwise a player might get confused to why a command is “not working”.
If the executor was not a player, we can send a form of error message. In our case, we assume the sender to be a console, as an entity usually does not try to send such
a command.

Finally, we just return from the lambda statement providing a return value. As our command succeeded, we can return `Command.SINGLE_SUCCESS`, whose value is `1`.
Don’t forget to close all your braces!

Running the command now works correctly:
![](https://docs.papermc.io/_astro/flyspeed-player.DS2fG2LU_mRl5K.webp)
![](https://docs.papermc.io/_astro/flyspeed-console.BoD8KNLp_16LKsY.webp)

We can even run it as another player, using `/execute as`:
![](https://docs.papermc.io/_astro/flyspeed-proxied.CmjD0Ay5_Z1n5On7.webp)

### Logic separation

[Section titled “Logic separation”](#logic-separation)

Sometimes, if the command is too big or due to personal preference, you might not want to have your logic code in your executes method, as it might be unreadable
due of the amount of indentations. In such an event we can, instead of defining our logic in the lambda statement, use a method reference instead. For that we
can just pass a method reference to the executes method. This might look like this:

FlightSpeedCommand.java

```java
public class FlightSpeedCommand {

public static LiteralArgumentBuilder<CommandSourceStack> createCommand() {

return Commands.literal("flyspeed")

.then(Commands.argument("speed", FloatArgumentType.floatArg(0, 1.0f))

.executes(FlightSpeedCommand::runFlySpeedLogic)

);

}

private static int runFlySpeedLogic(CommandContext<CommandSourceStack> ctx) {

float speed = FloatArgumentType.getFloat(ctx, "speed"); // Retrieve the speed argument

CommandSender sender = ctx.getSource().getSender(); // Retrieve the command sender

Entity executor = ctx.getSource().getExecutor(); // Retrieve the command executor, which may or may not be the same as the sender

// Check whether the executor is a player, as you can only set a player's flight speed

if (!(executor instanceof Player player)) {

// If a non-player tried to set their own flight speed

sender.sendPlainMessage("Only players can fly!");

return Command.SINGLE_SUCCESS;

}

// Set the player's speed

player.setFlySpeed(speed);

if (sender == executor) {

// If the player executed the command themselves

player.sendPlainMessage("Successfully set your flight speed to " + speed);

return Command.SINGLE_SUCCESS;

}

// If the speed was set by a different sender (Like using /execute)

sender.sendRichMessage("Successfully set <playername>'s flight speed to " + speed, Placeholder.component("playername", player.name()));

player.sendPlainMessage("Your flight speed has been set to " + speed);

return Command.SINGLE_SUCCESS;

}

}
```

As you can see, we have made our command tree way easily readable whilst preserving the same functionality.


================================================================================
Chapter Title: Registration
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/registration/
================================================================================

In the previous chapters, we have taken an extensive look at how Brigadier works, but never actually elaborated on how to register commands. So we will be doing that right here!

## The LifecycleEventManager

[Section titled “The LifecycleEventManager”](#the-lifecycleeventmanager)

In Paper, Brigadier commands are registered using the `LifecycleEventManager`. This is a special class which allows us to register commands in such a way that we never have to
worry about handling various server reload events, like `/reload`. Instead, whatever we register using the `LifecycleEventManager`, will be reregistered each time it is required.

But how does one get access to a `LifecycleEventManager` capable of registering commands? There are two “contexts” in which you can use a LifecycleEventManager. The first one,
and preferred one, is in the `PluginBootstrap` class of our plugin.

### Registering inside a plugin bootstrapper

[Section titled “Registering inside a plugin bootstrapper”](#registering-inside-a-plugin-bootstrapper)

Note

This requires you to use a [`paper-plugin.yml` plugin](https://docs.papermc.io/paper/dev/getting-started/paper-plugins).

If you are not using `paper-plugin.yml`, you can instead [register your commands inside your plugin’s main class](#registering-inside-a-plugin-main-class).

We can get access to a `LifecycleEventManager` capable of registering commands by running `context.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {})`
inside our bootstrap method, like this:

CustomPluginBootstrap.java

```java
public class CustomPluginBootstrap implements PluginBootstrap {

@Override

public void bootstrap(BootstrapContext context) {

context.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {

// register your commands here ...

});

}

}
```

A quick recap on what all of this means:
By running `context.getLifecycleManager()`, we get a `LifecycleEventManager<BootstrapContext>` object. We can call
`LifecycleEventManager#registerEventHandler(LifecycleEventType, LifecycleEventHandler)` on that to get our correct lifecycle event. The first parameter declares
the lifecycle event type we want to register stuff for, the second parameter is an interface that looks like this:

```java
@FunctionalInterface

public interface LifecycleEventHandler<E extends LifecycleEvent> {

void run(E event);

}
```

Due to it being a functional interface, we can, instead of implementing it, just pass in a lambda which has one parameter, `E`, and no return value. The `E` generic type is a
`ReloadableRegistrarEvent<Commands>`, which is thus also the type of our lambda parameter.

The `ReloadableRegistrarEvent<Commands>` class has two methods: `ReloadableRegistrarEvent.Cause cause()` and `Commands registrar()`. The more relevant method for us is
the `registrar` one. With it we can register our commands.

### Registering inside a plugin main class

[Section titled “Registering inside a plugin main class”](#registering-inside-a-plugin-main-class)

Getting access to a `LifecycleEventManager` for commands inside our plugin’s main class is very similar to how you access it inside the PluginBootstrap class, with the difference
that instead of getting the `LifecycleEventManager` using the `BootstrapContext` provided to us in the bootstrap method of our PluginBootstrap class, we can just retrieve it using
`JavaPlugin#getLifecycleManager`.

PluginMainClass.java

```java
public final class PluginMainClass extends JavaPlugin {

@Override

public void onEnable() {

this.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {

// register your commands here ...

});

}

}
```

This follows the same concept as the PluginBootstrap one, just that instead of being given a `LifecycleEventManager<BootstrapContext>`, we are instead given a
`LifecycleEventManager<Plugin>`. This doesn’t really matter for our use cases, but you might as well be aware of that.
The rest of the methods works the exact same way as with the `PluginBootstrap` parameterized `LifecycleEventManager`.

## Registering commands using the Commands class

[Section titled “Registering commands using the Commands class”](#registering-commands-using-the-commands-class)

Now that we have access to the instance of a `Commands` class via `commands.registrar()` in our event handler, we have access to a few overloads of the `Commands#register`
method.

### Registering a LiteralCommandNode

[Section titled “Registering a LiteralCommandNode”](#registering-a-literalcommandnode)

Most of the time, you will be using a `LiteralArgumentBuilder` to build up your command tree. In order to retrieve a `LiteralCommandNode` from that object, we need to call the
`LiteralArgumentBuilder#build()` method on it:

```java
LiteralArgumentBuilder<CommandSourceStack> command = Commands.literal("testcmd")

.then(Commands.literal("argument_one"))

.then(Commands.literal("argument_two"));

LiteralCommandNode<CommandSourceStack> buildCommand = command.build();
```

Or in short:

```java
LiteralCommandNode<CommandSourceStack> buildCommand = Commands.literal("testcmd")

.then(Commands.literal("argument_one"))

.then(Commands.literal("argument_two"))

.build();
```

Now that we have retrieved our `LiteralCommandNode`, we can register it. For that we have multiple overloads, which optionally allow us to set aliases and/or the description.
Registering our “testcmd” might look like this:

```java
this.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {

commands.registrar().register(buildCommand);

});
```

### Registering a BasicCommand

[Section titled “Registering a BasicCommand”](#registering-a-basiccommand)

A [`BasicCommand`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/BasicCommand.html) is a Bukkit-like way of defining commands. Instead of building up a command tree,
we allow all user input and retrieve the arguments as a simple array of strings. This type of commands is particularly useful for very simple, text based commands,
like a `/broadcast` command. You can read up on more details about basic commands [here](https://docs.papermc.io/paper/dev/command-api/misc/basic-command).

Assuming you already have your `BasicCommand` object, we can register it like this:

```java
final BasicCommand basicCommand = ...;

this.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {

commands.registrar().register("commandname", basicCommand);

});
```

Similar to the `LiteralCommandNode`, we also have overloads for setting various additional information for our command.

## Further reference

[Section titled “Further reference”](#further-reference)

* For a quick reference on the LifecycleEventManager, click [here](https://docs.papermc.io/paper/dev/lifecycle).


================================================================================
Chapter Title: Requirements
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/requirements/
================================================================================

Sometimes you want to limit a player’s ability to use and/or view certain commands or subcommands. Exactly for this purpose,
the `ArgumentBuilder<S>` class has a `requires(Predicate<S>)` method to define a requirement in order to use that specific branch of a command tree.
As always, the generic parameter `S` is just a `CommandSourceStack`, providing us with the executing entity, the command sender, and the location of the command.

## Defining permissions

[Section titled “Defining permissions”](#defining-permissions)

One of the most common usecases for requirements are permissions. Usually, these are checked on the **command sender**, as that is the actual entity/console/object
which ran the command, even if it is run as someone else (the executor). A simple command with a permission might look like this:

```java
Commands.literal("testcmd")

.requires(sender -> sender.getSender().hasPermission("permission.test"))

.executes(ctx -> {

ctx.getSource().getSender().sendRichMessage("<gold>You have permission to run this command!");

return Command.SINGLE_SUCCESS;

});
```

This command requires the `permission.test` permission to be had by a sender.
But you cannot only define permissions, you can also require a sender to be a server operator, like this:

```java
Commands.literal("testcmd")

.requires(sender -> sender.getSender().isOp())

.executes(ctx -> {

ctx.getSource().getSender().sendRichMessage("<gold>You are a server operator!");

return Command.SINGLE_SUCCESS;

});
```

## Defining more advanced predicates

[Section titled “Defining more advanced predicates”](#defining-more-advanced-predicates)

You don’t have to limit yourself to checking just for permissions - since it is a predicate, any boolean can be returned. For example, you can check for whether
a player has a diamond sword in their inventory:

```java
Commands.literal("givesword")

.requires(sender -> sender.getExecutor() instanceof Player player && !player.getInventory().contains(Material.DIAMOND_SWORD))

.executes(ctx -> {

if (ctx.getSource().getExecutor() instanceof Player player) {

player.getInventory().addItem(ItemType.DIAMOND_SWORD.createItemStack());

}

return Command.SINGLE_SUCCESS;

});
```

At first glance, this works just fine. But it does have a very big flaw - since the player’s client is not aware of the requirement, it still shows the command
as executable, even if the requirement resolves as false. But if the client tries to run the command, the server reports that this command doesn’t exist (meaning
the requirement was not met):

![](https://docs.papermc.io/_astro/client-server-mismatch.CZCt4lWh_Z27OOjb.webp)

How can we solve this? The `Player` interface has a method called [`#updateCommands()`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#updateCommands()) just for this usecase. It resends the currently registered commands back to the
client in an attempt to reload commands. For now, we can create a new command with which the player can update its own commands in order to resync its command state:

```java
Commands.literal("reloadcommands")

.executes(ctx -> {

if (ctx.getSource().getExecutor() instanceof Player player) {

player.updateCommands();

player.sendRichMessage("<gold>Successfully updated your commands!");

}

return Command.SINGLE_SUCCESS;

});
```

### Automating command reloads

[Section titled “Automating command reloads”](#automating-command-reloads)

Forcing a player to reload their own commands is not a viable option for user experience. For this reason, you can **automate** this behavior. It is safe to call
the update commands method as often as required, but it should generally be avoided as it can cost a great deal of bandwidth. If possible, you should instead place
these in very specific spots. Furthermore, this method is completely thread safe, meaning you are free to call it from an asynchronous context.

## Restricted commands

[Section titled “Restricted commands”](#restricted-commands)

From 1.21.6 onwards, commands can now be restricted. This feature is used by Vanilla in order to make a player confirm whether they
really want to run a command from a run-command click event. That includes ones on text components or dialog buttons.
All Vanilla commands, which require operator status by default, are restricted:

![](https://docs.papermc.io/_astro/vanilla-restriction.DCEks_9m_Z1POhEY.webp)

### Restricting your commands

[Section titled “Restricting your commands”](#restricting-your-commands)

You can apply the same behavior to your commands by wrapping the predicate inside your `.requires` with `Commands.restricted(...)`.
A simple implementation might look like this:

```java
Commands.literal("test-req")

.requires(Commands.restricted(source -> true))

.executes(ctx -> {

ctx.getSource().getSender().sendRichMessage("You passed!");

return Command.SINGLE_SUCCESS;

});
```

![](https://docs.papermc.io/_astro/custom-restriction.BpXtkwe6_1kiuAc.webp)

  

Inside the `.restricted` method you can put any logic which you would put into your `.requires` method.
It is nothing more but a simple wrapper around the usual `.requires` predicate:

```java
Commands.literal("mycommand")

.requires(Commands.restricted(source -> source.getSender().hasPermission("my.custom.permission")

&& source.getExecutor() instanceof Player player

&& player.getGameMode() == GameMode.ADVENTURE))

.executes(ctx -> {

// Command logic

});
```


================================================================================
Chapter Title: Suggestions
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/argument-suggestions/
================================================================================

Sometimes, you want to send your own suggestions to users. For this, you can use the `suggests(SuggestionProvider<CommandSourceStack>)` method when declaring
arguments.

## Examining `SuggestionProvider<S>`

[Section titled “Examining SuggestionProvider<S>”](#examining-suggestionproviders)

The `SuggestionProvider<S>` interface is defined as follows:

SuggestionProvider.java

```java
@FunctionalInterface

public interface SuggestionProvider<S> {

CompletableFuture<Suggestions> getSuggestions(final CommandContext<S> context, final SuggestionsBuilder builder) throws CommandSyntaxException;

}
```

Similar to other classes or interfaces with a `<S>` generic parameter, for Paper, this is usually a `CommandSourceStack`. Furthermore, similar to the `Command<S>` interface,
this is a functional interface, which means that instead of passing in a class which implements this interface, we can just pass a lambda statement or a method reference.

Our lambda consists of two parameters, `CommandContext<S>` and `SuggestionsBuilder`, and expects to have a `CompletableFuture<Suggestions>` returned.

A very simple lambda for our `suggests` method might look like this:

```java
Commands.argument("name", StringArgumentType.word())

.suggests((ctx, builder) -> builder.buildFuture());
```

This example obviously does not suggest anything, as we haven’t added any suggestions yet.

## The `SuggestionsBuilder`

[Section titled “The SuggestionsBuilder”](#the-suggestionsbuilder)

The `SuggestionsBuilder` has a few methods we can use to construct our suggestions:

### Input retrieval

[Section titled “Input retrieval”](#input-retrieval)

The first type of methods we will cover are the input retrieval methods: `getInput()`, `getStart()`, `getRemaining()`, and `getRemainingLowerCase()`.
The following table displays what each returns with the following input typed in the chat bar: `/customsuggestions Asumm13Text`.

| Method | Return Value | Description |
| --- | --- | --- |
| getInput() | /customsuggestions Asumm13Text | The full chat input |
| getStart() | 19 | The index of the first character of the argument’s input |
| getRemaining() | Asumm13Text | The input for the current argument |
| getRemainingLowerCase() | asumm13text | The input for the current argument, lowercased |

### Suggestions

[Section titled “Suggestions”](#suggestions)

The following overloads of the `SuggestionsBuilder#suggest` method add values that will be send to the client as argument suggestions:

| Overload | Description |
| --- | --- |
| suggest(String) | Adds a String to the suggestions |
| suggest(String, Message) | Adds a String with a tooltip to the suggestions |
| suggest(int) | Adds an int to the suggestions |
| suggest(int, Message) | Adds an int with a tooltip to the suggestions |

There are two ways of retrieving a `Message` instance:

* Using `LiteralMessage`, which can be used for basic, non-formatted text.
* Using the `MessageComponentSerializer`, which can be used to serialize `Component` objects into `Message` objects.

For example, if you add a suggestion like this:

```java
builder.suggest("suggestion", MessageComponentSerializer.message().serialize(

MiniMessage.miniMessage().deserialize("<green>Suggestion tooltip")

));
```

It will look like this on the client:
![](https://docs.papermc.io/_astro/suggestion-tooltip.Coi5XvhS_1fAHK0.webp)

### Building

[Section titled “Building”](#building)

There are two methods we can use to build our `Suggestions` object. The only difference between those is that one directly returns the finished `Suggestions` object,
whilst the other one returns a `CompletableFuture<Suggestions>`.

The reason for these two methods is that `SuggestionProvider` expects the return value to be `CompletableFuture<Suggestions>`. This for once
allows for constructing your suggestions asynchronously inside a `CompletableFuture.supplyAsync(Supplier<Suggestions>)` statement, or synchronously directly inside our
lambda and returning the final `Suggestions` object asynchronously.

Here are the same suggestions declared in the two different ways mentioned above:

```java
// Here, you are safe to use all Paper API

Commands.argument("name", StringArgumentType.word())

.suggests((ctx, builder) -> {

builder.suggest("first");

builder.suggest("second");

return builder.buildFuture();

});

// Here, most Paper API is not usable

Commands.argument("name", StringArgumentType.word())

.suggests((ctx, builder) -> CompletableFuture.supplyAsync(() -> {

builder.suggest("first");

builder.suggest("second");

return builder.build();

}));
```

## Example: Suggesting amounts in a give item command

[Section titled “Example: Suggesting amounts in a give item command”](#example-suggesting-amounts-in-a-give-item-command)

In commands, where you give players items, you oftentimes include an amount argument. We could suggest `1`, `16`, `32`, and `64` as common amounts for
items given. The command implementation could look like this:

```java
@NullMarked

public class SuggestionsTest {

public static LiteralCommandNode<CommandSourceStack> constructGiveItemCommand() {

// Create new command: /giveitem

return Commands.literal("giveitem")

// Require a player to execute the command

.requires(ctx -> ctx.getExecutor() instanceof Player)

// Declare a new ItemStack argument

.then(Commands.argument("item", ArgumentTypes.itemStack())

// Declare a new integer argument with the bounds of 1 to 99

.then(Commands.argument("amount", IntegerArgumentType.integer(1, 99))

// Here, we use method references, since otherwise, our command definition would grow too big

.suggests(SuggestionsTest::getAmountSuggestions)

.executes(SuggestionsTest::executeCommandLogic)

)

)

.build();

}

private static CompletableFuture<Suggestions> getAmountSuggestions(final CommandContext<CommandSourceStack> ctx, final SuggestionsBuilder builder) {

// Suggest 1, 16, 32, and 64 to the user when they reach the 'amount' argument

builder.suggest(1);

builder.suggest(16);

builder.suggest(32);

builder.suggest(64);

return builder.buildFuture();

}

private static int executeCommandLogic(final CommandContext<CommandSourceStack> ctx) {

// We know that the executor will be a player, so we can just silently return

if (!(ctx.getSource().getExecutor() instanceof Player player)) {

return Command.SINGLE_SUCCESS;

}

// If the player has no empty slot, we tell the player that they have no free inventory space

final int firstEmptySlot = player.getInventory().firstEmpty();

if (firstEmptySlot == -1) {

player.sendRichMessage("<light_purple>You do not have enough space in your inventory!");

return Command.SINGLE_SUCCESS;

}

// Retrieve our argument values

final ItemStack item = ctx.getArgument("item", ItemStack.class);

final int amount = IntegerArgumentType.getInteger(ctx, "amount");

// Set the item's amount and give it to the player

item.setAmount(amount);

player.getInventory().setItem(firstEmptySlot, item);

// Send a confirmation message

player.sendRichMessage("<light_purple>You have been given <white><amount>x</white> <aqua><item></aqua>!",

Placeholder.component("amount", Component.text(amount)),

Placeholder.component("item", Component.translatable(item).hoverEvent(item))

);

return Command.SINGLE_SUCCESS;

}

}
```

And here is how the command looks in-game:

[ 
Your device does not support video playback.
](/_astro/give-item-command.B4v-QnUF.mp4)

## Example: Filtering by user input

[Section titled “Example: Filtering by user input”](#example-filtering-by-user-input)

If you have multiple values, it is suggested that you filter your suggestions by what the user has already put in. For this, we can declare the following, simple command
as a test:

```java
public static LiteralCommandNode<CommandSourceStack> constructStringSuggestionsCommand() {

final List<String> names = List.of("Alex", "Andreas", "Stephanie", "Sophie", "Emily");

return Commands.literal("selectname")

.then(Commands.argument("name", StringArgumentType.word())

.suggests((ctx, builder) -> {

names.stream()

.filter(entry -> entry.toLowerCase().startsWith(builder.getRemainingLowerCase()))

.forEach(builder::suggest);

return builder.buildFuture();

})

).build();

}
```

This simple setup filters suggestions by user input, providing a smooth user experience when running the command:

[ 
Your device does not support video playback.
](/_astro/select-name-command.BF2GMAgq.mp4)


================================================================================
Chapter Title: Custom arguments
Original Link: https://docs.papermc.io/paper/dev/command-api/basics/custom-arguments/
================================================================================

Custom arguments are nothing more than a wrapper around existing argument types, which allow a developer to provide an argument with suggestions and reusable parsing in order to
reduce code repetition.

## Why would you use custom arguments?

[Section titled “Why would you use custom arguments?”](#why-would-you-use-custom-arguments)

As example, if you want to have an argument for a player, which is currently online and an operator, you could use a player argument type, add custom suggestions, and throw a
`CommandSyntaxException` in your `executes(...)` method body. This would look like this:

```java
Commands.argument("player", ArgumentTypes.player())

.suggests((ctx, builder) -> {

Bukkit.getOnlinePlayers().stream()

.filter(ServerOperator::isOp)

.map(Player::getName)

.filter(name -> name.toLowerCase(Locale.ROOT).startsWith(builder.getRemainingLowerCase()))

.forEach(builder::suggest);

return builder.buildFuture();

})

.executes(ctx -> {

final Player player = ctx.getArgument("player", PlayerSelectorArgumentResolver.class).resolve(ctx.getSource()).getFirst();

if (!player.isOp()) {

final Message message = MessageComponentSerializer.message().serialize(text(player.getName() + " is not a server operator!"));

throw new SimpleCommandExceptionType(message).create();

}

ctx.getSource().getSender().sendRichMessage("Player <player> is an operator!",

Placeholder.component("player", player.displayName())

);

return Command.SINGLE_SUCCESS;

})
```

As you can see, there is a ton of logic not directly involved with the functionality of the command. And if we want to use this same argument on another node, we have to
copy-paste a lot of code. It goes without saying that this would be incredibly tedious.

The solution to this problem are custom arguments. Before going into detail about them, this is how the argument would look when implemented as a custom argument:

OppedPlayerArgument.java

```java
@NullMarked

public final class OppedPlayerArgument implements CustomArgumentType<Player, PlayerSelectorArgumentResolver> {

private static final SimpleCommandExceptionType ERROR_BAD_SOURCE = new SimpleCommandExceptionType(

MessageComponentSerializer.message().serialize(Component.text("The source needs to be a CommandSourceStack!"))

);

private static final DynamicCommandExceptionType ERROR_NOT_OPERATOR = new DynamicCommandExceptionType(name -> {

return MessageComponentSerializer.message().serialize(Component.text(name + " is not a server operator!"));

});

@Override

public Player parse(StringReader reader) {

throw new UnsupportedOperationException("This method will never be called.");

}

@Override

public <S> Player parse(StringReader reader, S source) throws CommandSyntaxException {

if (!(source instanceof CommandSourceStack stack)) {

throw ERROR_BAD_SOURCE.create();

}

final Player player = getNativeType().parse(reader).resolve(stack).getFirst();

if (!player.isOp()) {

throw ERROR_NOT_OPERATOR.create(player.getName());

}

return player;

}

@Override

public ArgumentType<PlayerSelectorArgumentResolver> getNativeType() {

return ArgumentTypes.player();

}

@Override

public <S> CompletableFuture<Suggestions> listSuggestions(CommandContext<S> ctx, SuggestionsBuilder builder) {

Bukkit.getOnlinePlayers().stream()

.filter(ServerOperator::isOp)

.map(Player::getName)

.filter(name -> name.toLowerCase(Locale.ROOT).startsWith(builder.getRemainingLowerCase()))

.forEach(builder::suggest);

return builder.buildFuture();

}

}
```

At a first look, that seems like way more code than it was needed to just do the logic in the command tree itself. So what is the advantage?
The answer becomes apparent rather quickly when we look at how the argument is now declared:

```java
Commands.argument("player", new OppedPlayerArgument())

.executes(ctx -> {

final Player player = ctx.getArgument("player", Player.class);

ctx.getSource().getSender().sendRichMessage("Player <player> is an operator!",

Placeholder.component("player", player.displayName())

);

return Command.SINGLE_SUCCESS;

})
```

This is way more readable and easy to understand when using a custom argument. And it is reusable! Hopefully, you now have a basic grasp of **why** you should use custom arguments.

## Examining the `CustomArgumentType` interface

[Section titled “Examining the CustomArgumentType interface”](#examining-the-customargumenttype-interface)

The interface is declared as follows:

CustomArgumentType.java

```java
package io.papermc.paper.command.brigadier.argument;

@NullMarked

public interface CustomArgumentType<T, N> extends ArgumentType<T> {

@Override

T parse(final StringReader reader) throws CommandSyntaxException;

@Override

default <S> T parse(final StringReader reader, final S source) throws CommandSyntaxException {

return ArgumentType.super.parse(reader, source);

}

ArgumentType<N> getNativeType();

@Override

@ApiStatus.NonExtendable

default Collection<String> getExamples() {

return this.getNativeType().getExamples();

}

@Override

default <S> CompletableFuture<Suggestions> listSuggestions(final CommandContext<S> context, final SuggestionsBuilder builder) {

return ArgumentType.super.listSuggestions(context, builder);

}

}
```

### Generic types

[Section titled “Generic types”](#generic-types)

There are three generic types present in the interface:

* `T`: This is the type of the class that is returned when `CommandContext#getArgument` is called on this argument.
* `N`: The native type of the class which this custom argument extends. Used as the “underlying” argument.
* `S`: A generic type for the command source. Will usually be a `CommandSourceStack`.

### Methods

[Section titled “Methods”](#methods)

| Method declaration | Description |
| --- | --- |
| `ArgumentType<N> getNativeType()` | Here, you declare the underlying argument type, which is used as a base for client-side argument validation. |
| `T parse(final StringReader reader) throws CommandSyntaxException` | This method is used if `T parse(StringReader, S)` is not overridden. In here, you can run conversion and validation logic. |
| `default <S> T parse(final StringReader reader, final S source)` | If overridden, this method will be preferred to `T parse(StringReader)`. It serves the same purpose, but allows including the source in the parsing logic. |
| `default Collection<String> getExamples()` | This method should **not** be overridden. It is used internally to differentiate certain argument types while parsing. |
| `default <S> CompletableFuture<Suggestions> listSuggestions(final CommandContext<S> context, final SuggestionsBuilder builder)` | This method is the equivalent of `RequiredArgumentBuilder#suggests(SuggestionProvider<S>)`. You can override this method in order to send your own suggestions to the client. |

### A very basic implementation

[Section titled “A very basic implementation”](#a-very-basic-implementation)

```java
package io.papermc.commands;

import com.mojang.brigadier.StringReader;

import com.mojang.brigadier.arguments.ArgumentType;

import com.mojang.brigadier.arguments.StringArgumentType;

import io.papermc.paper.command.brigadier.argument.CustomArgumentType;

import org.jspecify.annotations.NullMarked;

@NullMarked

public class BasicImplementation implements CustomArgumentType<String, String> {

@Override

public String parse(StringReader reader) {

return reader.readUnquotedString();

}

@Override

public ArgumentType<String> getNativeType() {

return StringArgumentType.word();

}

}
```

Notice the use of `reader.readUnquotedString()`. In addition to allowing existing argument types to parse your argument,
you can also manually read input. Here, we read an unquoted string, the same as a word string argument type.

## `CustomArgumentType.Converted<T, N>`

[Section titled “CustomArgumentType.Converted<T, N>”](#customargumenttypeconvertedt-n)

In case that you need to parse the native type to your new type, you can instead use the `CustomArgumentType.Converted` interface.
This interface is an extension to the `CustomArgumentType` interface, which adds two new, overridable methods:

```java
T convert(N nativeType) throws CommandSyntaxException;

default <S> T convert(final N nativeType, final S source) throws CommandSyntaxException {

return this.convert(nativeType);

}
```

These methods work similarly to the `parse` methods, but they instead provide you with the parsed, native type instead of a `StringReader`.
This reduced the need to manually do string reader operations and instead directly uses the native type’s parsing rules.

## Error handling during the suggestions phase

[Section titled “Error handling during the suggestions phase”](#error-handling-during-the-suggestions-phase)

In case you are looking for the ability to make the client show currently typed input as red to display invalid input, it should be noted that this is **not possible** with
custom arguments. The client is only able to validate arguments it knows about and there is no way to throw a `CommandSyntaxException` during the suggestions phase. The only way to
achieve that is by using **literals**, but those cannot be modified dynamically during server runtime.

![](https://docs.papermc.io/_astro/ice-cream-invalid.DwGon3Tz_1EQz7T.webp)

## Example: Ice-cream argument

[Section titled “Example: Ice-cream argument”](#example-ice-cream-argument)

A practical example on how you can use a custom argument to your advantage could be a classical enum-type argument. In our case, we use this
`IceCreamFlavor` enum:

IceCreamFlavor.java

```java
package io.papermc.commands.icecream;

import org.jspecify.annotations.NullMarked;

@NullMarked

public enum IceCreamFlavor {

VANILLA,

CHOCOLATE,

STRAWBERRY;

@Override

public String toString() {

return name().toLowerCase();

}

}
```

We then can use a converted custom argument type in order to convert between a word string argument and our enum type, like this:

IceCreamArgument.java

```java
package io.papermc.commands.icecream;

@NullMarked

public class IceCreamArgument implements CustomArgumentType.Converted<IceCreamFlavor, String> {

private static final DynamicCommandExceptionType ERROR_INVALID_FLAVOR = new DynamicCommandExceptionType(flavor -> {

return MessageComponentSerializer.message().serialize(Component.text(flavor + " is not a valid flavor!"));

});

@Override

public IceCreamFlavor convert(String nativeType) throws CommandSyntaxException {

try {

return IceCreamFlavor.valueOf(nativeType.toUpperCase(Locale.ROOT));

} catch (IllegalArgumentException ignored) {

throw ERROR_INVALID_FLAVOR.create(nativeType);

}

}

@Override

public <S> CompletableFuture<Suggestions> listSuggestions(CommandContext<S> context, SuggestionsBuilder builder) {

for (IceCreamFlavor flavor : IceCreamFlavor.values()) {

String name = flavor.toString();

// Only suggest if the flavor name matches the user input

if (name.startsWith(builder.getRemainingLowerCase())) {

builder.suggest(flavor.toString());

}

}

return builder.buildFuture();

}

@Override

public ArgumentType<String> getNativeType() {

return StringArgumentType.word();

}

}
```

Finally, we can just declare our command like this, and we are done! And again, you can just directly get the argument as a ready `IceCreamFlavor`
type without any additional parsing in the `executes(...)` method, which makes custom argument types very powerful.

```java
Commands.literal("icecream")

.then(Commands.argument("flavor", new IceCreamArgument())

.executes(ctx -> {

final IceCreamFlavor flavor = ctx.getArgument("flavor", IceCreamFlavor.class);

ctx.getSource().getSender().sendRichMessage("<b><red>Y<green>U<aqua>M<light_purple>!</b> You just had a scoop of <flavor>!",

Placeholder.unparsed("flavor", flavor.toString())

);

return Command.SINGLE_SUCCESS;

})

)

.build();
```

![](https://docs.papermc.io/_astro/ice-cream.BgPSYVy0_1VpeF0.webp)


================================================================================
Chapter Title: Minecraft-specific
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/minecraft/
================================================================================

The [Arguments and Literals](https://docs.papermc.io/paper/dev/command-api/basics/arguments-and-literals) page covers the most used, native Brigadier arguments. But Minecraft (and Paper) define a few more. These can be accessed
in a static context using the [`ArgumentTypes`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/ArgumentTypes.html) class. We will go over all of those in this section.

## Quick overview

[Section titled “Quick overview”](#quick-overview)

A quick overview of all possible arguments is defined here:

| Method Name | Return Value | Quick Link |
| --- | --- | --- |
| `blockPosition()` | [BlockPositionResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/BlockPositionResolver.html) | [Block Position Argument](https://docs.papermc.io/paper/dev/command-api/arguments/location#block-position-argument) |
| `blockState()` | [BlockState](https://jd.papermc.io/paper/org/bukkit/block/BlockState.html) | [Block State Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#block-state-argument) |
| `component()` | [Component (Kyori)](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html) | [Component Argument](https://docs.papermc.io/paper/dev/command-api/arguments/adventure#component-argument) |
| `doubleRange()` | [DoubleRangeProvider](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/range/DoubleRangeProvider.html) | [Double Range argument](https://docs.papermc.io/paper/dev/command-api/arguments/predicate#double-range-argument) |
| `entity()` | [EntitySelectorArgumentResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/selector/EntitySelectorArgumentResolver.html) | [Entity Argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#entity-argument) |
| `entities()` | [EntitySelectorArgumentResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/selector/EntitySelectorArgumentResolver.html) | [Entities Argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#entities-argument) |
| `entityAnchor()` | [LookAnchor](https://jd.papermc.io/paper/io/papermc/paper/entity/LookAnchor.html) | [Entity Anchor Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#entity-anchor-argument) |
| `finePosition(boolean centerIntegers)` | [FinePositionResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/FinePositionResolver.html) | [Fine Position Argument](https://docs.papermc.io/paper/dev/command-api/arguments/location#fine-position-argument) |
| `gameMode()` | [GameMode](https://jd.papermc.io/paper/org/bukkit/GameMode.html) | [GameMode Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#gamemode-argument) |
| `heightMap()` | [HeightMap](https://jd.papermc.io/paper/org/bukkit/HeightMap.html) | [HeightMap Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#heightmap-argument) |
| `integerRange()` | [IntegerRangeProvider](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/range/IntegerRangeProvider.html) | [Integer Range Argument](https://docs.papermc.io/paper/dev/command-api/arguments/predicate#integer-range-argument) |
| `itemPredicate()` | [ItemStackPredicate](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/predicate/ItemStackPredicate.html) | [Item Predicate Argument](https://docs.papermc.io/paper/dev/command-api/arguments/predicate#item-predicate-argument) |
| `itemStack()` | [ItemStack](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html) | [ItemStack Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#itemstack-argument) |
| `key()` | [Key (Kyori)](https://jd.advntr.dev/key/latest/net/kyori/adventure/key/Key.html) | [Key Argument](https://docs.papermc.io/paper/dev/command-api/arguments/adventure#key-argument) |
| `namedColor()` | [NamedTextColor (Kyori)](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/format/NamedTextColor.html) | [Named Color Argument](https://docs.papermc.io/paper/dev/command-api/arguments/adventure#named-color-argument) |
| `namespacedKey()` | [NamespacedKey](https://jd.papermc.io/paper/org/bukkit/NamespacedKey.html) | [Bukkit NamespacedKey Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#namespacedkey-argument) |
| `objectiveCriteria()` | [Criteria](https://jd.papermc.io/paper/org/bukkit/scoreboard/Criteria.html) | [Objective Criteria Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#objective-criteria-argument) |
| `player()` | [PlayerSelectorArgumentResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/selector/PlayerSelectorArgumentResolver.html) | [Player Argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#player-argument) |
| `players()` | [PlayerSelectorArgumentResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/selector/PlayerSelectorArgumentResolver.html) | [Players Argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#players-argument) |
| `playerProfiles()` | [PlayerProfileListResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/PlayerProfileListResolver.html) | [Player Profiles Argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#player-profiles-argument) |
| `resource(RegistryKey)` | (Depends on RegistryKey) | [Resource Argument](https://docs.papermc.io/paper/dev/command-api/arguments/registry#resource-argument) |
| `resourceKey(RegistryKey)` | (Depends on RegistryKey) | [Resource Key Argument](https://docs.papermc.io/paper/dev/command-api/arguments/registry#resource-key-argument) |
| `style()` | [Style (Kyori)](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/format/Style.html) | [Style Argument](https://docs.papermc.io/paper/dev/command-api/arguments/adventure#adventure-style-argument) |
| `signedMessage()` | [SignedMessageResolver](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/SignedMessageResolver.html) | [Signed Message Argument](https://docs.papermc.io/paper/dev/command-api/arguments/adventure#signed-message-argument) |
| `scoreboardDisplaySlot()` | [DisplaySlot](https://jd.papermc.io/paper/org/bukkit/scoreboard/DisplaySlot.html) | [Scoreboard Display Slot Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#scoreboard-display-slot-argument) |
| `time(int mintime)` | Integer | [Time Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#time-argument) |
| `templateMirror()` | [Mirror](https://jd.papermc.io/paper/org/bukkit/block/structure/Mirror.html) | [Template Mirror Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#template-mirror-argument) |
| `templateRotation()` | [StructureRotation](https://jd.papermc.io/paper/org/bukkit/block/structure/StructureRotation.html) | [Template Rotation Argument](https://docs.papermc.io/paper/dev/command-api/arguments/enums#template-rotation-argument) |
| `uuid()` | UUID | [UUID Argument](https://docs.papermc.io/paper/dev/command-api/arguments/paper#uuid-argument) |
| `world()` | [World](https://jd.papermc.io/paper/org/bukkit/World.html) | [World Argument](https://docs.papermc.io/paper/dev/command-api/arguments/location#world-argument) |


================================================================================
Chapter Title: Location
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/location/
================================================================================

## Block position argument

[Section titled “Block position argument”](#block-position-argument)

The block position argument is used for retrieving the position of a block. It works the same way as the first argument of the `/setblock <position> <block>` Vanilla command.
In order to retrieve the `BlockPosition` variable from the
[`BlockPositionResolver`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/BlockPositionResolver.html), we have to resolve it using the command source.

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> blockPositionArgument() {

return Commands.literal("blockpositionargument")

.then(Commands.argument("arg", ArgumentTypes.blockPosition())

.executes(ctx -> {

final BlockPositionResolver blockPositionResolver = ctx.getArgument("arg", BlockPositionResolver.class);

final BlockPosition blockPosition = blockPositionResolver.resolve(ctx.getSource());

ctx.getSource().getSender().sendPlainMessage("Put in " + blockPosition.x() + " " + blockPosition.y() + " " + blockPosition.z());

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

[ 
Your device does not support video playback.
](/_astro/blockposition.M0WOO6Rj.mp4)

## Fine position argument

[Section titled “Fine position argument”](#fine-position-argument)

The fine position argument works similarly to the block position argument, with the only difference being that it can accept decimal (precise) location input. The optional
overload (`ArgumentTypes.finePosition(boolean centerIntegers)`), which defaults to false if not set, will center whole input, meaning 5 becomes 5.5 (5.0 would stay as 5.0 though),
as that is the “middle” of a block. This only applies to X/Z. The y coordinate is untouched by this operation.

This argument returns a [`FinePositionResolver`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/FinePositionResolver.html). You can resolve that by running `FinePositionResolver#resolve(CommandSourceStack)` to get the resulting
[`FinePosition`](https://jd.papermc.io/paper/io/papermc/paper/math/FinePosition.html).

### Example usage

[Section titled “Example usage”](#example-usage-1)

```java
public static LiteralCommandNode<CommandSourceStack> finePositionArgument() {

return Commands.literal("fineposition")

.then(Commands.argument("arg", ArgumentTypes.finePosition(true))

.executes(ctx -> {

final FinePositionResolver resolver = ctx.getArgument("arg", FinePositionResolver.class);

final FinePosition finePosition = resolver.resolve(ctx.getSource());

ctx.getSource().getSender().sendRichMessage("Position: <red><x></red> <green><y></green> <blue><z></blue>",

Placeholder.unparsed("x", Double.toString(finePosition.x())),

Placeholder.unparsed("y", Double.toString(finePosition.y())),

Placeholder.unparsed("z", Double.toString(finePosition.z()))

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/fineposition.DudQK_XO.mp4)

## World argument

[Section titled “World argument”](#world-argument)

This argument allows the user to select one of the currently loaded world. You can retrieve the result of that as a generic Bukkit
[`World`](https://jd.papermc.io/paper/org/bukkit/World.html) object.

### Example usage

[Section titled “Example usage”](#example-usage-2)

```java
public static LiteralCommandNode<CommandSourceStack> worldArgument() {

return Commands.literal("teleport-to-world")

.then(Commands.argument("world", ArgumentTypes.world())

.executes(ctx -> {

final World world = ctx.getArgument("world", World.class);

if (ctx.getSource().getExecutor() instanceof Player player) {

player.teleport(world.getSpawnLocation(), PlayerTeleportEvent.TeleportCause.COMMAND);

ctx.getSource().getSender().sendRichMessage("Successfully teleported <player> to <aqua><world></aqua>",

Placeholder.component("player", player.name()),

Placeholder.unparsed("world", world.getName())

);

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendRichMessage("<red>This command requires a player!");

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/world.DKrnF_6D.mp4)


================================================================================
Chapter Title: Entities and players
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/entity-player/
================================================================================

The arguments described in this section relate to arguments which you can use to retrieve entities. Their main usage is the selection of command targets.
All of these have entity selectors (`@a`, `@e`, `@n`, etc.) as valid inputs, though they require the `minecraft.command.selector` permission in order to
be able to be used. The specific arguments may allow or disallow certain selectors.

Due to the permission requirement for selectors it is advised to add a `requires` statement to your command:

```java
.requires(ctx -> ctx.getSender().hasPermission("minecraft.command.selector"))
```

You can find more information about requirements [here](https://docs.papermc.io/paper/dev/command-api/basics/requirements).

## Entity argument

[Section titled “Entity argument”](#entity-argument)

This argument, after resolving its returning `EntitySelectorArgumentResolver`, returns a list of exactly one, no more and no less, entity. It is safe
to call `List#getFirst()` to retrieve that entity. You can resolve it using [`ArgumentResolver#resolve(CommandSourceStack)`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/ArgumentResolver.html#resolve(io.papermc.paper.command.brigadier.CommandSourceStack))

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> entityArgument() {

return Commands.literal("entityarg")

.then(Commands.argument("arg", ArgumentTypes.entity())

.executes(ctx -> {

final EntitySelectorArgumentResolver entitySelectorArgumentResolver = ctx.getArgument("arg", EntitySelectorArgumentResolver.class);

final List<Entity> entities = entitySelectorArgumentResolver.resolve(ctx.getSource());

ctx.getSource().getSender().sendRichMessage("Found <green><entityname>",

Placeholder.component("entityname", entities.getFirst().name())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

If the executing player doesn’t have the `minecraft.command.selector` permission:

[ 
Your device does not support video playback.
](/_astro/entity-unopped.D1N9jElM.mp4)

If the executing player has the `minecraft.command.selector` permission:

[ 
Your device does not support video playback.
](/_astro/entity-opped.DJ6OQm3_.mp4)

## Entities argument

[Section titled “Entities argument”](#entities-argument)

In contrast to the single entity argument, this multiple-entities argument accepts any amount of entities, with the minimum amount of entities being 1. They can, once again, be resolved using
[`ArgumentResolver#resolve(CommandSourceStack)`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/resolvers/ArgumentResolver.html#resolve(io.papermc.paper.command.brigadier.CommandSourceStack)),
which returns a `List<Entity>`.

### Example usage

[Section titled “Example usage”](#example-usage-1)

```java
public static LiteralCommandNode<CommandSourceStack> entitiesArgument() {

return Commands.literal("entitiesarg")

.then(Commands.argument("arg", ArgumentTypes.entities())

.executes(ctx -> {

final EntitySelectorArgumentResolver entitySelectorArgumentResolver = ctx.getArgument("arg", EntitySelectorArgumentResolver.class);

final List<Entity> entities = entitySelectorArgumentResolver.resolve(ctx.getSource());

final Component foundEntities = Component.join(JoinConfiguration.commas(true), entities.stream().map(Entity::name).toList());

ctx.getSource().getSender().sendRichMessage("Found <green><entitynames>",

Placeholder.component("entitynames", foundEntities)

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/entities.Ci8k7Mem.mp4)

## Player argument

[Section titled “Player argument”](#player-argument)

The player argument allows to retrieve a `PlayerSelectorArgumentResolver` for player arguments.
For this “single player” argument, you can safely get the target player by running `PlayerSelectorArgumentResolver.resolve(ctx.getSource()).getFirst()`,
which returns a [Player](https://jd.papermc.io/paper/org/bukkit/entity/Player.html) object.

### Example usage

[Section titled “Example usage”](#example-usage-2)

This command yeets the targeted player into the air!

```java
public static LiteralCommandNode<CommandSourceStack> playerArgument() {

return Commands.literal("player")

.then(Commands.argument("target", ArgumentTypes.player())

.executes(ctx -> {

final PlayerSelectorArgumentResolver targetResolver = ctx.getArgument("target", PlayerSelectorArgumentResolver.class);

final Player target = targetResolver.resolve(ctx.getSource()).getFirst();

target.setVelocity(new Vector(0, 100, 0));

target.sendRichMessage("<rainbow>Yeeeeeeeeeet");

ctx.getSource().getSender().sendRichMessage("Yeeted <target>!",

Placeholder.component("target", target.name())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/player.kjODFTes.mp4)

## Players argument

[Section titled “Players argument”](#players-argument)

The “multiple players” argument works similarly to the “single player” argument, also returning a `PlayerSelectorArgumentResolver`. Instead of just resolving to exactly one `Player`, this
one can resolve to more than just one player - which you should account for in case of using this argument. `PlayerSelectorArgumentResolver.resolve(ctx.getSource())` returns a
`List<Player>`, which you can just iterate through.

### Example usage

[Section titled “Example usage”](#example-usage-3)

Extending the “single player” yeet command to support multiple targets can look like this:

```java
public static LiteralCommandNode<CommandSourceStack> playersArgument() {

return Commands.literal("players")

.then(Commands.argument("targets", ArgumentTypes.players())

.executes(ctx -> {

final PlayerSelectorArgumentResolver targetResolver = ctx.getArgument("targets", PlayerSelectorArgumentResolver.class);

final List<Player> targets = targetResolver.resolve(ctx.getSource());

final CommandSender sender = ctx.getSource().getSender();

for (final Player target : targets) {

target.setVelocity(new Vector(0, 100, 0));

target.sendRichMessage("<rainbow>Yeeeeeeeeeet");

sender.sendRichMessage("Yeeted <target>!",

Placeholder.component("target", target.name())

);

}

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-3)

[ 
Your device does not support video playback.
](/_astro/players.C11PUskT.mp4)

## Player profiles argument

[Section titled “Player profiles argument”](#player-profiles-argument)

The player profiles argument is a very powerful argument which can retrieve both offline and online players. It returns the result of the argument as a `PlayerProfileListResolver`,
which resolves to a `Collection<PlayerProfile>`. This collection can be iterated to get the resulting profile(s). Usually, it only returns a single `PlayerProfile` if retrieving
a player by name, but it can return multiple if using the entity selectors (like `@a` on online players). Thus it always makes sense to run whatever operation you want to run on
all entries in the collection instead of just the first one.

This argument will run API calls to Mojang servers in order to retrieve player information for players which have never joined the server before. Due to this operation sometimes
taking a bit longer, it is suggested to resolve this argument in an asynchronous context in order to not cause any server lag.

Sometimes, these API calls may fail. This is also visible in the in-game preview down below. This behavior is also the reason for `/whitelist add` sometimes.

### Example usage - player lookup command

[Section titled “Example usage - player lookup command”](#example-usage---player-lookup-command)

```java
public static LiteralCommandNode<CommandSourceStack> playerProfilesArgument() {

return Commands.literal("lookup")

.then(Commands.argument("profile", ArgumentTypes.playerProfiles())

.executes(ctx -> {

final PlayerProfileListResolver profilesResolver = ctx.getArgument("profile", PlayerProfileListResolver.class);

final Collection<PlayerProfile> foundProfiles = profilesResolver.resolve(ctx.getSource());

for (final PlayerProfile profile : foundProfiles) {

ctx.getSource().getSender().sendPlainMessage("Found " + profile.getName());

}

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-4)

[ 
Your device does not support video playback.
](/_astro/playerprofiles.DNelBGFn.mp4)


================================================================================
Chapter Title: Registry
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/registry/
================================================================================

Registries in Minecraft hold all sort of information - possible item or block types, enchantments, potion effects, … and more!

There are two types of registry arguments: `resource` and `resourceKey`.
The main difference between those arguments is the return value: The `resource` argument returns the parsed value, whilst the `resourceKey` only returns a `TypedKey`, which
you can use to retrieve the value yourself.

## Resource argument

[Section titled “Resource argument”](#resource-argument)

Just like any other argument, you can get a `ArgumentType<T>` reference to it using `ArgumentTypes.resource(RegistryKey<T>)`. A selection of possible registry keys can be
found below. They are accessed in a static context using the [`RegistryKey`](https://jd.papermc.io/paper/io/papermc/paper/registry/RegistryKey.html) interface.

Each entry in `RegistryKey` returns a `RegistryKey<T>`. The `<T>` generic parameter here describes the return type. This means that if we were to retrieve
[`RegistryKey.ITEM`](https://jd.papermc.io/paper/io/papermc/paper/registry/RegistryKey.html#ITEM), the return type would be an `ItemType`, since it is defined as follows:

RegistryKey.java

```java
public sealed interface RegistryKey<T> extends Keyed permits RegistryKeyImpl {

// ...

RegistryKey<ItemType> ITEM = RegistryKeyImpl.create("item");

// ...

}
```

And really, there isn’t much more to it. For that exact reason, here is an example on the implementation of such an argument:

```java
public static LiteralCommandNode<CommandSourceStack> enchantmentRegistry() {

return Commands.literal("enchants-registry")

.then(Commands.argument("enchantment", ArgumentTypes.resource(RegistryKey.ENCHANTMENT))

.executes(ctx -> {

final Enchantment enchantment = ctx.getArgument("enchantment", Enchantment.class);

if (ctx.getSource().getExecutor() instanceof Player player) {

final ItemStack stack = player.getInventory().getItemInMainHand();

stack.addUnsafeEnchantment(enchantment, 10);

ctx.getSource().getSender().sendRichMessage("Enchanted <player>'s <item> with <enchantment>!",

Placeholder.component("player", player.name()),

Placeholder.component("item", Component.translatable(stack)),

Placeholder.component("enchantment", enchantment.displayName(10))

);

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendRichMessage("<red>This command requires a player!");

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

We define an `enchantment` argument using a enchantment registry key resource and retrieve the value of that using `ctx.getArgument("enchantment", Enchantment.class)`.
Finally, we enchant the item of the executing player’s hand with whatever enchantment the sender chose at level 10 and send a success message.

Here is how it looks in-game:

[ 
Your device does not support video playback.
](/_astro/enchants-registry.CFJry4Gn.mp4)

Caution

There are certain edge-cases, where this argument, due to missing registries on the client, will cause a **Network Protocol Error**.
Basically, the only argument where this is the case right now is with the `STRUCTURE` registry key.

```java
// Registering this command will cause clients to not be able to connect to the server.

final LiteralCommandNode<CommandSourceStack> invalidRegistryArgument = Commands.literal("registry-structure")

.then(Commands.argument("value", ArgumentTypes.resource(RegistryKey.STRUCTURE)))

.build();
```

Due to this fact, it is advised to only use the `STRUCTURE` registry key argument with a `resourceKey(...)` argument type and parse the values yourself.

## Resource key argument

[Section titled “Resource key argument”](#resource-key-argument)

For the client, there is barely any difference between the using `ArgumentTypes.resource` or `ArgumentTypes.resourceKey`. The only difference is that
using `ArgumentTypes.resourceKey` does not provide **error checking**. We can visualize this using `RegistryKey.ITEM`.

Here is the tab completion when using `ArgumentTypes.resource(RegistryKey.ITEM)`:

[ 
Your device does not support video playback.
](/_astro/resource-item.B-JVrNDu.mp4)
  

And here is the tab completion when using `ArgumentTypes.resourceKey(RegistryKey.ITEM)`:

[ 
Your device does not support video playback.
](/_astro/resourcekey-item.CkRP0Kuf.mp4)
  

Note

In the example given above, due to an unhandled null pointer exception, the command does not successfully run. The code for that command is directly trying to use the value retrieved
by the registry access by doing `ItemType item = RegistryAccess.registryAccess().getRegistry(itemKey.registryKey()).get(itemKey.key())`. If you try to do any
operation with the result, it might be null and error.

You should **always** check the result of a registry retrieval operation. An example for that is given below in the [direct code comparison](#direct-code-comparison).

The resource argument provides a much cleaner user experience, whilst the `resourceKey` argument has one very important use case: You get the raw
`TypedKey<T>` returned as an argument result. This object is particularly useful, as it provides all information required to be able to retrieve
a value from a registry yourself.

Tip

Unless you have a specific reason for using the `resourceKey` argument over the `resource` one, the `resource` argument is preferred due to the client-side error
checking and simple usability.

### Direct code comparison

[Section titled “Direct code comparison”](#direct-code-comparison)

Here is a simple code snipped on how one could use the `RegistryKey.ITEM` registry with a `resource` argument type:

```java
Commands.argument("item", ArgumentTypes.resource(RegistryKey.ITEM))

.executes(ctx -> {

final ItemType item = ctx.getArgument("item", ItemType.class);

if (ctx.getSource().getExecutor() instanceof Player player) {

player.getInventory().addItem(item.createItemStack());

}

return Command.SINGLE_SUCCESS;

});
```

Here is the same code, using a `resourceKey` argument type. Instead of directly retrieving the argument using `ctx.getArgument("item", TypedKey.class)`, we instead use the
[`RegistryArgumentExtractor`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/RegistryArgumentExtractor.html) to retrieve our `TypedKey<ItemType>`.

```java
Commands.argument("item", ArgumentTypes.resourceKey(RegistryKey.ITEM))

.executes(ctx -> {

final TypedKey<ItemType> itemKey = RegistryArgumentExtractor.getTypedKey(ctx, RegistryKey.ITEM, "item");

ItemType item = RegistryAccess.registryAccess().getRegistry(itemKey.registryKey()).get(itemKey.key());

if (item == null) {

ctx.getSource().getSender().sendRichMessage("<red>Please provide a valid item!");

return Command.SINGLE_SUCCESS;

}

if (ctx.getSource().getExecutor() instanceof Player player) {

player.getInventory().addItem(item.createItemStack());

}

return Command.SINGLE_SUCCESS;

})
```

### Using a TypedKey

[Section titled “Using a TypedKey”](#using-a-typedkey)

First, in order to get the correct registry, you can run `RegistryAccess#getRegistry(RegistryKey)`. In order to get a `RegistryAccess`, you can just use the static
`RegistryAccess.registryAccess()` method. The `RegistryKey` is retrieved using `TypedKey#registryKey()`.
Now, in order to get the final value `T`, you can run `Registry#get(Key)`, where the key can be retrieved using `TypedKey#key()`. This will return the backing instance
from that resource key or null, if no value has been found.

### Use case over resource argument

[Section titled “Use case over resource argument”](#use-case-over-resource-argument)

The main use case for this argument type is the ability to store the key (the value returned to you by `TypedKey#key`). If you want to be able to store the exact user
input and be able to retrieve the backed instance without much trouble, that is the way to do it.

## Registry key previews

[Section titled “Registry key previews”](#registry-key-previews)

The following `RegistryKeys` exist:

| RegistryKeys Field | Return Value | Preview Video |
| --- | --- | --- |
| ATTRIBUTE | Attribute | [Attribute](#attribute) |
| BANNER\_PATTERN | PatternType | [Banner Pattern](#banner-pattern) |
| BIOME | Biome | [Biome](#biome) |
| BLOCK | BlockType | [Block](#block) |
| CAT\_VARIANT | Cat.Type | [Cat Variant](#cat-variant) |
| CHICKEN\_VARIANT | Chicken.Variant | [Chicken Variant](#chicken-variant) |
| COW\_VARIANT | Cow.Variant | [Cow Variant](#cow-variant) |
| DAMAGE\_TYPE | DamageType | [Damage Type](#damage-type) |
| DATA\_COMPONENT\_TYPE | DataComponentType | [Data Component Type](#data-component-type) |
| DIALOG | Dialog | [Dialog](#dialog) |
| ENCHANTMENT | Enchantment | [Enchantment](#enchantment) |
| ENTITY\_TYPE | EntityType | [Entity Type](#entity-type) |
| FLUID | Fluid | [Fluid](#fluid) |
| FROG\_VARIANT | Frog.Variant | [Frog Variant](#frog-variant) |
| GAME\_EVENT | GameEvent | [Game Event](#game-event) |
| INSTRUMENT | MusicInstrument | [Instrument](#instrument) |
| ITEM | ItemType | [Item](#item) |
| JUKEBOX\_SONG | JukeboxSong | [Jukebox Song](#jukebox-song) |
| MAP\_DECORATION\_TYPE | MapCursor.Type | [Map Decoration Type](#map-decoration-type) |
| MEMORY\_MODULE\_TYPE | MemoryKey<?> | [Memory Module Type](#memory-module-type) |
| MENU | MenuType | [Menu](#menu) |
| MOB\_EFFECT | PotionEffectType | [Mob effect](#mob-effect) |
| PAINTING\_VARIANT | Art | [Painting variant](#painting-variant) |
| PARTICLE\_TYPE | Particle | [Particle](#particle) |
| PIG\_VARIANT | Pig.Variant | [Pig Variant](#pig-variant) |
| POTION | PotionType | [Potion](#potion) |
| SOUND\_EVENT | Sound | [Sound](#sound) |
| STRUCTURE | Structure | [Structure](#structure) |
| STRUCTURE\_TYPE | StructureType | [Structure Type](#structure-type) |
| TRIM\_MATERIAL | TrimMaterial | [Trim Material](#trim-material) |
| TRIM\_PATTERN | TrimPattern | [Trim Pattern](#trim-pattern) |
| VILLAGER\_PROFESSION | Villager.Profession | [Villager Profession](#villager-profession) |
| VILLAGER\_TYPE | Villager.Type | [Villager Type](#villager-type) |
| WOLF\_SOUND\_VARIANT | Wolf.SoundVariant | [Wolf Sound Variant](#wolf-sound-variant) |
| WOLF\_VARIANT | Wolf.Variant | [Wolf Variant](#wolf-variant) |

### Attribute

[Section titled “Attribute”](#attribute)

[ 
Your device does not support video playback.
](/_astro/resource-attributes.BkJRbYPX.mp4)

### Banner pattern

[Section titled “Banner pattern”](#banner-pattern)

[ 
Your device does not support video playback.
](/_astro/resource-banner-pattern.CDyip5xc.mp4)

### Biome

[Section titled “Biome”](#biome)

[ 
Your device does not support video playback.
](/_astro/resource-biome.D8fS7zdz.mp4)

### Block

[Section titled “Block”](#block)

[ 
Your device does not support video playback.
](/_astro/resource-block.CLil1UKa.mp4)

### Cat variant

[Section titled “Cat variant”](#cat-variant)

[ 
Your device does not support video playback.
](/_astro/resource-cat-variant.vJSU0nEN.mp4)

### Chicken variant

[Section titled “Chicken variant”](#chicken-variant)

[ 
Your device does not support video playback.
](/_astro/resource-chicken-variant.CsYxp7jm.mp4)

### Cow variant

[Section titled “Cow variant”](#cow-variant)

[ 
Your device does not support video playback.
](/_astro/resource-cow-variant.Dv-QykPC.mp4)

### Damage type

[Section titled “Damage type”](#damage-type)

[ 
Your device does not support video playback.
](/_astro/resource-damage-type.Chhx-3GQ.mp4)

### Data component type

[Section titled “Data component type”](#data-component-type)

[ 
Your device does not support video playback.
](/_astro/resource-data-component-type.BfripP_o.mp4)

### Dialog

[Section titled “Dialog”](#dialog)

[ 
Your device does not support video playback.
](/_astro/resource-dialog.DHipYOoL.mp4)

### Enchantment

[Section titled “Enchantment”](#enchantment)

[ 
Your device does not support video playback.
](/_astro/resource-enchantment.BpOxw4kD.mp4)

### Entity type

[Section titled “Entity type”](#entity-type)

[ 
Your device does not support video playback.
](/_astro/resource-entity-type.B6HVmOkB.mp4)

### Fluid

[Section titled “Fluid”](#fluid)

[ 
Your device does not support video playback.
](/_astro/resource-fluid.CefdYNTl.mp4)

### Frog variant

[Section titled “Frog variant”](#frog-variant)

[ 
Your device does not support video playback.
](/_astro/resource-frog-variant.CRJyX4oH.mp4)

### Game event

[Section titled “Game event”](#game-event)

[ 
Your device does not support video playback.
](/_astro/resource-game-event.8lNM0aSU.mp4)

### Instrument

[Section titled “Instrument”](#instrument)

[ 
Your device does not support video playback.
](/_astro/resource-instrument.Bg7k4ao6.mp4)

### Item

[Section titled “Item”](#item)

[ 
Your device does not support video playback.
](/_astro/resource-item.B-JVrNDu.mp4)

### Jukebox Song

[Section titled “Jukebox Song”](#jukebox-song)

[ 
Your device does not support video playback.
](/_astro/resource-jukebox-song.v3ia4kky.mp4)

### Map decoration type

[Section titled “Map decoration type”](#map-decoration-type)

[ 
Your device does not support video playback.
](/_astro/resource-map-decoration-type.C_lMj4WP.mp4)

### Memory module type

[Section titled “Memory module type”](#memory-module-type)

[ 
Your device does not support video playback.
](/_astro/resource-memory-module-type.BesiknDu.mp4)

### Menu

[Section titled “Menu”](#menu)

[ 
Your device does not support video playback.
](/_astro/resource-menu.DAADn3fE.mp4)

### Mob effect

[Section titled “Mob effect”](#mob-effect)

[ 
Your device does not support video playback.
](/_astro/resource-mob-effect.DsJgentz.mp4)

### Painting variant

[Section titled “Painting variant”](#painting-variant)

[ 
Your device does not support video playback.
](/_astro/resource-painting-variant.CtsMBA7Q.mp4)

### Particle

[Section titled “Particle”](#particle)

[ 
Your device does not support video playback.
](/_astro/resource-particle-type.C25GhWfc.mp4)

### Pig variant

[Section titled “Pig variant”](#pig-variant)

[ 
Your device does not support video playback.
](/_astro/resource-pig-variant.DJ0HnuQA.mp4)

### Potion

[Section titled “Potion”](#potion)

[ 
Your device does not support video playback.
](/_astro/resource-potion.CKVYV7sT.mp4)

### Sound

[Section titled “Sound”](#sound)

[ 
Your device does not support video playback.
](/_astro/resource-sound-event.ClhBhxsy.mp4)

### Structure

[Section titled “Structure”](#structure)

This argument kicks the client, so no preview for this one ¯\\_(ツ)\_/¯

### Structure type

[Section titled “Structure type”](#structure-type)

[ 
Your device does not support video playback.
](/_astro/resource-structure-type.DWeRP41j.mp4)

### Trim material

[Section titled “Trim material”](#trim-material)

[ 
Your device does not support video playback.
](/_astro/resource-trim-material.BWXLV3uT.mp4)

### Trim pattern

[Section titled “Trim pattern”](#trim-pattern)

[ 
Your device does not support video playback.
](/_astro/resource-trim-pattern.ISalJl1s.mp4)

### Villager profession

[Section titled “Villager profession”](#villager-profession)

[ 
Your device does not support video playback.
](/_astro/resource-villager-profession.miyBbFiy.mp4)

### Villager type

[Section titled “Villager type”](#villager-type)

[ 
Your device does not support video playback.
](/_astro/resource-villager-type.NgbpEPT_.mp4)

### Wolf sound variant

[Section titled “Wolf sound variant”](#wolf-sound-variant)

[ 
Your device does not support video playback.
](/_astro/resource-wolf-sound-variant.DSCRvSNL.mp4)

### Wolf variant

[Section titled “Wolf variant”](#wolf-variant)

[ 
Your device does not support video playback.
](/_astro/resource-wolf-variant.Cv0rL6T9.mp4)


================================================================================
Chapter Title: Paper-specific
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/paper/
================================================================================

The arguments in this section return objects frequently used in Paper API.

## Block state argument

[Section titled “Block state argument”](#block-state-argument)

The block state argument can be used for getting a block type and explicit, associated data.

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> blockStateArgument() {

return Commands.literal("blockstateargument")

.then(Commands.argument("arg", ArgumentTypes.blockState())

.executes(ctx -> {

final BlockState blockState = ctx.getArgument("arg", BlockState.class);

ctx.getSource().getSender().sendPlainMessage("You specified a " + blockState.getType() + "!");

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

[ 
Your device does not support video playback.
](/_astro/blockstate.Ca1vJxgG.mp4)

## ItemStack argument

[Section titled “ItemStack argument”](#itemstack-argument)

The item stack argument is the way to retrieve an [`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html) following the same argument format as the Vanilla `/give <player> <item> [<amount>]`
command as its second argument. The user may also define components to further customize the `ItemStack`. If you only require a [`Material`](https://jd.papermc.io/paper/org/bukkit/Material.html), you should instead
check out the [registry arguments](https://docs.papermc.io/paper/dev/command-api/arguments/registry).

### Example usage

[Section titled “Example usage”](#example-usage-1)

```java
public static LiteralCommandNode<CommandSourceStack> itemStackArgument() {

return Commands.literal("itemstack")

.then(Commands.argument("stack", ArgumentTypes.itemStack())

.executes(ctx -> {

final ItemStack itemStack = ctx.getArgument("stack", ItemStack.class);

if (ctx.getSource().getExecutor() instanceof Player player) {

player.getInventory().addItem(itemStack);

ctx.getSource().getSender().sendRichMessage("<green>Successfully gave <player> a <item>",

Placeholder.component("player", player.name()),

Placeholder.component("item", Component.translatable(itemStack))

);

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendRichMessage("<red>This argument requires a player!");

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/itemstack.DfagSbHv.mp4)

## NamespacedKey argument

[Section titled “NamespacedKey argument”](#namespacedkey-argument)

This argument allows the user to provide any artificial (namespaced) key. The return value of this argument is a
[`NamespacedKey`](https://jd.papermc.io/paper/org/bukkit/NamespacedKey.html), which makes it useful when dealing with Bukkit API.

### Example usage

[Section titled “Example usage”](#example-usage-2)

```java
public static LiteralCommandNode<CommandSourceStack> namespacedKeyArgument() {

return Commands.literal("namespacedkey")

.then(Commands.argument("key", ArgumentTypes.namespacedKey())

.executes(ctx -> {

final NamespacedKey key = ctx.getArgument("key", NamespacedKey.class);

ctx.getSource().getSender().sendRichMessage("You put in <aqua><key></aqua>!",

Placeholder.unparsed("key", key.toString())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/namespacedkey.iVt3x9AG.mp4)

## Time argument

[Section titled “Time argument”](#time-argument)

The time argument allows the user to define a time frame, similar to the Vanilla `/time <set|time> <time>` time argument. The user has 4 possible ways of inputting time:

* Just as a number: This resolves to as usual ticks (`/timearg 1` —> 1 tick)
* With a `t` suffix: This also resolves to ticks (`/timearg 1t` —> 1 tick)
* With a `s` suffix: This resolves to seconds, meaning multiplying the first number by 20. (`/timearg 1s` —> 20 ticks)
* With a `d` suffix. This resolves as in-game days, meaning multiplying the first number by 24000. (`/timearg 1d` —> 24000 ticks)

If you choose to use this argument, it is advised to explain to the users what these suffixes mean, as real time (`s` suffix) is mixed with in-game time (`t` and `d` suffix).

The `ArgumentTypes.time()` method has one additional overload: `ArgumentTypes.time(int mintime)`. This allows to set the minimum required amount of ticks this argument has to resolve to.
By default this value is set to 0.

### Example usage

[Section titled “Example usage”](#example-usage-3)

```java
public static LiteralCommandNode<CommandSourceStack> timeArgument() {

return Commands.literal("timearg")

.then(Commands.argument("time", ArgumentTypes.time())

.executes(ctx -> {

final int timeInTicks = IntegerArgumentType.getInteger(ctx, "time");

if (ctx.getSource().getExecutor() instanceof Player player) {

player.getWorld().setFullTime(player.getWorld().getFullTime() + timeInTicks);

player.sendRichMessage("Moved time forward by " + timeInTicks + " ticks!");

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendPlainMessage("This argument requires a player!");

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-3)

[ 
Your device does not support video playback.
](/_astro/time.7NmFdTe-.mp4)

## UUID argument

[Section titled “UUID argument”](#uuid-argument)

The UUID argument allows the user to input a valid UUID. You can retrieve that value as a `UUID` object, which is used in various places, like `Bukkit.getOfflinePlayer(UUID)`.
This argument is not very user-friendly, which is why it is suggested to only use this as a moderation or debug argument. For user input regarding offline player
retrieval, the [player profiles argument](https://docs.papermc.io/paper/dev/command-api/arguments/entity-player#player-profiles-argument) is preferred, as it allows by-name lookup.

### Example usage - Lookup command

[Section titled “Example usage - Lookup command”](#example-usage---lookup-command)

```java
public static LiteralCommandNode<CommandSourceStack> uuidArgument() {

return Commands.literal("uuid-lookup")

.then(Commands.argument("uuid", ArgumentTypes.uuid())

.executes(ctx -> {

final UUID uuid = ctx.getArgument("uuid", UUID.class);

final OfflinePlayer result = Bukkit.getOfflinePlayer(uuid);

ctx.getSource().getSender().sendRichMessage("Has <aqua><uuid></aqua> played before: <result>",

Placeholder.unparsed("uuid", uuid.toString()),

Placeholder.parsed("result", result.hasPlayedBefore() ? "<green>true</green>" : "<red>false</red>")

);

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-4)

[ 
Your device does not support video playback.
](/_astro/uuid.Yp4ES51A.mp4)

## Objective criteria argument

[Section titled “Objective criteria argument”](#objective-criteria-argument)

You can retrieve the argument value as a `Criteria` enum value, which can be used with `Scoreboard` objects.

### Example usage

[Section titled “Example usage”](#example-usage-4)

```java
public static LiteralCommandNode<CommandSourceStack> objectiveCriteriaArgument() {

return Commands.literal("objectivecriteria")

.then(Commands.argument("criteria", ArgumentTypes.objectiveCriteria())

.executes(ctx -> {

final Criteria criteria = ctx.getArgument("criteria", Criteria.class);

ctx.getSource().getSender().sendRichMessage("Default render type for <criteria>: <rendertype>",

Placeholder.unparsed("criteria", criteria.getName()),

Placeholder.unparsed("rendertype", criteria.getDefaultRenderType().name())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-5)

[ 
Your device does not support video playback.
](/_astro/objectivecriteria.BdZOlix7.mp4)


================================================================================
Chapter Title: Enums
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/enums/
================================================================================

## Entity anchor argument

[Section titled “Entity anchor argument”](#entity-anchor-argument)

The entity anchor argument has two valid inputs: `feet` and `eyes`. The resulting [`LookAnchor`](https://jd.papermc.io/paper/io/papermc/paper/entity/LookAnchor.html) is mainly used for methods like
[`Entity#lookAt(Position, LookAnchor)`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#lookAt(io.papermc.paper.math.Position,io.papermc.paper.entity.LookAnchor)) or
[`Player#lookAt(Entity, LookAnchor, LookAnchor)`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#lookAt(org.bukkit.entity.Entity,io.papermc.paper.entity.LookAnchor,io.papermc.paper.entity.LookAnchor)).

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> entityAnchorArgument() {

return Commands.literal("entityanchor")

.then(Commands.argument("arg", ArgumentTypes.entityAnchor())

.executes(ctx -> {

final LookAnchor lookAnchor = ctx.getArgument("arg", LookAnchor.class);

ctx.getSource().getSender().sendRichMessage("You chose <aqua><anchor></aqua>!",

Placeholder.unparsed("anchor", lookAnchor.name())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

[ 
Your device does not support video playback.
](/_astro/entityanchor.B4hnFy39.mp4)

## GameMode argument

[Section titled “GameMode argument”](#gamemode-argument)

The game mode argument works the same way as the first argument of the Vanilla `/gamemode <gamemode>` command. It accepts any of the 4 valid game modes, returning
a [`GameMode`](https://jd.papermc.io/paper/org/bukkit/GameMode.html) enum to use in code.

### Example usage

[Section titled “Example usage”](#example-usage-1)

```java
public static LiteralCommandNode<CommandSourceStack> gameModeArgument() {

return Commands.literal("gamemodearg")

.then(Commands.argument("arg", ArgumentTypes.gameMode())

.executes(ctx -> {

final GameMode gamemode = ctx.getArgument("arg", GameMode.class);

if (ctx.getSource().getExecutor() instanceof Player player) {

player.setGameMode(gamemode);

player.sendRichMessage("Your gamemode has been set to <red><gamemode></red>!",

Placeholder.component("gamemode", Component.translatable(gamemode))

);

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendPlainMessage("This command requires a player!");

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/gamemode.CSX0dhyN.mp4)

## HeightMap argument

[Section titled “HeightMap argument”](#heightmap-argument)

The [`HeightMap`](https://jd.papermc.io/paper/org/bukkit/HeightMap.html) argument consists of the following, valid inputs: `motion_blocking`, `motion_blocking_no_leaves`, `ocean_floor`, and `world_surface`. It is often
used for declaring relative positioning for data packs or the `/execute positioned over <height_map>` command. E.g. `world_surface`
would mean that the Y coordinate of the surface of the world on the set X/Z values should be used.

### Example usage

[Section titled “Example usage”](#example-usage-2)

```java
public static LiteralCommandNode<CommandSourceStack> heightMapArgument() {

return Commands.literal("heightmap")

.then(Commands.argument("arg", ArgumentTypes.heightMap())

.executes(ctx -> {

final HeightMap heightMap = ctx.getArgument("arg", HeightMap.class);

ctx.getSource().getSender().sendRichMessage("You selected <gold><selection></gold>",

Placeholder.unparsed("selection", heightMap.name())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/heightmap.C1K2t520.mp4)

## Scoreboard display slot argument

[Section titled “Scoreboard display slot argument”](#scoreboard-display-slot-argument)

This argument allows you to retrieve a [`DisplaySlot`](https://jd.papermc.io/paper/org/bukkit/scoreboard/DisplaySlot.html) enum value from the user.

### Example usage

[Section titled “Example usage”](#example-usage-3)

```java
public static LiteralCommandNode<CommandSourceStack> scoreboardDisplaySlotArgument() {

return Commands.literal("scoreboarddisplayslot")

.then(Commands.argument("slot", ArgumentTypes.scoreboardDisplaySlot())

.executes(ctx -> {

final DisplaySlot slot = ctx.getArgument("slot", DisplaySlot.class);

ctx.getSource().getSender().sendPlainMessage("You selected: " + slot.getId());

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-3)

[ 
Your device does not support video playback.
](/_astro/scoreboarddisplayslot.DbPSi1Ca.mp4)

## Template mirror argument

[Section titled “Template mirror argument”](#template-mirror-argument)

Here, the user has 3 valid input possibilities: `front_back`, `left_right`, and `none`. You can retrieve the result of
the argument as a [`Mirror`](https://jd.papermc.io/paper/org/bukkit/block/structure/Mirror.html) enum value.

### Example usage

[Section titled “Example usage”](#example-usage-4)

```java
public static LiteralCommandNode<CommandSourceStack> templateMirrorArgument() {

return Commands.literal("templatemirror")

.then(Commands.argument("mirror", ArgumentTypes.templateMirror())

.executes(ctx -> {

final Mirror mirror = ctx.getArgument("mirror", Mirror.class);

ctx.getSource().getSender().sendPlainMessage("You selected: " + mirror.name());

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-4)

[ 
Your device does not support video playback.
](/_astro/templatemirror.234uRkBd.mp4)

## Template rotation argument

[Section titled “Template rotation argument”](#template-rotation-argument)

For the template rotation argument, the user has 4 valid input possibilities: `180`, `clockwise_90`, `counterclockwise_90`, and `none`. You can retrieve the result
of the argument as a [`StructureRotation`](https://jd.papermc.io/paper/org/bukkit/block/structure/StructureRotation.html) enum value.

### Example usage

[Section titled “Example usage”](#example-usage-5)

```java
public static LiteralCommandNode<CommandSourceStack> templateRotationArgument() {

return Commands.literal("templaterotation")

.then(Commands.argument("rotation", ArgumentTypes.templateRotation())

.executes(ctx -> {

final StructureRotation rotation = ctx.getArgument("rotation", StructureRotation.class);

ctx.getSource().getSender().sendPlainMessage("You selected: " + rotation.name());

return Command.SINGLE_SUCCESS;

})

).build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-5)

[ 
Your device does not support video playback.
](/_astro/templaterotation.Dmzj8eae.mp4)


================================================================================
Chapter Title: Predicates
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/predicate/
================================================================================

A predicate allows for checking for valid values. These arguments are dedicated to checking whether some sort of value is valid according to user input.

## Double range argument

[Section titled “Double range argument”](#double-range-argument)

This argument can be used as a predicate for numbers, which require precise input.

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> doubleRangeArgument() {

return Commands.literal("doublerange")

.then(Commands.argument("arg", ArgumentTypes.doubleRange())

.executes(ctx -> {

final DoubleRangeProvider doubleRangeProvider = ctx.getArgument("arg", DoubleRangeProvider.class);

final CommandSender sender = ctx.getSource().getSender();

for (int i = 0; i < 5; i++) {

sender.sendRichMessage("Is <index> in bounds? <result>",

Placeholder.unparsed("index", Integer.toString(i)),

Placeholder.unparsed("result", Boolean.toString(doubleRangeProvider.range().test((double) i)))

);

}

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

[ 
Your device does not support video playback.
](/_astro/doublerange.DMtKyOBR.mp4)

## Integer range argument

[Section titled “Integer range argument”](#integer-range-argument)

This argument works very similarly to the double range argument, with the only difference being that this argument only accepts integers.

### Example usage

[Section titled “Example usage”](#example-usage-1)

MinecraftArguments.java

```java
public static LiteralCommandNode<CommandSourceStack> integerRangeArgument() {

return Commands.literal("integerrange")

.then(Commands.argument("range", ArgumentTypes.integerRange())

.then(Commands.argument("tested_integer", IntegerArgumentType.integer())

.executes(MinecraftArguments::runIntegerRangeCommand)))

.build();

}

private static int runIntegerRangeCommand(final CommandContext<CommandSourceStack> ctx) {

final IntegerRangeProvider integerRangeProvider = ctx.getArgument("range", IntegerRangeProvider.class);

final int integerToTest = IntegerArgumentType.getInteger(ctx, "tested_integer");

if (integerRangeProvider.range().contains(integerToTest)) {

ctx.getSource().getSender().sendRichMessage("<aqua><input></aqua> <green>is</green> inside the specified range!",

Placeholder.unparsed("input", Integer.toString(integerToTest))

);

return Command.SINGLE_SUCCESS;

}

ctx.getSource().getSender().sendRichMessage("<aqua><input></aqua> <red>is not</red> inside the specified range!",

Placeholder.unparsed("input", Integer.toString(integerToTest))

);

return Command.SINGLE_SUCCESS;

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/integerrange.CmIluBR1.mp4)

## Item predicate argument

[Section titled “Item predicate argument”](#item-predicate-argument)

This argument allows for checking whether an item fits some predicate. It is useful for filtering out certain items based on some criteria.

### Example usage

[Section titled “Example usage”](#example-usage-2)

```java
public static LiteralCommandNode<CommandSourceStack> itemPredicateArgument() {

return Commands.literal("itempredicate")

.then(Commands.argument("predicate", ArgumentTypes.itemPredicate())

.executes(ctx -> {

final ItemStackPredicate predicate = ctx.getArgument("predicate", ItemStackPredicate.class);

final ItemStack defaultWoodenSword = ItemType.WOODEN_SWORD.createItemStack();

ctx.getSource().getSender().sendRichMessage("Does predicate include a default wooden sword? <result>",

Placeholder.parsed("result", predicate.test(defaultWoodenSword) ? "<green>true</green>" : "<red>false</red>")

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/itempredicate.Cvfybj4M.mp4)


================================================================================
Chapter Title: Adventure
Original Link: https://docs.papermc.io/paper/dev/command-api/arguments/adventure/
================================================================================

These arguments return a class from the `net.kyori` package. They are technically not native to Minecraft or Bukkit, but as Paper includes the Adventure library, they are
widely used in the Paper ecosystem.

## Component argument

[Section titled “Component argument”](#component-argument)

Note

This argument is very technical. Following the same format as the `/tellraw <player> <component>` command for its second argument, it expects the JSON
representation of a text component, making it inappropriate for general user input.

The result is returned as an Adventure component to work with.

### Example usage

[Section titled “Example usage”](#example-usage)

```java
public static LiteralCommandNode<CommandSourceStack> componentArgument() {

return Commands.literal("componentargument")

.then(Commands.argument("arg", ArgumentTypes.component())

.executes(ctx -> {

final Component component = ctx.getArgument("arg", Component.class);

ctx.getSource().getSender().sendRichMessage(

"Your message: <input>",

Placeholder.component("input", component)

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

[ 
Your device does not support video playback.
](/_astro/component.AgrTNg1-.mp4)

## Key argument

[Section titled “Key argument”](#key-argument)

The key argument allows a user to put in any artificial (namespaced) key, ensuring its validity. This returns a [`Key`](https://jd.advntr.dev/key/latest/net/kyori/adventure/key/Key.html),
which can be used at various other places in the Paper API.

### Example usage

[Section titled “Example usage”](#example-usage-1)

```java
public static LiteralCommandNode<CommandSourceStack> keyArgument() {

return Commands.literal("key")

.then(Commands.argument("key_input", ArgumentTypes.key())

.executes(ctx -> {

final Key key = ctx.getArgument("key_input", Key.class);

ctx.getSource().getSender().sendRichMessage("You put in <aqua><key></aqua>!",

Placeholder.unparsed("key", key.asString())

);

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-1)

[ 
Your device does not support video playback.
](/_astro/key.C1ssPMwA.mp4)

## Named color argument

[Section titled “Named color argument”](#named-color-argument)

This argument provides the user with the ability to select between the 16 built-in “named” text colors. This argument returns a
[`NamedTextColor`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/format/NamedTextColor.html),
which you can use for applying a color to components.

### Example usage

[Section titled “Example usage”](#example-usage-2)

```java
public static LiteralCommandNode<CommandSourceStack> namedColorArgument() {

return Commands.literal("namedcolor")

.then(Commands.argument("color", ArgumentTypes.namedColor())

.then(Commands.argument("message", StringArgumentType.greedyString())

.executes(ctx -> {

final NamedTextColor color = ctx.getArgument("color", NamedTextColor.class);

final String msg = StringArgumentType.getString(ctx, "message");

ctx.getSource().getSender().sendMessage(

Component.text(msg).color(color)

);

return Command.SINGLE_SUCCESS;

})))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-2)

[ 
Your device does not support video playback.
](/_astro/namedcolor.ByH9xLeG.mp4)

## Adventure style argument

[Section titled “Adventure style argument”](#adventure-style-argument)

Note

Similar to the component argument, this argument is not really appropriate for general user input, as it also follows the JSON format for displaying components. Most users
do not know how to use that format and thus its general usage is not advised.

The style argument returns its value in the form of a [`Style`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/format/Style.html) object.
This can be applied to any component using `Component#style(Style)`. Whilst the JSON input allows for the `text` field, its content is completely ignored.

### Example usage

[Section titled “Example usage”](#example-usage-3)

```java
public static LiteralCommandNode<CommandSourceStack> styleArgument() {

return Commands.literal("style")

.then(Commands.argument("style", ArgumentTypes.style())

.then(Commands.argument("message", StringArgumentType.greedyString())

.executes(ctx -> {

final Style style = ctx.getArgument("style", Style.class);

final String msg = StringArgumentType.getString(ctx, "message");

ctx.getSource().getSender().sendRichMessage("Your input: <input>",

Placeholder.component("input", Component.text(message).style(style))

);

return Command.SINGLE_SUCCESS;

})))

.build();

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-3)

[ 
Your device does not support video playback.
](/_astro/style.LG2_UHbk.mp4)

## Signed message argument

[Section titled “Signed message argument”](#signed-message-argument)

The signed message argument allows a player to send an argument in the form of a **signed message** to the server. This signed message is a special type - it
allows the server to send that message, without the ability to directly modify it, to any player. The visible difference is that unsigned messages have a white bar at the left,
whilst signed messages don’t.

A signed message argument returns a `SignedMessageResolver`. In order to call its `#resolve` method, you have to pass in two parameters:

* The argument name
* The `CommandContext<CommandSourceStack>` object

The resolved value is a `CompletableFuture<SignedMessage>`, whose [`SignedMessage`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/SignedMessage.html)
value you can handle using `thenAccept(Consumer<T>)`. Inside of the consumer, you can send the signed message to players or work with it in other ways.

Caution

By default, the consumer passed into `thenAccept` is not executed on the main thread, making it unsafe to use most of Paper API within it.
If you need to use the API, you can schedule a task to be run on the next available tick. For this you can use the
[main thread executor](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitScheduler.html#getMainThreadExecutor(org.bukkit.plugin.Plugin)).
You can read up on that [here](https://docs.papermc.io/paper/dev/scheduler).

Note

A non-player sender is not capable of sending a signed message, which means that the resolved `CompletableFuture` will never be completed.
You should make sure that only players can use your argument with `.requires(ctx -> ctx.getSender() instanceof Player)` on your `SignedArgument`. You may
add a fallback greedy string argument for non-player senders if you want the argument to execute regardless of signing.

### Example usage

[Section titled “Example usage”](#example-usage-4)

MinecraftArguments.java

```java
public static LiteralCommandNode<CommandSourceStack> signedMessageArgument() {

return Commands.literal("signedmessage")

.then(Commands.argument("target", ArgumentTypes.player())

.then(Commands.argument("message", ArgumentTypes.signedMessage())

.executes(MinecraftArguments::executeSignedMessageCommand)))

.build();

}

private static int executeSignedMessageCommand(final CommandContext<CommandSourceStack> ctx) throws CommandSyntaxException {

final Player target = ctx.getArgument("target", PlayerSelectorArgumentResolver.class).resolve(ctx.getSource()).getFirst();

final SignedMessageResolver messageResolver = ctx.getArgument("message", SignedMessageResolver.class);

messageResolver.resolveSignedMessage("message", ctx).thenAccept(msg -> {

target.sendMessage(msg, ChatType.CHAT.bind(ctx.getSource().getSender().name()));

});

return Command.SINGLE_SUCCESS;

}
```

### In-game preview

[Section titled “In-game preview”](#in-game-preview-4)

[ 
Your device does not support video playback.
](/_astro/signedmessage.8CJk9RH1.mp4)


================================================================================
Chapter Title: Basic commands
Original Link: https://docs.papermc.io/paper/dev/command-api/misc/basic-command/
================================================================================

For very simple commands Paper has a way to declare Bukkit-style commands by implementing the [`BasicCommand`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/BasicCommand.html) interface.

This interface has one method you have to override:

* `void execute(CommandSourceStack source, String[] args)`

And three more, optional methods which you can, but don’t have to override:

* `Collection<String> suggest(CommandSourceStack source, String[] args)`
* `boolean canUse(CommandSender sender)`
* `@Nullable String permission()`

## Simple usage

[Section titled “Simple usage”](#simple-usage)

Implementing the execute method, your class might look like this:

YourCommand.java

```java
package your.package.name;

import io.papermc.paper.command.brigadier.BasicCommand;

import io.papermc.paper.command.brigadier.CommandSourceStack;

import org.jspecify.annotations.NullMarked;

@NullMarked

public class YourCommand implements BasicCommand {

@Override

public void execute(CommandSourceStack source, String[] args) {

}

}
```

With a `CommandSourceStack` you can retrieve basic information about the sender of the command, the location the command was send from,
and the entity for which the command was executed for. You can find more information on [our page on command executors](https://docs.papermc.io/paper/dev/command-api/basics/executors).

## The optional methods

[Section titled “The optional methods”](#the-optional-methods)

You can freely choose whether to implement either of the mentioned, optional methods. Here is a quick overview on what which one does:

### `suggest(CommandSourceStack, String[])`

[Section titled “suggest(CommandSourceStack, String[])”](#suggestcommandsourcestack-string)

This method returns some sort of `Collection<String>` and takes in a `CommandSourceStack` and a `String[] args` as parameters. This is similar to the
`onTabComplete(CommandSender, Command, String, String[])` method of the `TabCompleter` interface, which is used for tab completion on Bukkit commands.

Each entry in the collection that you return will be send to the client to be shown as suggestions the same way as with Bukkit commands.

### `canUse(CommandSender)`

[Section titled “canUse(CommandSender)”](#canusecommandsender)

With this method, you can set up a basic `requires` structure from Brigadier commands. [You can read more on that here](https://docs.papermc.io/paper/dev/command-api/basics/requirements).
This method returns a `boolean`, which is required to return `true` in order for a command sender to be able to execute that command.

Note

If you override this method, overriding `permission()` does nothing. This is because the default implementation
uses the return value of `permission()`, which wouldn’t be used anymore if you were to override it.

BasicCommand.java

```java
default boolean canUse(final CommandSender sender) {

final String permission = this.permission();

return permission == null || sender.hasPermission(permission);

}
```

### `permission()`

[Section titled “permission()”](#permission)

With the permission method you can, similar to the `canUse` method, set the permission required to be able to execute and view this command.

## Registering basic commands

[Section titled “Registering basic commands”](#registering-basic-commands)

Registering a `BasicCommand` is very simple: In your plugin’s main class, you can simply call one of the
[`registerCommand(...)`](https://jd.papermc.io/paper/org/bukkit/plugin/java/JavaPlugin.html#registerCommand(java.lang.String,io.papermc.paper.command.brigadier.BasicCommand))
methods inside the `onEnable` method.

YourPlugin.java

```java
public class YourPlugin extends JavaPlugin {

@Override

public void onEnable() {

BasicCommand yourCommand = ...;

registerCommand("mycommand", yourCommand);

}

}
```

### Basic commands are functional interfaces

[Section titled “Basic commands are functional interfaces”](#basic-commands-are-functional-interfaces)

Because you only have to override one method, you can directly pass in a lambda statement. This is not recommended for styling
reasons, as it makes the code harder to read.

```java
@Override

public void onEnable() {

registerCommand(

"quickcmd",

(source, args) -> source.getSender().sendRichMessage("<yellow>Hello!")

);

}
```

## Example: Broadcast command

[Section titled “Example: Broadcast command”](#example-broadcast-command)

As an example, we can create a simple broadcast command. We start by declaring creating a class which implements `BasicCommand` and overrides `execute` and `permission`:

BroadcastCommand.java

```java
package your.package.name;

import io.papermc.paper.command.brigadier.BasicCommand;

import io.papermc.paper.command.brigadier.CommandSourceStack;

import org.jspecify.annotations.NullMarked;

import org.jspecify.annotations.Nullable;

@NullMarked

public class BroadcastCommand implements BasicCommand {

@Override

public void execute(CommandSourceStack source, String[] args) {

}

@Override

public @Nullable String permission() {

return "example.broadcast.use";

}

}
```

Our permission is set to `example.broadcast.use`. In order to give yourself that permission, it is suggested that you use a plugin like [LuckPerms](https://luckperms.net) or just give yourself
operator permissions. You can also set this permission to be `true` by default. For this, please check out the [plugin.yml documentation](https://docs.papermc.io/paper/dev/plugin-yml).

Now, in our `execute` method, we can retrieve the name of the executor of that command. If we do not find one, we can just get the name of the command sender, like this:

```java
final Component name = source.getExecutor() != null

? source.getExecutor().name()

: source.getSender().name();
```

This makes sure that we cover all cases and even allow the command to work correctly with `/execute as`.

Next, we retrieve all arguments and join them to a string or tell the sender that at least one argument is required in order to send a broadcast in case they defined no
arguments (meaning that `args` has a length of 0):

```java
if (args.length == 0) {

source.getSender().sendRichMessage("<red>You cannot send an empty broadcast!");

return;

}

final String message = String.join(" ", args);
```

Finally, we can build our broadcast message and send it via `Bukkit.broadcast(Component)`:

```java
final Component broadcastMessage = MiniMessage.miniMessage().deserialize(

"<red><bold>BROADCAST</red> <name> <dark_gray>»</dark_gray> <message>",

Placeholder.component("name", name),

Placeholder.unparsed("message", message)

);

Bukkit.broadcast(broadcastMessage);
```

And we are done! As you can see, this is a very simple way to define commands. Here is the final result of our class:

BroadcastCommand.java

```java
package your.package.name;

import io.papermc.paper.command.brigadier.BasicCommand;

import io.papermc.paper.command.brigadier.CommandSourceStack;

import net.kyori.adventure.text.Component;

import net.kyori.adventure.text.minimessage.MiniMessage;

import net.kyori.adventure.text.minimessage.tag.resolver.Placeholder;

import org.bukkit.Bukkit;

import org.jspecify.annotations.NullMarked;

import org.jspecify.annotations.Nullable;

@NullMarked

public class BroadcastCommand implements BasicCommand {

@Override

public void execute(CommandSourceStack source, String[] args) {

final Component name = source.getExecutor() != null

? source.getExecutor().name()

: source.getSender().name();

if (args.length == 0) {

source.getSender().sendRichMessage("<red>You cannot send an empty broadcast!");

return;

}

final String message = String.join(" ", args);

final Component broadcastMessage = MiniMessage.miniMessage().deserialize(

"<red><bold>BROADCAST</red> <name> <dark_gray>»</dark_gray> <message>",

Placeholder.component("name", name),

Placeholder.unparsed("message", message)

);

Bukkit.broadcast(broadcastMessage);

}

@Override

public @Nullable String permission() {

return "example.broadcast.use";

}

}
```

Registering the command looks like this:

PluginMainClass.java

```java
@Override

public void onEnable() {

registerCommand("broadcast", new BroadcastCommand());

}
```

And this is how it looks like in-game:
![](https://docs.papermc.io/_astro/broadcast-command.B-V19PYL_qVtVU.webp)

### Adding suggestions

[Section titled “Adding suggestions”](#adding-suggestions)

Our broadcast command works pretty well, but it is lacking on suggestions. A very common kind of suggestion for text based commands are player names.
In order to suggest player names, we can just map all online players to their name, like this:

```java
@Override

public Collection<String> suggest(CommandSourceStack source, String[] args) {

return Bukkit.getOnlinePlayers().stream().map(Player::getName).toList();

}
```

This works great, but as you can see here, it will always suggest all players, regardless of user input, which can feel unnatural at times:
![](https://docs.papermc.io/_astro/broadcast-suggestions-unfinished.CQP8ruUs_Z4rGIF.webp)

In order to fix this, we have to do some changes:

First, we early return what we already have in case there is no arguments, as we cannot filter by input then:

```java
if (args.length == 0) {

return Bukkit.getOnlinePlayers().stream().map(Player::getName).toList();

}
```

After this, we can add a `filter` clause to our stream, where we filter all names by whether they start with our current input, which is `args[args.length - 1]`:

```java
return Bukkit.getOnlinePlayers().stream()

.map(Player::getName)

.filter(name -> name.toLowerCase().startsWith(args[args.length - 1].toLowerCase()))

.toList();
```

And we are done! As you can see, suggestions still work fine:
![](https://docs.papermc.io/_astro/broadcast-suggestions-finished.CUL7XqRN_2l4pQs.webp)

But when there is no player who starts with an input, it just suggests nothing:
![](https://docs.papermc.io/_astro/broadcast-suggestions-none.iBum2A2i_2wAgiJ.webp)

### Final code

[Section titled “Final code”](#final-code)

Here is the final code for our whole `BroadcastCommand` class, including the suggestions:

```java
package your.package.name;

import io.papermc.paper.command.brigadier.BasicCommand;

import io.papermc.paper.command.brigadier.CommandSourceStack;

import net.kyori.adventure.text.Component;

import net.kyori.adventure.text.minimessage.MiniMessage;

import net.kyori.adventure.text.minimessage.tag.resolver.Placeholder;

import org.bukkit.Bukkit;

import org.bukkit.entity.Player;

import org.jspecify.annotations.NullMarked;

import org.jspecify.annotations.Nullable;

import java.util.Collection;

@NullMarked

public class BroadcastCommand implements BasicCommand {

@Override

public void execute(CommandSourceStack source, String[] args) {

final Component name = source.getExecutor() != null

? source.getExecutor().name()

: source.getSender().name();

if (args.length == 0) {

source.getSender().sendRichMessage("<red>You cannot send an empty broadcast!");

return;

}

final String message = String.join(" ", args);

final Component broadcastMessage = MiniMessage.miniMessage().deserialize(

"<red><bold>BROADCAST</red> <name> <dark_gray>»</dark_gray> <message>",

Placeholder.component("name", name),

Placeholder.unparsed("message", message)

);

Bukkit.broadcast(broadcastMessage);

}

@Override

public @Nullable String permission() {

return "example.broadcast.use";

}

@Override

public Collection<String> suggest(CommandSourceStack source, String[] args) {

if (args.length == 0) {

return Bukkit.getOnlinePlayers().stream().map(Player::getName).toList();

}

return Bukkit.getOnlinePlayers().stream()

.map(Player::getName)

.filter(name -> name.toLowerCase().startsWith(args[args.length - 1].toLowerCase()))

.toList();

}

}
```


================================================================================
Chapter Title: Comparison
Original Link: https://docs.papermc.io/paper/dev/command-api/misc/comparison-bukkit-brigadier/
================================================================================

## Registering commands

[Section titled “Registering commands”](#registering-commands)

### The old Bukkit way

[Section titled “The old Bukkit way”](#the-old-bukkit-way)

In order to register Bukkit commands, you would define a class that extends `BukkitCommand`, and implements the `execute(...)` and `tabComplete(...)`
methods. This might look like this:

BukkitPartyCommand.java

```java
package your.package.name;

import org.bukkit.Bukkit;

import org.bukkit.command.CommandSender;

import org.bukkit.command.defaults.BukkitCommand;

import org.bukkit.entity.Player;

import org.jspecify.annotations.NullMarked;

import java.util.List;

@NullMarked

public class BukkitPartyCommand extends BukkitCommand {

public BukkitPartyCommand(String name, String description, String usageMessage, List<String> aliases) {

super(name, description, usageMessage, aliases);

}

@Override

public boolean execute(CommandSender sender, String commandLabel, String[] args) {

if (args.length == 0) {

sender.sendPlainMessage("Please provide a player!");

return false;

}

final Player targetPlayer = Bukkit.getPlayer(args[0]);

if (targetPlayer == null) {

sender.sendPlainMessage("Please provide a valid player!");

return false;

}

targetPlayer.sendPlainMessage(sender.getName() + " started partying with you!");

sender.sendPlainMessage("You are now partying with " + targetPlayer.getName() + "!");

return true;

}

@Override

public List<String> tabComplete(CommandSender sender, String alias, String[] args) throws IllegalArgumentException {

if (args.length == 1) {

return Bukkit.getOnlinePlayers().stream().map(Player::getName).toList();

}

return List.of();

}

}
```

After that, you can define your command like this:

PluginClass.java

```java
this.getServer().getCommandMap().register(

this.getName().toLowerCase(),

new BukkitPartyCommand("bukkitparty", "Have a party", "/bukkitparty <player>", List.of())

);
```

As you can see, you have to do a lot of manual checking in order to register a single, very simple command. But how does
the Brigadier API do it?

### The new Paper way

[Section titled “The new Paper way”](#the-new-paper-way)

First, we need to retrieve a `LiteralCommandNode<CommandSourceStack>`. That’s a special Brigadier class that holds some sort of [command tree](https://docs.papermc.io/paper/dev/command-api/basics/command-tree).
In our case, it is the root of our command. We can do that by running `Commands.literal(final String literal)`, which returns a
`LiteralArgumentBuilder<CommandSourceStack>`, where we can define some arguments and executors. Once we are done, we can call
`LiteralArgumentBuilder#build()` to retrieve our build `LiteralCommandNode`, which we can then register. That sounds complicated at first,
but once you see it in action, it looks less terrifying:

PaperPartyCommand.java

```java
public static LiteralCommandNode<CommandSourceStack> createCommand(final String commandName) {

return Commands.literal(commandName)

.then(Commands.argument("target", ArgumentTypes.player())

.executes(ctx -> {

final PlayerSelectorArgumentResolver playerSelector = ctx.getArgument("target", PlayerSelectorArgumentResolver.class);

final Player targetPlayer = playerSelector.resolve(ctx.getSource()).getFirst();

final CommandSender sender = ctx.getSource().getSender();

targetPlayer.sendPlainMessage(sender.getName() + " started partying with you!");

sender.sendPlainMessage("You are now partying with " + targetPlayer.getName() + "!");

return Command.SINGLE_SUCCESS;

}))

.build();

}
```

Each `.then(...)` defines a new branch in our tree, which can either be a literal (`Commands.literal(String)`) or an argument
(`Commands.argument(String, ArgumentType<T>)`). Each branch may or may not define an `.executes(Command)` executor. This is
where all the logic happens.

We will take a closer look at that in different pages, but for now, how do we register it? Paper uses a `LifecycleEventManager` system.
In a nutshell, that is a way to register commands (or tags) that get loaded each time the server reloads its resources, like using /reload.
Registering our command looks like this:

PluginClass.java

```java
this.getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS, commands -> {

commands.registrar().register(PaperPartyCommand.createCommand("paperparty"), "Have a nice party");

});
```

And we are done! As you can see here, both commands do the same thing:

![](https://docs.papermc.io/_astro/bukkitparty-command.Bui70wtw_Z1UiJef.webp) ![](https://docs.papermc.io/_astro/paperparty-command.CPdWND_7_fAd7N.webp)


================================================================================
Chapter Title: Introduction
Original Link: https://docs.papermc.io/paper/dev/component-api/introduction/
================================================================================

Note

This documentation page applies to both the Paper and Velocity projects.

Since Minecraft 1.7, the game has utilized components to represent text to be displayed
by clients. Components offer a number of benefits over plain text strings which are enumerated below.
Paper and Velocity natively implements the Adventure API to add component support wherever possible.

## Why you should use Components

[Section titled “Why you should use Components”](#why-you-should-use-components)

Previously, text was a linear structure with the only formatting options being
confusing symbols like `§c` and `§k` to control basic colors and styles of text.
Components are a tree-like structure that inherits style and colors from their parents.

Components have several types which do different things than just display raw text, like
translating text to the client’s language based on a key, or showing a client-specific keybind
to a player.

All these component types support more style options like any RGB color, interaction events
(click and hover). The other component types and these style options have poor or missing
representations in the legacy string format.

## Usage

[Section titled “Usage”](#usage)

Representing text as components is now the supported way of representing text for Paper and Velocity. They are used
for almost all aspects of text being displayed to clients. Text like item names, lore, bossbars, team prefixes and
suffixes, custom names, and much more all support components in respective APIs.
[Mojang has stated](https://bugs-legacy.mojang.com/browse/MC-190605?focusedId=993040&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-993040)
that client support for the legacy format with `§` will be removed in the future.

Tip

In the Paper API, there are lots of deprecated methods and types that deal with this legacy format. This is to
signal that a better alternative in components is available and should be migrated to going forward.

## Creating components

[Section titled “Creating components”](#creating-components)

Components can be interacted with as objects. There are different interfaces for each type along with
builders for all the types. These objects are immutable so when constructing more complex components, it’s
recommended to use builders to avoid creating new Component instances with every change.

```java
// This is a sub-optimal construction of the

// component as each change creates a new component

final Component component = Component.text("Hello")

.color(TextColor.color(0x13f832))

.append(Component.text(" world!", NamedTextColor.GREEN));

/* This is an optimal use of the builder to create

the same component. Also note that Adventure

Components are designed for use with static method imports

to make code less verbose */

final Component component = text()

.content("Hello").color(color(0x13f832))

.append(text(" world!", GREEN))

.build();
```

In-Depth Documentation

For complete documentation on the Adventure Component API Paper and Velocity use, please look at the
[Adventure documentation](https://docs.advntr.dev).

## MiniMessage

[Section titled “MiniMessage”](#minimessage)

Paper and Velocity include the MiniMessage library, which is a string representation of components. If you prefer working with
strings rather than objects, MiniMessage is vastly superior to the legacy string format. It can utilize the tree
structure for style inheritance and can represent the more complex component types while legacy cannot.

```java
final Component component = MiniMessage.miniMessage().deserialize(

"<#438df2><b>This is the parent component; its style is " +

"applied to all children.\n<u><!b>This is the first child, " +

"which is rendered after the parent</!b></u><key:key.inventory></b></#438df2>"

);

// if the syntax above is too verbose for you, create a helper method!

public final class Components {

public static Component mm(String miniMessageString) { // mm, short for MiniMessage

return MiniMessage.miniMessage().deserialize(miniMessageString);

}

}

// ...

import static io.papermc.docs.util.Components.mm; // replace with your own package

final Component component = mm("<blue>Hello <red>World!");
```

We recommend using this format for user-facing input such as commands or configuration values.

In-Depth Documentation

MiniMessage is a part of Adventure, and you can find its documentation on [Adventure’s documentation](https://docs.papermc.io/adventure/minimessage/).

Tip

MiniMessage has a [web viewer](https://webui.advntr.dev/), which is useful for constructing more complicated components and seeing the results in real time.

## JSON format

[Section titled “JSON format”](#json-format)

Components can be serialized and deserialized from a standard JSON format. This format is used
in Vanilla in various commands which accept component arguments like `/tellraw`. Below is a simple example
of this format.

```java
{

"text": "This is the parent component; its style is applied to all children.\n",

"color": "#438df2",

"bold": true,

"extra": [

{

"text": "This is this first child, which is rendered after the parent",

"underlined": true,

// This overrides the parent's "bold" value just for this component

"bold": false

},

{

// This is a keybind component which will display the client's keybind for that action

"keybind": "key.inventory"

}

]

}
```

In-Depth Documentation

The JSON format is fully documented on the [Minecraft Wiki](https://minecraft.wiki/w/Text_component_format).

Tip

There are online tools to make generating this format much easier like [JSON Text Generator](https://minecraft.tools/en/json_text.php).

## Serializers

[Section titled “Serializers”](#serializers)

Paper and Velocity come bundled with different serializers for converting between
[`Component`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html)s and other forms of serialized text.

### [`GsonComponentSerializer`](https://jd.advntr.dev/text-serializer-gson/latest)

[Section titled “GsonComponentSerializer”](#gsoncomponentserializer)

Converts between `Component`
and JSON-formatted strings with convenience methods to directly deal with Gson’s
[`JsonElement`](https://javadoc.io/doc/com.google.code.gson/gson/latest/com.google.gson/com/google/gson/JsonElement.html).
This conversion is lossless and is the preferred form of serialization for components that do not have to be edited by users regularly.

### [`MiniMessage`](https://jd.advntr.dev/text-minimessage/latest)

[Section titled “MiniMessage”](#minimessage-1)

Converts between `Component`
and a MiniMessage-formatted string. This conversion is lossless and is the preferred form of
serialization for components that have to be edited by users. There is also extensive customization you can add to the
serializer, which is [documented here](https://docs.papermc.io/adventure/minimessage/api/#getting-started).

### [`PlainTextComponentSerializer`](https://jd.advntr.dev/text-serializer-plain/latest)

[Section titled “PlainTextComponentSerializer”](#plaintextcomponentserializer)

Serializes a `Component` into a plain text string. This is very lossy as all style information as well as most other
types of components will lose information. There may be special handling for
[`TranslatableComponent`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/TranslatableComponent.html)s to be serialized
into a default language, but generally this shouldn’t be used except in certain circumstances, like logging to a text file.

### [`LegacyComponentSerializer`](https://jd.advntr.dev/text-serializer-legacy/latest)

[Section titled “LegacyComponentSerializer”](#legacycomponentserializer)

Caution

This is not recommended for use as the legacy format may be removed in the future.

Converts between `Component` and the legacy string format.
This conversion is very lossy as component types and events do not have a legacy string representation.

A more useful use case is converting legacy text to MiniMessage format in a migration process.

```java
final String legacyString = ChatColor.RED + "This is a legacy " + ChatColor.GOLD + "string";

// runs the legacy string through two serializers to convert legacy -> MiniMessage

final String miniMessageString = MiniMessage.miniMessage().serialize(

LegacyComponentSerializer.legacySection().deserialize(legacyString)

);
```

Note

There are 2 built-in legacy serializers, one dealing with `§` symbols and the other for
`&` symbols. They have their own instances available through
[`LegacyComponentSerializer#legacySection()`](https://jd.advntr.dev/text-serializer-legacy/latest/net/kyori/adventure/text/serializer/legacy/LegacyComponentSerializer.html#legacySection())
and [`LegacyComponentSerializer#legacyAmpersand()`](https://jd.advntr.dev/text-serializer-legacy/latest/net/kyori/adventure/text/serializer/legacy/LegacyComponentSerializer.html#legacyAmpersand()).


================================================================================
Chapter Title: Internationalization
Original Link: https://docs.papermc.io/paper/dev/component-api/i18n/
================================================================================

Generally it’s a good idea to support translations in your plugin, especially if you want to
appeal to the largest user base. Adventure makes this simple by adding a server-side
translation layer to almost all text that ends up being displayed to clients.

Javadocs

Adventure’s Javadocs for all-things translations can be found [here](https://jd.advntr.dev/api/latest/net/kyori/adventure/translation/package-summary.html).

## GlobalTranslator

[Section titled “GlobalTranslator”](#globaltranslator)

All translation is done through [`GlobalTranslator`](https://jd.advntr.dev/api/latest/net/kyori/adventure/translation/GlobalTranslator.html).
You can render translations yourself and add new sources for translations.

You can add sources to the `GlobalTranslator` by creating instances of [`TranslationStore`](https://jd.advntr.dev/api/latest/net/kyori/adventure/translation/TranslationStore.html)
or implementing the [`Translator`](https://jd.advntr.dev/api/latest/net/kyori/adventure/translation/Translator.html) interface yourself.

## Where translations work

[Section titled “Where translations work”](#where-translations-work)

Vanilla Minecraft handles translations on the client by using the language files bundled with the client or provided via resource packs. If you don’t want to send custom language files
in a resource pack, server-side translations are the only alternative. They work anywhere the component API exists, except for [`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html)
display text like the display name or lore. So chat, entity display names, scoreboards, tab lists, etc., all support translations.

## Examples

[Section titled “Examples”](#examples)

### `ResourceBundle`

[Section titled “ResourceBundle”](#resourcebundle)

src/main/resources/your/plugin/Bundle\_en\_US.properties

```java
some.translation.key=Translated Message: {0}
```

```java
TranslationStore.StringBased<MessageFormat> store = TranslationStore.messageFormat(Key.key("namespace:value"));

ResourceBundle bundle = ResourceBundle.getBundle("your.plugin.Bundle", Locale.US, UTF8ResourceBundleControl.get());

store.registerAll(Locale.US, bundle, true);

GlobalTranslator.translator().addSource(store);
```

This creates a new `TranslationStore` under a specified namespace. Then, a [`ResourceBundle`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ResourceBundle.html)
is created from a bundle located on the classpath with the specified [`Locale`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Locale.html).
Finally, that `ResourceBundle` is added to the store. That store is then added as a source to the `GlobalTranslator`.
This makes all the translations available server-side.

Now you can use your translation keys in translatable components.

```java
Component.translatable("some.translation.key", Component.text("The Argument"))
```

This will show to clients using the US English language: `Translated Message: The Argument`.


================================================================================
Chapter Title: Audiences
Original Link: https://docs.papermc.io/paper/dev/component-api/audiences/
================================================================================

Audiences wrap a collection of recipients that can receive messages. They can be used to send messages to individual
players, groups of players, or even the entire server (including the console).

## Who is an `Audience`?

[Section titled “Who is an Audience?”](#who-is-an-audience)

All `CommandSender`s are single audiences. This includes players, the console, and command blocks. `Server`, `Team` and
`World` are all forwarding audiences. This means that they are made up of multiple audiences. For example, the server is
made up of all online players and the console.

This means that all the [`Audience`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html)
methods are available on [`CommandSender`](https://jd.papermc.io/paper/org/bukkit/command/CommandSender.html),
[`Server`](https://jd.papermc.io/paper/org/bukkit/Server.html), [`Team`](https://jd.papermc.io/paper/org/bukkit/scoreboard/Team.html)
and [`World`](https://jd.papermc.io/paper/org/bukkit/World.html).

## `ForwardingAudience`

[Section titled “ForwardingAudience”](#forwardingaudience)

The [`ForwardingAudience`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/ForwardingAudience.html)
wraps a collection of [`Audience`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html)
instances and forwards messages to all of them. This is useful for sending messages to multiple audiences (players) at once.

```java
// Server is a ForwardingAudience which includes all online players and the console

ForwardingAudience audience = Bukkit.getServer();

// To construct an audience from a collection of players, use:

Audience audience = Audience.audience(Audience...);

// If you pass in a single Audience, it will be returned as-is. If you pass in a collection of Audiences, they will be

// wrapped in a ForwardingAudience.
```

## What do `Audience`s do?

[Section titled “What do Audiences do?”](#what-do-audiences-do)

Audiences are used for interacting with players. They can be used to send messages, play sounds, show bossbars, and more.
They are mostly used for sending other parts of the API to players. For example, you can send a [`Component`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html)
to a player using [`Audience#sendMessage(Component)`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#sendMessage(net.kyori.adventure.text.Component)).

## Pointers

[Section titled “Pointers”](#pointers)

Audiences can also provide arbitrary information, such as display name or UUID. This is done using the pointer system.

```java
// Get the uuid from an audience member, returning an Optional<UUID>

Optional<UUID> uuid = audience.get(Identity.UUID);

// Get the display name, returning a default

Component name = audience.getOrDefault(Identity.DISPLAY_NAME, Component.text("no display name!"));
```


================================================================================
Chapter Title: Signed messages
Original Link: https://docs.papermc.io/paper/dev/component-api/signed-messages/
================================================================================

Since [Minecraft version 1.19](https://minecraft.wiki/w/Java_Edition_1.19), the client now signs any
messages it sends so that they are uniquely identifiable and verifiable to be sent by a specific player.
With this update, they also introduced the ability **delete specific messages** previously sent by a player.

Note

This guide does not go in-depth into the specifics of chat signing and its implementation on either client or server.
For a full overview, you can refer [to this linked gist](https://gist.github.com/kennytv/ed783dd244ca0321bbd882c347892874).

## How are signed messages represented in code?

[Section titled “How are signed messages represented in code?”](#how-are-signed-messages-represented-in-code)

Paper uses Adventure’s [`SignedMessage`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/SignedMessage.html)
object to represent a signed message. We differentiate two kinds of signed messages: system messages and non-system messages.
System messages (checked with [`SignedMessage#isSystem()`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/SignedMessage.html#isSystem()))
are messages send by the server, whilst non-system messages are not.

You can also differentiate the **signed plain text** `String` content of the message
([`SignedMessage#message()`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/SignedMessage.html#message()))
from the unsigned, nullable [`Component`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html)
content ([`SignedMessage#unsignedContent()`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/SignedMessage.html#unsignedContent())).

## Obtaining a signed message

[Section titled “Obtaining a signed message”](#obtaining-a-signed-message)

Signed messages can be obtained in two ways.

1. From an [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html) using
   [`AbstractChatEvent#signedMessage()`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AbstractChatEvent.html#signedMessage()).
2. From an [`ArgumentTypes.signedMessage()`](https://jd.papermc.io/paper/io/papermc/paper/command/brigadier/argument/ArgumentTypes.html#signedMessage())
   Brigadier argument type.

## Using signed messages

[Section titled “Using signed messages”](#using-signed-messages)

You can send signed message objects to an [`Audience`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html)
using the [`Audience#sendMessage(SignedMessage, ChatType.Bound)`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#sendMessage(net.kyori.adventure.chat.SignedMessage,net.kyori.adventure.chat.ChatType.Bound))
method. You can obtain a [`ChatType.Bound`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/ChatType.Bound.html) object
from the [`ChatType`](https://jd.advntr.dev/api/latest/net/kyori/adventure/chat/ChatType.html) interface.

Deleting messages is much simpler. Adventure provides the [`Audience#deleteMessage(SignedMessage)`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#deleteMessage(net.kyori.adventure.chat.SignedMessage))
or [`Audience#deleteMessage(SignedMessage.Signature)`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#deleteMessage(net.kyori.adventure.chat.SignedMessage.Signature))
methods for that.

## Example: Making user sent messages deletable

[Section titled “Example: Making user sent messages deletable”](#example-making-user-sent-messages-deletable)

For our example, we will create a chat format plugin which allows a user to delete
their own messages in case they made a mistake. For this we will use the [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html).

AsyncChatEvent

The [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html) is covered in the [chat events](https://docs.papermc.io/paper/dev/chat-events)
documentation page. If you want to read up on more detail on the chat renderer, you can do so there.

### In-game preview

[Section titled “In-game preview”](#in-game-preview)

![](https://docs.papermc.io/_astro/signed-messages-deletion.CS-ZEcGo_1piilQ.webp)

### Code

[Section titled “Code”](#code)

SignedChatListener.java

```java
10 collapsed lines

1

package io.papermc.docs.signedmessages;

2

3

import io.papermc.paper.event.player.AsyncChatEvent;

4

import net.kyori.adventure.text.Component;

5

import net.kyori.adventure.text.event.ClickEvent;

6

import net.kyori.adventure.text.format.NamedTextColor;

7

import net.kyori.adventure.text.format.TextDecoration;

8

import org.bukkit.Bukkit;

9

import org.bukkit.event.EventHandler;

10

import org.bukkit.event.Listener;

11

12

public class SignedChatListener implements Listener {

13

14

@EventHandler

15

void onPlayerChat(AsyncChatEvent event) {

16

// We modify the chat format, so we use a chat renderer.

17

event.renderer((player, playerName, message, viewer) -> {

18

// This is the base format of our message. It will format chat as "<player> » <message>".

19

final Component base = Component.textOfChildren(

20

playerName.colorIfAbsent(NamedTextColor.GOLD),

21

Component.text(" » ", NamedTextColor.DARK_GRAY),

22

message

23

);

24

25

// Send the base format to any player who is not the sender.

26

if (viewer != player) {

27

return base;

28

}

29

30

// Create a base delete suffix. The creation is separated into two

31

// parts purely for readability reasons.

32

final Component deleteCrossBase = Component.textOfChildren(

33

Component.text("[", NamedTextColor.DARK_GRAY),

34

Component.text("X", NamedTextColor.DARK_RED, TextDecoration.BOLD),

35

Component.text("]", NamedTextColor.DARK_GRAY)

36

);

37

38

// Add a hover and click event to the delete suffix.

39

final Component deleteCross = deleteCrossBase

40

.hoverEvent(Component.text("Click to delete your message!", NamedTextColor.RED))

41

// We retrieve the signed message with event.signedMessage() and request a server-wide deletion if the

42

// deletion cross were to be clicked.

43

.clickEvent(ClickEvent.callback(audience -> Bukkit.getServer().deleteMessage(event.signedMessage())));

44

45

// Send the base format but with the delete suffix.

46

return base.appendSpace().append(deleteCross);

47

});

48

}

49

}
```


================================================================================
Chapter Title: Listeners
Original Link: https://docs.papermc.io/paper/dev/event-listeners/
================================================================================

Events are an efficient way to listen for specific actions that happen in the game. They can be called by the server, or by plugins.
These are called by the server or plugins when something happens, such as a player joining the server, or a block being broken.
Plugins are able to call custom events, such as a player completing a quest, for other plugins to listen for.

## Your listener class

[Section titled “Your listener class”](#your-listener-class)

To listen for events, you need to create a class that implements [`Listener`](https://jd.papermc.io/paper/org/bukkit/event/Listener.html).
This class can be called anything you want, but it is recommended to name it something related to the events you are listening for.

ExampleListener.java

```java
public class ExampleListener implements Listener {

// ...

}
```

## `@EventHandler`

[Section titled “@EventHandler”](#eventhandler)

To listen for an event, you need to create a method that is annotated with [`@EventHandler`](https://jd.papermc.io/paper/org/bukkit/event/EventHandler.html).
This method can be named anything you want, but it is recommended to name it something meaningful related to the event it is listening for.

## The listener method

[Section titled “The listener method”](#the-listener-method)

The method body does not need to return any data, for this reason, use void as the return type.
Listeners take in a single parameter, which is the event that is being listened to.

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler

public void onPlayerMove(PlayerMoveEvent event) {

// ...

}

}
```

Events

There is no list of events that can be listened to, however take a
look [here](https://jd.papermc.io/paper/org/bukkit/event/Event.html)
to see all classes that extend `Event`.

An event can only be listened to if it has a static `getHandlerList` method.

## Registering the listener

[Section titled “Registering the listener”](#registering-the-listener)

To register the listener, you need to call `Bukkit.getPluginManager().registerEvents()`
and pass in your listener class instance and an instance of your plugin.

This will register your listener class and allow it to listen for events.
This is commonly done in the `onEnable()` method of your plugin so that it is registered when the server starts ticking.

ExamplePlugin.java

```java
public class ExamplePlugin extends JavaPlugin {

@Override

public void onEnable() {

getServer().getPluginManager().registerEvents(new ExampleListener(), this);

}

}
```

## Event priority

[Section titled “Event priority”](#event-priority)

You can also specify the priority of the event.

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler(priority = EventPriority.HIGH)

public void onPlayerMove(PlayerMoveEvent event) {

// ...

}

}
```

There are six different priorities that you can use:

* [`EventPriority.LOWEST`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#LOWEST)
* [`EventPriority.LOW`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#LOW)
* [`EventPriority.NORMAL`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#NORMAL)
* [`EventPriority.HIGH`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#HIGH)
* [`EventPriority.HIGHEST`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#HIGHEST)
* [`EventPriority.MONITOR`](https://jd.papermc.io/paper/org/bukkit/event/EventPriority.html#MONITOR)

The order of the priorities is somewhat counter-intuitive. The **higher** the priority, the **later** the event is called.
For example, if it is important that your plugin has the last say in a certain event - to avoid it being changed - you
should use `EventPriority.HIGHEST`.

Note

The `MONITOR` priority is used to monitor the event, but not change it. It is called after all other priorities have been called.
This means you can get the result of any plugin interaction such as cancellation or modification.

## Event cancellation

[Section titled “Event cancellation”](#event-cancellation)

Some events can be cancelled, preventing the given action from being completed.
These events implement [`Cancellable`](https://jd.papermc.io/paper/org/bukkit/event/Cancellable.html).

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler

public void onPlayerMove(PlayerMoveEvent event) {

event.setCancelled(true);

}

}
```

Caution

It is important to consider that another plugin could have cancelled or changed the event before your plugin is called.
Always check the event before doing anything with it.

The above example will cancel the event, meaning that the player will not be able to move.
Once an event is cancelled, it will continue to call any other listeners for that event unless they add
`ignoreCancelled = true` to the `@EventHandler` annotation to ignore cancelled events.

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler(ignoreCancelled = true)

public void onPlayerMove(PlayerMoveEvent event) {

// ...

}

}
```


================================================================================
Chapter Title: Custom events
Original Link: https://docs.papermc.io/paper/dev/custom-events/
================================================================================

Creating custom events is a great way to add functionality to your plugin.
This will allow other plugins to listen to your custom events and add functionality to your plugin.

## Creating a custom event

[Section titled “Creating a custom event”](#creating-a-custom-event)

To create a custom event, you need to create a class that extends [`Event`](https://jd.papermc.io/paper/org/bukkit/event/Event.html).
Each event requires a [`HandlerList`](https://jd.papermc.io/paper/org/bukkit/event/HandlerList.html) that will contain all the listeners that are listening to that event.
The only exception to this requirement is when you have an event class that cannot be fired, but serves as a parent for other events instead.
An example of this is [`BlockPistonEvent`](https://jd.papermc.io/paper/org/bukkit/event/block/BlockPistonEvent.html), which cannot be listened to directly.

This list is used to call the listeners when the event is called.

Note

Although `getHandlerList` is not inherited from `Event`, you need to add a static `getHandlerList()` method and return the `HandlerList` for your event.
Both methods are required for your event to work.

PaperIsCoolEvent.java

```java
public class PaperIsCoolEvent extends Event {

private static final HandlerList HANDLER_LIST = new HandlerList();

public static HandlerList getHandlerList() {

return HANDLER_LIST;

}

@Override

public HandlerList getHandlers() {

return HANDLER_LIST;

}

}
```

Now that we have created our event, we can add some functionality to it.
Perhaps this will contain a message that will be broadcast to the server when the event is called.

PaperIsCoolEvent.java

```java
public class PaperIsCoolEvent extends Event {

private static final HandlerList HANDLER_LIST = new HandlerList();

private Component message;

public PaperIsCoolEvent(Component message) {

this.message = message;

}

public Component getMessage() {

return this.message;

}

public void setMessage(Component message) {

this.message = message;

}

public static HandlerList getHandlerList() {

return HANDLER_LIST;

}

@Override

public HandlerList getHandlers() {

return HANDLER_LIST;

}

}
```

## Calling the event

[Section titled “Calling the event”](#calling-the-event)

Now that we have created our event, we can call it.

ExamplePlugin.java

```java
public class ExamplePlugin extends JavaPlugin {

// ...

public void callCoolPaperEvent() {

PaperIsCoolEvent coolEvent = new PaperIsCoolEvent(Component.text("Paper is cool!"));

coolEvent.callEvent();

// Plugins could have changed the message from inside their listeners here. So we need to get the message again.

// This event structure allows for other plugins to change the message to their taste.

// Like, for example, a plugin that adds a prefix to all messages.

Bukkit.broadcast(coolEvent.getMessage());

}

}
```

## Implementing cancellation

[Section titled “Implementing cancellation”](#implementing-cancellation)

If you want to allow your event to be cancelled, you can implement the `Cancellable` interface.

PaperIsCoolEvent.java

```java
public class PaperIsCoolEvent extends Event implements Cancellable {

private static final HandlerList HANDLER_LIST = new HandlerList();

private Component message;

private boolean cancelled;

// ...

@Override

public boolean isCancelled() {

return this.cancelled;

}

@Override

public void setCancelled(boolean cancelled) {

this.cancelled = cancelled;

}

}
```

Now, when the event is called, you can check if it is cancelled and act accordingly.

ExamplePlugin.java

```java
public class ExamplePlugin extends JavaPlugin {

// ...

public void callCoolPaperEvent() {

PaperIsCoolEvent coolEvent = new PaperIsCoolEvent(Component.text("Paper is cool!"));

coolEvent.callEvent();

if (!coolEvent.isCancelled()) {

Bukkit.broadcast(coolEvent.getMessage());

}

}

}
```

When an event is cancellable, [`Event#callEvent()`](https://jd.papermc.io/paper/org/bukkit/event/Event.html#callEvent())
will return false if the event was cancelled. This allows you to directly use `callEvent` in your `if` statement,
instead of having to check [`Cancellable#isCancelled()`](https://jd.papermc.io/paper/org/bukkit/event/Cancellable.html#isCancelled()) manually.

ExamplePlugin.java

```java
public class ExamplePlugin extends JavaPlugin {

// ...

public void callCoolPaperEvent() {

PaperIsCoolEvent coolEvent = new PaperIsCoolEvent(Component.text("Paper is cool!"));

if (coolEvent.callEvent()) { // Directly get the output from callEvent

Bukkit.broadcast(coolEvent.getMessage());

}

}

}
```


================================================================================
Chapter Title: Handler lists
Original Link: https://docs.papermc.io/paper/dev/handler-lists/
================================================================================

Every [`Event`](https://jd.papermc.io/paper/org/bukkit/event/Event.html) that can be listened to has a
[`HandlerList`](https://jd.papermc.io/paper/org/bukkit/event/HandlerList.html) containing all the listeners that are listening to that event.
This list is used to call the listeners when the event is called.

## Getting the handler list for an event

[Section titled “Getting the handler list for an event”](#getting-the-handler-list-for-an-event)

To get the handler list for an event, you can call `getHandlerList()` on the specific event class.

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler

public void onPlayerJoin(PlayerJoinEvent event) {

HandlerList handlerList = event.getHandlerList();

// ...

}

// Or:

public ExampleListener() {

// Access the handler list through the static getter

HandlerList handlerList = PlayerJoinEvent.getHandlerList();

// ...

}

}
```

## Unregistering a listener

[Section titled “Unregistering a listener”](#unregistering-a-listener)

To unregister a listener, you can call `unregister()` on the `HandlerList` that the listener is registered to.

ExampleListener.java

```java
public class ExampleListener implements Listener {

@EventHandler

public void onPlayerJoin(PlayerJoinEvent event) {

HandlerList handlerList = event.getHandlerList();

handlerList.unregister(this);

// ...

}

// Or:

public ExampleListener() {

// Access the handler list through the static getter

HandlerList handlerList = PlayerJoinEvent.getHandlerList();

handlerList.unregister(this);

// Granted this is a pretty stupid example...

}

}
```

You can unregister based on [`Listener`](https://jd.papermc.io/paper/org/bukkit/event/Listener.html)
or [`Plugin`](https://jd.papermc.io/paper/org/bukkit/plugin/Plugin.html) for more convenience.
Likewise, you can also unregister all listeners for a specific event by calling
[`unregisterAll()`](https://jd.papermc.io/paper/org/bukkit/event/HandlerList.html#unregisterAll()) on the `HandlerList`.


================================================================================
Chapter Title: Chat events
Original Link: https://docs.papermc.io/paper/dev/chat-events/
================================================================================

The chat event has evolved a few times over the years.
This guide will explain how to properly use the new [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html)
and its [`ChatRenderer`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html).
The [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html)
is an improved version of the old [`AsyncPlayerChatEvent`](https://jd.papermc.io/paper/org/bukkit/event/player/AsyncPlayerChatEvent.html)
that allows you to render chat messages individually for each player.

`AsyncChatEvent` vs `ChatEvent`

The key difference between [`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html)
and [`ChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/ChatEvent.html) is that
[`AsyncChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AsyncChatEvent.html) is fired asynchronously.

This means that it does not block the main thread and sends the chat message when the listener has completed.
Be aware that using the Bukkit API in an asynchronous context (i.e. the event handler) is unsafe and exceptions may be thrown.
If you need to use the Bukkit API, you can use [`ChatEvent`](https://jd.papermc.io/paper/io/papermc/paper/event/player/ChatEvent.html).
However, we recommend using [`BukkitScheduler`](https://docs.papermc.io/paper/dev/scheduler).

## Understanding the renderer

[Section titled “Understanding the renderer”](#understanding-the-renderer)

Before we can start using the new chat event, we need to understand how the new renderer works.
The renderer is Paper’s way of allowing plugins to modify the chat message before it is sent to the player.
This is done by using the [`ChatRenderer`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html) interface with its
[`ChatRenderer#render(Player, Component, Component, Audience)`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html#render(org.bukkit.entity.Player,net.kyori.adventure.text.Component,net.kyori.adventure.text.Component,net.kyori.adventure.audience.Audience))
method. Previously, this was done by using the [`AsyncPlayerChatEvent`](https://jd.papermc.io/paper/org/bukkit/event/player/AsyncPlayerChatEvent.html)
with its [`AsyncPlayerChatEvent#setFormat(String)`](https://jd.papermc.io/paper/org/bukkit/event/player/AsyncPlayerChatEvent.html#setFormat(java.lang.String)) method.

ChatRenderer#render

```java
public Component render(Player source, Component sourceDisplayName, Component message, Audience viewer) {

// ...

}
```

* The [`render`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html#render(org.bukkit.entity.Player,net.kyori.adventure.text.Component,net.kyori.adventure.text.Component,net.kyori.adventure.audience.Audience)) method is called when a chat message is sent to the player.
* The `source` parameter is the player that sent the message.
* The `sourceDisplayName` parameter is the display name of the player that sent the message.
* The `message` parameter is the message that was sent.
* The `viewer` parameter is the player that is receiving the message.

`ChatRenderer.ViewerUnaware`

If your renderer does not need to know about the viewer, you can use the
[`ChatRenderer.ViewerUnaware`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.ViewerUnaware.html)
interface instead of the [`ChatRenderer`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html) interface.
This will benefit performance as the message will only be rendered once instead of each individual player.

## Using the renderer

[Section titled “Using the renderer”](#using-the-renderer)

There are two ways to use the renderer.

1. Implementing the [`ChatRenderer`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html) interface in a class.
2. Using a lambda expression.

Depending on the complexity of your renderer, you may want to use one or the other.

### Implementing the `ChatRenderer` interface

[Section titled “Implementing the ChatRenderer interface”](#implementing-the-chatrenderer-interface)

The first way of using the renderer is by implementing the [`ChatRenderer`](https://jd.papermc.io/paper/io/papermc/paper/chat/ChatRenderer.html)
interface in a class. In this example, we will be using our `ChatListener` class.

Next, we need to tell the event to use the renderer by using the
[`AbstractChatEvent#renderer()`](https://jd.papermc.io/paper/io/papermc/paper/event/player/AbstractChatEvent.html#renderer()) method.

ChatListener.java

```java
public class ChatListener implements Listener, ChatRenderer { // Implement the ChatRenderer and Listener interface

// Listen for the AsyncChatEvent

@EventHandler

public void onChat(AsyncChatEvent event) {

event.renderer(this); // Tell the event to use our renderer

}

// Override the render method

@Override

public Component render(Player source, Component sourceDisplayName, Component message, Audience viewer) {

// ...

}

}
```

Note

If you decide to create a separate class for your renderer, it is important to know that you don’t need to instantiate the class every time the event is called.
In this case, you can use [the singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern) to create a single instance of the class.

### Using a lambda expression

[Section titled “Using a lambda expression”](#using-a-lambda-expression)

Another way of using the renderer is by using a lambda expression.

ChatListener.java

```java
public class ChatListener implements Listener {

@EventHandler

public void onChat(AsyncChatEvent event) {

event.renderer((source, sourceDisplayName, message, viewer) -> {

// ...

});

}

}
```

## Rendering the message

[Section titled “Rendering the message”](#rendering-the-message)

Now that we have our renderer, we can start rendering the message.

Let’s say we want to render our chat to look like this:

![](https://docs.papermc.io/_astro/plain-message-rendering.CSp3azaV_96FDz.webp)

To do this, we need to return a new [`Component`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html) that contains the message we want to send.

ChatListener.java

```java
public class ChatListener implements Listener, ChatRenderer {

// Listener logic

@Override

public Component render(Player source, Component sourceDisplayName, Component message, Audience viewer) {

return sourceDisplayName

.append(Component.text(": "))

.append(message);

}

}
```

Now you can see that the message is rendered as we wanted it to be.

## Conclusion

[Section titled “Conclusion”](#conclusion)

That is all you need to know about the new chat event and its renderer.
Of course there are many more things you can do with components in general.
If you want to learn more about components, you can read the [Component Documentation](https://docs.papermc.io/adventure/text/).


================================================================================
Chapter Title: Teleportation
Original Link: https://docs.papermc.io/paper/dev/entity-teleport/
================================================================================

Entities can be instantaneously teleported to specific positions, synchronously and asynchronously with the
[`teleport`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#teleport(org.bukkit.Location)) and
[`teleportAsync`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#teleportAsync(org.bukkit.Location)) API.

Performance

If you expect to teleport into unloaded chunks, it is recommended to use the `teleportAsync` API,
as it avoids doing synchronous chunk loads, which put a lot of stress on the server’s main thread -
hurting overall performance.

```java
entity.teleport(location); // loads chunks synchronously and teleports the entity

entity.teleportAsync(location).thenAccept(success -> { // loads chunks asynchronously and teleports the entity

// this code is ran when the teleport completes

// the Future is completed on the main thread, so it is safe to use the API here

if (success) {

// the entity was teleported successfully!

}

});
```

Danger

You should **NEVER** call `.get()`/`.join()` on the `teleportAsync` `Future` on the main thread,
as it **WILL** deadlock your server, if the chunk you’re teleporting into is not loaded.

## Look at

[Section titled “Look at”](#look-at)

The [`lookAt`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#lookAt(org.bukkit.entity.Entity,io.papermc.paper.entity.LookAnchor,io.papermc.paper.entity.LookAnchor))
API allows you to make a player look at a certain position or entity.

```java
player.lookAt(

position,

LookAnchor.EYES // the player's eyes will be facing the position

);

player.lookAt(

entity,

LookAnchor.EYES // the player's eyes will be facing the entity

LookAnchor.FEET // the player will be facing the entity's feet

);
```

## Teleport flags

[Section titled “Teleport flags”](#teleport-flags)

Teleport flags offer a way to teleport entities whilst being able to customize behavior.
This allows you to do things like teleport players using relative flags and being able to retain passengers.

All available teleport flags can be found in the [`TeleportFlag`](https://jd.papermc.io/paper/io/papermc/paper/entity/TeleportFlag.html) class.

### Relative teleportation

[Section titled “Relative teleportation”](#relative-teleportation)

Teleport a player relatively, preventing velocity from being reset in the X, Y and Z axes.

```java
player.teleport(

location,

TeleportFlag.Relative.VELOCITY_X,

TeleportFlag.Relative.VELOCITY_Y,

TeleportFlag.Relative.VELOCITY_Z

);
```

### Retaining passengers

[Section titled “Retaining passengers”](#retaining-passengers)

Warning

Since 1.21.10, this flag does not do anything, as it’s been made the default behavior when teleporting entities.

Teleport an entity with the [`RETAIN_PASSENGERS`](https://jd.papermc.io/paper/io/papermc/paper/entity/TeleportFlag.EntityState.html#RETAIN_PASSENGERS) flag,
allowing its passengers to be transferred with the entity.

```java
entity.teleport(location, TeleportFlag.EntityState.RETAIN_PASSENGERS);
```


================================================================================
Chapter Title: Display entities
Original Link: https://docs.papermc.io/paper/dev/display-entities/
================================================================================

Added in 1.19.4, [display entities](https://minecraft.wiki/w/Display) are a powerful way to display
various things in the world, like blocks, items and text.

By default, these entities have no hitbox, don’t move, make sounds or take damage,
making them the perfect for all kinds of applications, like holograms.

## Types

[Section titled “Types”](#types)

### Text

[Section titled “Text”](#text)

Text can be displayed via a [`TextDisplay`](https://jd.papermc.io/paper/org/bukkit/entity/TextDisplay.html)
entity.

```java
TextDisplay display = world.spawn(location, TextDisplay.class, entity -> {

// customize the entity!

entity.text(Component.text("Some awesome content", NamedTextColor.BLACK));

entity.setBillboard(Display.Billboard.VERTICAL); // pivot only around the vertical axis

entity.setBackgroundColor(Color.RED); // make the background red

// see the Display and TextDisplay Javadoc, there are many more options

});
```

### Blocks

[Section titled “Blocks”](#blocks)

Blocks can be displayed via a [`BlockDisplay`](https://jd.papermc.io/paper/org/bukkit/entity/BlockDisplay.html)
entity.

```java
BlockDisplay display = world.spawn(location, BlockDisplay.class, entity -> {

// customize the entity!

entity.setBlock(Material.GRASS_BLOCK.createBlockData());

});
```

### Items

[Section titled “Items”](#items)

Items can be displayed via an [`ItemDisplay`](https://jd.papermc.io/paper/org/bukkit/entity/ItemDisplay.html)
entity.

Despite its name, an *item* display can also display *blocks*, with the difference being the
position in the model - an item display has its position in the center, whereas a block display has
its position in the corner of the block (this can be seen with the hitbox debug mode - F3+B).

```java
ItemDisplay display = world.spawn(location, ItemDisplay.class, entity -> {

// customize the entity!

entity.setItemStack(ItemStack.of(Material.SKELETON_SKULL));

});
```

## Transformation

[Section titled “Transformation”](#transformation)

Displays can have an arbitrary affine transformation applied to them, allowing you to position and
warp them as you choose in 3D space.

Transformations are applied to the display in this order:

![Diagram](https://docs.papermc.io/d2/docs/paper/dev/api/entity-api/display-entities-0.svg)

Visualizing transformations

Use the [Transformation Visualizer](https://misode.github.io/transformation/) website to visualize
a transformation for quick prototyping!

### Scale

[Section titled “Scale”](#scale)

The most basic transformation is scaling, let’s take a grass block and scale it up:

```java
world.spawn(location, BlockDisplay.class, entity -> {

entity.setBlock(Material.GRASS_BLOCK.createBlockData());

entity.setTransformation(

new Transformation(

new Vector3f(), // no translation

new AxisAngle4f(), // no left rotation

new Vector3f(2, 2, 2), // scale up by a factor of 2 on all axes

new AxisAngle4f() // no right rotation

)

);

// or set a raw transformation matrix from JOML

// entity.setTransformationMatrix(

//         new Matrix4f()

//                 .scale(2) // scale up by a factor of 2 on all axes

// );

});
```

![Scaling example](https://docs.papermc.io/_astro/display-scale.CGw8wYbk_ZHVVu4.webp)

### Rotation

[Section titled “Rotation”](#rotation)

You can also rotate it, let’s tip it on its corner:

```java
world.spawn(location, BlockDisplay.class, entity -> {

entity.setBlock(Material.GRASS_BLOCK.createBlockData());

entity.setTransformation(

new Transformation(

new Vector3f(), // no translation

new AxisAngle4f((float) -Math.toRadians(45), 1, 0, 0), // rotate -45 degrees on the X axis

new Vector3f(2, 2, 2), // scale up by a factor of 2 on all axes

new AxisAngle4f((float) Math.toRadians(45), 0, 0, 1) // rotate +45 degrees on the Z axis

)

);

// or set a raw transformation matrix from JOML

// entity.setTransformationMatrix(

//         new Matrix4f()

//                 .scale(2) // scale up by a factor of 2 on all axes

//                 .rotateXYZ(

//                         (float) Math.toRadians(360 - 45), // rotate -45 degrees on the X axis

//                         0,

//                         (float) Math.toRadians(45) // rotate +45 degrees on the Z axis

//                 )

// );

});
```

![Rotation example](https://docs.papermc.io/_astro/display-rotation.BGw2MF-Y_1cV1JM.webp)

### Translation

[Section titled “Translation”](#translation)

Finally, we can also apply a translation transformation (position offset) to the display, for example:

```java
world.spawn(location, BlockDisplay.class, entity -> {

entity.setBlock(Material.GRASS_BLOCK.createBlockData());

entity.setTransformation(

new Transformation(

new Vector3f(0.5F, 0.5F, 0.5F), // offset by half a block on all axes

new AxisAngle4f((float) -Math.toRadians(45), 1, 0, 0), // rotate -45 degrees on the X axis

new Vector3f(2, 2, 2), // scale up by a factor of 2 on all axes

new AxisAngle4f((float) Math.toRadians(45), 0, 0, 1) // rotate +45 degrees on the Z axis

)

);

// or set a raw transformation matrix from JOML

// entity.setTransformationMatrix(

//         new Matrix4f()

//                 .translate(0.5F, 0.5F, 0.5F) // offset by half a block on all axes

//                 .scale(2) // scale up by a factor of 2 on all axes

//                 .rotateXYZ(

//                         (float) Math.toRadians(360 - 45), // rotate -45 degrees on the X axis

//                         0,

//                         (float) Math.toRadians(45) // rotate +45 degrees on the Z axis

//                 )

// );

});
```

![Translation example](https://docs.papermc.io/_astro/display-trans.DS2MbS_l_2agHdP.webp)

## Interpolation

[Section titled “Interpolation”](#interpolation)

Transformations and teleports can be linearly interpolated by the client to create a smooth animation,
switching from one transformation/location to the next.

### Transformation

[Section titled “Transformation”](#transformation-1)

An example of this would be smoothly rotating a block/item/text in-place. In conjunction with the
[Scheduler API](https://docs.papermc.io/paper/dev/scheduler), the animation can be restarted after it’s done,
making the display spin indefinitely:

```java
ItemDisplay display = location.getWorld().spawn(location, ItemDisplay.class, entity -> {

entity.setItemStack(ItemStack.of(Material.GOLDEN_SWORD));

});

int duration = 5 * 20; // duration of half a revolution (5 * 20 ticks = 5 seconds)

Matrix4f mat = new Matrix4f().scale(0.5F); // scale to 0.5x - smaller item

Bukkit.getScheduler().runTaskTimer(plugin, task -> {

if (!display.isValid()) { // display was removed from the world, abort task

task.cancel();

return;

}

display.setTransformationMatrix(mat.rotateY(((float) Math.toRadians(180)) + 0.1F /* prevent the client from interpolating in reverse */));

display.setInterpolationDelay(0); // no delay to the interpolation

display.setInterpolationDuration(duration); // set the duration of the interpolated rotation

}, 1 /* delay the initial transformation by one tick from display creation */, duration);
```

![Interpolation example](https://docs.papermc.io/_astro/display-interp.BKwIK_Zm_tgJkR.webp)

### Teleportation

[Section titled “Teleportation”](#teleportation)

Similarly to the transformation interpolation, you may also want to interpolate the movement
of the entire display entity between two points.

A similar effect may be achieved using an interpolated translation, however if you change
other properties of the transformation, those too will be interpolated, which may or may not be what you want.

```java
// new position will be 10 blocks higher

Location newLocation = display.getLocation().add(0, 10, 0);

display.setTeleportDuration(20 * 2); // the movement will take 2 seconds (1 second = 20 ticks)

display.teleport(newLocation); // perform the movement
```

## Use cases

[Section titled “Use cases”](#use-cases)

Displays have many different use cases, ranging from stationary decoration to complex animation.

A popular, simple use case is to make a decoration that’s visible to only specific players,
which can be achieved using standard entity API - [`Entity#setVisibleByDefault()`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#setVisibleByDefault(boolean))
and [`Player#showEntity()`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#showEntity(org.bukkit.plugin.Plugin,org.bukkit.entity.Entity))/
[`Player#hideEntity()`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#hideEntity(org.bukkit.plugin.Plugin,org.bukkit.entity.Entity)).

Caution

If the display is only used temporarily, its persistence can be disabled with
[`Entity#setPersistent()`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#setPersistent(boolean)),
meaning it will disappear when the chunk unloads.

*However, if the display is located in a chunk that never unloads, i.e. a spawn chunk, it will never
be removed, creating a resource leak. Make sure to remove the display afterward with
[`Entity#remove()`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#remove()).*

They can also be added as passengers to entities with the
[`Entity#addPassenger()`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#addPassenger(org.bukkit.entity.Entity))/
[`Entity#removePassenger()`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html#removePassenger(org.bukkit.entity.Entity))
methods, useful for making styled name tags!

```java
TextDisplay display = world.spawn(location, TextDisplay.class, entity -> {

// ...

entity.setVisibleByDefault(false); // hide it for everyone

entity.setPersistent(false); // don't save the display, it's temporary

});

entity.addPassenger(display); // mount it on top of an entity's head

player.showEntity(plugin, display); // show it to a player

// ...

display.remove(); // done with the display
```


================================================================================
Chapter Title: Menu Type APIExperimental
Original Link: https://docs.papermc.io/paper/dev/menu-type-api/
================================================================================

Experimental

The Menu Type API and anything that uses it is currently experimental and may change in the future.

Minecraft has a lot of types of menus. From chests, to crafting tables, to anvils, and even villager trade menus.
With the old Bukkit inventory API, it was not possible to replicate most of these perfectly. Exactly for
this reason, the menu type API was introduced.

## What is a menu?

[Section titled “What is a menu?”](#what-is-a-menu)

Menus, also referred to as views, are user interfaces, which can be created and viewed by players. The
[`MenuType`](https://jd.papermc.io/paper/org/bukkit/inventory/MenuType.html) interface declares all possible menu types a menu can have.
The difference between menus and inventories is that inventories are containers and menus are
their visual representations.

Menus created using this API **follow the same logic as Vanilla**, meaning they are fully
functional. Some of them can directly represent a block, like a furnace. The [`MERCHANT`](https://jd.papermc.io/paper/org/bukkit/inventory/MenuType.html#MERCHANT)
can represent a merchant entity in the world.

## What are inventory views?

[Section titled “What are inventory views?”](#what-are-inventory-views)

An [`InventoryView`](https://jd.papermc.io/paper/org/bukkit/inventory/InventoryView.html) is a specific view created from a menu type.
In the general sense, an inventory view links together **two separate inventories** and always has a player viewing them.
The bottom linked inventory is the player’s inventory.

Some views have specialized subinterfaces for quickly checking their type, like [`FurnaceView`](https://jd.papermc.io/paper/org/bukkit/inventory/view/FurnaceView.html)
for furnace inventories. For other views, which don’t have their own sub type, you can instead use the
[`InventoryView#getMenuType`](https://jd.papermc.io/paper/org/bukkit/inventory/InventoryView.html#getMenuType()) method.

## Building inventory views from menu types

[Section titled “Building inventory views from menu types”](#building-inventory-views-from-menu-types)

The most common way to create inventory views from menu types is by using their respective builders. **Every menu type
has a builder** which can be used to customize the resulting view. For example, a simple crafting table
inventory view can be created and opened like this:

```java
// MenuType.CRAFTING is used to open a crafting table.

MenuType.CRAFTING.builder()

// Set the title of the view, which will be displayed at the top.

.title(Component.text("The inventory view's title"))

// Determines whether the server should check if the player can reach the location.

.checkReachable(true)

// Set the location. Because of checkReachable being set to `true`, this has to be a valid

// crafting table. The server will check and make sure that the player does not get pushed

// away too far to use the crafting table and will close the player's inventory if the

// crafting table were to be pushed away.

.location(location)

// Build this view for the provided player, linking the inventory of the crafting table

// together with the player's own inventory into an inventory view.

.build(player)

// Open the view.

.open();
```

Reusing Builders

Builders can be reused in order to reduce code repetition.

## Opening blocks that have menus

[Section titled “Opening blocks that have menus”](#opening-blocks-that-have-menus)

Almost all inventory views have a block attached to them. The only exception being the
[`MenuType.MERCHANT`](https://jd.papermc.io/paper/org/bukkit/inventory/MenuType.html#MERCHANT), which
instead has a [`Merchant`](https://jd.papermc.io/paper/org/bukkit/inventory/Merchant.html) attached to it.

There are two types of blocks that have menus: Block entity blocks and stateless blocks.

Stateless blocks, as the name implies, do not have any state associated with them. Under
those count the majority of “workbench” blocks, like crafting tables, grindstones, anvils, and more.

Block entity blocks (also referred to as tile entity blocks) have a state associated with them.
Meaning when you open a specific location with the `#location` builder method, and the block matches
the expected block from the menu type, the state of that block can change. This means that all players
can see the change live.

Under those blocks count the beacon, chests, furnaces, and similar. For example,
[`MenuType.FURNACE`](https://jd.papermc.io/paper/org/bukkit/inventory/MenuType.html#FURNACE) would expect a furnace block.

## Persistent inventory views

[Section titled “Persistent inventory views”](#persistent-inventory-views)

Inventory views can be reused! This is useful for persistent operations.

For example, we can write a `/persistent` command with opens a player’s own, persistent, stash!

CommandPersistent.java

```java
18 collapsed lines

1

package io.papermc.docs.menutype;

2

3

import com.mojang.brigadier.Command;

4

import com.mojang.brigadier.tree.LiteralCommandNode;

5

import io.papermc.paper.command.brigadier.CommandSourceStack;

6

import io.papermc.paper.command.brigadier.Commands;

7

import net.kyori.adventure.text.Component;

8

import net.kyori.adventure.text.format.NamedTextColor;

9

import org.bukkit.entity.Player;

10

import org.bukkit.event.EventHandler;

11

import org.bukkit.event.Listener;

12

import org.bukkit.event.player.PlayerQuitEvent;

13

import org.bukkit.inventory.Inventory;

14

import org.bukkit.inventory.InventoryView;

15

import org.bukkit.inventory.MenuType;

16

17

import java.util.HashMap;

18

import java.util.Map;

19

20

public class CommandPersistent implements Listener {

21

22

// A map to store all inventory views in. Generally it is not recommended

23

// to use Player objects as keys or values, but in this case it is acceptable

24

// because the inventory view is also bound to a player object, meaning we

25

// couldn't reuse it after a player rejoins anyways.

26

private static final Map<Player, InventoryView> VIEWS = new HashMap<>();

27

28

// Create a command. Commands are explained in the Command API documentation

29

// pages and therefore won't be covered here.

30

public static LiteralCommandNode<CommandSourceStack> createCommand() {

31

return Commands.literal("persistent").executes(ctx -> {

32

if (!(ctx.getSource().getExecutor() instanceof Player player)) {

33

return 0;

34

}

35

36

// First, attempt to get a stored view.

37

InventoryView view = VIEWS.get(player);

38

39

// If there is no view currently stored, create it.

40

if (view == null) {

41

view = MenuType.GENERIC_9X6.builder()

42

.title(Component.text(player.getName() + "'s stash", NamedTextColor.DARK_RED))

43

.build(player);

44

45

// And finally store it in the map.

46

VIEWS.put(player, view);

47

}

48

49

// As the inventory view is directly bound to the player, we do not have

50

// to reassign the player and can just open it.

51

view.open();

52

return Command.SINGLE_SUCCESS;

53

}).build();

54

}

55

56

// There are two things we should do on the quit event:

57

// 1. Remove the player entry from the map, as it is no longer valid.

58

// 2. Store the top inventory somewhere so it persists across server restarts.

59

@EventHandler

60

void onPlayerQuit(PlayerQuitEvent event) {

61

InventoryView view = VIEWS.remove(event.getPlayer());

62

if (view != null) {

63

Inventory topInventory = view.getTopInventory();

64

// Save the contents of the inventory to a file or database.

65

}

66

}

67

}
```


================================================================================
Chapter Title: Custom InventoryHolders
Original Link: https://docs.papermc.io/paper/dev/custom-inventory-holder/
================================================================================

`InventoryHolder`s are a way to identify your plugin’s inventories in events.

## Why use an `InventoryHolder`?

[Section titled “Why use an InventoryHolder?”](#why-use-an-inventoryholder)

`InventoryHolder`s simplify the steps you need to do to make sure an inventory was created by your plugin.

Using inventory names for identification is unreliable, as other plugins, or even players, can create inventories with names the exact same as yours.
With components, you also need to make sure the name is exactly the same or serialize it to other formats.

Custom `InventoryHolder`s have no such downsides and by using them you’re guaranteed to have methods available to handle your inventory.

## Creating a custom holder

[Section titled “Creating a custom holder”](#creating-a-custom-holder)

The first step is to implement the [`InventoryHolder`](https://jd.papermc.io/paper/org/bukkit/inventory/InventoryHolder.html) interface.
We can do this the following way: create a new class that will create our [`Inventory`](https://jd.papermc.io/paper/org/bukkit/inventory/Inventory.html) in the constructor.

Note

The constructor takes your main plugin class as an argument in order to create the `Inventory`.
If you wish, you can use the static method [`Bukkit#createInventory(InventoryHolder, int)`](https://jd.papermc.io/paper/org/bukkit/Bukkit.html#createInventory(org.bukkit.inventory.InventoryHolder,int)) instead and remove the argument.

MyInventory.java

```java
public class MyInventory implements InventoryHolder {

private final Inventory inventory;

public MyInventory(MyPlugin plugin) {

// Create an Inventory with 9 slots, `this` here is our InventoryHolder.

this.inventory = plugin.getServer().createInventory(this, 9);

}

@Override

public Inventory getInventory() {

return this.inventory;

}

}
```

## Opening the inventory

[Section titled “Opening the inventory”](#opening-the-inventory)

To open the inventory, first we have to instantiate our `MyInventory` class and then open the inventory for the player.
You can do that wherever you need.

Note

We pass an instance of our plugin’s main class as it’s required by the constructor. If you’ve used the static method and removed the constructor
argument you don’t have to pass it here.

```java
Player player; // Assume we have a Player instance.

// This can be a command, another event or anywhere else you have a Player.

MyInventory myInventory = new MyInventory(myPlugin);

player.openInventory(myInventory.getInventory());
```

## Listening to an event

[Section titled “Listening to an event”](#listening-to-an-event)

Once we have the inventory open, we can listen to any inventory events we like and check if
[`Inventory#getHolder()`](https://jd.papermc.io/paper/org/bukkit/inventory/Inventory.html#getHolder()) returns an instance of our `MyInventory`.

```java
@EventHandler

public void onInventoryClick(InventoryClickEvent event) {

Inventory inventory = event.getInventory();

// Check if the holder is our MyInventory,

// if yes, use instanceof pattern matching to store it in a variable immediately.

if (!(inventory.getHolder(false) instanceof MyInventory myInventory)) {

// It's not our inventory, ignore it.

return;

}

// Do what we need in the event.

}
```

## Storing data on the holder

[Section titled “Storing data on the holder”](#storing-data-on-the-holder)

You can store extra data for your inventories on the `InventoryHolder` by adding fields and methods to your class.

Let’s make an inventory that counts the amount of times we clicked a stone inside it.
First, let’s modify our `MyInventory` class a little:

MyInventory.java

```java
public class MyInventory implements InventoryHolder {

private final Inventory inventory;

private int clicks = 0; // Store the amount of clicks.

public MyInventory(MyPlugin plugin) {

this.inventory = plugin.getServer().createInventory(this, 9);

// Set the stone that we're going to be clicking.

this.inventory.setItem(0, ItemStack.of(Material.STONE));

}

// A method we will call in the listener whenever the player clicks the stone.

public void addClick() {

this.clicks++;

this.updateCounter();

}

// A method that will update the counter item.

private void updateCounter() {

this.inventory.setItem(8, ItemStack.of(Material.BEDROCK, this.clicks));

}

@Override

public Inventory getInventory() {

return this.inventory;

}

}
```

Now, we can modify our listener to check if the player clicked the stone, and if so, add a click.

```java
@EventHandler

public void onInventoryClick(InventoryClickEvent event) {

// We're getting the clicked inventory to avoid situations where the player

// already has a stone in their inventory and clicks that one.

Inventory inventory = event.getClickedInventory();

// Add a null check in case the player clicked outside the window.

if (inventory == null || !(inventory.getHolder(false) instanceof MyInventory myInventory)) {

return;

}

event.setCancelled(true);

ItemStack clicked = event.getCurrentItem();

// Check if the player clicked the stone.

if (clicked != null && clicked.getType() == Material.STONE) {

// Use the method we have on MyInventory to increment the field

// and update the counter.

myInventory.addClick();

}

}
```

Note

You can store the created `MyInventory` instance, e.g. on a `Map<UUID, MyInventory>` for per-player use, or as a field to share the inventory between
all players, and use it to persist the counter even when opening the inventory for the next time.


================================================================================
Chapter Title: Introduction
Original Link: https://docs.papermc.io/paper/dev/lifecycle/
================================================================================

The lifecycle API can be used for lifecycle-related registration. It is currently used by the
Brigadier command API. It is planned to be used for the Registry Modification API as well.
Generally, systems that are initialized very early in the startup process can take advantage of this
event system.

## LifecycleEventManager

[Section titled “LifecycleEventManager”](#lifecycleeventmanager)

The [LifecycleEventManager](https://jd.papermc.io/paper/io/papermc/paper/plugin/lifecycle/event/LifecycleEventManager.html) is tied
to either a [Plugin](https://jd.papermc.io/paper/org/bukkit/plugin/Plugin.html) instance or a
[BootstrapContext](https://jd.papermc.io/paper/io/papermc/paper/plugin/bootstrap/BootstrapContext.html) depending on where you access it from. For example in your plugin’s main class:

TestPlugin.java

```java
@Override

public void onEnable() {

final LifecycleEventManager<Plugin> lifecycleManager = this.getLifecycleManager();

}
```

Or, with a bootstrapper:

TestPluginBootstrap.java

```java
@Override

public void bootstrap(BootstrapContext context) {

final LifecycleEventManager<BootstrapContext> lifecycleManager = context.getLifecycleManager();

}
```

## LifecycleEvents

[Section titled “LifecycleEvents”](#lifecycleevents)

After obtaining the correct `LifecycleEventManager`, create an event handler by selecting an
event type from [LifecycleEvents](https://jd.papermc.io/paper/io/papermc/paper/plugin/lifecycle/event/types/LifecycleEvents.html):

TestPlugin.java

```java
@Override

public void onEnable() {

final LifecycleEventManager<Plugin> lifecycleManager = this.getLifecycleManager();

PrioritizedLifecycleEventHandlerConfiguration<LifecycleEventOwner> config = LifecycleEvents.SOME_EVENT.newHandler((event) -> {

// Handler for the event

});

}
```

### Configuration

[Section titled “Configuration”](#configuration)

Each handler created can be configured in several ways. The available configuration options
depend on the event type itself and will vary from event type to event type.

#### Priority

[Section titled “Priority”](#priority)

Setting the priority of a handler can determine where it runs relative to other handlers
on the same event type. The lower the number, the earlier it will be run. The default priority
is 0.

#### Monitor

[Section titled “Monitor”](#monitor)

Marking the handler as a monitor will cause it to be called after all other non-monitor handlers
have been called. Only use this to inspect some state in the event. Do not modify any state in
the handler.

The priority and monitor state are exclusive options, setting one will reset the other.

TestPlugin.java

```java
@Override

public void onEnable() {

final LifecycleEventManager<Plugin> lifecycleManager = this.getLifecycleManager();

PrioritizedLifecycleEventHandlerConfiguration<LifecycleEventOwner> config = LifecycleEvents.SOME_EVENT.newHandler((event) -> {

// Handler for the event

});

config.priority(10); // sets a priority of 10

// or

config.monitor(); // marks the handler as a monitor

}
```

### Registering

[Section titled “Registering”](#registering)

Once the handler has been configured, it can be registered with the lifecycle manager:

TestPlugin.java

```java
@Override

public void onEnable() {

final LifecycleEventManager<Plugin> lifecycleManager = this.getLifecycleManager();

PrioritizedLifecycleEventHandlerConfiguration<LifecycleEventOwner> config = LifecycleEvents.SOME_EVENT.newHandler((event) -> {

// Handler for the event

}).priority(10);

lifecycleManager.registerEventHandler(config);

}
```

There is also a shorthand way to register just the handler without doing any configuration:

TestPlugin.java

```java
@Override

public void onEnable() {

final LifecycleEventManager<Plugin> lifecycleManager = this.getLifecycleManager();

lifecycleManager.registerEventHandler(LifecycleEvents.COMMANDS, (event) -> {

// Handler for the event

});

}
```

Note

Some event types have special behaviors that restrict certain mechanics. The reloading plugins
functionality (via `/bukkit:reload` or `Server#reload()`) is disabled if plugins register handlers
in certain situations. This is due to the plugin reloads having to fully unload the plugin and its
classes which is an issue if an event has to run while the plugin is unloaded.

## Why does this exist?

[Section titled “Why does this exist?”](#why-does-this-exist)

We already have an event system, why do we need another one? This is a fair question. The answer is
that some of these events fire well before `JavaPlugin` instances are created, before the
`MinecraftServer` instance is created, right at the very start of server startup. These can be
before all the registries have been initialized which is one of the first things to happen on a Vanilla
server. The existing Bukkit event system is not designed to exist at this time, and modifying it to
support this environment is more trouble than just having a separate system for specific events that
can fire during this early initialization.

Technical Explanation

Here is an ever-expanding list of specific reasons why we can’t just modify the existing event
system to support this new need for events:

* You cannot have generics on Bukkit events because there is 0 compile time checking since they are
  registered reflectively. This is a problem because the events are mostly going to follow a very
  similar pattern, specifically the registry modification events. If we can’t use generics, there’s
  going to be many useless classes.
* Another reason is that the existing system has priorities, but always has them. With the lifecycle
  events, there may be some events for which we do not want to support priorities (it would
  be based purely on plugin load order then).
* Exists too late. `HandlerList` and event registration all use the `Plugin` instance which does not exist,
  and cannot exist, during the bootstrapper. Changing this would require a substantial rewrite of the
  existing system and probably confuse API users who expect all `RegisteredListeners` to have a
  Plugin attached.
* A new system lets us use interfaces and server implementations for events which dramatically
  simplifies them. With the Bukkit system you could kind of do this with a server impl event
  extending the API event, but interfaces are more flexible.
* A new system lets us enforce, at compile time, which events you can register where based on the
  context of the registration. So you can’t even register a handler for an event in the wrong spot,
  that will be a compiler error thanks to our implementation using Generics.


================================================================================
Chapter Title: Datapack discoveryExperimental
Original Link: https://docs.papermc.io/paper/dev/lifecycle/datapacks/
================================================================================

Experimental

The datapack discovery API is currently experimental and may change in the future.

The lifecycle API grants developers much more direct access to modifying some of the core parts of the server.
One such core aspect are **datapacks**. No more asking users to download your datapack alongside the plugin — you
can now include the datapack in your plugin JAR and load it yourself!

Note

This feature requires you to have a basic understanding of the [Lifecycle API](https://docs.papermc.io/paper/dev/lifecycle),
the datapack format (which you can look up in the [Minecraft wiki](https://minecraft.wiki/w/Data_pack)), and
requires you to use a [`paper-plugin.yml` plugin](https://docs.papermc.io/paper/dev/getting-started/paper-plugins).

## The datapack discovery lifecycle event

[Section titled “The datapack discovery lifecycle event”](#the-datapack-discovery-lifecycle-event)

The [`LifecycleEvents.DATAPACK_DISCOVERY`](https://jd.papermc.io/paper/io/papermc/paper/plugin/lifecycle/event/types/LifecycleEvents.html#DATAPACK_DISCOVERY) lifecycle
event allows developers to add, check for, and even remove datapacks which are about to be loaded by the server.

Tip

The following code examples are assumed to be executed inside a `PluginBootstrap`’s `bootstrap(BootstrapContext context)` method.
They are also assumed to already be inside an event handler, resulting in a structure like this:

CustomPluginBootstrap.java

```java
1

@NullMarked

2

public class CustomPluginBootstrap implements PluginBootstrap {

3

4

@Override

5

public void bootstrap(BootstrapContext context) {

6

context.getLifecycleManager().registerEventHandler(LifecycleEvents.DATAPACK_DISCOVERY.newHandler(

7

event -> {

8

// All code is contained here.

9

}

10

));

11

}

12

}
```

### Retrieving all currently discovered datapacks

[Section titled “Retrieving all currently discovered datapacks”](#retrieving-all-currently-discovered-datapacks)

For the sake of simplicity, let’s start with the most basic operation: Retrieving discovered data packs.
For this, we can use the following simple code:

```java
8

context.getLogger().info("The following datapacks were found: {}",

9

String.join(", ", event.registrar().getDiscoveredPacks().keySet())

10

);
```

This might yield the following log output:

```java
[00:26:12 INFO]: [PaperDocsTestProject] The following datapacks were found: file/bukkit, minecart_improvements, paper, redstone_experiments, trade_rebalance, vanilla
```

This resulted in a few more datapacks than one might expect. Primarily, at the time of writing, the experimental `minecart_improvements`, `redstone_experiments`,
and `trade_rebalance` datapacks. The datapack discovery does not care about whether a datapack should be enabled or not. It simply **looks for** datapacks that
the server *could* enable.

### Removing discovered datapacks

[Section titled “Removing discovered datapacks”](#removing-discovered-datapacks)

You can very easily prevent datapacks from being discovered by calling [`DatapackRegistrar#removeDiscoveredPack(String name)`](https://jd.papermc.io/paper/io/papermc/paper/datapack/DatapackRegistrar.html#removeDiscoveredPack(java.lang.String))
on the datapack’s name.

To remove the above-mentioned, experimental datapacks, you could the following code:

```java
8

// The names of the datapacks we want to remove.

9

final Set<String> datapacksToRemove = Set.of("minecart_improvements", "redstone_experiments", "trade_rebalance");

10

11

datapacksToRemove.forEach(

12

// Iterate through every datapack and remove it from the discovered packs.

13

datapack -> event.registrar().removeDiscoveredPack(datapack)

14

);

15

16

// The logging line from before.

17

context.getLogger().info("The following datapacks were found: {}",

18

String.join(", ", event.registrar().getDiscoveredPacks().keySet())

19

);
```

This would, as expected, remove the entries from being logged (and thus discovered):

```java
[00:35:39 INFO]: [PaperDocsTestProject] The following datapacks were found: file/bukkit, paper, vanilla
```

## Registering custom datapacks

[Section titled “Registering custom datapacks”](#registering-custom-datapacks)

The main use case of the datapack register lifecycle event is the adding of plugin included datapacks. And Paper makes this pretty simple:
You have to include your datapack in the plugin’s JAR file, as already mentioned. This **does not** mean including the datapack zip.
This means including the **source files**, which makes it very convenient to work with in a dev environment.

Tip

This section assumes that you already have a working datapack. If you do not have one, but still want to play around with datapack inclusion in your plugin,
you can check out [Vanilla Tweaks](https://vanillatweaks.net) for their data packs.

### Including the datapack in your plugin

[Section titled “Including the datapack in your plugin”](#including-the-datapack-in-your-plugin)

Before you can let the server know about your datapack, you must first include it. For this, you can just add it to your **plugins src/main/resources** folder.
The datapack should have at least one extra folder (so don’t dump all the contents into the `resources` root). For this example, it will be located under
**resources/custom\_datapack**, but you can rename this second folder to any name you want to. If you have done everything correctly, you should have a folder structure,
which looks similar to this:

* Directorysrc/main/resources
  + Directorycustom\_datapack
    - pack.mcmeta
    - Directorydata/
      * …

Build your plugin and verify that there is a `custom_datapack` folder in the root of your plugin’s JAR file.

### Discovering the datapack

[Section titled “Discovering the datapack”](#discovering-the-datapack)

To discover the datapack, you must call the [`DatapackRegistrar#discoverPack(URI uri, String id)`](https://jd.papermc.io/paper/io/papermc/paper/datapack/DatapackRegistrar.html#discoverPack(java.net.URI,java.lang.String))
method. The uri should point to **your datapack’s folder in your JAR**. This can be achieved simply by calling
`getClass().getResource("/custom_datapack").toURI()`. **The preceding slash is very important**. The id can be set to
whatever you want to identify your datapack with. The final name of the loaded pack will be `<YourPluginName>/<id>`.

Code example:

```java
8

try {

9

// Retrieve the URI of the datapack folder.

10

URI uri = this.getClass().getResource("/custom_datapack").toURI();

11

// Discover the pack. The ID is set to "provided", which indicates to

12

// a server owner that your plugin includes this data pack.

13

event.registrar().discoverPack(uri, "provided");

14

} catch (URISyntaxException | IOException e) {

15

throw new RuntimeException(e);

16

}
```

### Verifying that the datapack loaded correctly

[Section titled “Verifying that the datapack loaded correctly”](#verifying-that-the-datapack-loaded-correctly)

You can verify that a datapack loaded simply by executing the command `/datapack list enabled`.

Alternatively, you can check for the loaded status of your datapack during normal execution
of your plugin. For example, a simple check inside your plugin’s `onLoad` method might look like this:

CustomJavaPlugin.java

```java
1

public final class CustomJavaPlugin extends JavaPlugin {

2

3

@Override

4

public void onLoad() {

5

Datapack pack = this.getServer().getDatapackManager().getPack(getPluginMeta().getName() + "/provided");

6

if (pack != null) {

7

if (pack.isEnabled()) {

8

this.getLogger().info("The datapack loaded successfully!");

9

} else {

10

this.getLogger().warn("The datapack failed to load.");

11

}

12

}

13

}

14

}
```

If everything has gone correctly, the console should contain output similar to this:

```java
[01:10:12 INFO]: [PaperDocsTestProject] Loading server plugin PaperDocsTestProject v1.0-DEV

[01:10:12 INFO]: [PaperDocsTestProject] The datapack loaded successfully!
```


================================================================================
Chapter Title: Data componentsExperimental
Original Link: https://docs.papermc.io/paper/dev/data-component-api/
================================================================================

Experimental

The data component API is currently experimental, and is additionally subject to change across versions.

The data component API provides a version-specific interface for accessing and manipulating item data that is otherwise not representable by the `ItemMeta` API.
Through this API, you can read and modify properties of an item, so called data components, in a stable and object-oriented manner.

## Introduction

[Section titled “Introduction”](#introduction)

### What is a data component?

[Section titled “What is a data component?”](#what-is-a-data-component)

A data component represents a piece of data associated with an item. Vanilla items can have properties such as custom model data, container loot contents, banner patterns, or potion effects.

### Structure

[Section titled “Structure”](#structure)

![Component Structure](https://docs.papermc.io/_astro/data-component-api-tree.Cp6qgmua_Z1Jh1Sy.webp)
For implementation details, [click here](#example-cool-sword).

#### The prototype (default values)

[Section titled “The prototype (default values)”](#the-prototype-default-values)

Items come with an initial set of components that we call the prototype.
These components are defined on the `ItemType` of the `ItemStack`. They control the base behavior
of the item, representing a brand new item without any modifications.

The prototype gives items their initial properties such as if they are food, a tool, a weapon, etc.

#### The patch

[Section titled “The patch”](#the-patch)

The patch represents the modifications made to the item. This may include giving it a custom name,
modifying the enchantments, damaging it, or adding to the lore. The patch is applied ontop of the prototype,
allowing us to make modifications to an item.

The patch also allows for removing components that were previously in the prototype. This is shown by
the `minecraft:tool` example in red. We are removing this component, so this sword item will no longer
break cobweb or other sword blocks faster.

We can also add new components, as seen from the new `minecraft:enchantment_glint_override` component, which
allows us to make it appear as if it were enchanted.

## Differences compared to `ItemMeta`

[Section titled “Differences compared to ItemMeta”](#differences-compared-to-itemmeta)

The `ItemMeta` API provides methods to modify `ItemStack`s in a hierarchical manner, such as `CompassMeta`, which allows you to modify the components of a `minecraft:compass`.
While `ItemMeta` is still very useful, it does not properly represent the prototype/patch relationship that Minecraft items use.

### Key differences

[Section titled “Key differences”](#key-differences)

#### Expanded data model

[Section titled “Expanded data model”](#expanded-data-model)

The data component API exposes a much broader and more detailed set of item properties than `ItemMeta`.
Data components allow the entire item to be modified in a fashion that better represents how Minecraft does item modifications.

#### Version-specific

[Section titled “Version-specific”](#version-specific)

The data component API is designed to adapt to version changes. The data component API may experience breaking changes on version updates as Minecraft makes changes to components.
Backwards compatibility is not promised.

Because `ItemMeta` is represented in a different format, breaking changes made to components by Mojang may not result in breaking changes to `ItemMeta`.

#### Builders and immutability

[Section titled “Builders and immutability”](#builders-and-immutability)

Many complex data components require a builder approach for construction and editing. All data types that are returned by the api are also immutable, so they will not directly modify the component.

#### Patch-only

[Section titled “Patch-only”](#patch-only)

`ItemMeta` only represents the patch of an `ItemStack`. This means that you cannot get the original properties (prototype) of the `ItemStack`, such as its default
durability or default attributes.

#### No snapshots

[Section titled “No snapshots”](#no-snapshots)

Currently, `ItemMeta` represents a **snapshot** of an `ItemStack`’s patched map.
This is expensive as it requires the entire patch to be read, even values that you may not be using.

The data component API integrates directly with `ItemStack`. Although conceptually similar, the data component API focuses on explicit, strongly typed data retrieval and updates without this additional overhead.

### When should I use `DataComponents` or `ItemMeta`?

[Section titled “When should I use DataComponents or ItemMeta?”](#when-should-i-use-datacomponents-or-itemmeta)

You would want to use `ItemMeta` if you:

* Are doing only simple changes to `ItemStack`s
* Want to keep cross-version compatibility with your plugin

You would want to use data components if you:

* Want more complicated `ItemStack` modifications
* Do not care about cross-version compatibility
* Want to access default (prototype) values
* Want to remove components from an `ItemStack`’s prototype

## Basic usage

[Section titled “Basic usage”](#basic-usage)

The data component API will fetch values according to the behavior seen in game. So, if the patch removes the `minecraft:tool` component,
trying to get that component will return null.

### Retrieving a prototype value

[Section titled “Retrieving a prototype value”](#retrieving-a-prototype-value)

```java
// Get the default durability of diamond sword

int defaultDurability = Material.DIAMOND_SWORD.getDefaultData(DataComponentTypes.MAX_DAMAGE)
```

### Checking for a data component

[Section titled “Checking for a data component”](#checking-for-a-data-component)

```java
// Check if this item has a custom name data component

boolean hasCustomName = stack.hasData(DataComponentTypes.CUSTOM_NAME);

logger.info("Has custom name? " + hasCustomName);
```

### Reading a valued data component

[Section titled “Reading a valued data component”](#reading-a-valued-data-component)

```java
// The damage of an item can be null, so we require a null check

Integer damageValue = stack.getData(DataComponentTypes.DAMAGE);

if (damageValue != null) {

logger.info("Current damage: " + damageValue);

} else {

logger.info("This item doesn't have a damage component set.");

}

// Certain components, like the max stack size, will always be present on an item

Integer maxStackSize = stack.getData(DataComponentTypes.MAX_STACK_SIZE);
```

### Setting a valued data component

[Section titled “Setting a valued data component”](#setting-a-valued-data-component)

```java
// Set a custom model data value on this item

stack.setData(DataComponentTypes.CUSTOM_MODEL_DATA, CustomModelData.customModelData()

.addFloat(0.5f)

.addFlag(true)

.build()

);
```

### Removing or resetting a data component

[Section titled “Removing or resetting a data component”](#removing-or-resetting-a-data-component)

```java
// Remove an existing component (e.g. tool)

stack.unsetData(DataComponentTypes.TOOL);

// Reset a component to the default (prototype) value for its item type (e.g. max stack size)

stack.resetData(DataComponentTypes.MAX_STACK_SIZE);
```

### Non-valued data components

[Section titled “Non-valued data components”](#non-valued-data-components)

Some components are only flags and don’t carry any sort of value:

```java
// Make the item a glider to be used like elytra (combined with the equippable component)

stack.setData(DataComponentTypes.GLIDER);

// Remove the glider flag

stack.unsetData(DataComponentTypes.GLIDER);
```

## Advanced usage with builders

[Section titled “Advanced usage with builders”](#advanced-usage-with-builders)

Many data components have complex structures that require builders.

### Modifying prototype component values

[Section titled “Modifying prototype component values”](#modifying-prototype-component-values)

```java
ItemStack helmet = ItemStack.of(Material.DIAMOND_HELMET);

// Get the equippable component for this item, and make it a builder.

// Note: Not all types have .toBuilder() methods

// This is the prototype value of the diamond helmet.

Equippable.Builder builder = helmet.getData(DataComponentTypes.EQUIPPABLE).toBuilder();

// Make the helmet look like netherite

// We get the prototype equippable value from NETHERITE_HELMET

builder.assetId(Material.NETHERITE_HELMET.getDefaultData(DataComponentTypes.EQUIPPABLE).assetId());

// And give it a spooky sound when putting it on

builder.equipSound(SoundEventKeys.ENTITY_GHAST_HURT);

// Set our new item

helmet.setData(DataComponentTypes.EQUIPPABLE, builder);
```

This will create a diamond helmet that looks like a netherite helmet and plays a spooky ghast sound when equipped.

### Example: Written book

[Section titled “Example: Written book”](#example-written-book)

```java
ItemStack book = ItemStack.of(Material.WRITTEN_BOOK);

WrittenBookContent.Builder builder = WrittenBookContent.writtenBookContent("My Book", "AuthorName");

// Add a page

builder.addPage(Component.text("This is a new page!"));

// Add a page that shows differently for people who have swear filtering on

// Players who have disabled filtering, will see "I hate Paper!", while those with filtering on will see the "I love Paper!".

builder.addFilteredPage(

Filtered.of(Component.text("I hate Paper!"), Component.text("I love Paper!"))

);

// Change generation

builder.generation(1);

// Apply changes

book.setData(DataComponentTypes.WRITTEN_BOOK_CONTENT, builder.build());
```

### Example: Cool sword

[Section titled “Example: Cool sword”](#example-cool-sword)

```java
ItemStack sword = ItemStack.of(Material.DIAMOND_SWORD);

sword.setData(DataComponentTypes.LORE, ItemLore.lore().addLine(Component.text("Cool sword!")).build());

sword.setData(DataComponentTypes.ENCHANTMENTS, ItemEnchantments.itemEnchantments().add(Enchantment.SHARPNESS, 10).build());

sword.setData(DataComponentTypes.RARITY, ItemRarity.RARE);

sword.unsetData(DataComponentTypes.TOOL); // Remove the tool component

sword.setData(DataComponentTypes.MAX_DAMAGE, 10);

sword.setData(DataComponentTypes.ENCHANTMENT_GLINT_OVERRIDE, true); // Make it glow!
```

## Matching items without certain data components

[Section titled “Matching items without certain data components”](#matching-items-without-certain-data-components)

When comparing items, you sometimes want to ignore certain values. For this, we can use the
[`ItemStack#matchesWithoutData`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#matchesWithoutData(org.bukkit.inventory.ItemStack,java.util.Set))
method.

For example, here we compare two diamond swords whilst ignoring their durability:

```java
ItemStack originalSword = ItemStack.of(Material.DIAMOND_SWORD);

ItemStack damagedSword = ItemStack.of(Material.DIAMOND_SWORD);

damagedSword.setData(DataComponentTypes.DAMAGE, 100);

boolean match = damagedSword.matchesWithoutData(originalSword, Set.of(DataComponentTypes.DAMAGE), false);

logger.info("Do the sword match? " + match); // -> true
```


================================================================================
Chapter Title: Persistent data container (PDC)
Original Link: https://docs.papermc.io/paper/dev/pdc/
================================================================================

The Persistent Data Container (PDC) is a way to store custom data on a whole range of objects; such as items, entities, and block entities.
The full list of classes that support the PDC are:

* [`ItemStack`](#itemstack)
* [`Chunk`](#chunk)
* [`World`](#world)
* [`Entity`](#entity)
* [`TileState`](#tilestate)
* [`Structure`](#structure)
* [`GeneratedStructure`](#generatedstructure)
* [`Raid`](#raid)
* [`OfflinePlayer`](#offlineplayer)
* [`ItemMeta`](#itemmeta)

## What is it used for?

[Section titled “What is it used for?”](#what-is-it-used-for)

In the past, developers resorted to a variety of methods to store custom data on objects:

* NBT tags: Requires reflection to access internals and was generally unreliable in the long term.
* Lore and display names: Prone to collisions as well as slow to access.

The benefit of the PDC is that it allows for a more reliable and performant way to store arbitrary data on objects.
It also doesn’t rely on accessing server internals, so it’s less likely to break on future versions. It also removes the need to
manually track the data lifecycle, as, for example with an entity, the PDC will be saved when the entity unloads.

## Adding data

[Section titled “Adding data”](#adding-data)

To store data in the PDC, there are a few things you need first. The first is a [`NamespacedKey`](https://jd.papermc.io/paper/org/bukkit/NamespacedKey.html),
which is used to identify the data. The second is a [`PersistentDataContainer`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataContainer.html),
which is the object you want to store the data on. The third is the data itself.

```java
NamespacedKey key = new NamespacedKey(pluginInstance, "example-key"); // Create a NamespacedKey

World world = Bukkit.getServer().getWorlds().getFirst();

PersistentDataContainer pdc = world.getPersistentDataContainer();

pdc.set(key, PersistentDataType.STRING, "I love tacos!");
```

[`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html) however doesn’t have this method and instead requires you to use its builder-style consumer:

```java
NamespacedKey key = ...;

// For 1.20.4 and below, use 'new ItemStack(Material.DIAMOND)' instead

ItemStack item = ItemStack.of(Material.DIAMOND);

item.editPersistentDataContainer(pdc -> {

pdc.set(key, PersistentDataType.STRING, "I love tacos!");

});
```

Note

The [`ItemStack#editPersistentDataContainer()`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#editPersistentDataContainer(java.util.function.Consumer)) method on `ItemStack` is only available in 1.21.4+. For older versions, you need to access and modify the [`ItemMeta`](https://jd.papermc.io/paper/org/bukkit/inventory/meta/ItemMeta.html) instead.
For 1.16.5+, there’s the [`ItemStack#editMeta()`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#editMeta(java.util.function.Consumer)) method though.

Note

It is considered good practice to reuse `NamespacedKey` objects. They can be constructed with either:

* A [`Plugin`](https://jd.papermc.io/paper/org/bukkit/plugin/Plugin.html) instance and a [`String`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) identifier
* A [`String`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) namespace and a [`String`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html) identifier

The first option is often preferred as it will automatically use the plugin’s lowercased name as namespace; however, the second option can be used if you want to use a different namespace or access the data from another plugin.

## Getting data

[Section titled “Getting data”](#getting-data)

To get data from the PDC, you need to know the `NamespacedKey` and the [`PersistentDataType`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataType.html) of the data.
Some API parts, such as Adventure’s [`Component.text(String)`](https://jd.advntr.dev/api/latest/net/kyori/adventure/text/Component.html#text(java.lang.String)), require non-null values. In such cases, use the [`getOrDefault`](https://jd.papermc.io/paper/io/papermc/paper/persistence/PersistentDataContainerView.html#getOrDefault(org.bukkit.NamespacedKey,org.bukkit.persistence.PersistentDataType,C)) on the pdc instead of [`get`](https://jd.papermc.io/paper/io/papermc/paper/persistence/PersistentDataContainerView.html#get(org.bukkit.NamespacedKey,org.bukkit.persistence.PersistentDataType)), which is nullable.

```java
NamespacedKey key = ...; // Use the same key as the adding-data example

World world = ...; // Use the same world as the adding-data example

PersistentDataContainer pdc = world.getPersistentDataContainer();

// Utilize the data from the PDC

String value = pdc.getOrDefault(key, PersistentDataType.STRING, "<null>");

// Do something with the value

player.sendPlainMessage(value);
```

## Data types

[Section titled “Data types”](#data-types)

The PDC supports a wide range of data types, such as:

* `Byte`, `Byte Array`
* `Double`
* `Float`
* `Integer`, `Integer Array`
* `Long`, `Long Array`
* `Short`
* `String`
* `Boolean`
* `Tag Containers` - a way to nest PDCs within each other. To create a new `PersistentDataContainer`, you can use:

  ```java
  // Get an existing container

  PersistentDataContainer container = ...;

  // Create a new container

  PersistentDataContainer newContainer = container.getAdapterContext().newPersistentDataContainer();
  ```
* `Lists` - a way to represent lists of data that can be stored via another persistent data type. You may create them via:

  ```java
  // Storing a list of strings in a container by verbosely creating

  // a list data type wrapping the string data type.

  container.set(

  key,

  PersistentDataType.LIST.listTypeFrom(PersistentDataType.STRING),

  List.of("a", "list", "of", "strings")

  );

  // Storing a list of strings in a container by using the API

  // provided pre-definitions of commonly used list types.

  container.set(key, PersistentDataType.LIST.strings(), List.of("a", "list", "of", "strings"));

  // Retrieving a list of strings from the container.

  List<String> strings = container.get(key, PersistentDataType.LIST.strings());
  ```

Boolean `PersistentDataType`

The [`Boolean`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataType.html#BOOLEAN) PDC type exists for convenience

* you cannot make more complex types distill to a `Boolean`.

### Custom data types

[Section titled “Custom data types”](#custom-data-types)

You can store a wide range of data in the PDC with the native adapters; however, if you need a more complex data type, you can
implement your own `PersistentDataType` and use that instead.
The `PersistentDataType`’s job is to “deconstruct” a complex data type into something that is natively supported (see above) and then vice-versa.

Here is an example of how to do that for a UUID:

UUIDDataType.java

```java
@NullMarked

public class UUIDDataType implements PersistentDataType<byte[], UUID> {

public static final UUIDDataType INSTANCE = new UUIDDataType();

// We just need a singleton, so there's no need to allow instantiation

private UUIDDataType() {}

@Override

public Class<byte[]> getPrimitiveType() {

return byte[].class;

}

@Override

public Class<UUID> getComplexType() {

return UUID.class;

}

@Override

public byte[] toPrimitive(UUID complex, PersistentDataAdapterContext context) {

ByteBuffer bb = ByteBuffer.allocate(Long.BYTES * 2);

bb.putLong(complex.getMostSignificantBits());

bb.putLong(complex.getLeastSignificantBits());

return bb.array();

}

@Override

public UUID fromPrimitive(byte[] primitive, PersistentDataAdapterContext context) {

ByteBuffer bb = ByteBuffer.wrap(primitive);

long firstLong = bb.getLong();

long secondLong = bb.getLong();

return new UUID(firstLong, secondLong);

}

}
```

Note

In order to use your own `PersistentDataType`, you must pass an instance of it to the
[`get`](https://jd.papermc.io/paper/io/papermc/paper/persistence/PersistentDataContainerView.html#get(org.bukkit.NamespacedKey,org.bukkit.persistence.PersistentDataType))/
[`set`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataContainer.html#set(org.bukkit.NamespacedKey,org.bukkit.persistence.PersistentDataType,C))/
[`has`](https://jd.papermc.io/paper/io/papermc/paper/persistence/PersistentDataContainerView.html#has(org.bukkit.NamespacedKey,org.bukkit.persistence.PersistentDataType)) methods.

```java
container.set(key, UUIDDataType.INSTANCE, uuid);
```

## Read-only containers

[Section titled “Read-only containers”](#read-only-containers)

Certain classes, like `ItemStack` or [`OfflinePlayer`](https://jd.papermc.io/paper/org/bukkit/OfflinePlayer.html), provide a read-only view of their PDC.
In contrast to `ItemStack`, `OfflinePlayer` does not provide any way to modify the underlying container.
This is because the `OfflinePlayer` is directly read from disk and would require a blocking file operation.
Mutable objects, like the [`PersistentDataHolder#getPersistentDataContainer()`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataHolder.html#getPersistentDataContainer()), generally need to be re-saved even without modification or monitored.
That’s why it’s better to use unmodifiable “views” for read-only operations.

```java
NamespacedKey key = ...;

ItemStack item = ...;

PersistentDataContainerView pdcView = item.getPersistentDataContainer();

// Utilize the data from the PDC "view"

String value = pdcView.getOrDefault(key, PersistentDataType.STRING, "<null>");

// Do something with the value

player.sendPlainMessage(value);
```

Note

PDC-view support for `ItemStack` was only introduced in 1.21.1. For older versions, you need to use the `ItemMeta` instead.

## Storing on different objects

[Section titled “Storing on different objects”](#storing-on-different-objects)

Caution

Data is **not** copied across holders for you, and needs to be **manually** copied if ‘moving’ between PersistentDataHolders.

E.g. Placing an ItemStack as a Block (with a TileState) ***does not*** copy over PDC data.

Objects that can have a PDC implement the [`PersistentDataHolder`](https://jd.papermc.io/paper/org/bukkit/persistence/PersistentDataHolder.html) interface
and their PDC can be fetched with `PersistentDataHolder#getPersistentDataContainer()`.

* ##### [`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html)

  [Section titled “ItemStack”](#itemstack)

  + The persistent data container of an `ItemStack` has historically been accessed by
    the `ItemStack`’s `ItemMeta`. This, however, includes the overhead of constructing the entire `ItemMeta`, which acts as a snapshot of the `ItemStack`’s data at the point of creation.

    To avoid this overhead in 1.21.1+, ItemStack exposes a read-only view of its persistent data container at [`ItemStack#getPersistentDataContainer()`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#getPersistentDataContainer()).
    Edits to the persistent data container can also be simplified in 1.21.4+ using `ItemStack#editPersistentDataContainer(java.util.function.Consumer)`.
    The persistent data container available in the consumer is not valid outside the consumer.

    ```java
    ItemStack itemStack = ...;

    itemStack.editPersistentDataContainer(pdc -> {

    pdc.set(key, PersistentDataType.STRING, "I love tacos!");

    });
    ```
* ##### [`Chunk`](https://jd.papermc.io/paper/org/bukkit/Chunk.html)

  [Section titled “Chunk”](#chunk)

  + `Chunk#getPersistentDataContainer()`
* ##### [`World`](https://jd.papermc.io/paper/org/bukkit/World.html)

  [Section titled “World”](#world)

  + `World#getPersistentDataContainer()`
* ##### [`Entity`](https://jd.papermc.io/paper/org/bukkit/entity/Entity.html)

  [Section titled “Entity”](#entity)

  + `Entity#getPersistentDataContainer()`
* ##### [`TileState`](https://jd.papermc.io/paper/org/bukkit/block/TileState.html)

  [Section titled “TileState”](#tilestate)

  + This is slightly more complicated, as you need to cast the block’s state to something that extends `TileState`.
    This does not work for all blocks, only those that have a block entity.

    ```java
    Block block = ...;

    if (block.getState() instanceof Chest chest) {

    chest.getPersistentDataContainer().set(key, PersistentDataType.STRING, "I love tacos!");

    chest.update();

    }
    ```
* ##### [`Structure`](https://jd.papermc.io/paper/org/bukkit/structure/Structure.html)

  [Section titled “Structure”](#structure)

  + `Structure#getPersistentDataContainer()`
* ##### [`GeneratedStructure`](https://jd.papermc.io/paper/org/bukkit/generator/structure/GeneratedStructure.html)

  [Section titled “GeneratedStructure”](#generatedstructure)

  + `GeneratedStructure#getPersistentDataContainer()`
* ##### [`Raid`](https://jd.papermc.io/paper/org/bukkit/Raid.html)

  [Section titled “Raid”](#raid)

  + `Raid#getPersistentDataContainer()`
* ##### [`OfflinePlayer`](https://jd.papermc.io/paper/org/bukkit/OfflinePlayer.html)

  [Section titled “OfflinePlayer”](#offlineplayer)

  + OfflinePlayer only exposes a read-only version of the persistent data container.
    It can be accessed via `OfflinePlayer#getPersistentDataContainer()`.
* ##### [`ItemMeta`](https://jd.papermc.io/paper/org/bukkit/inventory/meta/ItemMeta.html)

  [Section titled “ItemMeta”](#itemmeta)

  + `ItemMeta#getPersistentDataContainer()`


================================================================================
Chapter Title: Scheduling
Original Link: https://docs.papermc.io/paper/dev/scheduler/
================================================================================

The [`BukkitScheduler`](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitScheduler.html) can be used to schedule your code to be run later or repeatedly.

Folia

This guide is designed for non-Folia Bukkit servers. If you are using Folia, you should use its respective schedulers.

## What is a tick?

[Section titled “What is a tick?”](#what-is-a-tick)

Every game runs something called a game loop, which essentially executes all the logic of the game over and over.
A single execution of that loop in Minecraft is called a ‘tick’.

In Minecraft, there are 20 ticks per second or in other words, one tick every 50 milliseconds. This means that the game loop is executed
20 times per second. A tick taking more than 50ms to execute is the moment when your server starts to fall behind on
its work and lag.

A task that should run after 100 ticks will run after 5 seconds (100 ticks / 20 ticks per second = 5 seconds). However,
if the server is only running at 10 ticks per second, a task that is scheduled to run after 100 ticks will take 10
seconds.

### Converting between human units and Minecraft ticks

[Section titled “Converting between human units and Minecraft ticks”](#converting-between-human-units-and-minecraft-ticks)

Every method of the scheduler that takes a delay or period uses ticks as a unit of time.

Converting from human units to ticks and back is as simple as:

* `ticks = seconds * 20`
* `seconds = ticks / 20`

You can make your code more readable by using the
[`TimeUnit`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/TimeUnit.html)
enum, e.g. to convert 5 minutes to ticks and back:

* `TimeUnit.MINUTES.toSeconds(5) * 20`
* `TimeUnit.SECONDS.toMinutes(ticks / 20)`

You can also use the `Tick` class from Paper to convert between human units and ticks, e.g. to convert 5 minutes to ticks:
`Tick.tick().fromDuration(Duration.ofMinutes(5))` will yield `6000` ticks.

## Obtaining the scheduler

[Section titled “Obtaining the scheduler”](#obtaining-the-scheduler)

To obtain a scheduler, you can use the [`getScheduler`](https://jd.papermc.io/paper/org/bukkit/Server.html#getScheduler()) method
on the [`Server`](https://jd.papermc.io/paper/org/bukkit/Server.html) class, e.g. in your `onEnable` method:

```java
@Override

public void onEnable() {

BukkitScheduler scheduler = this.getServer().getScheduler();

}
```

## Scheduling tasks

[Section titled “Scheduling tasks”](#scheduling-tasks)

Scheduling a task requires you to pass:

* Your plugin’s instance
* The code to run, either with a [`Runnable`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html)
  or `Consumer<BukkitTask>`
* The delay in ticks before the task should run for the first time
* The period in ticks between each execution of the task, if you’re scheduling a repeating task

### Difference between synchronous and asynchronous tasks

[Section titled “Difference between synchronous and asynchronous tasks”](#difference-between-synchronous-and-asynchronous-tasks)

#### Synchronous tasks (on the main thread)

[Section titled “Synchronous tasks (on the main thread)”](#synchronous-tasks-on-the-main-thread)

Synchronous tasks are tasks that are executed on the main server thread. This is the same
thread that handles all game logic.

All tasks scheduled on the main thread will affect the server’s performance. If your task
is making web requests, accessing files, databases or otherwise time-consuming operations, you should consider using
an asynchronous task.

#### Asynchronous tasks (off the main thread)

[Section titled “Asynchronous tasks (off the main thread)”](#asynchronous-tasks-off-the-main-thread)

Asynchronous tasks are tasks that are executed on separate threads, therefore will not directly affect
your server’s performance.

Caution

**Large portions of the Bukkit API are not safe to use from within asynchronous tasks**. If a method changes or
accesses the world state, it is not safe to be used from an asynchronous task.

Note

While the tasks are executed on separate threads, they are still started from the main thread
and will be affected if the server is lagging, an example would be 20 ticks not being exactly 1 second.

If you need a scheduler that runs independently of the server, consider using your own
[`ScheduledExecutorService`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ScheduledExecutorService.html).
You can follow [this guide](https://www.baeldung.com/java-executor-service-tutorial#ScheduledExecutorService) to learn how to use it.

### Different ways to schedule tasks

[Section titled “Different ways to schedule tasks”](#different-ways-to-schedule-tasks)

#### Using `Runnable`

[Section titled “Using Runnable”](#using-runnable)

The [`Runnable`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Runnable.html) interface is used for the simplest tasks
that don’t require a [`BukkitTask`](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitTask.html) instance.

You can either implement it in a separate class, e.g.:

MyRunnableTask.java

```java
public class MyRunnableTask implements Runnable {

private final MyPlugin plugin;

public MyRunnableTask(MyPlugin plugin) {

this.plugin = plugin;

}

@Override

public void run() {

this.plugin.getServer().broadcast(Component.text("Hello, World!"));

}

}
```

```java
scheduler.runTaskLater(plugin, new MyRunnableTask(plugin), 20);
```

Or use a lambda expression, which is great for simple and short tasks:

```java
scheduler.runTaskLater(plugin, /* Lambda: */ () -> {

this.plugin.getServer().broadcast(Component.text("Hello, World!"));

}, /* End of the lambda */ 20);
```

#### Using `Consumer<BukkitTask>`

[Section titled “Using Consumer<BukkitTask>”](#using-consumerbukkittask)

The [`Consumer`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/Consumer.html) interface is used for tasks
that require a [`BukkitTask`](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitTask.html) instance (usually in repeated tasks),
e.g. when you want to cancel the task from inside it.

You can either implement it in a separate class similarly to the `Runnable`, e.g.:

MyConsumerTask.java

```java
public class MyConsumerTask implements Consumer<BukkitTask> {

private final UUID entityId;

public MyConsumerTask(UUID uuid) {

this.entityId = uuid;

}

@Override

public void accept(BukkitTask task) {

Entity entity = Bukkit.getServer().getEntity(this.entityId);

if (entity instanceof LivingEntity livingEntity) {

livingEntity.addPotionEffect(new PotionEffect(PotionEffectType.SPEED, 20, 1));

return;

}

task.cancel(); // The entity is no longer valid, there's no point in continuing to run this task

}

}
```

```java
scheduler.runTaskTimer(plugin, new MyConsumerTask(someEntityId), 0, 20);
```

Or use a lambda expression, which again is much cleaner for short and simple tasks:

```java
scheduler.runTaskTimer(plugin, /* Lambda: */ task -> {

Entity entity = Bukkit.getServer().getEntity(entityId);

if (entity instanceof LivingEntity livingEntity) {

livingEntity.addPotionEffect(new PotionEffect(PotionEffectType.SPEED, 20, 1));

return;

}

task.cancel(); // The entity is no longer valid, there's no point in continuing to run this task

} /* End of the lambda */, 0, 20);
```

##### Using `BukkitRunnable`

[Section titled “Using BukkitRunnable”](#using-bukkitrunnable)

[`BukkitRunnable`](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitRunnable.html) is a class that implements `Runnable`
and holds a `BukkitTask` instance. This means that you do not need to access the task from inside the `run()` method,
you can simply use the [`this.cancel()`](https://jd.papermc.io/paper/org/bukkit/scheduler/BukkitRunnable.html#cancel()) method:

CustomRunnable.java

```java
public class CustomRunnable extends BukkitRunnable {

private final UUID entityId;

public CustomRunnable(UUID uuid) {

this.entityId = uuid;

}

@Override

public void run() {

Entity entity = Bukkit.getServer().getEntity(this.entityId);

if (entity instanceof LivingEntity livingEntity) {

livingEntity.addPotionEffect(new PotionEffect(PotionEffectType.SPEED, 20, 1));

return;

}

this.cancel(); // The entity is no longer valid, there's no point in continuing to run this task

}

}
```

This simply adds a potion effect until the entity dies.

#### Using a delay of 0 ticks

[Section titled “Using a delay of 0 ticks”](#using-a-delay-of-0-ticks)

A delay of 0 ticks is treated as you wanting to run the task on the next tick. If you schedule a task with a delay of 0 ticks
while the server is starting, or before it is enabled, it will be executed before the server is enabled.


================================================================================
Chapter Title: Plugin messaging
Original Link: https://docs.papermc.io/paper/dev/plugin-messaging/
================================================================================

First introduced in [2012](https://web.archive.org/web/20220711204310/https://dinnerbone.com/blog/2012/01/13/minecraft-plugin-channels-messaging/),
Plugin messaging is a way for plugins to communicate with clients. When your servers are behind a proxy,
it will allow your plugins to communicate with the proxy server.

## BungeeCord channel

[Section titled “BungeeCord channel”](#bungeecord-channel)

The BungeeCord channel is used for communication between your Paper server and a BungeeCord (or a BungeeCord-compatible) proxy.

Originally, the channel supported by the BungeeCord proxy was called `BungeeCord`. In versions 1.13 and above,
the channel was renamed to `bungeecord:main` to create a key structure for plugin messaging channels.

Paper handles this change internally and automatically changes any messages sent on the `BungeeCord` channel
to the `bungeecord:main` channel. This means that your plugins should continue to use the `BungeeCord` channel.

## Sending plugin messages

[Section titled “Sending plugin messages”](#sending-plugin-messages)

First, we’re going to take a look at your Paper server. Your plugin will need to register that it
will be sending on any given plugin channel. You should to do this alongside your other event listener registrations.

PluginMessagingSample.java

```java
public final class PluginMessagingSample extends JavaPlugin {

@Override

public void onEnable() {

getServer().getMessenger().registerOutgoingPluginChannel(this, "BungeeCord");

// Blah blah blah...

}

}
```

Now that we’re registered, we can send messages on the `BungeeCord` channel.

Plugin messages are formatted as byte arrays and can be sent using the [`sendPluginMessage`](https://jd.papermc.io/paper/org/bukkit/plugin/messaging/PluginMessageRecipient.html#sendPluginMessage(org.bukkit.plugin.Plugin,java.lang.String,byte%5B%5D))
method on a [`Player`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html) object.
Let’s take a look at an example of sending a plugin message to the `BungeeCord` channel to send our player to another server.

PluginMessagingSample.java

```java
public final class PluginMessagingSample extends JavaPlugin implements Listener {

@Override

public void onEnable() {

getServer().getPluginManager().registerEvents(this, this);

getServer().getMessenger().registerOutgoingPluginChannel(this, "BungeeCord");

}

@EventHandler

public void onPlayerJump(PlayerJumpEvent event) {

Player player = event.getPlayer();

ByteArrayDataOutput out = ByteStreams.newDataOutput();

out.writeUTF("Connect");

out.writeUTF("hub2");

player.sendPluginMessage(this, "BungeeCord", out.toByteArray());

}

}
```

Tip

These channels rely on the Minecraft protocol, and are sent as a special type of packet called a
[Plugin Message](https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge/Plugin_channels). They piggyback on player connections, so if there is no
player connected to the server, it will not be able to send or receive plugin messages.

### What did we just do?

[Section titled “What did we just do?”](#what-did-we-just-do)

We sent a plugin message on the `BungeeCord` channel! The message we sent was a byte array that contained two strings converted to bytes: `Connect` and `hub2`.

Our proxy server received the message through the player who triggered the [`PlayerJumpEvent`](https://jd.papermc.io/paper/com/destroystokyo/paper/event/player/PlayerJumpEvent.html) on our Java server.
Then, it recognized the channel as its own and, in alignment with BungeeCord’s protocol, sent our player to the `hub2` server.

For BungeeCord, we can think of this message as a case-sensitive command with arguments.
Here, our command is `Connect` and our only argument is `hub2`, but some “commands” may have multiple arguments.
For other channels introduced by client side mods, refer to their documentation to best understand how to format your messages.

### Plugin message types

[Section titled “Plugin message types”](#plugin-message-types)

Although we sent a `Connect` message to the proxy, there are a few other cases that BungeeCord-compatible proxies will act on.
These are the following:

| Message Type | Description | Arguments | Response |
| --- | --- | --- | --- |
| `Connect` | Connects the player to the specified server. | `server name` | N/A |
| `ConnectOther` | Connects another player to the specified server. | `player name`, `server name` | N/A |
| `IP` | Returns the IP of the player. | N/A | `IP`, `port` |
| `IPOther` | Returns the IP of the specified player. | `player name` | `player name`, `IP`, `port` |
| `PlayerCount` | Returns the number of players on the specified server. | `server name` | `server name`, `player count` |
| `PlayerList` | Returns a list of players on the specified server. | `server name` | `server name`, `CSV player names` |
| `GetServers` | Returns a list of all servers. | N/A | `CSV server names` |
| `Message` | Sends a message to the specified player. | `player name`, `message` | N/A |
| `MessageRaw` | Sends a raw chat component to the specified player. | `player name`, `JSON chat component` | N/A |
| `GetServer` | Returns the server the player is connected to. | N/A | `server name` |
| `GetPlayerServer` | Returns the server name of the specified player. | `player name` | `player name`, `server name` |
| `UUID` | Returns the UUID of the player. | N/A | `UUID` |
| `UUIDOther` | Returns the UUID of the specified player. | `player name` | `player name`, `UUID` |
| `ServerIp` | Returns the IP of the specified server. | `server name` | `server name`, `IP`, `port` |
| `KickPlayer` | Kicks the specified player. | `player name`, `reason` | N/A |
| `KickPlayerRaw` | Kicks the specified player. | `player name`, `JSON chat component` | N/A |
| `Forward` | Forwards a plugin message to another server. | `server`, `subchannel`, `size of plugin message`, `message` | `subchannel`, `size of plugin message`, `message` |
| `ForwardToPlayer` | Forwards a plugin message to another player. | `player name`, `subchannel`, `size of plugin message`, `message` | `subchannel`, `size of plugin message`, `message` |

#### `PlayerCount`

[Section titled “PlayerCount”](#playercount)

MyPlugin.java

```java
public class MyPlugin extends JavaPlugin implements PluginMessageListener {

@Override

public void onEnable() {

this.getServer().getMessenger().registerOutgoingPluginChannel(this, "BungeeCord");

this.getServer().getMessenger().registerIncomingPluginChannel(this, "BungeeCord", this);

Player player = ...;

ByteArrayDataOutput out = ByteStreams.newDataOutput();

out.writeUTF("PlayerCount");

out.writeUTF("lobby");

player.sendPluginMessage(this, "BungeeCord", out.toByteArray());

// The response will be handled in onPluginMessageReceived

}

@Override

public void onPluginMessageReceived(String channel, Player player, byte[] message) {

if (!channel.equals("BungeeCord")) {

return;

}

ByteArrayDataInput in = ByteStreams.newDataInput(message);

String subchannel = in.readUTF();

if (subchannel.equals("PlayerCount")) {

// This is our response to the PlayerCount request

String server = in.readUTF();

int playerCount = in.readInt();

}

}

}
```

#### `Forward`

[Section titled “Forward”](#forward)

MyPlugin.java

```java
public class MyPlugin extends JavaPlugin implements PluginMessageListener {

@Override

public void onEnable() {

this.getServer().getMessenger().registerOutgoingPluginChannel(this, "BungeeCord");

this.getServer().getMessenger().registerIncomingPluginChannel(this, "BungeeCord", this);

Player player = ...;

ByteArrayDataOutput out = ByteStreams.newDataOutput();

out.writeUTF("Forward");

out.writeUTF("ALL"); // This is the target server. "ALL" will message all servers apart from the one sending the message

out.writeUTF("SecretInternalChannel"); // This is the channel.

ByteArrayOutputStream msgbytes = new ByteArrayOutputStream();

DataOutputStream msgout = new DataOutputStream(msgbytes);

msgout.writeUTF("Paper is the meaning of life"); // You can do anything you want with msgout

msgout.writeShort(42); // Writing a random short

out.writeShort(msgbytes.toByteArray().length); // This is the length.

out.write(msgbytes.toByteArray()); // This is the message.

player.sendPluginMessage(this, "BungeeCord", out.toByteArray());

// The response will be handled in onPluginMessageReceived

}

@Override

public void onPluginMessageReceived(String channel, Player player, byte[] message) {

if (!channel.equals("BungeeCord")) {

return;

}

ByteArrayDataInput in = ByteStreams.newDataInput(message);

String subchannel = in.readUTF();

if (subchannel.equals("SecretInternalChannel")) {

short len = in.readShort();

byte[] msgbytes = new byte[len];

in.readFully(msgbytes);

DataInputStream msgIn = new DataInputStream(new ByteArrayInputStream(msgbytes));

String secretMessage = msgIn.readUTF(); // Read the data in the same way you wrote it

short meaningofLife = msgIn.readShort();

}

}

}
```

This message is used to forward a plugin message to another server. This is useful for server-to-server communication within a proxy network.
For example, if a certain player is banned on one server, you can forward a message to all other servers to ban them there too.

Example of banning a player on all servers

This is not a recommended way to ban players, because there may not be anyone online on the target servers,
but it is an example of how this can be used.

#### `MessageRaw`

[Section titled “MessageRaw”](#messageraw)

The `MessageRaw` message type is used to send a raw chat component to a player. The target player is specified
by the second parameter - Player name or “ALL” for all players. This is also useful for sending messages to
players who are on a different server within the proxied network.

MyPlugin.java

```java
public class MyPlugin extends JavaPlugin {

@Override

public void onEnable() {

this.getServer().getMessenger().registerOutgoingPluginChannel(this, "BungeeCord");

Player player = ...;

ByteArrayDataOutput out = ByteStreams.newDataOutput();

out.writeUTF("MessageRaw");

out.writeUTF("ALL");

out.writeUTF(GsonComponentSerializer.gson().serialize(

Component.text("Click Me!").clickEvent(ClickEvent.openUrl("https://papermc.io"))

));

player.sendPluginMessage(this, "BungeeCord", out.toByteArray());

}

}
```

This will send the player a clickable message saying “Click Me!” that opens `https://papermc.io` upon clicking.


================================================================================
Chapter Title: Plugin configuration
Original Link: https://docs.papermc.io/paper/dev/plugin-configurations/
================================================================================

Configuration files allow users to change certain behavior and functionality of plugins. This guide will outline how to use them.

## Format

[Section titled “Format”](#format)

By default, plugins use a YAML configuration format (`.yml` file). Other formats, such as JSON or TOML, can be used;
however, these are not natively supported by Paper, so they will not be covered in this guide.

YAML works by having a tree-like `key: value` pair structure, as you would have seen in your [`plugin.yml`](https://docs.papermc.io/paper/dev/plugin-yml).
An example would look like this:

```java
root:

one-key: 10

another-key: David
```

When accessing indented values, you separate the levels with dots (`.`). For example, the key for the `David` string would be `root.another-key`.

## Creating a `config.yml`

[Section titled “Creating a config.yml”](#creating-a-configyml)

By placing a `config.yml` file inside your plugin, you can specify the default values for certain settings.
This will be located in the `resources` directory:

* Directoryexample-plugin/
  + Directorysrc/
    - Directorymain/
      * Directoryjava/
        + …
      * Directoryresources/
        + **config.yml**
        + plugin.yml

When your plugin is initialized, you must save this resource into the plugin’s data directory, so that a user can edit the values.
Here is an example of how you would do this in your plugin’s `onEnable`:

TestPlugin.java

```java
public class TestPlugin extends JavaPlugin {

@Override

public void onEnable() {

saveResource("config.yml", /* replace */ false);

// You can also use this for configuration files:

saveDefaultConfig();

// Where the default config.yml will be saved if it does not already exist

// getConfig()...

}

}
```

Note

The boolean `replace` parameter specifies whether it should replace an existing file if one exists.
If set to true, the configuration will be overwritten on every call.

## Getting and setting data

[Section titled “Getting and setting data”](#getting-and-setting-data)

The [`FileConfiguration`](https://jd.papermc.io/paper/org/bukkit/configuration/file/FileConfiguration.html) of the plugin can be fetched with
[`JavaPlugin#getConfig()`](https://jd.papermc.io/paper/org/bukkit/plugin/java/JavaPlugin.html#getConfig()) once it has been saved.
This will allow data to be fetched and set with the respective `#get...(key)` and
[`#set(key, value)`](https://jd.papermc.io/paper/org/bukkit/configuration/ConfigurationSection.html#set(java.lang.String,java.lang.Object)).
By default, most basic data types are supported by YAML. These can be fetched simply with
[`#getString(key)`](https://jd.papermc.io/paper/org/bukkit/configuration/ConfigurationSection.html#getString(java.lang.String)) or
[`#getBoolean(key)`](https://jd.papermc.io/paper/org/bukkit/configuration/ConfigurationSection.html#getBoolean(java.lang.String)).

However, some more complex Bukkit data types are also supported. A few of these include
[`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html),
[`Location`](https://jd.papermc.io/paper/org/bukkit/Location.html) and [`Vector`](https://jd.papermc.io/paper/org/bukkit/util/Vector.html)s.
Here is an example of loading a value from the config for teleporting a player:

Saving Configs

Whenever setting data in configurations, you must call
[`FileConfiguration#save(File/String)`](https://jd.papermc.io/paper/org/bukkit/configuration/file/FileConfiguration.html#save(java.io.File))
for the changes to be persisted to disk.

TestPlugin.java

```java
public class TestPlugin extends JavaPlugin {

public void teleportPlayer(Player player) {

Location to = getConfig().getLocation("target_location");

player.teleport(to);

}

}
```

This is possible as they implement [`ConfigurationSerializable`](https://jd.papermc.io/paper/org/bukkit/configuration/serialization/ConfigurationSerializable.html).
You can use this yourself, by implementing and registering a custom class.

TeleportOptions.java

```java
public class TeleportOptions implements ConfigurationSerializable {

private int chunkX;

private int chunkZ;

private String name;

public TeleportOptions(int chunkX, int chunkZ, String name) {

// Set the values

}

public Map<String, Object> serialize() {

Map<String, Object> data = new HashMap<>();

data.put("chunk-x", this.chunkX);

data.put("chunk-z", this.chunkZ);

data.put("name", this.name);

return data;

}

public static TeleportOptions deserialize(Map<String, Object> args) {

return new TeleportOptions(

(int) args.get("chunk-x"),

(int) args.get("chunk-z"),

(String) args.get("name")

);

}

}
```

Here we can see that we have an instance-based `serialize` method, which returns a map, and then a static `deserialize`
method that takes a [`Map`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Map.html) as a parameter and returns an instance
of the `TeleportOptions` class. Finally, for this to work, we must call:
`ConfigurationSerialization.registerClass(TeleportOptions.class)`

Caution

If you do not call [`ConfigurationSerialization#registerClass(Class)`](https://jd.papermc.io/paper/org/bukkit/configuration/serialization/ConfigurationSerialization.html#registerClass(java.lang.Class))
with Paper plugins, you will not be able to load nor save your custom classes.

## Custom configuration files

[Section titled “Custom configuration files”](#custom-configuration-files)

It is highly likely that you will have many different things to configure in your plugin. If you choose to split these
across multiple different files, you can still use the Bukkit `FileConfiguration` API to read the data from these.
It is as simple as:

```java
File file = new File(plugin.getDataFolder(), "items.yml");

YamlConfiguration config = YamlConfiguration.loadConfiguration(file);

// Work with config here

config.save(file);
```

This example reads the `items.yml` file from your plugin’s data directory. If the file does not exist or an error occurs
during reading, an empty configuration will be returned.

Blocking I/O

Loading and saving files on the main thread will slow your server. `load` and `save` operations should be executed asynchronously.

## Configurate

[Section titled “Configurate”](#configurate)

Configurate is a third-party library for working with configurations, maintained by the Sponge project. This project is
used internally by Paper for its configuration and offers many features that the `FileConfiguration` API doesn’t have. See their project
[here](https://github.com/SpongePowered/Configurate) for more information.


================================================================================
Chapter Title: RegistriesExperimental
Original Link: https://docs.papermc.io/paper/dev/registries/
================================================================================

Experimental

The Registry API and anything that uses it is currently experimental and may change in the future.

## What is a registry?

[Section titled “What is a registry?”](#what-is-a-registry)

In the context of Minecraft, a registry holds onto a set of values of the same type, identifying
each by a key. An example of such a registry would be the [ItemType registry](https://jd.papermc.io/paper/org/bukkit/Registry.html#ITEM) which holds all known item types.
Registries are available via the [RegistryAccess](https://jd.papermc.io/paper/io/papermc/paper/registry/RegistryAccess.html) class.

While a large portion of registries are defined by the server and client independently, more and
more are defined by the server and sent to the client while joining the server.
This enables the server, and to that extent plugins, to define custom content for both itself and
clients playing on it.
Notable examples include **enchantments** and **biomes**.

### Retrieving values from a registry

[Section titled “Retrieving values from a registry”](#retrieving-values-from-a-registry)

To retrieve elements from a registry, their respective keys can be used.
The API defines two types of keys.

* `net.kyori.adventure.key.Key` represents a namespace and a key.
* [TypedKey](https://jd.papermc.io/paper/io/papermc/paper/registry/TypedKey.html) wraps an Adventure key,
  but also includes the [key of
  the registry](https://jd.papermc.io/paper/io/papermc/paper/registry/TypedKey.html#registryKey()) the
  [TypedKey](https://jd.papermc.io/paper/io/papermc/paper/registry/TypedKey.html) belongs to.

An example of retrieving the `Sharpness` enchantment using
[TypedKeys](https://jd.papermc.io/paper/io/papermc/paper/registry/TypedKey.html) looks as follows:

```java
// Fetch the enchantment registry from the registry access

final Registry<Enchantment> enchantmentRegistry = RegistryAccess

.registryAccess()

.getRegistry(RegistryKey.ENCHANTMENT);

// Get the sharpness enchantment using its key.

// getOrThrow may be replaced with get if the registry may not contain said value

final Enchantment enchantment = enchantmentRegistry.getOrThrow(TypedKey.create(

RegistryKey.ENCHANTMENT, Key.key("minecraft:sharpness"))

);

// Same as above, but using the instance's method

final Enchantment enchantment = enchantmentRegistry.getOrThrow(

RegistryKey.ENCHANTMENT.typedKey(Key.key("minecraft:sharpness"))

);

// Same as above, but using generated create method

// available for data-driven registries or "writable" ones

// (those bound to a lifecycle event in RegistryEvents).

final Enchantment enchantment = enchantmentRegistry.getOrThrow(

EnchantmentKeys.create(Key.key("minecraft:sharpness"))

);

// Same as above too, but using generated typed keys.

// Only Vanilla entries have generated keys, for custom entries, the above method must be used.

final Enchantment enchantment = enchantmentRegistry.getOrThrow(EnchantmentKeys.SHARPNESS);
```

### Referencing registry values

[Section titled “Referencing registry values”](#referencing-registry-values)

Referencing entries in a registry is easier said than done.
While in most cases, a plain [Collection](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Collection.html) of the values might suffice, alternative approaches are
more often used by Minecraft and will hence be encountered.

A [`RegistrySet`](https://jd.papermc.io/paper/io/papermc/paper/registry/set/RegistrySet.html) defines a
collection of elements that *relate* to a registry.

Its most common subtype is the
[`RegistryKeySet`](https://jd.papermc.io/paper/io/papermc/paper/registry/set/RegistryKeySet.html) which
simply holds onto [TypedKey](https://jd.papermc.io/paper/io/papermc/paper/registry/TypedKey.html) instances.
An advantage of this data structure is its ability to remain valid even if the values of a
registry change.

A [`RegistryKeySet`](https://jd.papermc.io/paper/io/papermc/paper/registry/set/RegistryKeySet.html) can be
created via the factory methods on [`RegistrySet`](https://jd.papermc.io/paper/io/papermc/paper/registry/set/RegistrySet.html) like this:

```java
// Create a new registry key set that holds a collection enchantments

final RegistryKeySet<Enchantment> bestEnchantments = RegistrySet.keySet(

RegistryKey.ENCHANTMENT,

// Arbitrary keys of enchantments to store in the key set.

EnchantmentKeys.CHANNELING,

EnchantmentKeys.create(Key.key("papermc:softspoon"))

);
```

A [`Tag`](https://jd.papermc.io/paper/io/papermc/paper/registry/tag/Tag.html) follows up the concept
of a [`RegistryKeySet`](https://jd.papermc.io/paper/io/papermc/paper/registry/set/RegistryKeySet.html)
but is itself named and can hence be referenced.
A list of Vanilla tags can be found [on the Minecraft wiki](https://minecraft.wiki/w/Tag#Java_Edition_2).

## Mutating registries

[Section titled “Mutating registries”](#mutating-registries)

Beyond plain reading access to registries, Paper also offers a way for plugins to modify registries.

Caution

Mutating registries needs to be done during the server’s bootstrap phase.
As such, this section is only applicable to [Paper plugins](https://docs.papermc.io/paper/dev/getting-started/paper-plugins).

**Exceptions** thrown by plugins during this phase will cause the server to shutdown before loading,
as missing values or modifications to the registries would otherwise cause data loss.

Note

Mutating registries is done via the
[LifecycleEventManager](https://jd.papermc.io/paper/io/papermc/paper/plugin/lifecycle/event/LifecycleEventManager.html).
See the [Lifecycle Events](https://docs.papermc.io/paper/dev/lifecycle) page for more information.

The general entrypoint for mutating registries is
the [RegistryEvents](https://jd.papermc.io/paper/io/papermc/paper/registry/event/RegistryEvents.html) type,
which provides an entry point for each registry that can be modified.
Modification of a registry can take two different forms.

### Create new entries

[Section titled “Create new entries”](#create-new-entries)

Creating new entries is done via the [`compose` lifecycle event](https://jd.papermc.io/paper/io/papermc/paper/registry/event/RegistryEventProvider.html#compose())
on the respective registries.
The compose event is called after a registry’s content has been loaded from “vanilla” sources, like the built-in
datapack or any detected, enabled, datapacks. Plugins can hence register their own entries at this point.
The following example shows how to create a new enchantment:

TestPluginBootstrap.java

```java
public class TestPluginBootstrap implements PluginBootstrap {

@Override

public void bootstrap(BootstrapContext context) {

// Register a new handler for the compose lifecycle event on the enchantment registry

context.getLifecycleManager().registerEventHandler(RegistryEvents.ENCHANTMENT.compose().newHandler(event -> {

event.registry().register(

// The key of the registry

// Plugins should use their own namespace instead of minecraft or papermc

EnchantmentKeys.create(Key.key("papermc:pointy")),

b -> b.description(Component.text("Pointy"))

.supportedItems(event.getOrCreateTag(ItemTypeTagKeys.SWORDS))

.anvilCost(1)

.maxLevel(25)

.weight(10)

.minimumCost(EnchantmentRegistryEntry.EnchantmentCost.of(1, 1))

.maximumCost(EnchantmentRegistryEntry.EnchantmentCost.of(3, 1))

.activeSlots(EquipmentSlotGroup.ANY)

);

}));

}

}
```

### Modifying existing entries

[Section titled “Modifying existing entries”](#modifying-existing-entries)

Modification of existing entries is useful for plugins that aim to change the way Vanilla entries
behave. For this, use the [`entryAdd` lifecycle event](https://jd.papermc.io/paper/io/papermc/paper/registry/event/RegistryEventProvider.html#entryAdd()).
The event is called for *\*any\** entry added to a registry, however the API provides an easy way to target a specific entry for modification.
The following example shows how to increase the maximum level of the `Sharpness` enchantment.

```java
@Override

public void bootstrap(BootstrapContext context) {

context.getLifecycleManager().registerEventHandler(RegistryEvents.ENCHANTMENT.entryAdd()

// Increase the max level to 20

.newHandler(event -> event.builder().maxLevel(20))

// Configure the handler to only be called for the Vanilla sharpness enchantment.

.filter(EnchantmentKeys.SHARPNESS)

);

}
```


================================================================================
Chapter Title: Dialog APIExperimental
Original Link: https://docs.papermc.io/paper/dev/dialogs/
================================================================================

Experimental

The dialog API is currently experimental and might change in the future.

[Dialogs](https://minecraft.wiki/w/Dialog) are a feature added to Minecraft in the [1.21.6](https://minecraft.wiki/w/Java_Edition_1.21.6)
update. Paper released developer API for creating custom dialogs in 1.21.7. This section is meant
as an introduction to this API and what you can and cannot do with dialogs.

## What is a dialog?

[Section titled “What is a dialog?”](#what-is-a-dialog)

Dialogs are a way for servers to send custom in-game menus to clients. They allow for displaying various information
or provide an easy way to gather user input.

Dialogs can be shown to players during the configuration phase or normal gameplay, which makes them a very
versatile tool. A simple dialog might look like this:

![A dialog sent during the configuration phase](https://docs.papermc.io/_astro/confirmation-dialog.qlIGNgwP_WdyIc.webp)

The dialog shown here is a **confirmation**-type dialog, which just means it always contains two buttons, one meant for
confirmation and one meant for refusal.

## Showing dialogs

[Section titled “Showing dialogs”](#showing-dialogs)

Dialogs can be shown in-game using the `/dialog show <players> <dialog>` command. Alternatively, you can show them
using the API by using [Audience#showDialog(DialogLike)](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#showDialog(net.kyori.adventure.dialog.DialogLike)).
You can get built-in dialogs statically from the [`Dialog`](https://jd.papermc.io/paper/io/papermc/paper/dialog/Dialog.html) interface.
New dialogs can be created dynamically using [`Dialog#create`](https://jd.papermc.io/paper/io/papermc/paper/dialog/Dialog.html#create(java.util.function.Consumer))
or, if registered during the bootstrap phase, retrieved from the dialog registry with `RegistryAccess.registryAccess().getRegistry(RegistryKey.DIALOG).get(Key)`.

## Built-in dialogs

[Section titled “Built-in dialogs”](#built-in-dialogs)

There are three built-in dialogs:

* [Server Links](https://jd.papermc.io/paper/io/papermc/paper/registry/keys/DialogKeys.html#SERVER_LINKS)
* [Quick Actions](https://jd.papermc.io/paper/io/papermc/paper/registry/keys/DialogKeys.html#QUICK_ACTIONS)
* [Custom Options](https://jd.papermc.io/paper/io/papermc/paper/registry/keys/DialogKeys.html#CUSTOM_OPTIONS)

### Adding server links

[Section titled “Adding server links”](#adding-server-links)

You can add server links by retrieving the [`ServerLinks`](https://jd.papermc.io/paper/org/bukkit/ServerLinks.html) instance from
[`Bukkit.getServer().getServerLinks()`](https://jd.papermc.io/paper/org/bukkit/Server.html#getServerLinks()) and using the various mutation methods.
The player can open the server links menu at any time by opening the game menu (pressing `esc`) and clicking on
the `Server Links...` button. This button only appears if server links are present.

## Creating dialogs dynamically

[Section titled “Creating dialogs dynamically”](#creating-dialogs-dynamically)

You can build a [`Dialog`](https://jd.papermc.io/paper/io/papermc/paper/dialog/Dialog.html) object using the [`Dialog#create`](https://jd.papermc.io/paper/io/papermc/paper/dialog/Dialog.html#create(java.util.function.Consumer))
method. The consumer parameter allows you to build the dialog. **A dialog always requires a base and a type**, which
can be declared in the builder. You can either create a new dialog or alternatively use an existing
[registry-registered](#registering-dialogs-in-the-registry) dialog as a base instead.

For reference, a very simple (notice-type) dialog can be constructed and shown to a player with the following code:

In-game preview
![A dialog with only a title and an ok button](https://docs.papermc.io/_astro/notice-dialog.DaeSpFd2_Z2vgIol.webp)

```java
Dialog dialog = Dialog.create(builder -> builder.empty()

.base(DialogBase.builder(Component.text("Title")).build())

.type(DialogType.notice())

);

player.showDialog(dialog);
```

### Dialog base

[Section titled “Dialog base”](#dialog-base)

You can create a dialog base using its [builder](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html), which can be created
using [`DialogBase.builder(Component title)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.html#builder(net.kyori.adventure.text.Component)).
A dialog base can declare the following values:

| Builder Method | Description |
| --- | --- |
| [`afterAction(DialogAfterAction)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html#afterAction(io.papermc.paper.registry.data.dialog.DialogBase.DialogAfterAction)) | The action to take after the dialog is closed |
| [`canCloseWithEscape(boolean)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html#canCloseWithEscape(boolean)) | Whether the dialog can be closed with the `esc` key |
| [`externalTitle(Component)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html#externalTitle(net.kyori.adventure.text.Component)) | The title to display on buttons which open this dialog |
| [`body(List<? extends DialogBody>)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html#body(java.util.List)) | The body of the dialog. |
| [`inputs(List<? extends DialogInput>)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/DialogBase.Builder.html#inputs(java.util.List)) | The inputs of the dialog. |

#### Dialog body

[Section titled “Dialog body”](#dialog-body)

A dialog can contain an arbitrary number of body components. A body entry can be created using [`DialogBody.plainMessage(Component)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/body/DialogBody.html#plainMessage(net.kyori.adventure.text.Component))
for displaying text or [`DialogBody.item(ItemStack)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/body/DialogBody.html#item(org.bukkit.inventory.ItemStack))
for displaying items.

#### Dialog input

[Section titled “Dialog input”](#dialog-input)

There are four ways to gather input:

* [`DialogInput.bool`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/input/DialogInput.html#bool(java.lang.String,net.kyori.adventure.text.Component))

  A simple tick box representing a true or false state

  ![](https://docs.papermc.io/_astro/input-boolean.Cpo3o710_ZH59VB.webp)
* [`DialogInput.singleOption`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/input/DialogInput.html#singleOption(java.lang.String,net.kyori.adventure.text.Component,java.util.List))

  A multiple-choice button

  ![](https://docs.papermc.io/_astro/input-multi-options.CgHkNz2V_ZFE0MH.webp)
* [`DialogInput.text`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/input/DialogInput.html#text(java.lang.String,net.kyori.adventure.text.Component))

  A simple string input field

  ![](https://docs.papermc.io/_astro/input-text.CJMeHKdP_Zp5W5p.webp)
* [`DialogInput.numberRange`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/input/DialogInput.html#numberRange(java.lang.String,net.kyori.adventure.text.Component,float,float))

  A slider for number input

  ![](https://docs.papermc.io/_astro/input-number-range.DuG-Gl9K_ZBJsU0.webp)

### Dialog type

[Section titled “Dialog type”](#dialog-type)

The [`DialogType`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html) interface defines a few static
methods for the various dialog types. The following types exist:

| Type | Method | Description |
| --- | --- | --- |
| notice | [`notice()`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#notice()) or [`notice(ActionButton button)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#notice(io.papermc.paper.registry.data.dialog.ActionButton)) | A simple dialog with just one button |
| confirmation | [`confirmation(ActionButton yesButton, ActionButton noButton)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#confirmation(io.papermc.paper.registry.data.dialog.ActionButton,io.papermc.paper.registry.data.dialog.ActionButton)) | A dialog with a yes and no button |
| dialog list | [`dialogList(RegistrySet dialogs)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#dialogList(io.papermc.paper.registry.set.RegistrySet)) | A dialog for opening the specified dialogs |
| multiple actions | [`multiAction(List<ActionButton> actions)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#multiAction(java.util.List)) | A dialog for displaying multiple buttons |
| server links | [`serverLinks(ActionButton exitAction, int columns, int buttonWidth)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/type/DialogType.html#serverLinks(io.papermc.paper.registry.data.dialog.ActionButton,int,int)) | A server links dialog |

The type primarily influences the bottom part of the dialog.

## Registering dialogs in the registry

[Section titled “Registering dialogs in the registry”](#registering-dialogs-in-the-registry)

If you want dialogs to be registered in the dialogs registry, you must register them inside a registry modification lifecycle
event in your plugin’s bootstrapper. Some general information on that can be read [here](https://docs.papermc.io/paper/dev/registries).

Tip

The advantage of registering dialogs in the registry is that it allows you to use that same dialog
elsewhere in your code without having to pass around the `Dialog` object. This also allows the dialog
to be referenced in commands with a dialog parameter.

The general registration looks fairly similar to dynamically created dialogs:

YourPluginBootstrapper.java

```java
1

@Override

2

public void bootstrap(BootstrapContext context) {

3

context.getLifecycleManager().registerEventHandler(RegistryEvents.DIALOG.compose()

4

.newHandler(event -> event.registry().register(

5

DialogKeys.create(Key.key("papermc:custom_dialog")),

6

builder -> builder

7

// Build your dialog here ...

8

.base(DialogBase.builder(Component.text("Title")).build())

9

.type(DialogType.notice())

10

)));

11

}
```

## Closing dialogs

[Section titled “Closing dialogs”](#closing-dialogs)

Dialogs can be closed from the API. There are two ways to achieve that:

* The intended way of using [`Adventure#closeDialog()`](https://jd.advntr.dev/api/latest/net/kyori/adventure/audience/Audience.html#closeDialog()).
* The slightly hacky way of using [`Player#closeInventory()`](https://jd.papermc.io/paper/org/bukkit/entity/HumanEntity.html#closeInventory()).

Using `closeDialog()` will result in the dialog being closed and the player returning to the previous non-dialog or game menu screen they were on.
This means any previously open inventories will be kept open.

In contrast, `closeInventory()` will close not only the currently open dialog, but also any other screens, like an open inventory.

## Example: A blocking confirmation dialog

[Section titled “Example: A blocking confirmation dialog”](#example-a-blocking-confirmation-dialog)

If you want your players to read some information, agree to something, or give general input before they join your server,
you can send them a dialog during the configuration phase. For this example, we will be creating the dialog shown at
the start.

### The dialog

[Section titled “The dialog”](#the-dialog)

The dialog is a simple confirmation-type dialog with a single plain message body components. We will register it in
the bootstrapper so that we can easily retrieve it from the `AsyncPlayerConnectionConfigureEvent`, where the dialog will
be sent from.

CustomPluginBootstrapper.java

```java
1

ctx.getLifecycleManager().registerEventHandler(RegistryEvents.DIALOG.compose(),

2

e -> e.registry().register(

3

DialogKeys.create(Key.key("papermc:praise_paperchan")),

4

builder -> builder

5

.base(DialogBase.builder(Component.text("Accept our rules!", NamedTextColor.LIGHT_PURPLE))

6

.canCloseWithEscape(false)

7

.body(List.of(

8

DialogBody.plainMessage(Component.text("By joining our server you agree that Paper-chan is cute!"))

9

))

10

.build()

11

)

12

.type(DialogType.confirmation(

13

ActionButton.builder(Component.text("Paper-chan is cute!", TextColor.color(0xEDC7FF)))

14

.tooltip(Component.text("Click to agree!"))

15

.action(DialogAction.customClick(Key.key("papermc:paperchan/agree"), null))

16

.build(),

17

ActionButton.builder(Component.text("I hate Paper-chan!", TextColor.color(0xFF8B8E)))

18

.tooltip(Component.text("Click this if you are a bad person!"))

19

.action(DialogAction.customClick(Key.key("papermc:paperchan/disagree"), null))

20

.build()

21

))

22

)

23

);
```

Notice the `.action` methods on the confirmation `ActionButton`s. These hold a key and an optional, custom NBT payload
that will be sent from the client to the server when the player clicks one of the buttons. We use that to identify
the click event.

This example uses two separate keys for both keys, but you can also use only one and set a custom NBT payload.

### Requiring the player to agree before allowing them to join

[Section titled “Requiring the player to agree before allowing them to join”](#requiring-the-player-to-agree-before-allowing-them-to-join)

In order to block the player from joining the server, we send them the dialog and await a response. We do
this by constructing a `CompletableFuture`, putting it into a map, and waiting until the future gets
completed, will only happen as soon the player pressed one of the two confirmation buttons of the dialog.

The code for that would look something like this:

In-game preview[ 
Your device does not support video playback.
](/_astro/dialog-showcase.Bi4RLwPL.mp4)

ServerJoinListener.java

```java
1

@NullMarked

2

public class ServerJoinListener implements Listener {

3

4

/**

5

* A map for holding all currently connecting players.

6

*/

7

private final Map<UUID, CompletableFuture<Boolean>> awaitingResponse = new ConcurrentHashMap<>();

8

9

@EventHandler

10

void onPlayerConfigure(AsyncPlayerConnectionConfigureEvent event) {

11

Dialog dialog = RegistryAccess.registryAccess().getRegistry(RegistryKey.DIALOG).get(Key.key("papermc:praise_paperchan"));

12

if (dialog == null) {

13

// The dialog failed to load :(

14

// This would happen if the dialog could not be found in the registry by the provided key.

15

// Usually that is an indicator that the used key is different from the one used to register your

16

// dialog, your bootstrapper might not be registered, or an exception occurred in the bootstrap phase.

17

return;

18

}

19

20

PlayerConfigurationConnection connection = event.getConnection();

21

UUID uniqueId = connection.getProfile().getId();

22

if (uniqueId == null) {

23

return;

24

}

25

26

// Construct a new completable future without a task.

27

CompletableFuture<Boolean> response = new CompletableFuture<>();

28

// Complete the future if nothing has been done after one minute.

29

response.completeOnTimeout(false, 1, TimeUnit.MINUTES);

30

31

// Put it into our map.

32

awaitingResponse.put(uniqueId, response);

33

34

Audience audience = connection.getAudience();

35

// Show the connecting player the dialog.

36

audience.showDialog(dialog);

37

38

// Wait until the future is complete. This step is necessary in order to keep the player in the configuration phase.

39

if (!response.join()) {

40

// We close the dialog manually because the client might not do it on its own.

41

audience.closeDialog();

42

// If the response is false, they declined. Therefore, we kick them from the server.

43

connection.disconnect(Component.text("You hate Paper-chan :(", NamedTextColor.RED));

44

}

45

46

// We clean the map to avoid unnecessary entry buildup.

47

awaitingResponse.remove(uniqueId);

48

}

49

50

/**

51

* An event for handling dialog button click events.

52

*/

53

@EventHandler

54

void onHandleDialog(PlayerCustomClickEvent event) {

55

// Handle custom click only for configuration connection.

56

if (!(event.getCommonConnection() instanceof PlayerConfigurationConnection configurationConnection)) {

57

return;

58

}

59

60

UUID uniqueId = configurationConnection.getProfile().getId();

61

if (uniqueId == null) {

62

return;

63

}

64

65

Key key = event.getIdentifier();

66

if (key.equals(Key.key("papermc:paperchan/disagree"))) {

67

// If the identifier is the same as the disagree one, set the connection result to false.

68

setConnectionJoinResult(uniqueId, false);

69

} else if (key.equals(Key.key("papermc:paperchan/agree"))) {

70

// If it is the same as the agree one, set the result to true.

71

setConnectionJoinResult(uniqueId, true);

72

}

73

}

74

75

/**

76

* An event handler for cleanup the map to avoid unnecessary entry buildup.

77

*/

78

@EventHandler

79

void onConnectionClose(PlayerConnectionCloseEvent event) {

80

awaitingResponse.remove(event.getPlayerUniqueId());

81

}

82

83

/**

84

* Simple utility method for setting a connection's dialog response result.

85

*/

86

private void setConnectionJoinResult(UUID uniqueId, boolean value) {

87

CompletableFuture<Boolean> future = awaitingResponse.get(uniqueId);

88

if (future != null) {

89

future.complete(value);

90

}

91

}

92

}
```

And that’s all there is to it. You can use this code to block players from joining your server before they should
be allowed to.

## Example: Retrieving and parsing user input

[Section titled “Example: Retrieving and parsing user input”](#example-retrieving-and-parsing-user-input)

The dialog for this example will be fairly simple: We once again create a confirmation-type dialog which contains two number range inputs.
The top input will be for setting the level, the bottom input for setting the experience percentage towards the next level.
When the player clicks on the confirmation button, they should have their levels and exp set to the configured values.

```java
1

Dialog.create(builder -> builder.empty()

2

.base(DialogBase.builder(Component.text("Configure your new experience value"))

3

.inputs(List.of(

4

DialogInput.numberRange("level", Component.text("Level", NamedTextColor.GREEN), 0f, 100f)

5

.step(1f)

6

.initial(0f)

7

.width(300)

8

.build(),

9

DialogInput.numberRange("experience", Component.text("Experience", NamedTextColor.GREEN), 0f, 100f)

10

.step(1f)

11

.initial(0f)

12

.labelFormat("%s: %s percent to the next level")

13

.width(300)

14

.build()

15

))

16

.build()

17

)

18

.type(DialogType.confirmation(

19

ActionButton.create(

20

Component.text("Confirm", TextColor.color(0xAEFFC1)),

21

Component.text("Click to confirm your input."),

22

100,

23

DialogAction.customClick(Key.key("papermc:user_input/confirm"), null)

24

),

25

ActionButton.create(

26

Component.text("Discard", TextColor.color(0xFFA0B1)),

27

Component.text("Click to discard your input."),

28

100,

29

null // If we set the action to null, it doesn't do anything and closes the dialog

30

)

31

))

32

);
```

### Reading the input

[Section titled “Reading the input”](#reading-the-input)

To retrieve the values the user put into the dialog, we can once again listen to a `PlayerCustomClickEvent`.
We first check the identifier of the action. After that, we can retrieve the input values from the
[`DialogResponseView`](https://jd.papermc.io/paper/io/papermc/paper/dialog/DialogResponseView.html) retrievable from
[`PlayerCustomClickEvent#getDialogResponseView()`](https://jd.papermc.io/paper/io/papermc/paper/event/player/PlayerCustomClickEvent.html#getDialogResponseView()).

This view allows us to retrieve the value of an input field with the field’s key. Those are declared as the first
parameter of the `DialogInput.numberRange` method.

The last issue is getting a player object from this event. We cannot just call `event.getPlayer()`. Instead, we have
to cast the connection retrievable from [`PlayerCustomClickEvent#getCommonConnection()`](https://jd.papermc.io/paper/io/papermc/paper/event/player/PlayerCustomClickEvent.html#getCommonConnection()).
to a [`PlayerGameConnection`](https://jd.papermc.io/paper/io/papermc/paper/connection/PlayerGameConnection.html), from which we can get the player.

The full event handler code looks like this:

In-game preview[ 
Your device does not support video playback.
](/_astro/input-dialog-showcase.DqwuoQW7.mp4)

```java
@EventHandler

void handleLevelsDialog(PlayerCustomClickEvent event) {

if (!event.getIdentifier().equals(Key.key("papermc:user_input/confirm"))) {

return;

}

DialogResponseView view = event.getDialogResponseView();

if (view == null) {

return;

}

int levels = view.getFloat("level").intValue();

float exp = view.getFloat("experience").floatValue();

if (event.getCommonConnection() instanceof PlayerGameConnection conn) {

Player player = conn.getPlayer();

player.sendRichMessage("You selected <color:#ccfffd><level> levels</color> and <color:#ccfffd><exp>% exp</color> to the next level!",

Placeholder.component("level", Component.text(levels)),

Placeholder.component("exp", Component.text(exp))

);

player.setLevel(levels);

player.setExp(exp / 100);

}

}
```

### Using callbacks

[Section titled “Using callbacks”](#using-callbacks)

Instead of registering another event handler, you can instead use the
[`DialogAction.customClick(DialogActionCallback, ClickCallback.Options)`](https://jd.papermc.io/paper/io/papermc/paper/registry/data/dialog/action/DialogAction.html#customClick(io.papermc.paper.registry.data.dialog.action.DialogActionCallback,net.kyori.adventure.text.event.ClickCallback.Options))
method to register a callback locally.

The code for the dialog action would therefore look like this:

```java
1

DialogAction.customClick(

2

(view, audience) -> {

3

int levels = view.getFloat("level").intValue();

4

float exp = view.getFloat("experience").floatValue();

5

6

if (audience instanceof Player player) {

7

player.sendRichMessage("You selected <color:#ccfffd><level> levels</color> and <color:#ccfffd><exp>% exp</color> to the next level!",

8

Placeholder.component("level", Component.text(levels)),

9

Placeholder.component("exp", Component.text(exp))

10

);

11

12

player.setLevel(levels);

13

player.setExp(exp / 100);

14

}

15

},

16

ClickCallback.Options.builder()

17

.uses(1) // Set the number of uses for this callback. Defaults to 1

18

.lifetime(ClickCallback.DEFAULT_LIFETIME) // Set the lifetime of the callback. Defaults to 12 hours

19

.build()

20

)
```


================================================================================
Chapter Title: Recipes
Original Link: https://docs.papermc.io/paper/dev/recipes/
================================================================================

Recipes are a way to define a way to craft a particular item. They are defined by a plugin or
datapack, however we are only going to cover the plugin side of things here.

## [`ShapedRecipe`](https://jd.papermc.io/paper/org/bukkit/inventory/ShapedRecipe.html)

[Section titled “ShapedRecipe”](#shapedrecipe)

A shaped recipe is a recipe that requires a specific pattern of items in the crafting grid to craft an item.
These are created using a pattern string and a map of characters to items. The pattern strings are 3,
3-character strings that represent the rows of the crafting grid. They can be created as follows:

TestPlugin.java

```java
public class TestPlugin extends JavaPlugin {

@Override

public void onEnable() {

NamespacedKey key = new NamespacedKey(this, "television");

ItemStack item = ItemStack.of(Material.BLACK_WOOL);

item.setData(DataComponentTypes.ITEM_NAME, Component.text("Television"));

ShapedRecipe recipe = new ShapedRecipe(key, item);

recipe.shape("AAA", "ABA", "AAA");

recipe.setIngredient('A', Material.WHITE_CONCRETE);

recipe.setIngredient('B', Material.BLACK_STAINED_GLASS_PANE);

getServer().addRecipe(recipe);

}

}
```

This recipe would require a television to be crafted with one black stained glass pane surrounded
by white concrete. The result would look like this in the crafting grid:

```java
AAA

ABA

AAA
```

Note

You do not need to register the recipe within your plugin’s `onEnable` method, You can register it
at any time. However, if you do not register it after the plugin has been enabled and there are
players online, you will need to either resend all the recipes to the players or use the boolean
parameter in the [`addRecipe`](https://jd.papermc.io/paper/org/bukkit/Server.html#addRecipe(org.bukkit.inventory.Recipe,boolean))
method to update all players with the new recipe.

Caution

You cannot use Air as a material in a shaped recipe, this will cause an error.

## [`ShapelessRecipe`](https://jd.papermc.io/paper/org/bukkit/inventory/ShapelessRecipe.html)

[Section titled “ShapelessRecipe”](#shapelessrecipe)

A shapeless recipe is a recipe that requires a specific number of items in the crafting grid to craft an item.
These are created using a list of items. They can be created as follows:

TestPlugin.java

```java
public class TestPlugin extends JavaPlugin {

@Override

public void onEnable() {

NamespacedKey key = new NamespacedKey(this, "WarriorSword");

ItemStack item = ItemStack.of(Material.DIAMOND_SWORD);

ShapelessRecipe recipe = new ShapelessRecipe(key, item);

recipe.addIngredient(3, Material.DIAMOND);

recipe.addIngredient(2, Material.STICK);

getServer().addRecipe(recipe);

}

}
```

This recipe declares that you simply need 3 diamonds and 2 sticks to craft the item, without any specific
orientation of the cross pattern in the crafting grid. This could be crafted in any of the following ways:

```java
DSS   |   SDS   |   S D

D     |   D     |   D

D     |   D     |   D S
```

And, any other composition of the 5 items.


================================================================================
Chapter Title: Particles
Original Link: https://docs.papermc.io/paper/dev/particles/
================================================================================

This guide explains how to spawn different types of particles.

If the particle you’re trying to spawn isn’t mentioned in this guide, then it most likely has no special behavior.

There are two ways to spawn particles.
The first option is using the [`ParticleBuilder`](https://jd.papermc.io/paper/com/destroystokyo/paper/ParticleBuilder.html) class, which is
preferred over the `spawnParticle()` methods. It is reusable and offers improved readability and clarity. The builder also includes
the method [`receivers()`](https://jd.papermc.io/paper/com/destroystokyo/paper/ParticleBuilder.html#receivers()), which provides you
with greater control over receivers.

An example of spawning 14 note particles in a 4x0.4x4 cuboid:

```java
Particle.NOTE.builder()

.location(someLocation)

.offset(2, 0.2, 2)

.count(14)

.receivers(32, true)

.spawn();
```

Note

The use of [`ParticleBuilder.receivers(32, true)`](https://jd.papermc.io/paper/com/destroystokyo/paper/ParticleBuilder.html#receivers(int,boolean))
select all players in a distance of 32 blocks from the particle’s location,
resulting in a sphere shape. Setting the boolean parameter to `false` would select all players in a cube.

The second way is using the `spawnParticle()` methods in `World` and `Player` classes:

* [`World.spawnParticle()`](https://jd.papermc.io/paper/org/bukkit/World.html#spawnParticle(org.bukkit.Particle,double,double,double,int)) which spawns the particle for all players and
* [`Player.spawnParticle()`](https://jd.papermc.io/paper/org/bukkit/entity/Player.html#spawnParticle(org.bukkit.Particle,double,double,double,int)) which spawns the particle only for the player.

## `count` argument behavior Important

[Section titled “count argument behavior ”](#count-argument-behavior)

When spawning particles, the Minecraft client behaves differently based on the `count` argument:

* If `count = 0`, a singular particle spawns and the client uses the provided location without modification.
  The offset values are multiplied by the `extra` argument and passed to the particle constructor. The way these values are
  used may vary between particle types.
* If `count > 0`, the client spawns `count` number of particles. For each particle, it generates new offset
  values using a Gaussian (normal) distribution, multiplies them by the `extra` argument, and passes
  them to the particle constructor.

## Directional particles

[Section titled “Directional particles”](#directional-particles)

This type of particle has an initial velocity when spawned.

Note

Effective speed varies between particles.

In the following example 8 `FLAME` particles are spawned in a 1x1x1 cube shape randomly. `someLocation` serves as its center.
The `extra` argument is set to 0, so the particles don’t move.

* [ParticleBuilder](#tab-panel-39)
* [spawnParticle](#tab-panel-40)

```java
Particle.FLAME.builder()

.location(someLocation)

.offset(0.5, 0.5, 0.5)

.count(8)

.extra(0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.FLAME, someLocation, 8, 0.5, 0.5, 0.5, 0);
```

  

Caution

Leaving the `extra` parameter unset will default it to `1`, likely resulting in unexpected behavior.

### Random direction

[Section titled “Random direction”](#random-direction)

Setting the `count` parameter to anything positive will yield a random direction for the velocity as described in
[`count` argument behavior](#count-argument-behavior).

An example of spawning 6 `CRIT` particles at a location, without offset, that will move in a random direction at a moderate speed:

* [ParticleBuilder](#tab-panel-41)
* [spawnParticle](#tab-panel-42)

```java
Particle.CRIT.builder()

.location(someLocation)

.count(6)

.extra(0.6)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.CRIT, someLocation, 6, 0, 0, 0, 0.6);
```

 

![Crit particles going in random directions](https://docs.papermc.io/_astro/random-direction-crit.v2ZiLlgQ_wrIlv.webp)

### Specified direction

[Section titled “Specified direction”](#specified-direction)

To specify the velocity’s direction, set the `count` argument to `0` and use the offset arguments as the direction vector.
See [`count` argument behavior](#count-argument-behavior) for more details.

An example of a repeating task spawning campfire smoke that slowly goes “up” (positive Y axis):

* [ParticleBuilder](#tab-panel-43)
* [spawnParticle](#tab-panel-44)

```java
ParticleBuilder particleBuilder = Particle.CAMPFIRE_SIGNAL_SMOKE.builder()

.location(someLocation)

.offset(0, 1, 0)

.count(0)

.extra(0.1);

Bukkit.getScheduler().runTaskTimer(plugin,

() -> particleBuilder.receivers(32, true).spawn(),

0, 4);
```

```java
Bukkit.getScheduler().runTaskTimer(plugin,

() -> someWorld.spawnParticle(Particle.CAMPFIRE_SIGNAL_SMOKE, someLocation, 0, 0, 1, 0, 0.1),

0, 4);
```

 

![Campfire signal smoke going up](https://docs.papermc.io/_astro/smoke-going-up.Dc_KEGOA_ZtnOkH.webp)

We could also make the smoke go down if we wanted to:

* [ParticleBuilder](#tab-panel-45)
* [spawnParticle](#tab-panel-46)

```java
ParticleBuilder particleBuilder = Particle.CAMPFIRE_SIGNAL_SMOKE.builder()

.location(someLocation)

.offset(0, -1, 0)

.count(0)

.extra(0.1);

Bukkit.getScheduler().runTaskTimer(plugin,

() -> particleBuilder.receivers(32, true).spawn(),

0, 4);
```

```java
Bukkit.getScheduler().runTaskTimer(plugin,

() -> someWorld.spawnParticle(Particle.CAMPFIRE_SIGNAL_SMOKE, someLocation, 0, 0, -1, 0, 0.1),

0, 4);
```

 

### List of directional particles

[Section titled “List of directional particles”](#list-of-directional-particles)

Show list

* BLOCK
* BUBBLE
* BUBBLE\_COLUMN\_UP
* BUBBLE\_POP
* CAMPFIRE\_COSY\_SMOKE
* CAMPFIRE\_SIGNAL\_SMOKE
* CLOUD
* CRIT
* DAMAGE\_INDICATOR
* DRAGON\_BREATH
* DUST
* DUST\_COLOR\_TRANSITION
* DUST\_PLUME
* ELECTRIC\_SPARK
* ENCHANTED\_HIT
* END\_ROD
* FIREWORK
* FISHING
* FLAME
* FLASH
* GLOW\_SQUID\_INK
* ITEM
* LARGE\_SMOKE
* POOF
* REVERSE\_PORTAL
* SCRAPE
* SCULK\_CHARGE
* SCULK\_CHARGE\_POP
* SCULK\_SOUL
* SMALL\_FLAME
* SMOKE
* SNEEZE
* SNOWFLAKE
* SOUL
* SOUL\_FIRE\_FLAME
* SPIT
* SQUID\_INK
* TOTEM\_OF\_UNDYING
* TRIAL\_SPAWNER\_DETECTION
* TRIAL\_SPAWNER\_DETECTION\_OMINOUS
* WAX\_OFF
* WAX\_ON
* WHITE\_SMOKE

## Colored particles

[Section titled “Colored particles”](#colored-particles)

These particles can be colored by passing a [`Color`](https://jd.papermc.io/paper/org/bukkit/Color.html) object as the `data` argument.

Example of spawning 10 potion effect particles in a 2x2x2 area with a slightly translucent orange color:

* [ParticleBuilder](#tab-panel-47)
* [spawnParticle](#tab-panel-48)

```java
Particle.ENTITY_EFFECT.builder()

.location(someLocation)

.offset(1, 1, 1)

.count(10)

.data(Color.fromARGB(200, 255, 128, 0))

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.ENTITY_EFFECT, someLocation, 10, 1, 1, 1, Color.fromARGB(200, 255, 128, 0));
```

 

![Colored potion effect particles](https://docs.papermc.io/_astro/orange-spell-particles.CI9ISSWI_1AakMk.webp)

Note

Only the `ENTITY_EFFECT` particle supports the alpha channel, which is used to create translucent particles.

Caution

While `FLASH` and `TINTED_LEAVES` particles take an ARGB color, the alpha channel is ignored.

### Dust particles

[Section titled “Dust particles”](#dust-particles)

Vanilla uses the dust particle for redstone particles. They can have a custom color by passing
[Particle.DustOptions](https://jd.papermc.io/paper/org/bukkit/Particle.DustOptions.html) as `data`.

Note

The scale factor must be in the range of `0.01` to `4.0`. Values outside this range will be clamped to the nearest valid value.

An example of creating a vertical line of blue dust particles, that are two times the regular size:

* [ParticleBuilder](#tab-panel-49)
* [spawnParticle](#tab-panel-50)

```java
ParticleBuilder particleBuilder = Particle.DUST.builder()

.color(Color.BLUE, 2.0f);

// We can reuse the builder

for (double i = -1.0; i <= 1.0; i += 0.25) {

particleBuilder.location(someLocation.clone().add(0, i, 0)).receivers(32, true).spawn();

}
```

```java
for (double i = -1.0; i <= 1.0; i += 0.25) {

someWorld.spawnParticle(

Particle.DUST,

someLocation.clone().add(0, i, 0),

1,

new Particle.DustOptions(Color.BLUE, 2.0f)

);

}
```

 

![Blue dust particles in a vertical line](https://docs.papermc.io/_astro/blue-dust-particles-in-line.C6ZDFGxY_Z1e2R03.webp)

Note

Here, adding a size argument would control the dust particle’s lifetime, in ticks. By default, the value is a random
integer between 8 and 40, which is multiplied by the particle’s scale, to get the final lifetime (with a minimum of 1).

#### Dust transition particles

[Section titled “Dust transition particles”](#dust-transition-particles)

Dust transition particles work exactly like [dust particles](#dust-particles), but instead of having a static color, they **transition**
their color from one to another. A [Particle.DustTransition](https://jd.papermc.io/paper/org/bukkit/Particle.DustTransition.html) is used for
specifying the transition.

An example where three dust transition particles spawn on the x-axis within a 1-block length:

* [ParticleBuilder](#tab-panel-51)
* [spawnParticle](#tab-panel-52)

```java
Particle.DUST_COLOR_TRANSITION.builder()

.location(someLocation)

.offset(0.5, 0, 0)

.count(3)

.colorTransition(Color.RED, Color.BLUE)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(

Particle.DUST_COLOR_TRANSITION,

someLocation,

3,

0.5, 0, 0,

new Particle.DustTransition(Color.RED, Color.BLUE, 1.0f)

);
```

 

![Dust transition particles in a line](https://docs.papermc.io/_astro/dust-transition-particles.WjyCcjPJ_1e17OR.webp)

### Note particles

[Section titled “Note particles”](#note-particles)

The note particles will use the `offsetX` argument in a custom function to determine the color,
see [Note particle color picker](#note-particle-color-picker) for more details. `offsetY` and `offsetZ` are ignored in this case.

Example:

* [ParticleBuilder](#tab-panel-53)
* [spawnParticle](#tab-panel-54)

```java
Particle.NOTE.builder()

.location(someLocation)

.offset(0.4f, 0, 0)

.count(0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.NOTE, someLocation, 0, 0.4f, 0, 0);
```

 

![Note particle](https://docs.papermc.io/_astro/note-particle.CcQH9Bz1_Z1SknWi.webp)

#### Note particle color picker

[Section titled “Note particle color picker”](#note-particle-color-picker)

This tool allows you to pick a color for the note particle by adjusting the `offsetX` value. It only allows you to
choose `offsetX` values between `-1.0` and `1.0`; values outside this range will repeat the color pattern.

![Note particle](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAQAAABuBnYAAAAALElEQVR42mOAgc3/J/0H0UgCGahCm4GcQGQBiCzRAp//A41EFsj4H/gfZiAAXXUYtS3tm1IAAAAASUVORK5CYII=)  

offsetX = 0

Tip

To achieve the Vanilla note particle colors you must set the offsetX to a fraction of 24.

Example:

* [ParticleBuilder](#tab-panel-55)
* [spawnParticle](#tab-panel-56)

```java
Particle.NOTE.builder()

.location(someLocation)

.offset(2.0f/24.0f, 0, 0)

.count(0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.NOTE, someLocation, 0, 2.0f/24.0f, 0, 0);
```

### Trail particles

[Section titled “Trail particles”](#trail-particles)

Trail particles require you to pass a [`Particle.Trail`](https://jd.papermc.io/paper/org/bukkit/Particle.Trail.html) object as `data`.

An example where eight randomly offset trail particles travel towards a specified location
(`someLocation.clone().add(-4, 0, 4)`) with a yellow color and a travel time of 40 ticks:

* [ParticleBuilder](#tab-panel-57)
* [spawnParticle](#tab-panel-58)

```java
Particle.TRAIL.builder()

.location(someLocation)

.offset(1, 1, 1)

.count(8)

.data(new Particle.Trail(someLocation.clone().add(-4, 0, 4), Color.YELLOW, 40))

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(

Particle.TRAIL,

someLocation,

8,

1, 1, 1,

new Particle.Trail(someLocation.clone().add(-4, 0, 4), Color.YELLOW, 40)

);
```

 

![Yellow trail particles floating towards the right side of the screen](https://docs.papermc.io/_astro/trail-particles.B0CRsMRO_2fF4wk.webp)

## Converging particles

[Section titled “Converging particles”](#converging-particles)

As the name implies, this type of particle converges to a single point (location), which in this case is the supplied location.
Offset arguments are used to determine the relative spawn location of the particle.
The particle will then travel from this relative location to the supplied location.

An example where an enchantment particle will spawn at `someLocation.clone().add(-2, 0, 2)` and travel to `someLocation`:

* [ParticleBuilder](#tab-panel-59)
* [spawnParticle](#tab-panel-60)

```java
Particle.ENCHANT.builder()

.location(someLocation)

.offset(-2, 0, 2)

.count(0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.ENCHANT, someLocation, 0, -2, 0, 2);
```

 

![Enchant particle going towards the center of the screen](https://docs.papermc.io/_astro/converging-enchant-particle.C3ZWc8Zd_5uMRR.webp)

Note

There are two types of converging particles:

* **Curving**: Particles that follow a curved path to the specified location.
* **Straight**: Particles that move in a straight line to the specified location.

The `ENCHANT`, `NAUTILUS`, `PORTAL` and `VAULT_CONNECTION` particles use curved paths, while the `OMINOUS_SPAWNING` particle
travels in a straight line.

### List of converging particles

[Section titled “List of converging particles”](#list-of-converging-particles)

Show list

* ENCHANT
* NAUTILUS
* OMINOUS\_SPAWNING
* PORTAL
* VAULT\_CONNECTION

## Material particles

[Section titled “Material particles”](#material-particles)

### BlockData

[Section titled “BlockData”](#blockdata)

To spawn particles that require `BlockData`, simply put `BlockData` as its `data` argument.

Example:

* [ParticleBuilder](#tab-panel-61)
* [spawnParticle](#tab-panel-62)

```java
Particle.BLOCK_CRUMBLE.builder()

.location(someLocation)

.count(4)

.data(BlockType.GLOWSTONE.createBlockData())

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.BLOCK_CRUMBLE, someLocation, 4, BlockType.GLOWSTONE.createBlockData());
```

 

Note

This guide uses [`BlockType.createBlockData()`](https://jd.papermc.io/paper/org/bukkit/block/BlockType.html#createBlockData()). While using
[`Material.createBlockData()`](https://jd.papermc.io/paper/org/bukkit/Material.html#createBlockData()) or
[`Bukkit.createBlockData(Material)`](https://jd.papermc.io/paper/org/bukkit/Bukkit.html#createBlockData(org.bukkit.Material)) yields the same result,
they are considered **legacy**.

Tip

The `BLOCK` particle is a [directional particle](#directional-particles).

In this case, **velocity matters** a lot. A higher velocity will ensure the same general direction of the particle, while a lower one will
result in a more random direction.

To achieve this, the effective velocity vector’s length should be high (around 10 is fine).

### ItemStack

[Section titled “ItemStack”](#itemstack)

To spawn particles that require an `ItemStack`, simply put an `ItemStack` as its `data` argument.

Example:

* [ParticleBuilder](#tab-panel-63)
* [spawnParticle](#tab-panel-64)

```java
Particle.ITEM.builder()

.location(someLocation)

.count(4)

.data(ItemStack.of(Material.DIAMOND_PICKAXE))

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.ITEM, someLocation, 4, ItemStack.of(Material.DIAMOND_PICKAXE));
```

 

Note

This guide uses [`ItemStack.of(Material)`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#of(org.bukkit.Material)). While using
[`new ItemStack(Material)`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html) yields the same result,
it is considered **legacy**. [`ItemType.createItemStack()`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemType.html#createItemStack())
also yields the same result, but is more likely to get removed in the future.

Tip

The `ITEM` particle is a [directional particle](#directional-particles).

## Sculk particles

[Section titled “Sculk particles”](#sculk-particles)

### Sculk charge

[Section titled “Sculk charge”](#sculk-charge)

The `SCULK_CHARGE` particle takes a `float` as its `data` argument. This is used as the particle’s “roll.” Or, more formally,
the angle the particle displays at in **radians**.

Example of spawning a sculk charge particle at 45° that doesn’t move:

* [ParticleBuilder](#tab-panel-65)
* [spawnParticle](#tab-panel-66)

```java
Particle.SCULK_CHARGE.builder()

.location(someLocation)

.data((float) Math.toRadians(45))

.extra(0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.SCULK_CHARGE, someLocation, 1, 0, 0, 0, 0, (float) Math.toRadians(45));
```

 

![Sculk charge particle at 45°](https://docs.papermc.io/_astro/sculk-charge.DhF0cvGv_1KTF9H.webp)

Tip

The `SCULK_CHARGE` particle is a [directional particle](#directional-particles).

### Shriek

[Section titled “Shriek”](#shriek)

The `SHRIEK` particle takes an `integer` as its `data` argument. This is used to set the delay **in ticks** before the particle spawns.

It is completely up to your implementation when choosing to use `data` or a scheduler.

Example where a shriek particle will spawn after one second:

* [ParticleBuilder](#tab-panel-67)
* [spawnParticle](#tab-panel-68)

```java
Particle.SHRIEK.builder()

.location(someLocation)

.data(20)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.SHRIEK, someLocation, 1, 20);
```

 

![Shriek particle](https://docs.papermc.io/_astro/shriek.rOQSE48g_ZfuPhI.webp)

### Vibration

[Section titled “Vibration”](#vibration)

Vibration particles require you to pass a [`Vibration`](https://jd.papermc.io/paper/org/bukkit/Vibration.html) object as `data`, where you can choose between a
location ([`Vibration.Destination.BlockDestination`](https://jd.papermc.io/paper/org/bukkit/Vibration.Destination.BlockDestination.html))
or an entity target ([`Vibration.Destination.EntityDestination`](https://jd.papermc.io/paper/org/bukkit/Vibration.Destination.EntityDestination.html)).
The constructor’s second argument is the travel time in **ticks**.

An example where a vibration particle will spawn at `someLocation` and travel to `otherLocation` in 40 ticks:

* [ParticleBuilder](#tab-panel-69)
* [spawnParticle](#tab-panel-70)

```java
Particle.VIBRATION.builder()

.location(someLocation)

.data(new Vibration(new Vibration.Destination.BlockDestination(otherLocation), 40))

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(

Particle.VIBRATION,

someLocation,

1,

new Vibration(new Vibration.Destination.BlockDestination(otherLocation), 40)

);
```

 

![Vibration particle going to the left side of the screen](https://docs.papermc.io/_astro/vibration.CMBu2C4q_Z1Rfqh3.webp)

## Rising particles

[Section titled “Rising particles”](#rising-particles)

These particles will use `offsetY` as the particle’s y-axis velocity.

If you set `offsetX` AND `offsetZ` to `0`, the particle will have almost no x or z-axis velocity, but will still have
a y-axis velocity set by the `offsetY` argument. In both cases, `offsetX` and `offsetZ` are not used in the velocity vector.

Caution

`EFFECT` and `INSTANT_EFFECT` are [powered particles](#powered-particles) and use [`Particle.Spell`](https://jd.papermc.io/paper/org/bukkit/Particle.Spell.html)
as their data. Due to the nature of rising particles’ final calculated vertical velocity being very low (in range [-0.056, 0.056])
and how powered particles calculate the vertical velocity, the resulting vertical velocity will always be the opposite of
`power` value’s sign.

Example of spawning a `GLOW` particle that moves up:

* [ParticleBuilder](#tab-panel-71)
* [spawnParticle](#tab-panel-72)

```java
Particle.GLOW.builder()

.location(someLocation)

.count(0)

.offset(0, 2, 0)

.receivers(32, true)

.spawn();
```

```java
someWorld.spawnParticle(Particle.GLOW, someLocation, 0, 0, 2, 0);
```

 

![Glow particle going up](https://docs.papermc.io/_astro/rising-glow-particle.QaTGa-06_ZTgW0J.webp)

Note

These particles rise up, meaning that the initial velocity will be used only briefly, and the particle will
start to travel up after a short time. Therefore, negative vertical velocity will only stop the particle from rising temporarily,
while a positive vertical velocity will make the particle rise immediately.

### List of rising particles

[Section titled “List of rising particles”](#list-of-rising-particles)

Show list

* EFFECT
* ENTITY\_EFFECT
* GLOW
* INFESTED
* INSTANT\_EFFECT
* RAID\_OMEN
* TRIAL\_OMEN
* WITCH

## Scalable particles

[Section titled “Scalable particles”](#scalable-particles)

These particles can be scaled with `offsetX`, while `offsetY` and `offsetZ` are ignored. This chapter does not include dust particles,
those particles are covered in [Dust particles](#dust-particles) and [Dust transition particles](#dust-transition-particles) chapters.

Note

If the final calculated scale is negative, the particle will appear mirrored.

### Sweep attack particles

[Section titled “Sweep attack particles”](#sweep-attack-particles)

The `SWEEP_ATTACK` particle’s scale is calculated as `1.0 - offsetX * 0.5`.

An example where two sweep attack particles will spawn at `someLocation`. First one with a scale of `1.0` and the second
one with a scale of `2.0` right after:

* [ParticleBuilder](#tab-panel-73)
* [spawnParticle](#tab-panel-74)

```java
ParticleBuilder sweepAttackParticleBuilder = Particle.SWEEP_ATTACK.builder()

.location(someLocation)

.count(0)

.receivers(32, true)

.spawn();

Bukkit.getScheduler().runTaskLater(plugin,

() -> sweepAttackParticleBuilder.offset(-2.0, 0, 0).spawn(), 10);
```

```java
someWorld.spawnParticle(Particle.SWEEP_ATTACK, someLocation, 0);

Bukkit.getScheduler().runTaskLater(plugin,

() -> someWorld.spawnParticle(Particle.SWEEP_ATTACK, someLocation, 0, -2.0, 0, 0), 10);
```

 

![Sweep attack particle scale comparison](https://docs.papermc.io/_astro/sweep-attack.DBDkSQHB_2eM5sv.webp)

### Explosion particles

[Section titled “Explosion particles”](#explosion-particles)

The `EXPLOSION` particle’s scale is calculated as `2.0 * (1.0 - offsetX * 0.5)`.

An example where two explosion particles will spawn at `someLocation`. First one with a scale of `1.0` and the second
one with a scale of `4.0` right after:

* [ParticleBuilder](#tab-panel-75)
* [spawnParticle](#tab-panel-76)

```java
ParticleBuilder explosionParticleBuilder = Particle.EXPLOSION.builder()

.location(someLocation)

.offset(1, 0, 0)

.count(0)

.receivers(32, true)

.spawn();

Bukkit.getScheduler().runTaskLater(plugin,

() -> explosionParticleBuilder.offset(-2.0, 0, 0).spawn(), 10);
```

```java
someWorld.spawnParticle(Particle.EXPLOSION, someLocation, 0, 1, 0, 0);

Bukkit.getScheduler().runTaskLater(plugin,

() -> someWorld.spawnParticle(Particle.EXPLOSION, someLocation, 0, -2.0, 0, 0), 10);
```

 

![Explosion particle scale comparison](https://docs.papermc.io/_astro/explosion.tBoNBCF__26jkHM.webp)

## Miscellaneous behaviors

[Section titled “Miscellaneous behaviors”](#miscellaneous-behaviors)

This chapter covers particles that have unique behaviors when spawning.

### Angry villager particles

[Section titled “Angry villager particles”](#angry-villager-particles)

The `ANGRY_VILLAGER` particle always spawns `0.5` higher (y-axis) than the supplied location.

### Cloud particles

[Section titled “Cloud particles”](#cloud-particles)

The `CLOUD` and `SNEEZE` particles move towards the player’s y level, if they are within two blocks distance from the player’s
location. When they reach the player’s y level, their vertical velocity will be greatly reduced.

If the player is moving vertically, the particles will attempt to match the player’s vertical velocity.

### Damage indicator particles

[Section titled “Damage indicator particles”](#damage-indicator-particles)

The `DAMAGE_INDICATOR` particle adds `1.0` to the provided `offsetY`.

### Dust pillar particles

[Section titled “Dust pillar particles”](#dust-pillar-particles)

The `DUST_PILLAR` particle uses `offsetY` for the y-axis velocity, while `offsetX` and `offsetZ` are ignored.

### Dust plume particles

[Section titled “Dust plume particles”](#dust-plume-particles)

The `DUST_PLUME` particle adds `0.15` to the provided `offsetY`.

### Firefly particles

[Section titled “Firefly particles”](#firefly-particles)

The `FIREFLY` particle uses `offsetY` as the particle’s initial y-axis velocity, however, there is 50% chance for the `offsetY`’s
sign to be inverted. This means that the particle will either move up or down, with equal probability.

### Powered particles

[Section titled “Powered particles”](#powered-particles)

The powered particles multiply the particle’s velocity vector by the supplied argument.

Note

The y component of the vector is calculated as `(verticalVelocity - 0.1) * power + 0.1`.

#### List of powered particles

[Section titled “List of powered particles”](#list-of-powered-particles)

* EFFECT
* INSTANT\_EFFECT
* DRAGON\_BREATH

### Splash particles

[Section titled “Splash particles”](#splash-particles)

The `SPLASH` particle uses the `offsetX` and `offsetZ` arguments to determine the particle’s velocity vector, if two conditions are met:

1. `offsetY` is `0`
2. Either `offsetX` or `offsetZ` are not `0`


================================================================================
Chapter Title: Supporting Paper and Folia
Original Link: https://docs.papermc.io/paper/dev/folia-support/
================================================================================

![](https://docs.papermc.io/_astro/folia_2lIm0P.webp)

[Folia](https://github.com/PaperMC/Folia) is a fork of Paper, which is currently maintained by the PaperMC team.
It adds the ability to split the world into regions as outlined [here](https://docs.papermc.io/folia/reference/overview) in more depth.

# Checking for Folia

[Section titled “Checking for Folia”](#checking-for-folia)

Depending on what platform your plugin is running on, you may need to implement features differently. For this, you can
use this utility method to check if the current server is running Folia:

```java
private static boolean isFolia() {

try {

Class.forName("io.papermc.paper.threadedregions.RegionizedServer");

return true;

} catch (ClassNotFoundException e) {

return false;

}

}
```

## Schedulers

[Section titled “Schedulers”](#schedulers)

In order to support Paper and Folia, you must use the correct scheduler. Folia has different types of schedulers
that can be used for different things. They are:

* [Global](#global-scheduler)
* [Region](#region-scheduler)
* [Async](#async-scheduler)
* [Entity](#entity-scheduler)

If you use these schedulers when running Paper, they will be internally handled to provide the same functionality as if you were
running Folia.

### Global scheduler

[Section titled “Global scheduler”](#global-scheduler)

The tasks that you run on the global scheduler will be executed on the global region, see [here](https://docs.papermc.io/folia/reference/overview#global-region) for
more information. You should use this scheduler for any tasks that do not belong to any particular region. These can be fetched with:

```java
GlobalRegionScheduler globalScheduler = server.getGlobalRegionScheduler();
```

### Region scheduler

[Section titled “Region scheduler”](#region-scheduler)

The region scheduler will be in charge of running tasks for the region that owns a certain location. Do not use this scheduler for
operations on entities, as this scheduler is tied to the region. Each entity has its [own scheduler](#entity-scheduler)
which will follow it across regions. As an example, let’s say I want to set a block to a beehive:

```java
Location locationToChange = ...;

RegionScheduler scheduler = server.getRegionScheduler();

scheduler.execute(plugin, locationToChange, () -> {

locationToChange.getBlock().setType(Material.BEEHIVE);

});
```

We pass the location as a parameter to the [`RegionScheduler`](https://jd.papermc.io/paper/io/papermc/paper/threadedregions/scheduler/RegionScheduler.html)
as it needs to work out which region to execute on.

### Async scheduler

[Section titled “Async scheduler”](#async-scheduler)

The async scheduler can be used for running tasks independent of the server tick process. This can be fetched with:

```java
AsyncScheduler asyncScheduler = server.getAsyncScheduler();
```

### Entity scheduler

[Section titled “Entity scheduler”](#entity-scheduler)

Entity schedulers are used for executing tasks on an entity. These will follow the entity wherever it goes, so you must use
these instead of the region schedulers.

```java
EntityScheduler scheduler = entity.getScheduler();
```


================================================================================
Chapter Title: Roadmap
Original Link: https://docs.papermc.io/paper/dev/roadmap/
================================================================================

Paper offers a rich API with a wide range of features that can help you unlock the full potential of your server.
However, in order to make room for new features and improvements, some of the older APIs will be phased out. This page
is intended to document any future API changes that are planned or possible deprecations that may be coming up.

## Future plans

[Section titled “Future plans”](#future-plans)

### Interface `ItemStack`s

[Section titled “Interface ItemStacks”](#interface-itemstacks)

When you create `ItemStack`s using the constructor, you create an API representation of an [`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html).
This is an object that delegates to a NMS-backed object, you should instead use [`ItemStack#of`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html#of(org.bukkit.Material)) to get the NMS-backed object directly.

In the future, `ItemStack` will be converted to an interface and the constructor will be removed.

#### Precautions

[Section titled “Precautions”](#precautions)

* Avoid directly extending the `ItemStack` class.
  + Custom implementations of this class are not supported and **will** break.

### `ServerPlayer` reuse

[Section titled “ServerPlayer reuse”](#serverplayer-reuse)

*Note: Only applies to NMS usage, will not apply to API.*

Avoid directly storing player (`ServerPlayer`) entity instances. Currently, the player instance is reused when switching
worlds, however, in the future, this behavior will be reverted to match Vanilla behavior. API entities (wrappers) will
continue to function and will have their underlying instance replaced automatically.

This is done to help reduce possible inconsistencies between world switching between Vanilla and Paper.

## Deprecation policy

[Section titled “Deprecation policy”](#deprecation-policy)

Caution

It is highly recommended that you avoid using any APIs that are marked as deprecated.

If you continue to use deprecated APIs, your server may become unstable and may not function as expected.
You may also experience performance issues and other problems. To ensure the best possible experience and longevity
of your plugins, it is important to stay up-to-date with the latest API changes and avoid using any APIs
that are marked for deprecation.

API marked with [`@Deprecated`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Deprecated.html) should not be used in your code base,
as alternative API may be able to be used instead. While certain API may continue to function despite being deprecated,
it **cannot** be promised that this API won’t be marked as deprecated for removal in the future.

```java
@Deprecated

public void exampleMethod(); // Example deprecated method
```

### Deprecated for removal

[Section titled “Deprecated for removal”](#deprecated-for-removal)

In addition to being marked as `@Deprecated`, API may be marked as `forRemoval` with a given
[`@ApiStatus.ScheduledForRemoval`](https://javadoc.io/doc/org.jetbrains/annotations/latest/org/jetbrains/annotations/ApiStatus.ScheduledForRemoval.html) version.
API scheduled for removal should only occur within major release versions of Minecraft.
It is highly recommended you migrate away from API scheduled for removal.

It should be noted, that API scheduled for removal will be given adequate time to allow plugin developers to migrate
away from said API.

```java
@ApiStatus.ScheduledForRemoval(inVersion = "1.20")

@Deprecated(forRemoval = true)

public void exampleMethod(); // Example method marked for removal in 1.20
```

## Deprecation reasons

[Section titled “Deprecation reasons”](#deprecation-reasons)

There are many possible reasons why an API might be deprecated.
Some of the common reasons why API can be deprecated is:

### Old API

[Section titled “Old API”](#old-api)

As the game evolves, the API may represent concepts that no longer exist in the core game.

Old API is most likely not functional and/or may behave unexpectedly in newer versions of the game,
therefore it may be scheduled for removal.

### Duplicate API

[Section titled “Duplicate API”](#duplicate-api)

Since Paper used to downstream Spigot, it can occasionally include APIs added by Spigot that clash with what Paper already has.
Typically, Paper will deprecate Spigot’s API in favor of their own API.

However, in cases where upstream offers a more powerful API, Paper’s may be deprecated instead.

### Obsolete API

[Section titled “Obsolete API”](#obsolete-api)

Paper strives to improve on APIs that may already be included. There may be some cases where we have built new
APIs to offer as a replacement to another.

Obsolete API is expected for function for the far future and may not be scheduled for removal
for a fair amount of time.


================================================================================
Chapter Title: Using databases
Original Link: https://docs.papermc.io/paper/dev/using-databases/
================================================================================

When you are storing larger amounts of data inside a plugin, we recommend using a database. This guide will walk you through the startup process.

## What is a database?

[Section titled “What is a database?”](#what-is-a-database)

A database is a collection of information that is stored electronically on a computer system. There are many different types of databases,
and the main two categories are SQL and NoSQL.

### NoSQL vs SQL

[Section titled “NoSQL vs SQL”](#nosql-vs-sql)

A NoSQL (Not Only SQL) database is a type of database management system that differs from the traditional relational database model.
Unlike traditional SQL databases, which store data in structured tables with predefined schemas, NoSQL databases are schema-less
and offer flexible data models.

They are designed to handle large volumes of unstructured or semi-structured data.
NoSQL databases use various data models, such as key-value, document, column-family, or graph, depending on
the specific requirements of the application.

On the other hand, an SQL database is a type of database management system that follows the relational database model.
It organizes data into structured tables with predefined schemas, where each table represents an entity and columns
represent attributes of that entity. SQL (Structured Query Language) is used to interact with the database,
allowing users to perform various operations like querying, inserting, updating, and deleting data.

## File-based vs standalone databases

[Section titled “File-based vs standalone databases”](#file-based-vs-standalone-databases)

When working with databases, you have two options: file-based or standalone. File-based databases are stored in a file on the disk,
and are usually used for smaller databases. Standalone databases operate in a separate process, and are usually used for larger data models.

### File-based databases

[Section titled “File-based databases”](#file-based-databases)

File-based databases are all stored within a single file on the disk. They are usually used for smaller databases, as they are easier to set up and use.
They can be created and handled from within your plugin code, but offer lesser performance than standalone databases.
Some examples of file-based databases are `SQLite` and `H2`.

Simple SQLite Setup

#### SQLite

[Section titled “SQLite”](#sqlite)

To work with SQLite, you will need a driver to connect / initialize the database.

Note

The JDBC Driver is bundled with Paper, so you do not need to shade/relocate it in your plugin.

##### Usage

[Section titled “Usage”](#usage)

You must invoke a [`Class#forName(String)`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Class.html#forName(java.lang.String))
on the driver to allow it to initialize and then create the connection to the database:

DatabaseManager.java

```java
public class DatabaseManager {

public void connect() {

Class.forName("org.sqlite.JDBC");

Connection connection = DriverManager.getConnection("jdbc:sqlite:plugins/TestPlugin/database.db");

}

}
```

You then have access to a [`Connection`](https://docs.oracle.com/en/java/javase/25/docs/api/java.sql/java/sql/Connection.html) object,
which you can use to create a [`Statement`](https://docs.oracle.com/en/java/javase/25/docs/api/java.sql/java/sql/Statement.html) and execute SQL queries.
To learn more about the Java Database Connectivity API, see [here](https://www.baeldung.com/java-jdbc)

### Standalone databases

[Section titled “Standalone databases”](#standalone-databases)

As previously mentioned, standalone databases operate in a separate process. They are harder to set up and use,
but offer better performance than file-based databases. Some examples of standalone databases are `MySQL`, `MariaDB` and `PostgreSQL`.
There are many more, but these are some of the most popular ones. Each has their own advantages and disadvantages,
so it is up to you to decide which one to use.

The connectors for these databases often have connection pooling. Database connection pooling is where it creates
a pool of pre-established and reusable database connections. Instead of opening a new connection every time a
database operation is required, the application can request a connection from the pool, use it for the required task,
and then return it back to the pool for future reuse. This significantly reduces the overhead of creating and tearing
down connections repeatedly, leading to improved application performance and better scalability.

Simple MySQL Setup

#### MySQL

[Section titled “MySQL”](#mysql)

Working with MySQL requires a few more steps, however it can offer performance benefits for larger databases with
many tables and concurrent accesses. This is a short setup guide for using the [Hikari](https://github.com/brettwooldridge/HikariCP) library with MySQL.

Note

This will require a running MySQL database to connect to.

First, add the dependency to your project with the following dependency:

##### Maven

[Section titled “Maven”](#maven)

pom.xml

```java
<dependency>

<groupId>com.zaxxer</groupId>

<artifactId>HikariCP</artifactId>

<version>4.0.3</version>

<scope>compile</scope>

</dependency>
```

##### Gradle

[Section titled “Gradle”](#gradle)

build.gradle(.kts)

```java
dependencies {

implementation("com.zaxxer:HikariCP:4.0.3")

}
```

Caution

The Hikari library is not bundled with Paper, so you will need to shade/relocate it. In Gradle, you will need to use the [Shadow plugin](https://gradleup.com/shadow/).
Alternatively, you can use the library loader with your Paper plugin to load the library at runtime. See [here](https://docs.papermc.io/paper/dev/getting-started/paper-plugins#loaders)
for more information on how to use this.

##### Usage

[Section titled “Usage”](#usage-1)

Once you have the dependency added, we can work with the connector in our code:

DatabaseManager.java

```java
public class DatabaseManager {

public void connect() {

HikariConfig config = new HikariConfig();

config.setJdbcUrl("jdbc:mysql://localhost:3306/mydatabase"); // Address of your running MySQL database

config.setUsername("username"); // Username

config.setPassword("password"); // Password

config.setMaximumPoolSize(10); // Pool size defaults to 10

config.addDataSourceProperty("", ""); // MISC settings to add

HikariDataSource dataSource = new HikariDataSource(config);

try (Connection connection = dataSource.getConnection()) {

// Use a try-with-resources here to autoclose the connection.

PreparedStatement sql = connection.prepareStatement("SQL");

// Execute statement

} catch (Exception e) {

// Handle any exceptions that arise from getting / handing the exception.

}

}

}
```

## Security

[Section titled “Security”](#security)

### SQL Injection

[Section titled “SQL Injection”](#sql-injection)

SQL injection is a malicious technique where attackers exploit improper input validation to execute unauthorized SQL commands,
potentially causing data breaches or damage to the database.

For example, consider the following code:

```java
public void login(String username, String password) {

String sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

// Execute SQL

}
```

If the user enters the following as their username:

```java
' OR 1=1; --
```

The SQL statement will become:

```java
SELECT * FROM users WHERE username = '' OR 1=1; -- AND password = 'password'
```

This will return all users in the database, regardless of the password they entered. This is a simple example,
but it can be used to do much more malicious things, such as deleting the entire database or stealing user data.

### Prepared statements

[Section titled “Prepared statements”](#prepared-statements)

Using prepared statements in Java with [`PreparedStatement`](https://docs.oracle.com/en/java/javase/25/docs/api/java.sql/java/sql/PreparedStatement.html)s
helps prevent SQL injection. They separate SQL code from user input by using placeholders, reducing the risk of executing unintended SQL commands.
**Always** use prepared statements to ensure the security and integrity of your data. Read more about SQL injection
[here](https://www.baeldung.com/sql-injection).

When using `PreparedStatement` the `login` method will become:

```java
public void login(DataSource dataSource, String username, String password) {

try (Connection connection = dataSource.getConnection()) {

PreparedStatement statement = connection.prepareStatement("SELECT * FROM users WHERE username = ? AND password = ?");

statement.setString(1, username);

statement.setString(2, password);

ResultSet result = statement.executeQuery();

// Do work

} catch (Exception e) {

// Handle any exceptions that arise from getting / handing the exception

}

}
```

## Database tools

[Section titled “Database tools”](#database-tools)

Given the complexity of working with databases (managing connections, building and securing queries, or just parsing the data) several tools
exist in the world of Java to leverage this work.

Some plugin developers use lightweight tools like [JDBI](https://jdbi.org/), [JOOQ](https://www.jooq.org/doc/latest/manual/)
or [Exposed](https://www.jetbrains.com/help/exposed/get-started-with-exposed.html), which take care of all the heavy lifting,
allowing the developers to focus on their plugins rather than the database.


================================================================================
Chapter Title: Debugging your plugin
Original Link: https://docs.papermc.io/paper/dev/debugging/
================================================================================

Debugging your plugin is vital to being able to fix bugs and issues in your plugin. This page will cover some of the most common debugging techniques.

## Printing to the console

[Section titled “Printing to the console”](#printing-to-the-console)

One of the most common debugging techniques is to print to the console. This is likely something you’ve done before, as it’s very simple.
This has a few downsides, though. It can be hard to find the print statements in the console, and it can be hard to remove them all when you’re done debugging. Most notably, you have to recompile your plugin and restart the server to add or remove debugging.

When debugging, you can use `System.out.println("");` to print to the console. It is recommended to use your plugin’s logger instead though,
as it will be easier to know which plugin the log has come from. This can be done simply with:

```java
plugin.getComponentLogger().debug(Component.text("SuperDuperBad Thing has happened"));
```

Logger Levels

In some consoles, using the `warning` level will print the message in different colors.
This can be useful for finding your print statements in the console.

## Using a remote debugger

[Section titled “Using a remote debugger”](#using-a-remote-debugger)

A debugger is a tool that allows you to pause your code at a certain point and inspect the values of variables.
This can be very useful for finding out why your code isn’t working as expected and also for finding out where your code is going wrong.

### Setting up the debugger

[Section titled “Setting up the debugger”](#setting-up-the-debugger)

To use a debugger, you need to set up your IDE to use it. This is different for each IDE, but for the sake of this guide, we will be using IntelliJ IDEA.

To set up a debugger in IntelliJ, you need to create a new run configuration.
You can do this by clicking the dropdown next to the run button and clicking `Edit Configurations...`:

![](https://docs.papermc.io/_astro/config_dropdown.BFxL9k7t_Z1Pvn9Q.webp)

Then, click the `+` button in the top left and select `Remote JVM Debug`. You can then name the configuration whatever you want, and click `Apply`:

![](https://docs.papermc.io/_astro/config_add.BZo3OiyP_ZzqDYh.webp)

Finally, copy the command line arguments from the window, and paste these into your server’s startup script.
These will go after the `java` command and before `-jar`. Once you have done this, you can click `OK`. For example:

Terminal window

```java
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005 -jar paper-1.21.11.jar nogui
```

Once your server is running, you can use the bug icon in the top right to connect your debugger to the server:

![](https://docs.papermc.io/_astro/debugger_connect.mnUOoaKC_Z2b4R01.webp)

#### Using the debugger

[Section titled “Using the debugger”](#using-the-debugger)

Let’s say we have this code:

```java
@EventHandler

public void onPlayerMove(PlayerMoveEvent event) {

Player player = event.getPlayer();

Location location = player.getLocation();

if (location.getWorld() == null)

return;

if (location.getWorld().getEnvironment() == World.Environment.NETHER) {

player.sendMessage("You are in the nether!");

}

}
```

You can add a breakpoint to the line by clicking on the line number:

![](https://docs.papermc.io/_astro/add_breakpoints.Dgq1Prxb_23XIrA.webp)

This will pause the code when it reaches that line. You can then use the debugger to inspect the values of variables:

![](https://docs.papermc.io/_astro/debugger_use.Cd360zfH_NnSHS.webp)

You can inspect the values of each of the variables in the current scope.
You can also use the buttons in the top to step from one breakpoint to the next.
If needed, you can also use the text box at the top to evaluate expressions for debugging purposes.

### Using direct debugging

[Section titled “Using direct debugging”](#using-direct-debugging)

Direct debugging will allow you to run the server directly from your IDE, and will allow you to use breakpoints and step through your code.
We can achieve this by using [JPenilla’s Gradle plugin](https://github.com/jpenilla/run-task) to run the server directly from the IDE.
See [here](https://github.com/jpenilla/run-task#basic-usage) for instructions on how to set up the plugin.


================================================================================
Chapter Title: Minecraft internals
Original Link: https://docs.papermc.io/paper/dev/internals/
================================================================================

The code that runs Minecraft is not open source. Bukkit is an API that allows plugins to interact with the server. This
is implemented by CraftBukkit and interacts with Minecraft’s code. You will often hear the terms NMS and CraftBukkit
when talking about Minecraft internals.

Using Minecraft internals

Using Minecraft internals is not recommended. This is because using internal code directly is not guaranteed to be
stable and it changes often. This means that your plugin may break when a new version of Minecraft is released.
Whenever possible, you should use API instead of internals.

**PaperMC will offer no direct support for programming against Minecraft internals.**

## What is NMS?

[Section titled “What is NMS?”](#what-is-nms)

NMS stands for `net.minecraft.server` and refers to a Java package that contains a lot of Mojang’s code. This code is
proprietary and is not open source. This code is not guaranteed to be stable when invoked externally and may change at
any time.

## Accessing Minecraft internals

[Section titled “Accessing Minecraft internals”](#accessing-minecraft-internals)

In order to use Mojang and CraftBukkit code, you may either use the `paperweight-userdev` Gradle plugin or use reflection.
[`paperweight-userdev`](https://github.com/PaperMC/paperweight-test-plugin) is the recommended way to access internal code
as it is easier to use due to being able to have the remapped code in your IDE. You can find
out more about this in the [`paperweight-userdev`](https://docs.papermc.io/paper/dev/userdev) section.

However, if you are unable to use `paperweight-userdev`, you can use reflection.

### Reflection

[Section titled “Reflection”](#reflection)

Reflection is a way to access code at runtime. This allows you to access code that may not be available at compile time.
Reflection is often used to access internal code across multiple versions. However, reflection does come
with performance impacts if used improperly. For example, if you are accessing a method or field more than once,
you should cache the [`Field`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/reflect/Field.html)/
[`Method`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/reflect/Method.html) to prevent the performance
impact of looking up the field/method each time.

1.20.4 and older

The internal CraftBukkit code was relocated to `org.bukkit.craftbukkit.<version>` unless you ran a Mojang-mapped version
of Paper. This was unlikely to be the case in most production environments until 1.20.5. This means that any attempts to reflect had to
include the version. For example, `org.bukkit.craftbukkit.v1_20_R2.CraftServer` was the full class and package name
for the CraftServer class in version 1.20.2. You could access these classes easily with some reflection utilities.

```java
private static final String CRAFTBUKKIT_PACKAGE = Bukkit.getServer().getClass().getPackageName();

public static String cbClass(String clazz) {

return CRAFTBUKKIT_PACKAGE + "." + clazz;

}

// You can then use this method to get the CraftBukkit class:

Class.forName(cbClass("entity.CraftBee"));
```

Minecraft’s code is obfuscated. This means that the names of classes and methods are changed to make them harder to
understand. Paper deobfuscates these identifiers for development and since 1.20.5, also for runtime.

1.20.4 and older

Previously, to provide compatibility with legacy plugins, Paper was reobfuscated at runtime.
You could use a library like [reflection-remapper](https://github.com/jpenilla/reflection-remapper) to automatically remap the
reflection references. This allowed you to use the deobfuscated, Mojang-mapped names in your code. This was recommended as
it made the code easier to understand.

### Mojang-mapped servers

[Section titled “Mojang-mapped servers”](#mojang-mapped-servers)

Running a Mojang-mapped (moj-map) server is an excellent way to streamline your processes because you can develop using
the same mappings that will be present at runtime. This eliminates the need for remapping in your compilation, which in
turn simplifies debugging and allows you to hotswap plugins.

As of 1.20.5, Paper ships with a Mojang-mapped runtime by default instead of reobfuscating the server to Spigot mappings.
By adopting Mojang mappings, you ensure that your plugin won’t require internal remapping at runtime.
For more information, see the [plugin remapping](https://docs.papermc.io/paper/dev/project-setup#plugin-remapping) section
and [userdev](https://docs.papermc.io/paper/dev/userdev#1205-and-beyond) documentation covering these changes.

### Getting the current Minecraft version

[Section titled “Getting the current Minecraft version”](#getting-the-current-minecraft-version)

You can get the current Minecraft version to allow you to use the correct code for a specific version. This can be done
with one of the following methods:

```java
// Example value: 1.21.11

String minecraftVersion = Bukkit.getServer().getMinecraftVersion();

// Example value: 1.21.11-R0.1-SNAPSHOT

String bukkitVersion = Bukkit.getServer().getBukkitVersion();

// Example value for 1.20.1: 3465

int dataVersion = Bukkit.getUnsafe().getDataVersion();
```

Parsing the version

Parsing the version from the package name of classes is no longer possible as of 1.20.5 as Paper stopped relocating the CraftBukkit package.
See the [reflection](#reflection) section for more information.


================================================================================
Chapter Title: Reading stacktraces
Original Link: https://docs.papermc.io/paper/dev/reading-stacktraces/
================================================================================

## What is a stacktrace?

[Section titled “What is a stacktrace?”](#what-is-a-stacktrace)

In Java, a stacktrace shows the call stack of a thread. The call stack is the path of execution that led to the current point in the program.
Usually, the stacktrace will be printed to the console when an exception is not handled correctly.

Stacktraces are a useful tool for debugging your code. They show you the exact line of code that caused an error, and the
line of code that called that line of code, and so on. This is useful because it allows you to see the exact path of execution that led to the error.

### Example

[Section titled “Example”](#example)

Here is an example of a stacktrace, which has been caused due to a `NullPointerException`:

```java
[15:20:42 ERROR]: Could not pass event PluginEnableEvent to TestPlugin v1.0

java.lang.NullPointerException: Cannot invoke "Object.toString()" because "player" is null

at io.papermc.testplugin.TestPlugin.onPluginEnable(TestPlugin.java:23) ~[TestPlugin-1.0-SNAPSHOT.jar:?]

at com.destroystokyo.paper.event.executor.asm.generated.GeneratedEventExecutor1.execute(Unknown Source) ~[?:?]

at org.bukkit.plugin.EventExecutor$2.execute(EventExecutor.java:77) ~[paper-api-1.20.2-R0.1-SNAPSHOT.jar:?]

at co.aikar.timings.TimedEventExecutor.execute(TimedEventExecutor.java:81) ~[paper-api-1.20.2-R0.1-SNAPSHOT.jar:git-Paper-49]

at org.bukkit.plugin.RegisteredListener.callEvent(RegisteredListener.java:70) ~[paper-api-1.20.2-R0.1-SNAPSHOT.jar:?]

at io.papermc.paper.plugin.manager.PaperEventManager.callEvent(PaperEventManager.java:54) ~[paper-1.20.2.jar:git-Paper-49]

at io.papermc.paper.plugin.manager.PaperPluginManagerImpl.callEvent(PaperPluginManagerImpl.java:126) ~[paper-1.20.2.jar:git-Paper-49]

at org.bukkit.plugin.SimplePluginManager.callEvent(SimplePluginManager.java:615) ~[paper-api-1.20.2-R0.1-SNAPSHOT.jar:?]

at io.papermc.paper.plugin.manager.PaperPluginInstanceManager.enablePlugin(PaperPluginInstanceManager.java:200) ~[paper-1.20.2.jar:git-Paper-49]

at io.papermc.paper.plugin.manager.PaperPluginManagerImpl.enablePlugin(PaperPluginManagerImpl.java:104) ~[paper-1.20.2.jar:git-Paper-49]

at org.bukkit.plugin.SimplePluginManager.enablePlugin(SimplePluginManager.java:507) ~[paper-api-1.20.2-R0.1-SNAPSHOT.jar:?]

at org.bukkit.craftbukkit.v1_20_R2.CraftServer.enablePlugin(CraftServer.java:636) ~[paper-1.20.2.jar:git-Paper-49]

at org.bukkit.craftbukkit.v1_20_R2.CraftServer.enablePlugins(CraftServer.java:547) ~[paper-1.20.2.jar:git-Paper-49]

at net.minecraft.server.MinecraftServer.loadWorld0(MinecraftServer.java:636) ~[paper-1.20.2.jar:git-Paper-49]

at net.minecraft.server.MinecraftServer.loadLevel(MinecraftServer.java:435) ~[paper-1.20.2.jar:git-Paper-49]

at net.minecraft.server.dedicated.DedicatedServer.initServer(DedicatedServer.java:308) ~[paper-1.20.2.jar:git-Paper-49]

at net.minecraft.server.MinecraftServer.runServer(MinecraftServer.java:1101) ~[paper-1.20.2.jar:git-Paper-49]

at net.minecraft.server.MinecraftServer.lambda$spin$0(MinecraftServer.java:318) ~[paper-1.20.2.jar:git-Paper-49]

at java.lang.Thread.run(Thread.java:833) ~[?:?]
```

* Firstly, we can see that this certain error occurred when a [`PluginEnableEvent`](https://jd.papermc.io/paper/org/bukkit/event/server/PluginEnableEvent.html)
  was being handled by the `TestPlugin`.
* Then we can see on the second line, the cause of the exception:

  > `java.lang.NullPointerException: Cannot invoke "Object.toString()" because "player" is null`

  This tells us that the exception was caused by a [`NullPointerException`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/NullPointerException.html),
  and that the exception was caused because we tried to call the `toString()` method on a null “player” object.
* From here, as we work down the stacktrace, we can see the exact path of execution that led to the error. In this case,
  the next line of the stacktrace is:

  > `at io.papermc.testplugin.TestPlugin.onPluginEnable(TestPlugin.java:23) ~[TestPlugin-1.0-SNAPSHOT.jar:?]`

  Which tells us that the error was thrown at line 23 of `TestPlugin.java`.
* You can continue to work down the stacktrace, and see the exact path of execution that led to the error. In this case,
  it is server internals, so we can generally ignore it.

## Omitted stacktraces

[Section titled “Omitted stacktraces”](#omitted-stacktraces)

In JDK 5, the JVM started to omit stacktraces for certain exceptions. This was common when the JVM had optimized the code,
and you could get `NullPointerException`s without a stacktrace. In order to fix this, you can pass the `-XX:-OmitStackTraceInFastThrow` flag to the JVM:

Terminal window

```java
java -XX:-OmitStackTraceInFastThrow -jar paper.jar
```


================================================================================
Chapter Title: Events
Original Link: https://docs.papermc.io/paper/contributing/events/
================================================================================

There are several requirements for events in the Paper API.

Note

Note that while not all existing events may follow these
guidelines, all new and modified events should adhere to them.

All new events should go in the package (sub-package of) `io.papermc.paper.event`.

### Constructors

[Section titled “Constructors”](#constructors)

All new constructors added should be annotated with
[`@ApiStatus.Internal`](https://javadoc.io/doc/org.jetbrains/annotations/latest/org/jetbrains/annotations/ApiStatus.Internal.html)
to signify that they are not considered API and can change at any time without warning.

Constructors that are being replaced, if they aren’t being removed, should be marked with
[`@Deprecated`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Deprecated.html) and [`@DoNotUse`](https://jd.papermc.io/paper/io/papermc/paper/annotation/DoNotUse.html).

### Mutability

[Section titled “Mutability”](#mutability)

Certain API types are “mutable” which can lead to unexpected behavior within events. Mutable types like
[`Location`](https://jd.papermc.io/paper/org/bukkit/Location.html) and [`Vector`](https://jd.papermc.io/paper/org/bukkit/util/Vector.html)
should therefore be cloned when returned from a “getter” in an event.

### `HandlerList`

[Section titled “HandlerList”](#handlerlist)

For an event class or any subclass of it to be listened to, a [`HandlerList`](https://jd.papermc.io/paper/org/bukkit/event/HandlerList.html)
field must be present with an instance and static method to retrieve it.
See the docs for [`Event`](https://jd.papermc.io/paper/org/bukkit/event/Event.html) for specifics.
This field should be static and final and named `HANDLER_LIST`.

Also consider not putting a `HandlerList` on every event, just a “common parent” event so that a plugin can listen to the
parent event and capture any child events but also listen to the child event separately.

### Miscellaneous

[Section titled “Miscellaneous”](#miscellaneous)

* New parameters or method returns of type [`ItemStack`](https://jd.papermc.io/paper/org/bukkit/inventory/ItemStack.html)
  should not be [`@Nullable`](https://javadoc.io/doc/org.jspecify/jspecify/latest/org/jspecify/annotations/Nullable.html)
  in most case and instead accept an empty itemStack.
