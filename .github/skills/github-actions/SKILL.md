---
name: github-actions
description: Workflow CI на трьох ОС; workflow запускає лише скрипти збірки.
---

# Коли застосовувати
Після того як `ci.sh` і `ci.bat` працюють локально.

# Вхідні дані
Робочі скрипти збірки.

# Результат
`.github/workflows/ci.yml`:
- `on`: push і pull_request у `develop`, `master`;
- одна job `build-test`, `strategy.matrix.os: [ubuntu-latest, windows-latest, macos-latest]`, `fail-fast: false`;
- кроки: `actions/checkout@v4`; середовище – actions/setup-python@v5 з python-version: '3.12'; запуск `bash ./ci.sh` (Linux/macOS) або `.\ci.bat` (Windows) за умовою `runner.os`;
- `actions/upload-artifact@v4` з виконуваним файлом hello; `permissions: contents: read`; без секретів.

# Перевірка
1. YAML коректний
2. є всі три ОС
3. немає власних команд складання – лише виклик скриптів
4. у GitHub Actions усі job зелені

# Приклад
Push у feature-гілку → три job успішні.

# Типова помилка
На Windows скрипт не запускається – виклик через інтерпретатор і `.gitattributes`.
