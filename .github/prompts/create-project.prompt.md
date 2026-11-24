---
mode: agent
description: Каркас проєкту через project-scaffold.
---
# /create-project

**Передумови:** успішно виконана попередня команда сценарію.

**Дії:**
1. Застосувати skill `project-scaffold` (мова Python, назва hello): прочитай файл `.github/skills/project-scaffold/SKILL.md` і виконай його інструкції.

**Очікувані файли:** `src/hello_app/__init__.py`, `src/hello_app/cli.py`, `README.md`, `.gitignore`.

**Перевірка:** перевірки skill project-scaffold.

**Помилка:** назвати відсутній файл і зупинитися.

Повторний запуск безпечний: наявні файли не руйнуються, конфігурація не дублюється.
