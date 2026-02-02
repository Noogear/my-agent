# Java Comment Cleanup Rules

## Javadoc Minimalism Principle

**Core Rule**: ONE sentence maximum for classes and interfaces.

### Class/Interface Javadoc

```java
// ❌ Before: Verbose
/**
 * This class is responsible for translating messages using
 * the MiniMessage format. It provides various methods to
 * translate keys with placeholders and supports multiple
 * output formats including Component, String, and legacy text.
 * 
 * <p>Features:
 * <ul>
 *   <li>Placeholder support</li>
 *   <li>Multiple formats</li>
 *   <li>Caching</li>
 * </ul>
 * 
 * @author John
 * @version 1.0
 * @since 2024-01-01
 */
public class MiniMessageTranslatorImpl { ... }

// ✅ After: Core summary
/**
 * MiniMessage-based translator implementation.
 */
public class MiniMessageTranslatorImpl implements Translator { ... }
```

### Method Javadoc

```java
// ❌ Before
/**
 * Gets the name of the player.
 * @return the name
 */
public String getName() { return name; }

// ✅ After: No javadoc needed for simple getters
public String getName() { return name; }

// ❌ Before
/**
 * Translates the given key to a Component using the provided
 * placeholders. This method looks up the key in the message
 * source and applies MiniMessage formatting.
 * 
 * @param key the translation key to look up
 * @param placeholders the placeholders to replace
 * @return the translated Component
 */
public Component translate(String key, Object... placeholders);

// ✅ After
/**
 * Translates key to Component with placeholders.
 */
public Component translate(String key, Object... placeholders);
```

### Field Javadoc

```java
// ❌ Before
/** The message source that provides translation strings. */
private final MessageSource source;

// ✅ After
/** Translation string source. */
private final MessageSource source;

// ✅ Or skip entirely for obvious fields
private final MessageSource source;
```

## Comment Elimination Checklist

### Remove These

| Remove | Example |
|--------|---------|
| Author tags | `@author John` |
| Version tags | `@version 1.0` |
| Since tags (usually) | `@since 2024-01-01` |
| See tags (most) | `@see OtherClass` |
| Feature lists | `<ul><li>Feature 1</li>...` |
| Implementation details | "This uses HashMap internally" |
| Obvious descriptions | "Gets the name" for `getName()` |
| History/changelog | "Added in v2.0" |
| Redundant @return | `@return the name` for `getName()` |

### Keep These

| Keep | Reason |
|------|--------|
| Non-obvious behavior | `// Returns empty list, never null` |
| Constraints | `@param file must exist and be readable` |
| Thread safety notes | `// Not thread-safe` |
| Null handling | `@return null if not found` |
| Side effects | `// Modifies input list` |
| Why not what | `// Using LinkedList for O(1) removal` |

## Quick Javadoc Templates

```java
// Class: ONE sentence
/** [What it is/does]. */

// Interface: ONE sentence  
/** Contract for [purpose]. */

// Method (non-trivial): Verb phrase
/** [Verb] [object] [condition/context]. */

// Exception: When thrown
/** Thrown when [condition]. */

// Constant: What it represents
/** [What this value means]. */
```
