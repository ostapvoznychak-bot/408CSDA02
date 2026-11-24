---
name: git-init
description: "Перевірка репозиторію, .gitignore і стану Git."
disable-model-invocation: true
---
# /git-init

**Передумови:** немає.

**Дії:**
1. Якщо `.git` немає – `git init -b develop`, інакше нічого не змінювати.
2. Доповнити `.gitignore` рядками: `.venv/`, `__pycache__/`, `*.egg-info/`, `.pytest_cache/`, `build/`, `dist/`.
3. Показати `git status --short --branch`.

**Очікувані файли:** `.gitignore`.

**Перевірка:** git status без помилок, .gitignore повний.

**Помилка:** репозиторій недоступний – зупинка.

Повторний запуск безпечний: наявні файли не руйнуються, конфігурація не дублюється.
