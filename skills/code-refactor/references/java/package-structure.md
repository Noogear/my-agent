# Java Package Structure Reorganization

## Quick Classification Table

| Class Pattern | Target Package | Detection Keywords |
|--------------|----------------|-------------------|
| `*Utils`, `*Helper` | `util/` | static methods only, no state |
| `@interface *` | `annotation/` | annotation definition |
| `*Exception`, `*Error` | `exception/` | extends Throwable |
| `interface *` (API) | `api/` | public contract, no impl |
| `*Impl`, `*Default*` | `impl/` | implements interface |
| `*DTO`, `*VO`, `*Entity` | `model/` | data holder, getters/setters |
| `*Config`, `*Settings` | `config/` | configuration values |
| `*Event`, `*Listener` | `event/` | event system |
| `*Handler`, `*Processor` | `handler/` | handles/processes something |
| `*Factory` | `factory/` | creates objects |
| `*Builder` | `builder/` | fluent build pattern |
| `*Serializer`, `*Codec` | `serializer/` | serialize/deserialize |
| `*Validator`, `*Checker` | `validator/` | validation logic |
| `*Adapter`, `*Wrapper` | `adapter/` | adapts interface |
| `*Registry`, `*Manager` | `registry/` | manages instances |
| `*Service` | `service/` | business logic |
| `*Repository`, `*Dao` | `repository/` | data access |
| `*Controller` | `controller/` | request handling |
| `*Converter`, `*Mapper` | `converter/` | type conversion |
| `*Provider`, `*Supplier` | `provider/` | supplies instances |

## Class Detection Examples

```java
// → util/
public final class StringUtils {
    private StringUtils() {}  // private constructor
    public static String trim(String s) { ... }  // all static
}

// → annotation/
@Retention(RetentionPolicy.RUNTIME)
public @interface Check { ... }

// → exception/
public class ConfigException extends RuntimeException { ... }

// → api/
public interface Translator { Component translate(String key); }

// → impl/
public class MiniMessageTranslatorImpl implements Translator { ... }

// → model/
public record UserDTO(String name, int age) {}
public class ConfigData { private String value; /* getters/setters */ }

// → factory/
public class TranslatorFactory {
    public static Translator create(Type type) { ... }
}

// → builder/
public class WindowBuilder {
    public WindowBuilder title(String t) { ...; return this; }
    public Window build() { ... }
}
```

## Move Decision Flow

```
1. Is it an annotation? → annotation/
2. Is it an exception? → exception/
3. Is it an interface without impl? → api/
4. Is it implementing an interface in api/? → impl/
5. Is class name ending with Utils/Helper AND all methods static? → util/
6. Is it a pure data holder (record/POJO)? → model/
7. Does it create other objects? → factory/
8. Does it use fluent API returning this? → builder/
9. Does it validate something? → validator/
10. Does it convert types? → converter/
11. None of above → Keep in current location
```

## Move Execution Checklist

```bash
# Step 1: Create target directory
mkdir -p src/main/java/package/util

# Step 2: Move file
git mv OldPath.java NewPath.java

# Step 3: Update package declaration in moved file
# package old.package; → package new.package;

# Step 4: Find and update all imports
grep -r "import old.package.ClassName" --include="*.java" -l

# Step 5: Verify build
./gradlew build

# Step 6: Commit
git commit -m "refactor: move ClassName to util package"
```
