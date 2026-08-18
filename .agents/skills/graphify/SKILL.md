---
name: graphify
description: Convert codebases and multi-project repositories into queryable AST-based knowledge graphs using tree-sitter. Use when mapping code architecture, tracing cross-file dependencies, or building project knowledge graphs.
---

# Graphify — AST Codebase Knowledge Graph Skill

Graphify turns source code repositories into deterministic, queryable knowledge graphs without relying on external LLM extractions. It uses **Tree-Sitter** Abstract Syntax Tree (AST) parsers supporting over 40 programming languages (JavaScript, TypeScript, PHP, Kotlin, Java, Python, Solidity, Rust, Go, etc.).

---

## 🚀 When to Use Graphify

1. **Mapping Multi-Project Codebases:** When analyzing interconnected modules across `experience/` subprojects.
2. **Tracing Cross-File Dependencies:** Tracing imports, exports, class hierarchies, and API routes.
3. **Optimizing Context & Token Usage:** Querying the graph schema rather than reading raw bulk files.
4. **Architectural Verification:** Validating separation of concerns (e.g. View ➔ ViewModel ➔ Repository).

---

## 🛠️ Installation & Execution

### 1. Run via `uvx` / `pipx` (No persistent install required)
```bash
# Analyze a specific subproject
uvx graphify analyze "experience/pt-lapantiga-solusi-algoritma/overview-projects/koda-fe-utama/code" --output "output/graphs/koda-fe-utama.json"

# Analyze all projects
uvx graphify analyze "experience/" --output "output/graphs/experience-graph.json"
```

### 2. Install via `pip`
```bash
pip install graphify
graphify --help
```

---

## 📊 Output Formats & Querying

* **JSON Graph (`--format json`):** Nodes representing files, functions, classes, and edges representing imports, calls, inheritance.
* **DOT / Graphviz (`--format dot`):** For rendering visual dependency diagrams.
* **Mermaid (`--format mermaid`):** For embedding in markdown files like `README.md`.

---

## 🤖 AI Workflow Integration

1. **Generate Graph:** Run `graphify analyze <path>` to generate the repository structural map.
2. **Inspect Core Nodes:** Read graph nodes to identify critical controllers, routes, or components.
3. **Targeted Code View:** Open only the relevant source files discovered through the graph traversal.
