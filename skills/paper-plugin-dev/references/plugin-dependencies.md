# Plugin Dependencies and Maven Guide

Complete guide to managing dependencies, shading, relocation, and Maven configuration for Paper plugins.

## Table of Contents

- [Maven Basics](#maven-basics)
- [Repository Configuration](#repository-configuration)
- [Adding Dependencies](#adding-dependencies)
- [Dependency Scopes](#dependency-scopes)
- [Shading and Relocation](#shading-and-relocation)
- [Plugin Dependencies](#plugin-dependencies)
- [Best Practices](#best-practices)

## Maven Basics

### Project Structure

```
MyPlugin/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/myplugin/
│   │   │       └── MyPlugin.java
│   │   └── resources/
│   │       ├── paper-plugin.yml
│   │       └── config.yml
│   └── test/
│       └── java/
└── target/
    └── MyPlugin-1.0.0.jar
```

### Basic pom.xml Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- Project Coordinates -->
    <groupId>com.example</groupId>
    <artifactId>MyPlugin</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <!-- Project Info -->
    <name>MyPlugin</name>
    <description>My Paper plugin</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <paper.version>1.21.4-R0.1-SNAPSHOT</paper.version>
    </properties>

    <!-- Build Configuration -->
    <build>
        <!-- ... -->
    </build>

    <!-- Repositories -->
    <repositories>
        <!-- ... -->
    </repositories>

    <!-- Dependencies -->
    <dependencies>
        <!-- ... -->
    </dependencies>
</project>
```

## Repository Configuration

### Common Repositories

```xml
<repositories>
    <!-- PaperMC -->
    <repository>
        <id>papermc</id>
        <url>https://repo.papermc.io/repository/maven-public/</url>
    </repository>
    
    <!-- Spigot (if needed for legacy plugins) -->
    <repository>
        <id>spigot-repo</id>
        <url>https://hub.spigotmc.org/nexus/content/repositories/snapshots/</url>
    </repository>
    
    <!-- Maven Central (usually inherited) -->
    <repository>
        <id>central</id>
        <url>https://repo.maven.apache.org/maven2</url>
    </repository>
    
    <!-- JitPack (for GitHub projects) -->
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
    
    <!-- CodeMC (various plugins) -->
    <repository>
        <id>codemc-repo</id>
        <url>https://repo.codemc.io/repository/maven-public/</url>
    </repository>
    
    <!-- PlaceholderAPI -->
    <repository>
        <id>placeholderapi</id>
        <url>https://repo.extendedclip.com/content/repositories/placeholderapi/</url>
    </repository>
</repositories>
```

## Adding Dependencies

### Paper API

```xml
<dependency>
    <groupId>io.papermc.paper</groupId>
    <artifactId>paper-api</artifactId>
    <version>1.21.4-R0.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
```

**Note**: Always use `provided` scope for Paper API - it's already on the server!

### Adventure API (if needed separately)

```xml
<!-- Usually NOT needed - Paper includes Adventure -->
<dependency>
    <groupId>net.kyori</groupId>
    <artifactId>adventure-api</artifactId>
    <version>4.26.1</version>
    <scope>provided</scope>
</dependency>

<dependency>
    <groupId>net.kyori</groupId>
    <artifactId>adventure-text-minimessage</artifactId>
    <version>4.26.1</version>
    <scope>provided</scope>
</dependency>
```

### Common Plugin Dependencies

```xml
<!-- Vault (Economy API) -->
<dependency>
    <groupId>com.github.MilkBowl</groupId>
    <artifactId>VaultAPI</artifactId>
    <version>1.7.1</version>
    <scope>provided</scope>
</dependency>

<!-- PlaceholderAPI -->
<dependency>
    <groupId>me.clip</groupId>
    <artifactId>placeholderapi</artifactId>
    <version>2.11.5</version>
    <scope>provided</scope>
</dependency>

<!-- LuckPerms API -->
<dependency>
    <groupId>net.luckperms</groupId>
    <artifactId>api</artifactId>
    <version>5.4</version>
    <scope>provided</scope>
</dependency>

<!-- WorldGuard -->
<dependency>
    <groupId>com.sk89q.worldguard</groupId>
    <artifactId>worldguard-bukkit</artifactId>
    <version>7.0.9</version>
    <scope>provided</scope>
</dependency>
```

### Third-Party Libraries (to shade)

```xml
<!-- HikariCP (Database connection pooling) -->
<dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>5.0.1</version>
    <scope>compile</scope>
</dependency>

<!-- Gson (if need newer version than provided) -->
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.10.1</version>
    <scope>compile</scope>
</dependency>

<!-- Configurate (Advanced config library) -->
<dependency>
    <groupId>org.spongepowered</groupId>
    <artifactId>configurate-yaml</artifactId>
    <version>4.1.2</version>
    <scope>compile</scope>
</dependency>

<!-- SLF4J (Logging) -->
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.9</version>
    <scope>compile</scope>
</dependency>
```

## Dependency Scopes

### Understanding Scopes

| Scope | Description | Include in JAR? | Use Case |
|-------|-------------|----------------|----------|
| `compile` | Default scope | Yes | Libraries you need to shade |
| `provided` | Available at runtime | No | Paper API, other plugins |
| `runtime` | Runtime only | Yes | Runtime dependencies |
| `test` | Testing only | No | JUnit, Mockito |
| `system` | System path | No | Local JARs (avoid!) |

### Examples

```xml
<!-- Will be shaded into your plugin -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>mylibrary</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>

<!-- Provided by Paper - don't include -->
<dependency>
    <groupId>io.papermc.paper</groupId>
    <artifactId>paper-api</artifactId>
    <version>1.21.4-R0.1-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>

<!-- For testing only -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.1</version>
    <scope>test</scope>
</dependency>
```

## Shading and Relocation

### Why Shade?

Shading includes dependencies directly in your plugin JAR. You need to shade when:
- Library is NOT provided by Paper
- Other plugins might use different versions
- You need a specific version of a library

### Why Relocate?

Relocation prevents conflicts by moving library classes to your package:

```
com.zaxxer.hikari.HikariDataSource
    ↓ relocated to ↓
com.example.myplugin.libs.hikari.HikariDataSource
```

### Shade Plugin Configuration

```xml
<build>
    <plugins>
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
                    <configuration>
                        <!-- Don't create dependency-reduced-pom.xml -->
                        <createDependencyReducedPom>false</createDependencyReducedPom>
                        
                        <!-- Relocations -->
                        <relocations>
                            <!-- Relocate HikariCP -->
                            <relocation>
                                <pattern>com.zaxxer.hikari</pattern>
                                <shadedPattern>com.example.myplugin.libs.hikari</shadedPattern>
                            </relocation>
                            
                            <!-- Relocate Configurate -->
                            <relocation>
                                <pattern>org.spongepowered.configurate</pattern>
                                <shadedPattern>com.example.myplugin.libs.configurate</shadedPattern>
                            </relocation>
                        </relocations>
                        
                        <!-- Filters -->
                        <filters>
                            <filter>
                                <!-- Exclude signatures -->
                                <artifact>*:*</artifact>
                                <excludes>
                                    <exclude>META-INF/*.SF</exclude>
                                    <exclude>META-INF/*.DSA</exclude>
                                    <exclude>META-INF/*.RSA</exclude>
                                </excludes>
                            </filter>
                        </filters>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### What NOT to Shade/Relocate

**Never shade these**:
- Paper API (`io.papermc.paper`)
- Adventure API (`net.kyori.adventure`) - Paper provides it
- Bukkit API (`org.bukkit`)
- Dependencies from other plugins (Vault, PlaceholderAPI, etc.)

**If you shade Paper/Adventure APIs, your plugin won't work!**

### Minimal Shading Example

```xml
<build>
    <plugins>
        <!-- Maven Compiler -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>21</source>
                <target>21</target>
            </configuration>
        </plugin>
        
        <!-- Maven Shade (only if you have dependencies to shade) -->
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
    
    <!-- Resource filtering for version replacement -->
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
</build>
```

## Plugin Dependencies

### Declaring in paper-plugin.yml

```yaml
name: MyPlugin
version: '${project.version}'  # Replaced by Maven
main: com.example.MyPlugin
api-version: '1.21'

# Hard dependencies (must be installed)
dependencies:
  server:
    Vault:
      required: true
      load: BEFORE  # Load Vault before your plugin
      
    WorldGuard:
      required: true
      load: BEFORE

# Soft dependencies (optional)
dependencies:
  server:
    PlaceholderAPI:
      required: false
      load: AFTER  # Load after PlaceholderAPI if present
      
    LuckPerms:
      required: false
      load: AFTER
```

### Loading Plugin Dependencies

```java
public class MyPlugin extends JavaPlugin {
    private Economy economy = null;
    private boolean placeholderAPIAvailable = false;
    
    @Override
    public void onEnable() {
        // Check and load Vault
        if (!setupEconomy()) {
            getLogger().severe("Vault not found! Disabling plugin.");
            getServer().getPluginManager().disablePlugin(this);
            return;
        }
        
        // Check optional PlaceholderAPI
        if (getServer().getPluginManager().getPlugin("PlaceholderAPI") != null) {
            placeholderAPIAvailable = true;
            getLogger().info("PlaceholderAPI found - enabling integration");
        }
    }
    
    private boolean setupEconomy() {
        if (getServer().getPluginManager().getPlugin("Vault") == null) {
            return false;
        }
        
        RegisteredServiceProvider<Economy> rsp = 
            getServer().getServicesManager().getRegistration(Economy.class);
        if (rsp == null) {
            return false;
        }
        
        economy = rsp.getProvider();
        return economy != null;
    }
    
    public Economy getEconomy() {
        return economy;
    }
}
```

## Best Practices

### 1. Version Management

Use properties for versions:

```xml
<properties>
    <paper.version>1.21.4-R0.1-SNAPSHOT</paper.version>
    <hikari.version>5.0.1</hikari.version>
    <configurate.version>4.1.2</configurate.version>
</properties>

<dependencies>
    <dependency>
        <groupId>io.papermc.paper</groupId>
        <artifactId>paper-api</artifactId>
        <version>${paper.version}</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

### 2. Dependency Exclusions

Exclude transitive dependencies you don't need:

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>somelibrary</artifactId>
    <version>1.0.0</version>
    <exclusions>
        <!-- Exclude unneeded dependency -->
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

### 3. Bill of Materials (BOM)

For managing multiple related dependencies:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.spongepowered</groupId>
            <artifactId>configurate-bom</artifactId>
            <version>4.1.2</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <!-- Version inherited from BOM -->
    <dependency>
        <groupId>org.spongepowered</groupId>
        <artifactId>configurate-yaml</artifactId>
        <!-- No version needed -->
    </dependency>
</dependencies>
```

### 4. Check Dependency Tree

```bash
# View all dependencies and their versions
mvn dependency:tree

# Look for conflicts
mvn dependency:tree | grep -i "conflict"

# Analyze dependencies
mvn dependency:analyze
```

### 5. Minimize Shaded Size

```xml
<configuration>
    <!-- Only include specific packages -->
    <includes>
        <include>com.zaxxer.hikari:*</include>
    </includes>
    
    <!-- Or exclude unnecessary files -->
    <filters>
        <filter>
            <artifact>*:*</artifact>
            <excludes>
                <exclude>META-INF/*.MF</exclude>
                <exclude>META-INF/maven/**</exclude>
                <exclude>module-info.class</exclude>
            </excludes>
        </filter>
    </filters>
</configuration>
```

### 6. Minimize Relocations

Only relocate what's necessary:

```xml
<!-- ❌ BAD - Relocating everything -->
<relocation>
    <pattern>com</pattern>
    <shadedPattern>com.example.myplugin.libs</shadedPattern>
</relocation>

<!-- ✅ GOOD - Specific relocations -->
<relocation>
    <pattern>com.zaxxer.hikari</pattern>
    <shadedPattern>com.example.myplugin.libs.hikari</shadedPattern>
</relocation>
```

## Complete Example pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>MyPlugin</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>MyPlugin</name>
    <description>Example Paper plugin with dependencies</description>

    <properties>
        <java.version>21</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <paper.version>1.21.4-R0.1-SNAPSHOT</paper.version>
        <hikari.version>5.0.1</hikari.version>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${java.version}</source>
                    <target>${java.version}</target>
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
                        <configuration>
                            <createDependencyReducedPom>false</createDependencyReducedPom>
                            <relocations>
                                <relocation>
                                    <pattern>com.zaxxer.hikari</pattern>
                                    <shadedPattern>com.example.myplugin.libs.hikari</shadedPattern>
                                </relocation>
                            </relocations>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                        </configuration>
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
        <!-- Paper API (provided by server) -->
        <dependency>
            <groupId>io.papermc.paper</groupId>
            <artifactId>paper-api</artifactId>
            <version>${paper.version}</version>
            <scope>provided</scope>
        </dependency>
        
        <!-- HikariCP (shade this) -->
        <dependency>
            <groupId>com.zaxxer</groupId>
            <artifactId>HikariCP</artifactId>
            <version>${hikari.version}</version>
            <scope>compile</scope>
        </dependency>
    </dependencies>
</project>
```

## Common Issues

### 1. ClassNotFoundException after shading

**Problem**: Class not found even though it's shaded

**Solution**: Check relocations - make sure you're not relocating packages you reference directly

### 2. Multiple versions conflict

**Problem**: `java.lang.NoSuchMethodError`

**Solution**: 
```bash
# Check dependency tree
mvn dependency:tree

# Force specific version
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>2.0.0</version>
    <scope>compile</scope>
</dependency>
```

### 3. Fat JAR too large

**Problem**: Plugin JAR is >10MB

**Solution**:
- Exclude unnecessary transitive dependencies
- Use `provided` scope when possible
- Filter out unneeded resources

### 4. Plugin won't load after adding dependency

**Problem**: `InvalidPluginException`

**Solution**:
- Check paper-plugin.yml is valid
- Ensure main class exists and extends JavaPlugin
- Verify shaded JAR contains all required classes
