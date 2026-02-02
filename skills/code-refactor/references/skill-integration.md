# Skill Integration Guide

## Purpose

This guide describes how to integrate with other skills for domain-specific refactoring knowledge.

## Skill Discovery

Check for related skills based on project context:

### Detection Flow

```
1. Identify project type (language, framework)
2. Check user's skill directory for relevant skills
3. Load skill SKILL.md for domain patterns
4. Incorporate patterns into refactoring checklist
```

### Common Skill Locations

| OS | Skill Directory |
|----|-----------------|
| Windows | `%USERPROFILE%\.copilot\skills\` |
| macOS/Linux | `~/.copilot/skills/` |

## Language/Framework Skill Mapping

| Project Type | Related Skills | What to Extract |
|-------------|----------------|-----------------|
| Minecraft Paper Plugin | `paper-plugin-dev` | Paper API patterns, Folia compatibility, event handling |
| VS Code Extension | `vscode-extension` | VS Code API patterns, activation events |
| React/Vue/Angular | `frontend-dev` | Component patterns, state management |
| Spring Boot | `spring-boot` | Bean patterns, DI conventions |
| FastAPI/Flask | `python-web` | Route patterns, dependency injection |

## Integration with paper-plugin-dev (Example)

When refactoring a Paper plugin project:

1. **Detect**: Find `paper-api` in dependencies
2. **Load**: Read `paper-plugin-dev` skill if available
3. **Apply**: Use skill-specific patterns:
   - Use entity schedulers instead of sync schedulers (Folia)
   - Follow Adventure API patterns
   - Respect event priority conventions
   - Use proper ComponentLogger patterns

## Integration with Project Instructions

### Priority Chain

```
.github/copilot-instructions.md  →  Skill files  →  Default patterns
        (Highest)                    (Medium)        (Lowest)
```

### Conflict Resolution

If project instructions contradict skill patterns:
- **Follow project instructions** — They represent intentional project decisions
- **Note the conflict** — Mention in checklist for user awareness

## Skill Loading Protocol

```
1. DO NOT load skills unnecessarily (context budget)
2. Load only when project type matches skill domain
3. Read only relevant sections (use TOC if available)
4. Cache extracted patterns for session
```

## Example: Skill-Aware Checklist

```markdown
## 3.1 Method Grouping
- [ ] **3.1.1 Extract `GuiUtils`** — 4 GUI helper methods
  - ⚠️ Per `paper-plugin-dev`: Use entity schedulers, not sync schedulers
  - ⚠️ Per `paper-plugin-dev`: Prefer ItemBuilder.from() pattern
```

## Skills That May Provide Refactoring Context

| Skill Name | Provides |
|------------|----------|
| `paper-plugin-dev` | Minecraft/Paper patterns, Folia compatibility |
| `vscode-extension` | VS Code extension patterns |
| `react-dev` | React component patterns |
| `api-design` | REST/GraphQL API patterns |
| `database-patterns` | Repository/DAO patterns |
