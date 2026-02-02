# Java Method Grouping & Utility Extraction

## Method Grouping Categories

| Category | Examples | Target Class |
|----------|----------|--------------|
| IO Operations | File read/write, stream processing | `FileUtils` / `IOUtils` |
| String Processing | Parsing, formatting, validation | `StringUtils` / `TextUtils` |
| Collection Operations | Filtering, transformation, aggregation | `CollectionUtils` |
| Reflection Utilities | Field access, type checking | `ReflectionUtils` |
| Validation Logic | Null checks, range checks, format checks | `Preconditions` / `Validators` |
| Conversion Logic | Type casting, DTO mapping | `Converters` |
| Date/Time | Formatting, parsing, calculations | `TimeUtils` |

## Utility Class Extraction Decision Tree

```
Is method stateless (no instance fields used)?
├─ Yes → Candidate for utility class
│   └─ Used by 2+ classes? → Extract to shared util
│   └─ Used by 1 class only? → Keep as private static
└─ No → Keep as instance method
    └─ Used by child classes? → Consider protected
```

## Utility Class Pattern

```java
// Correct utility class structure
public final class StringUtils {
    
    private StringUtils() {
        // Prevent instantiation
    }
    
    public static String normalize(String input) {
        return input == null ? "" : input.toLowerCase().trim();
    }
    
    public static boolean isValidLength(String input, int maxLength) {
        return input != null && !input.isEmpty() && input.length() <= maxLength;
    }
}
```

## Method Organization Within Class

Organize methods in this order:

```java
public class ExampleClass {
    
    // ========== Static Fields ==========
    private static final Logger LOGGER = LoggerFactory.getLogger(ExampleClass.class);
    
    // ========== Instance Fields ==========
    private final String name;
    private int count;
    
    // ========== Constructors ==========
    public ExampleClass(String name) {
        this.name = name;
    }
    
    // ========== Lifecycle Methods ==========
    public void init() { }
    public void shutdown() { }
    
    // ========== Public API ==========
    public void process() { }
    public String getName() { return name; }
    
    // ========== Protected Methods ==========
    protected void onEvent() { }
    
    // ========== Private Methods ==========
    private void doInternalWork() { }
    
    // ========== Static Methods ==========
    public static ExampleClass create() { }
}
```
