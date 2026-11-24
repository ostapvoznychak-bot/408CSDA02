---
name: create-build
description: "Складання й тести через build-and-test."
disable-model-invocation: true
---
# /create-build

**Передумови:** успішно виконана попередня команда сценарію.

**Дії:**
1. Застосувати skill `build-and-test`: прочитай файл `.github/skills/build-and-test/SKILL.md` і виконай його інструкції.
2. Запустити `ci.sh` (Windows: `ci.bat`).

**Очікувані файли:** `pyproject.toml`, `src/hello_app/core.py`, `tests/test_core.py`, `ci.sh`, `ci.bat`.

**Перевірка:** скрипт збірки – код 0, BasicAddition passed.

**Помилка:** показати вивід компілятора/тестів і зупинитися.

Повторний запуск безпечний: наявні файли не руйнуються, конфігурація не дублюється.
