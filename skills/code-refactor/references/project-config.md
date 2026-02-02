# Project Configuration Integration Guide

## Purpose

This guide describes how to extract refactoring rules from project configuration files across different languages and frameworks.

## Universal Configuration Files

### EditorConfig (`.editorconfig`)

Applies to all languages:

| Property | Refactoring Impact |
|----------|-------------------|
| `indent_style` | Indentation after refactor |
| `indent_size` | Indentation level |
| `max_line_length` | Line wrapping decisions |
| `trim_trailing_whitespace` | Whitespace cleanup |

### Git Configuration

| File | What to Check |
|------|---------------|
| `.gitignore` | What files to skip |
| `.gitattributes` | Line ending treatment |

### Project Instructions

| File | Priority | Purpose |
|------|----------|---------|
| `.github/copilot-instructions.md` | **HIGH** | Project-specific AI instructions |
| `CONTRIBUTING.md` | Medium | Contribution guidelines, code style |
| `styleguide.md` | Medium | Custom style guidelines |
| `CODE_OF_CONDUCT.md` | Low | Usually not relevant |

---

## Language-Specific Configurations

### Java

See [java/project-config.md](java/project-config.md) for:
- Checkstyle integration
- Maven/Gradle settings
- IDE configurations

### TypeScript/JavaScript

| Config File | Key Rules |
|-------------|-----------|
| `.eslintrc.*` | `max-lines-per-function`, `complexity`, `max-params` |
| `.prettierrc` | `printWidth`, `tabWidth`, `singleQuote` |
| `tsconfig.json` | `strict`, module settings |
| `package.json` | `eslintConfig`, `prettier` sections |

**ESLint Rules to Extract:**
```json
{
  "rules": {
    "max-lines-per-function": ["warn", 50],  // → Method split threshold
    "complexity": ["warn", 10],              // → Complexity reduction
    "max-params": ["warn", 4]                // → Parameter object threshold
  }
}
```

### Python

| Config File | Key Rules |
|-------------|-----------|
| `pyproject.toml` | `[tool.black]`, `[tool.isort]`, `[tool.ruff]` |
| `.flake8` | `max-line-length`, `max-complexity` |
| `setup.cfg` | Legacy config location |
| `.pylintrc` | Pylint configuration |

**pyproject.toml Rules to Extract:**
```toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
select = ["E", "F", "C90"]  # C90 = mccabe complexity

[tool.ruff.mccabe]
max-complexity = 10  # → Complexity threshold
```

### Go

| Config File | Key Rules |
|-------------|-----------|
| `.golangci.yml` | Linter configurations |

### Rust

| Config File | Key Rules |
|-------------|-----------|
| `rustfmt.toml` | `max_width`, `imports_granularity` |
| `clippy.toml` | Clippy lint levels |

---

## Integration Workflow

```
1. Scan project root for config files
2. Parse detected configs
3. Extract thresholds and rules
4. Incorporate into checklist generation
5. After refactoring, validate against same rules
```

## Priority Order

When rules conflict:

1. **Project-specific** (`.github/copilot-instructions.md`) — Highest
2. **Linter configs** (`checkstyle.xml`, `.eslintrc`) — High
3. **Formatter configs** (`.prettierrc`, `rustfmt.toml`) — Medium
4. **Editor configs** (`.editorconfig`) — Low
5. **Default heuristics** — Lowest

## Default Thresholds (When No Config Found)

| Metric | Default | Usage |
|--------|---------|-------|
| Method/Function length | 30 lines | Split if exceeds |
| Class/Module size | 300 lines | Consider extraction |
| Parameter count | 4 params | Introduce param object |
| Nesting depth | 3 levels | Extract nested branches |
| Cyclomatic complexity | 10 | Simplify logic |
| Duplicate lines | 3+ lines, 2+ occurrences | Extract common code |
