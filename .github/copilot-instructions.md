# Copilot instructions

## Repository purpose

This repository contains a GitHub Copilot custom agent for building a small cross-platform Python Hello World project. The agent is organized around a manifest, skills, and command prompts:

- `.github/agents/build-engineer.agent.md` defines the agent role and completion criteria.
- `.github/skills/<skill>/SKILL.md` defines reusable implementation procedures.
- `.github/prompts/*.prompt.md` define the `/init`, `/git-init`, `/create-project`, `/create-build`, `/create-actions`, and `/check` commands.
- `docs/architecture.md` describes the component and orchestration model.

The `/init` command runs the stages in this order: `git-init` -> `create-project` -> `create-build` -> `create-actions` -> `check`. Stop at the first failed stage and report the step, command, output, and cause. Re-running an orchestration step must be safe and must not overwrite or duplicate existing configuration.

## Current state

The repository is primarily an agent template; the generated Python application and CI files may not exist until the agent stages are run. The expected generated structure includes:

- `src/hello_app/cli.py` - prints `Hello, World!`
- `src/hello_app/core.py` - contains `add(a: int, b: int) -> int`
- `tests/test_core.py` - includes `test_BasicAddition`
- `pyproject.toml` - PEP 621 package configuration and the `hello` script entry point
- `ci.sh` and `ci.bat` - platform-specific build/test scripts
- `.github/workflows/ci.yml` - the cross-platform GitHub Actions workflow
- `tools/verify.py` - repository and generated-project verification

Do not treat prompt or generated-file paths as present merely because they are named in the design documents. Inspect the working tree before changing or invoking a stage.

## Build, test, and verification commands

After `create-build` has generated the project, use:

- Linux/macOS: `./ci.sh`
- Windows: `ci.bat`
- Verification only, without changing files: `python tools/verify.py`
- Repository status including ignored build outputs: `git status --ignored --short`

The build scripts are the source of truth for a full build. They create `.venv`, install `.[test]` in editable mode, run pytest, and invoke the `hello` executable.

With the project environment created, run the full test suite on any platform with:

```text
.venv/bin/python -m pytest -v
```

On Windows, use `.venv\Scripts\python.exe -m pytest -v`.

Run one test with:

```text
.venv/bin/python -m pytest -v tests/test_core.py::test_BasicAddition
```

On Windows:

```text
.venv\Scripts\python.exe -m pytest -v tests/test_core.py::test_BasicAddition
```

Before `ci.sh`, `ci.bat`, `pyproject.toml`, or `tools/verify.py` exist, these commands cannot be run; first apply the corresponding agent skill or prompt stage. No dedicated linter or formatting command is currently defined.

## Architecture and data flow

The agent uses the filesystem as shared state between stages:

1. `git-init` initializes Git only when `.git` is absent and completes `.gitignore`.
2. `project-scaffold` creates the minimal Python source and README.
3. `build-and-test` creates packaging metadata, tests, and platform build scripts.
4. `github-actions` creates a matrix workflow that delegates commands to `ci.sh` or `ci.bat`.
5. `check` validates the template and generated project without modifying files.

Skills contain the detailed expected file contents and validation rules. Read the applicable skill before editing a generated-project area. The custom agent manifest in `.github/agents/build-engineer.agent.md` is the highest-level constraint for this repository's generated output.

## Repository-specific conventions

- Preserve and append to existing files rather than replacing them; repeated `/init` runs must remain idempotent.
- Paths in agent instructions and generated scripts are relative to the repository root.
- Keep `.venv/`, `__pycache__/`, `*.egg-info/`, `.pytest_cache/`, `build/`, and `dist/` ignored.
- Use CRLF for `.bat` files and LF for `.sh` files, as configured in `.gitattributes`.
- Package Python source under `src/hello_app`; do not move or duplicate it at the repository root.
- Configure `[tool.setuptools.packages.find]` with `where = ["src"]` and `testpaths = ["tests"]`.
- The package entry point must be `hello = "hello_app.cli:main"` and must print exactly `Hello, World!`.
- The required pytest test name is `test_BasicAddition`.
- Build scripts must stop on errors: use `set -euo pipefail` in `ci.sh` and check `ERRORLEVEL` after commands in `ci.bat`.
- CI must build only through `ci.sh` or `ci.bat`; do not add duplicate pip, pytest, or hello commands directly to `.github/workflows/ci.yml`.
- GitHub Actions should cover `ubuntu-latest`, `windows-latest`, and `macos-latest`, use Python 3.12, and set `permissions: contents: read`.
- Verification must be read-only and must print PASS/FAIL for each check.
- Record `/init` completion or failures in `docs/ai-log.md` according to the existing table format.
- Never add secrets or tokens, add build outputs to Git, reset the repository, clean Git state, or force-push.
