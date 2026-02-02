# Java Code Smell Detection

## Code Smell Detection Patterns

| Smell | Detection Pattern | Severity |
|-------|-------------------|----------|
| **Long Method** | >30 lines or >3 levels of nesting | High |
| **Large Class** | >300 lines or >10 public methods | High |
| **Duplicate Code** | 3+ identical lines appearing 2+ times | High |
| **Feature Envy** | Method uses another class's data more than its own | Medium |
| **Data Clump** | Same 3+ params appear together repeatedly | Medium |
| **Primitive Obsession** | Using primitives instead of small objects | Medium |
| **Long Parameter List** | >4 parameters | Medium |
| **Dead Code** | Unreachable/unused code | Low |
| **Speculative Generality** | Unused abstractions "for future use" | Low |

## Quick Wins (Fix First)

| Issue | Action |
|-------|--------|
| Unused imports | Delete |
| Unused private methods | Delete |
| Unused variables | Delete |
| Magic numbers | Extract to constants |

## Anti-Patterns to Fix

| Anti-Pattern | Fix |
|--------------|-----|
| `if (x) return true; else return false;` | `return x;` |
| `if (x == true)` | `if (x)` |
| `if (x == false)` | `if (!x)` |
| `str.equals("")` | `str.isEmpty()` |
| `list.size() == 0` | `list.isEmpty()` |
| `obj.toString().equals(...)` | Use proper equals |
| `catch (Exception e) { }` | Log or rethrow |
| `new Integer(x)` | `Integer.valueOf(x)` |
| `"" + number` | `String.valueOf(number)` |
| Double-checked locking wrong | Use `volatile` or holder pattern |

## Duplicate Code Types

```java
// Type 1: Exact Clone - identical code
// Action: Extract Method immediately

// Type 2: Renamed Clone - same structure, different names
void processUser(User u) { validate(u); save(u); log(u); }
void processOrder(Order o) { validate(o); save(o); log(o); }
// Action: Extract generic method with type parameter

// Type 3: Near Clone - minor differences
if (user != null && user.isActive()) { ... }
if (order != null && order.isValid()) { ... }
// Action: Extract with functional parameter

// Type 4: Semantic Clone - different code, same purpose
// Action: Keep one, delete others
```

## Refactoring Techniques

| Technique | When to Use | Example |
|-----------|-------------|---------|
| Extract Method | Same class, 3+ duplicate lines | `calculateTotal()` |
| Extract Superclass | Related classes share behavior | `AbstractProcessor` |
| Extract Interface | Need polymorphism | `Validatable` |
| Template Method | Same algorithm, different steps | `process()` + `doProcess()` |
| Strategy Pattern | Interchangeable algorithms | `SortStrategy` |
| Introduce Parameter Object | 3+ params always together | `DateRange(start, end)` |
