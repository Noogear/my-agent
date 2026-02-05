# Class Responsibility Reference

## Responsibility Pattern Detection

| Pattern | Expected Location | Detection |
|---------|-------------------|-----------|
| `*Utils`, `*Helper` | `util/` | All static methods, no state |
| `*Service` | `service/` | Business logic, orchestration |
| `*Repository`, `*Dao` | `repository/` | Data access |
| `*Controller`, `*Handler` | `controller/` | Request handling |
| `*Config` | `config/` | Configuration |
| `*Factory` | `factory/` | Object creation |
| `*Builder` | `builder/` | Fluent builders |
| `*Validator` | `validator/` | Validation logic |
| `*Converter`, `*Mapper` | `converter/` | Type conversion |
| `*Exception` | `exception/` | Custom exceptions |
| `*Event`, `*Listener` | `event/` | Event system |
| `*DTO`, `*VO`, `*Entity` | `model/` | Data objects |
| `interface *` (API) | `api/` | Public interfaces |
| `*Impl` | `impl/` | Interface implementations |

## Move Decision Flow

```
For each class:
1. Extract responsibility from name/content
2. Determine expected package
3. If current ≠ expected → Add to move plan
4. If multiple responsibilities → Add to split plan
```

## Execution Order

1. Create new packages/directories first
2. Move simple classes (no moved-class dependencies)
3. Move complex classes
4. Batch update all imports (one multi_replace)
5. Verify no circular dependencies
