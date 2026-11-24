---
name: build-and-test
description: Налаштування складання (venv + скрипт запуску, pytest), тест BasicAddition.
---

# Коли застосовувати
Після project-scaffold, коли немає системи складання або тестів.

# Вхідні дані
Каркас проєкту від `project-scaffold`.

# Результат
- `pyproject.toml` (PEP 621, backend setuptools>=61): name = "hello-app", version = "0.1.0",
  `requires-python = ">=3.9"`, `[project.optional-dependencies] test = ["pytest>=7"]`,
  `[project.scripts] hello = "hello_app.cli:main"` – саме це створює виконуваний файл `hello`;
  `[tool.setuptools.packages.find] where = ["src"]`, `[tool.pytest.ini_options] testpaths = ["tests"]`.
- `src/hello_app/core.py`: `def add(a: int, b: int) -> int`.
- `tests/test_core.py`: функція `test_BasicAddition` (`add(2, 3) == 5`) і ще щонайменше один тест (від'ємні числа).
- `ci.sh` (bash, `set -euo pipefail`) і `ci.bat` (`setlocal`, перевірка `%ERRORLEVEL%` після кожної команди):
  1) `python -m venv .venv`; 2) `pip install -e ".[test]"`; 3) `python -m pytest -v`; 4) запуск `hello`.
- Скрипт перевірки `python tools/verify.py`: нічого не змінює; FAIL, якщо бракує файлів проєкту/агента, рядків `.venv/`, `__pycache__/` у `.gitignore`, однієї з трьох ОС у `ci.yml` або якщо `ci.yml` містить власні команди складання; друкує PASS/FAIL на кожен пункт.

# Перевірка
1. `ci.sh` (Windows: `ci.bat`) завершується з кодом 0
2. є виконуваний файл: .venv/bin/hello (Windows: .venv\Scripts\hello.exe)
3. тест `tests/test_core.py::test_BasicAddition` – passed
4. `.venv/ та build/` ігнорується Git

# Приклад
Після каркаса → успішне складання і звіт тестів з BasicAddition passed.

# Типова помилка
Тест не знайдено (0 tests) – виправити назву/шлях тесту, тести не вимикати.
