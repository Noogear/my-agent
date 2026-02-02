# Java Project Configuration Integration

## Configuration Files to Read

Before refactoring, check for and read these configuration files:

### Checkstyle (`checkstyle.xml`, `config/checkstyle/checkstyle.xml`)

Extract these rules for refactoring decisions:

| Module | Rule | Refactoring Impact |
|--------|------|-------------------|
| `LineLength` | `max` attribute | Method splitting threshold |
| `MethodLength` | `max` attribute | When to extract methods |
| `ParameterNumber` | `max` attribute | When to introduce parameter objects |
| `CyclomaticComplexity` | `max` attribute | Nesting reduction priority |
| `ImportOrder` | Group order | Import organization |
| `MemberName` | Pattern | Variable renaming |
| `ConstantName` | Pattern | Constant naming conventions |
| `JavadocMethod` | Scope | Which methods need docs |

**Example: Extracting Checkstyle rules**
```xml
<!-- If checkstyle has: -->
<module name="MethodLength">
    <property name="max" value="50"/>
</module>

<!-- Then flag methods > 50 lines for splitting -->
```

### EditorConfig (`.editorconfig`)

| Property | Refactoring Impact |
|----------|-------------------|
| `indent_size` | Code formatting after refactor |
| `max_line_length` | Line wrapping decisions |
| `insert_final_newline` | File endings |

### Gradle/Maven Build Files

| File | What to Extract |
|------|-----------------|
| `build.gradle` | Source compatibility, dependencies |
| `pom.xml` | Java version, plugin configurations |
| `gradle.properties` | Custom properties |

### IDE Settings (if present)

| File | What to Extract |
|------|-----------------|
| `.idea/codeStyles/` | IntelliJ code style |
| `.vscode/settings.json` | VS Code Java settings |

## Integration Workflow

1. **Detect**: Find config files in project root and `config/` directory
2. **Parse**: Extract relevant rules
3. **Apply**: Use extracted thresholds in checklist generation
4. **Validate**: After refactoring, run linter to verify compliance

## Example Config-Aware Checklist Items

```markdown
## 2.1 Long Methods (Checkstyle: max 50 lines)
- [ ] **2.1.1 Split `processData()`** — 85 lines (exceeds 50) → extract...
```

Instead of hardcoded thresholds, use project-specific values.
