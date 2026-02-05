# Bundle Size Optimization Reference

## Dead Code Elimination

| Target | Detection | Action |
|--------|-----------|--------|
| Unused classes | No references anywhere | Delete entire file |
| Unused methods | Private + no internal calls | Delete method |
| Unused fields | Private + never read/written | Delete field |
| Unused dependencies | No class from dep is used | Remove from build file |

## Class Count Reduction

| Pattern | Before | After |
|---------|--------|-------|
| Merge tiny utils | 3 files × 2 methods | 1 file × 6 methods |
| Inline single-use class | Helper used once | Inline to caller |
| Convert class to static methods | Stateless service | Utility methods |
| Use lambdas over anonymous | `new Runnable() {...}` | `() -> {...}` |

**DO NOT merge if:**
- Classes have different responsibilities
- Classes are in public API
- Classes are used in tests separately

## Abstraction Overhead Reduction

| Over-abstraction | Simpler Alternative |
|------------------|---------------------|
| Interface + 1 impl | Just the implementation |
| Abstract class + 1 child | Merge into single class |
| Factory for 1 product | Direct instantiation |
| Builder for simple object | Constructor or static factory |

## Constant & String Optimization

| Issue | Optimization |
|-------|--------------|
| Repeated string literals | Extract to `static final` |
| String concat in loop | Use `StringBuilder` |
| Debug-only strings | Remove or conditional |

## Dependency Alternatives

| Heavy Dependency | Lighter Alternative |
|------------------|---------------------|
| Guava (2.5MB) | Java stdlib |
| Apache Commons Lang | Java stdlib |
| Jackson (large) | Gson (smaller) |
| Lombok | IDE generation (no runtime) |

**Gradle exclusion example:**
```groovy
implementation('some:library') {
    exclude group: 'unused.transitive', module: 'dep'
}
```

## Bytecode-Level Optimizations

| Technique | Impact | How |
|-----------|--------|-----|
| Use primitives | Less boxing | `int` vs `Integer` |
| Avoid varargs in hot paths | Array allocation | Provide overloads |
| Final classes/methods | JIT inlining | Add `final` |
| Static methods | No `this` reference | Convert stateless |
| Avoid reflection | Code + metadata | Use direct calls |

## Single-Class Package Rules

| Package Type | Min Classes | Action if Below |
|--------------|-------------|-----------------|
| `util/` | 3 | Merge with parent |
| `exception/` | 2 | Keep (special) |
| `model/dto/` | 2 | Merge with `model/` |
| `api/` | 1 | Keep (API stability) |
| Other | 2 | Consider merging |

**Keep single-class if:** Part of public API, documented future expansion, or framework convention.

## Empty Directory Cleanup

```bash
# Find empty directories (bash)
find src -type d -empty -delete

# PowerShell
Get-ChildItem -Directory -Recurse | Where-Object { (Get-ChildItem $_.FullName).Count -eq 0 } | Remove-Item
```

## Measurement Commands

```bash
# Gradle
./gradlew build && ls -lh build/libs/*.jar

# Maven
mvn package && ls -lh target/*.jar

# Node.js
npm run build && du -sh dist/
```
