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
| `CUSTOM` | Custom Items | 自定义项目 |

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

## 2. {CODE_SMELLS} 🔧
### 2.1 Long Methods
- [x] **2.1.1** Split `{functionName}()` — {lines} lines → extract `{newFunc}()`

### 2.2 Duplicate Code
- [x] **2.2.1** Merge duplicate — `{file1}:{line1}` ≈ `{file2}:{line2}`

### 2.3 Long Parameters
- [x] **2.3.1** Introduce parameter object — Replace `({params})`

## 3. {STRUCTURE} 🏗️
### 3.1 Method Grouping
- [x] **3.1.1** Extract `{UtilName}` — {count} static methods from `{source}`

### 3.2 Class Extraction
- [x] **3.2.1** Extract `{ClassName}` — {description}

## 4. {BUNDLE} 📦➖
### 4.1 Dead Code Removal
- [x] **4.1.1** Remove unused class — `{file}` (0 references)

### 4.2 Class Consolidation
- [x] **4.2.1** Merge small utils — `{class1}` + `{class2}` → `{target}`

### 4.3 Directory Cleanup
- [x] **4.3.1** Consolidate single-class package — `{pkg}/{class}` → `{targetPkg}/`
- [x] **4.3.2** Remove empty directories — {count} folders

## 5. {CLASS_RESP} 🎯
- [x] **5.1** Move `{class}` — `{oldPkg}` → `{newPkg}` ({reason})

## 6. {PACKAGE} 📦
- [x] **6.1** Move `{file}` — `{oldPath}` → `{newPath}`
- [x] **6.2** Create `{folder}/` — Move {count} related files

## 7. {DOC} 📝
- [x] **7.1** Simplify verbose docs — `{file}` ({before} → {after} lines)
- [x] **7.2** Remove redundant tags — {count} files

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
