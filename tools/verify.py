from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool) -> bool:
    print(f"{'PASS' if condition else 'FAIL'}: {label}")
    return condition


results: list[bool] = []

project_files = [
    "src/hello_app/__init__.py",
    "src/hello_app/cli.py",
    "src/hello_app/core.py",
    "tests/test_core.py",
    "pyproject.toml",
    "ci.sh",
    "ci.bat",
    "tools/verify.py",
]
results.append(check("generated project files", all((ROOT / path).is_file() for path in project_files)))

agent_files = [
    ".github/agents/build-engineer.agent.md",
    ".github/skills/project-scaffold/SKILL.md",
    ".github/skills/build-and-test/SKILL.md",
    ".github/skills/github-actions/SKILL.md",
]
agent_files.extend(
    f".github/prompts/{name}.prompt.md"
    for name in ("git-init", "create-project", "create-build", "create-actions", "check", "init")
)
results.append(check("manifest, skills, and command files", all((ROOT / path).is_file() for path in agent_files)))

gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8") if (ROOT / ".gitignore").is_file() else ""
results.append(check(".venv/ ignored", ".venv/" in gitignore))
results.append(check("__pycache__/ ignored", "__pycache__/" in gitignore))

workflow_path = ROOT / ".github/workflows/ci.yml"
workflow = workflow_path.read_text(encoding="utf-8") if workflow_path.is_file() else ""
for os_name in ("ubuntu-latest", "windows-latest", "macos-latest"):
    results.append(check(f"{os_name} in CI", os_name in workflow))
results.append(check("CI delegates to build scripts", "bash ci.sh" in workflow and "ci.bat" in workflow))

sys.exit(0 if all(results) else 1)
