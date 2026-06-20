<div align="center">

# Spawn

> You shouldn't need 7 commands to start a project.

[![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat-square)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![uv](https://img.shields.io/badge/Powered%20by-uv-orange?style=flat-square)](https://github.com/astral-sh/uv)

![Spawn Preview](assets/preview.png)

</div>

---

`mkdir`. `cd`. `git init`. `python -m venv`. `source .venv/activate`. `touch .gitignore`...

And you still haven't written a single line of actual code.

**Spawn does all of that in one command — and it looks good doing it.**

```bash
spawn create
```

Pick a template. Answer two questions. Walk into a ready-to-build project.

---

## Try It

**You'll need:** Python 3.12+, [uv](https://github.com/astral-sh/uv), Git

```bash
git clone https://github.com/Abhiix0/Spawn.git
cd Spawn
uv sync
uv tool install .
```

Then run `spawn create` and see what happens.

---

## What Spawn Sets Up

No spoilers on the full output — but after one command you'll have:

- A project structure that actually makes sense
- Git initialized (if you want it)
- A virtual environment ready to go
- The exact next commands printed for you — no guessing

There are 4 templates. You'll figure out which one fits.

---

## What's Coming

Some things are already in the works. Clone the repo and check the roadmap — there might be something you want to build.

---

[![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
