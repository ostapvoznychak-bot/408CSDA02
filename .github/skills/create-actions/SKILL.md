---
name: create-actions
description: "CI workflow через github-actions."
disable-model-invocation: true
---
# /create-actions

**Передумови:** успішно виконана попередня команда сценарію.

**Дії:**
1. Застосувати skill `github-actions`: прочитай файл `.github/skills/github-actions/SKILL.md` і виконай його інструкції.

**Очікувані файли:** `.github/workflows/ci.yml`.

**Перевірка:** перевірки 1–3 skill github-actions.

**Помилка:** вказати рядок YAML з помилкою.

Повторний запуск безпечний: наявні файли не руйнуються, конфігурація не дублюється.
