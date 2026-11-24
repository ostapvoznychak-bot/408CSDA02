---
name: project-scaffold
description: Створення мінімального Hello World (Python) з README і .gitignore.
---

# Коли застосовувати
Репозиторій не містить вихідного коду програми hello.

# Вхідні дані
- мова: Python; назва: `hello`
- README: Возничак Остап Маркіянович, КІ-408, варіант 2

# Результат
- `src/hello_app/__init__.py`
- `src/hello_app/cli.py`
- `README.md`
- `.gitignore`
- `.gitignore` з рядками: `.venv/`, `__pycache__/`, `*.egg-info/`, `.pytest_cache/`, `build/`, `dist/`

# Перевірка
1. усі файли з переліку існують
2. `python -m hello_app.cli` друкує `Hello, World!` (якщо потрібне складання – перевірка в build-and-test)
3. повторне застосування не змінює наявні файли

# Приклад
Вхід: «створи проєкт hello мовою Python» → вихід: структура вище й README з ПІБ.

# Типова помилка
README вже існує, і агент перезаписує його. Правильно – доповнити розділи.
