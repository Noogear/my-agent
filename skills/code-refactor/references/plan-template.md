# Plan File Template Reference

## Translation Table

| Key | EN | CN |
|-----|----|----|
| `TITLE` | Refactoring Plan | 重构计划 |
| `EDIT_HINT` | Edit this file to customize. Uncheck items to skip. | 编辑此文件自定义。取消勾选跳过项目。 |
| `SAVE_HINT` | Save and reply **"Proceed"** when ready. | 保存后回复 **"继续"** 开始执行。 |
| `PROCEED` | Proceed | 继续 |
| `CANCEL` | Cancel | 取消 |
| `QUICK_WINS` | Quick Wins (Low Risk) | 快速修复（低风险） |
| `CODE_SMELLS` | Code Smell Fixes (Medium Risk) | 代码异味修复（中等风险） |
| `STRUCTURE` | Structure Improvements (Medium-High Risk) | 结构改进（中高风险） |
| `BUNDLE` | Bundle Size Optimization | 包体积优化 |
| `PACKAGE` | Package/Module Reorganization (High Risk) | 包/模块重组（高风险） |
| `DOC` | Documentation Cleanup (Low Risk) | 文档清理（低风险） |
| `CLASS_RESP` | Class Responsibility Reorganization | 类责任重组 |
| `NAMING` | Naming Convention Fixes | 命名规范修复 |
| `CUSTOM` | Custom Items | 自定义项目 |
| `IMPACT_WARN` | ⚠️ Impact | ⚠️ 影响 |
| `IMPACT_SAFE` | ✅ Safe | ✅ 安全 |
| `IMPACT_TEST` | 📋 Tests | 📋 测试 |
| `IMPACT_RISK` | ❌ HIGH RISK | ❌ 高风险 |

## Impact Assessment Markers

Add after each item to show evaluation:

```markdown
- [x] **X.1** Rename `OldClass` → `NewClass`
  > ⚠️ **Impact**: 5 files import this class
  > ✅ **Safe**: No public API change, internal only
  > 📋 **Tests**: Covered by `OldClassTest.java`

- [ ] **X.2** Rename `PublicService` → `CoreService`
  > ❌ **HIGH RISK**: Public API, may break external consumers
  > 📋 **Tests**: No test coverage found
  > 💬 Unchecked by default — requires explicit approval
```

## Unified Template Structure

```markdown
<!-- {TITLE} -->

# 📋 {TITLE}

> {EDIT_HINT}
> {SAVE_HINT}

## 1. {QUICK_WINS} ✨
- [x] **1.1** Remove unused imports — `{file}` ({count} unused)
- [x] **1.2** Remove unused variables — `{varName}` in `{function}()`
- [x] **1.3** Remove dead code — Lines {start}-{end} in `{file}`
- [x] **1.4** Extract magic numbers — `{value}` → `{CONSTANT_NAME}`

## 2. {NAMING} 🏷️
### 2.1 Class Renames (Consistency)
- [x] **2.1.1** Rename `{OldClass}` → `{NewClass}` — {reason}
  > ✅ **Safe**: Internal class, {count} references
  > 📋 **Tests**: Covered
- [x] **2.1.2** Rename `{OldClass}` → `{NewClass}` — {reason}
  > ⚠️ **Impact**: {count} files affected

### 2.2 Pattern Unification
- [x] **2.2.1** Unify `*Util` → `*Utils` — {count} classes
- [x] **2.2.2** Unify `*Manager` → `*Service` — {count} classes

### 2.3 Import Updates
- [x] **2.3.1** Batch update imports — {count} files affected

## 3. {CODE_SMELLS} 🔧
### 3.1 Long Methods
- [x] **3.1.1** Split `{functionName}()` — {lines} lines → extract `{newFunc}()`

### 3.2 Duplicate Code
- [x] **3.2.1** Merge duplicate — `{file1}:{line1}` ≈ `{file2}:{line2}`

### 3.3 Long Parameters
- [x] **3.3.1** Introduce parameter object — Replace `({params})`

## 4. {STRUCTURE} 🏗️
### 4.1 Method Grouping
- [x] **4.1.1** Extract `{UtilName}` — {count} static methods from `{source}`

### 4.2 Class Extraction
- [x] **4.2.1** Extract `{ClassName}` — {description}

## 5. {BUNDLE} 📦➖
### 5.1 Dead Code Removal
- [x] **5.1.1** Remove unused class — `{file}` (0 references)

### 5.2 Class Consolidation
- [x] **5.2.1** Merge small utils — `{class1}` + `{class2}` → `{target}`

### 5.3 Directory Cleanup
- [x] **5.3.1** Consolidate single-class package — `{pkg}/{class}` → `{targetPkg}/`
- [x] **5.3.2** Remove empty directories — {count} folders

## 6. {CLASS_RESP} 🎯
- [x] **6.1** Move `{class}` — `{oldPkg}` → `{newPkg}` ({reason})

## 7. {PACKAGE} 📦
- [x] **7.1** Move `{file}` — `{oldPath}` → `{newPath}`
- [x] **7.2** Create `{folder}/` — Move {count} related files

## 8. {DOC} 📝
- [x] **8.1** Simplify verbose docs — `{file}` ({before} → {after} lines)
- [x] **8.2** Remove redundant tags — {count} files

---

## {CUSTOM}
- [ ] **Custom.1** — Description

---

**Reply:** ✅ `{PROCEED}` — Execute all | ❌ `{CANCEL}` — Abort
```

## Response Patterns

| Pattern | Action |
|---------|--------|
| `Proceed`/`继续`/`OK`/`Go` | Parse & execute checked items |
| `Cancel`/`取消`/`Abort` | Delete file, abort |
| Other | Answer without executing |
