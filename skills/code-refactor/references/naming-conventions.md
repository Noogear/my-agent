# Naming Conventions Reference

## Java Naming Rules

### Class Naming Patterns

| Category | Pattern | Example | Anti-Pattern |
|----------|---------|---------|--------------|
| Manager/Service | `*Manager` OR `*Service` (pick one) | `ConfigManager` | `ConfigManager` + `UserService` (inconsistent) |
| Utility | `*Utils` (plural) OR `*Util` (singular) | `StringUtils` | `StringUtil` + `FileUtils` (mixed) |
| Helper | `*Helper` OR `*Utils` (pick one) | `ValidationHelper` | `ConfigHelper` + `StringUtils` (mixed) |
| Factory | `*Factory` | `ConnectionFactory` | `ConnectionBuilder` (if creates, not builds) |
| Builder | `*Builder` | `QueryBuilder` | `QueryFactory` (if step-by-step) |
| Handler | `*Handler` | `RequestHandler` | `RequestProcessor` (if handles events) |
| Processor | `*Processor` | `DataProcessor` | `DataHandler` (if processes data) |
| Provider | `*Provider` | `ConfigProvider` | `ConfigSupplier` |
| Listener | `*Listener` | `EventListener` | `EventHandler` (if listens) |
| Adapter | `*Adapter` | `LegacyAdapter` | `LegacyWrapper` |
| Wrapper | `*Wrapper` | `ResponseWrapper` | `ResponseContainer` |
| Exception | `*Exception` | `ConfigException` | `ConfigError` |
| DTO/VO | `*DTO` OR `*VO` (pick one) | `UserDTO` | `UserData` + `OrderVO` (mixed) |
| Entity | `*Entity` OR no suffix | `UserEntity` or `User` | Mixed patterns |
| Config | `*Config` OR `*Configuration` | `AppConfig` | `AppSettings` |
| Context | `*Context` | `RequestContext` | `RequestState` |
| Result | `*Result` | `ValidationResult` | `ValidationOutput` |
| Info | `*Info` | `FileInfo` | `FileData` (if metadata) |
| Spec | `*Spec` | `QuerySpec` | `QueryCriteria` |
| Registry | `*Registry` | `ServiceRegistry` | `ServiceMap` |
| Cache | `*Cache` | `ConfigCache` | `ConfigStore` (if caching) |
| Pool | `*Pool` | `ConnectionPool` | `ConnectionCache` |
| Queue | `*Queue` | `TaskQueue` | `TaskList` (if FIFO) |
| Logger | `*Logger` | `ConfigLogger` | `ConfigLog` |

### Method Naming Patterns

| Category | Pattern | Example | Anti-Pattern |
|----------|---------|---------|--------------|
| Getter | `get*` | `getName()` | `fetchName()`, `retrieveName()` |
| Boolean getter | `is*`, `has*`, `can*` | `isValid()` | `getValid()`, `valid()` |
| Setter | `set*` | `setName(x)` | `updateName(x)` (if simple set) |
| Factory method | `create*`, `of*`, `from*` | `createUser()` | `makeUser()`, `newUser()` |
| Finder | `find*`, `get*By*` | `findById()` | `searchById()`, `lookupById()` |
| List getter | `list*`, `getAll*` | `listUsers()` | `fetchUsers()`, `retrieveUsers()` |
| Checker | `is*`, `has*`, `can*`, `should*` | `hasPermission()` | `checkPermission()` (if boolean) |
| Action | verb + noun | `saveConfig()` | `configSave()` |
| Converter | `to*`, `as*` | `toString()` | `convertToString()` |
| Parser | `parse*` | `parseJson()` | `readJson()` (if parsing) |
| Validator | `validate*`, `check*` | `validateInput()` | `testInput()` |
| Builder step | noun or adjective | `.withName()` | `.setName()` in builder |

### Consistency Detection

**Scan for inconsistent patterns within same project:**

```
1. List all classes with similar suffixes
2. Group by semantic meaning:
   - *Manager vs *Service → Pick one
   - *Utils vs *Util vs *Helper → Pick one
   - *DTO vs *VO → Pick one
3. Identify minority pattern → Rename to majority
4. If 50/50 split → Follow project conventions or pick more common
```

### Rename Strategy

| Scenario | Action |
|----------|--------|
| Single class rename | Rename file + class + update imports |
| Pattern unification | List all affected classes → batch rename |
| Public API class | **CAUTION** — may break external consumers |
| Internal class | Safe to rename with import updates |

### Batch Rename Workflow

```
1. Identify all classes to rename
2. Generate rename map: OldName → NewName
3. Create plan file entries for each
4. Execute in order:
   a. Rename class declaration
   b. Rename file
   c. Update all imports (batch)
   d. Update all references (grep + replace)
5. Validate build
```

## Package Naming

| Pattern | Example | Notes |
|---------|---------|-------|
| Singular | `util`, `exception` | Preferred in Java |
| Plural | `utils`, `exceptions` | Acceptable, be consistent |
| Abbreviation | `config`, `impl` | Common, accepted |

## File Naming (Non-Java)

| Language | Class/Type | File Pattern |
|----------|------------|--------------|
| Java | `ConfigManager` | `ConfigManager.java` |
| TypeScript | `ConfigManager` | `ConfigManager.ts` or `config-manager.ts` |
| Python | `ConfigManager` | `config_manager.py` |
| Go | `ConfigManager` | `config_manager.go` |
| Rust | `ConfigManager` | `config_manager.rs` |
