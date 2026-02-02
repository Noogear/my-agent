#!/usr/bin/env python3
"""
Create a complete Paper plugin project structure with Maven configuration.

Usage:
    python create_plugin_structure.py <plugin_name> <package> <output_dir>

Example:
    python create_plugin_structure.py "MyPlugin" "com.example.myplugin" ./my-plugin
"""

import os
import sys
from pathlib import Path


def create_plugin_structure(plugin_name: str, package: str, output_dir: str):
    """Create a complete Paper plugin structure."""
    
    base_path = Path(output_dir)
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Convert package to directory structure
    package_path = package.replace('.', '/')
    java_base = base_path / 'src' / 'main' / 'java' / package_path
    resources_base = base_path / 'src' / 'main' / 'resources'
    
    # Create directories
    java_base.mkdir(parents=True, exist_ok=True)
    resources_base.mkdir(parents=True, exist_ok=True)
    (java_base / 'commands').mkdir(exist_ok=True)
    (java_base / 'listeners').mkdir(exist_ok=True)
    (java_base / 'config').mkdir(exist_ok=True)
    
    # Create pom.xml
    pom_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>{package}</groupId>
    <artifactId>{plugin_name}</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>{plugin_name}</name>
    <description>A Paper plugin</description>

    <properties>
        <java.version>21</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${{java.version}}</source>
                    <target>${{java.version}}</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.5.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
    </build>

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
            <version>1.21.4-R0.1-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</project>
'''
    
    with open(base_path / 'pom.xml', 'w', encoding='utf-8') as f:
        f.write(pom_content)
    
    # Create main plugin class
    main_class_content = f'''package {package};

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.plugin.java.JavaPlugin;

public class {plugin_name} extends JavaPlugin {{

    @Override
    public void onEnable() {{
        // Save default config
        saveDefaultConfig();
        
        // Register events
        // getServer().getPluginManager().registerEvents(new YourListener(), this);
        
        // Register commands
        // getCommand("yourcommand").setExecutor(new YourCommand());
        
        getLogger().info("{plugin_name} has been enabled!");
    }}

    @Override
    public void onDisable() {{
        getLogger().info("{plugin_name} has been disabled!");
    }}
}}
'''
    
    with open(java_base / f'{plugin_name}.java', 'w', encoding='utf-8') as f:
        f.write(main_class_content)
    
    # Create paper-plugin.yml
    plugin_yml_content = f'''name: {plugin_name}
version: '${{project.version}}'
main: {package}.{plugin_name}
api-version: '1.21'
description: A Paper plugin
author: YourName

# Optional: Define permissions
# permissions:
#   {plugin_name.lower()}.use:
#     description: Basic permission
#     default: true

# Optional: Define commands
# commands:
#   yourcommand:
#     description: Your command description
#     usage: /<command> [args]
#     permission: {plugin_name.lower()}.use
'''
    
    with open(resources_base / 'paper-plugin.yml', 'w', encoding='utf-8') as f:
        f.write(plugin_yml_content)
    
    # Create config.yml
    config_yml_content = f'''# {plugin_name} Configuration

# Plugin settings
settings:
  enabled: true
  debug: false

# Messages (using MiniMessage format)
messages:
  prefix: "<gold>[{plugin_name}]</gold> "
  reload: "<green>Configuration reloaded!</green>"
  no-permission: "<red>You don't have permission to do that!</red>"
'''
    
    with open(resources_base / 'config.yml', 'w', encoding='utf-8') as f:
        f.write(config_yml_content)
    
    # Create example listener
    listener_content = f'''package {package}.listeners;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class JoinListener implements Listener {{

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {{
        // Example: Send a welcome message
        event.getPlayer().sendMessage(
            Component.text("Welcome to the server!", NamedTextColor.GREEN)
        );
        
        // Example: Set custom join message
        event.joinMessage(
            Component.text()
                .append(Component.text("→ ", NamedTextColor.GRAY))
                .append(Component.text(event.getPlayer().getName(), NamedTextColor.YELLOW))
                .append(Component.text(" joined the game", NamedTextColor.GRAY))
                .build()
        );
    }}
}}
'''
    
    with open(java_base / 'listeners' / 'JoinListener.java', 'w', encoding='utf-8') as f:
        f.write(listener_content)
    
    # Create .gitignore
    gitignore_content = '''# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml

# IntelliJ IDEA
.idea/
*.iml
*.iws
*.ipr

# Eclipse
.classpath
.project
.settings/

# VS Code
.vscode/

# macOS
.DS_Store

# Build output
*.jar
!src/
'''
    
    with open(base_path / '.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    
    print(f"✅ Plugin structure created at: {base_path.absolute()}")
    print(f"\nNext steps:")
    print(f"1. cd {output_dir}")
    print(f"2. Edit src/main/java/{package_path}/{plugin_name}.java")
    print(f"3. Build with: mvn clean package")
    print(f"4. Copy target/{plugin_name}-1.0.0-SNAPSHOT.jar to server plugins folder")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python create_plugin_structure.py <plugin_name> <package> <output_dir>")
        print("Example: python create_plugin_structure.py MyPlugin com.example.myplugin ./my-plugin")
        sys.exit(1)
    
    plugin_name = sys.argv[1]
    package = sys.argv[2]
    output_dir = sys.argv[3]
    
    # Validate plugin name (no spaces, valid Java class name)
    if not plugin_name.replace('_', '').isalnum():
        print("Error: Plugin name must be alphanumeric (underscores allowed)")
        sys.exit(1)
    
    # Validate package name
    if not all(part.replace('_', '').isalnum() for part in package.split('.')):
        print("Error: Package name must be valid Java package (e.g., com.example.plugin)")
        sys.exit(1)
    
    create_plugin_structure(plugin_name, package, output_dir)
