# Command Reference

## 1. Overview

| Command | Description | When to use it |
|---|---|---|
| `spawn create` | Scaffold a new Python project interactively | Starting a new project from a template |
| `spawn version` | Print the installed Spawn version | Confirming which version is on your PATH |
| `spawn doctor` | Score the current directory against project health checks | Auditing an existing project's setup |

---

## 2. `spawn create`

Creates a new project directory from a template, writes starter files, optionally runs `git init`, and runs `uv init --bare` + `uv venv`.

### Opening banner

```
╭─────────────────────────────────────────────╮
│ 🚀 Spawn                                    │
│ Create development environments in seconds  │
╰─────────────────────────────────────────────╯
```

### Prompt sequence

| Step | Prompt text | Valid input | On invalid input |
|---|---|---|---|
| 1 | `Project Name:` | Letters, numbers, `-`, `_` only; must contain at least one letter or digit | Re-prompts. Prints error in red (no `❌` prefix): `Project name can only contain letters, numbers, hyphens (-), and underscores (_).` |
| 2 | Template table (see below), then `Choose Template [1-4]:` | `1`, `2`, `3`, or `4` | Re-prompts. Prints error in red: `Invalid choice. Please select a valid number.` |
| 3 | `Initialize Git? [Y/n]:` | `Y` / `y` / Enter (default **Y**), or `N` / `n` | — |
| 4 | `Publish to GitHub? [y/N]:` | Only if Git was enabled. `Y` / `y`, or `N` / `n` / Enter (default **N**) | — |
| 5 | `Repository URL` | See valid URL formats below | Prints `❌ Invalid GitHub repository URL.` |

#### `Project Name:` validation

| Rule | Detail |
|---|---|
| Allowed characters | Letters, numbers, hyphens (`-`), underscores (`_`) |
| Required | At least one letter or digit |
| Rejected examples | `my project` (space), `my/project` (slash), `---` (no alphanumeric) |

**Error message (exact):**

```
Project name can only contain letters, numbers, hyphens (-), and underscores (_).
```

#### Template selection table

```
      Available Templates
┏━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Template      ┃
┡━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ Python Script │
│ 2 │ FastAPI       │
│ 3 │ Data Science  │
│ 4 │ ML Project    │
└───┴───────────────┘
```

| Input | Template key | Display name |
|---|---|---|
| `1` | `python` | Python Script |
| `2` | `fastapi` | FastAPI |
| `3` | `data-science` | Data Science |
| `4` | `ml` | ML Project |

**Invalid input error (exact):**

```
Invalid choice. Please select a valid number.
```

#### `Initialize Git?`

| Answer | Behavior |
|---|---|
| `Y` / Enter | Prints `Initializing Git...` (yellow), runs `git init` |
| `N` | Skips `git init`. After success panel, prints: `ℹ GitHub publishing requires Git. Skipping.` (yellow). Command ends — no GitHub prompt. |

**Git disabled message (exact):**

```
ℹ GitHub publishing requires Git. Skipping.
```

#### `Publish to GitHub?`

Only shown when Git was enabled. Default is **N**.

| Answer | Behavior |
|---|---|
| `N` / Enter | Command ends after success panel |
| `Y` | Prompts `Repository URL`, then runs publish flow |

#### `Repository URL`

| Format | Example |
|---|---|
| HTTPS | `https://github.com/user/repo` |
| HTTPS with `.git` | `https://github.com/user/repo.git` |
| SSH | `git@github.com:user/repo.git` |

**Invalid URL error (exact):**

```
❌ Invalid GitHub repository URL.
```

**Publish success (exact):**

```
🚀 Published successfully!
```

### Success output

Shown after project generation succeeds. Git status reflects your `Initialize Git?` answer.

```
╭────── ✨ Project Created Successfully ──────╮
│                                              │
│  Project      my-api                         │
│  Template     FastAPI                        │
│  Git          ✓ Enabled                      │
│  UV           ✓ Initialized                  │
│  Virtual Env  ✓ Created                      │
│                                              │
│  Next Steps                                  │
│    cd my-api                                 │
│    uv add fastapi uvicorn                    │
│    uv run uvicorn app.main:app --reload      │
│                                              │
╰──────────────────────────────────────────────╯
```

#### Next steps by template

| Template | Next steps lines |
|---|---|
| Python Script | `cd {name}` → `uv run python main.py` |
| FastAPI | `cd {name}` → `uv add fastapi uvicorn` → `uv run uvicorn app.main:app --reload` |
| Data Science | `cd {name}` → `uv add pandas numpy matplotlib` |
| ML Project | `cd {name}` → `uv add pandas numpy scikit-learn` |

### Error cases

All generation errors are prefixed with `❌` in red. The partially created directory is deleted on failure during generation.

| Situation | Message (exact) |
|---|---|
| Directory already exists | `❌ Directory '{name}' already exists.` |
| Git not installed | `❌ Git is not installed or not available in PATH.` |
| Git init failed | `❌ Failed to initialize Git repository.` |
| uv not installed | `❌ UV is not installed or not available in PATH.` |
| uv command failed | `❌ {uv stderr}` or `❌ Failed to initialize UV environment.` |
| Unknown template | `❌ Unknown template: {template}` |
| Invalid GitHub URL | `❌ Invalid GitHub repository URL.` |
| Origin remote already exists | `❌ Origin remote already exists.` |
| Project path missing (publish) | `❌ Project path does not exist: {path}` |
| Not a git repo (publish) | `❌ Project is not a Git repository.` |
| Git command failed (publish) | `❌ {git stderr}` or `❌ Git command failed.` |

---

## 3. `spawn version`

Prints the installed package version.

**Output (exact):**

```
Spawn v0.2.0
```

---

## 4. `spawn doctor`

Scans the **current working directory** for project health indicators and prints a weighted score out of 100.

### All checks

| Check Name | Category | Weight | What it looks for |
|---|---|---|---|
| README.md | Documentation | 10 | `README.md` file exists |
| LICENSE | Documentation | 5 | `LICENSE` file exists |
| Git Repository | Version Control | 15 | `.git/` directory exists |
| .gitignore | Version Control | 10 | `.gitignore` file exists |
| Tests | Quality | 15 | `tests/` directory exists |
| Ruff | Quality | 10 | `ruff.toml`, `.ruff.toml`, or Ruff config/dependency in `pyproject.toml` |
| Pytest | Quality | 10 | `pytest.ini`, `setup.cfg` `[pytest]`, or Pytest config/dependency in `pyproject.toml` |
| Dockerfile | Deployment | 10 | `Dockerfile` file exists |
| GitHub Actions | Deployment | 10 | `.github/workflows/*.yml` or `*.yaml` |
| .env.example | Configuration | 5 | `.env.example` file exists |

**Max score:** 100 (sum of all weights)

### Scoring

| Calculation | Detail |
|---|---|
| Formula | `(sum of passed check weights) / (sum of all weights) × 100` |
| Display | `Project Score: {earned}/{max} ({percent}%)` |

| Score range | Color | Meaning |
|---|---|---|
| 80%+ | Green | Strong project hygiene |
| 50–79% | Yellow | Core setup present, gaps remain |
| 0–49% | Red | Missing multiple essentials |

### Example output

```
╭─────────────── 🏥 Project Health Report ───────────────╮
│                                                          │
│  Documentation                                           │
│  ✓ README.md — Documentation file present               │
│  ⚠ LICENSE — Missing LICENSE file                       │
│                                                          │
│  Version Control                                         │
│  ✓ Git Repository — Git initialized                     │
│  ✓ .gitignore — Git ignore configured                   │
│                                                          │
│  Quality                                                 │
│  ✓ Tests — Test directory configured                    │
│  ✓ Ruff — Ruff configured in pyproject.toml             │
│  ✓ Pytest — Pytest configured in pyproject.toml         │
│                                                          │
│  Deployment                                              │
│  ⚠ Dockerfile — Missing Dockerfile                      │
│  ✓ GitHub Actions — GitHub Actions configured (1 workflow) │
│                                                          │
│  Configuration                                           │
│  ⚠ .env.example — Missing .env.example                  │
│                                                          │
│  Project Score: 70/100 (70%)                            │
╰──────────────────────────────────────────────────────────╯
```

### Recommendations

When any check fails, a second panel lists prioritized fixes (highest priority first):

| Failed check | Recommendation (exact) |
|---|---|
| Git Repository | `Initialize a git repository with 'git init'` |
| README.md | `Add a README.md file to document your project` |
| Tests | `Create a tests/ directory and add test files` |
| .gitignore | `Add a .gitignore file to exclude unnecessary files from version control` |
| Pytest | `Configure Pytest in pyproject.toml or create pytest.ini` |
| Ruff | `Configure Ruff linter in pyproject.toml for code quality` |
| GitHub Actions | `Set up GitHub Actions in .github/workflows/ for CI/CD` |
| Dockerfile | `Add a Dockerfile for containerized deployment` |
| LICENSE | `Add a LICENSE file to specify usage terms` |
| .env.example | `Create a .env.example file to document required environment variables` |
| Other | `Address: {check name}` |

**Recommendations panel title:** `💡 Recommendations`

---

## 5. Exit codes

Spawn does not call `sys.exit()` on handled errors. Caught exceptions print a message and return normally.

| Situation | Exit code |
|---|---|
| Command completes successfully | 0 |
| `spawn create` — `SpawnError` caught (directory exists, Git/uv missing, unknown template) | 0 |
| `spawn create` — `GitHubPublishError` caught (invalid URL, origin exists, publish failure) | 0 |
| Uncaught exception (e.g. keyboard interrupt) | 1 |
