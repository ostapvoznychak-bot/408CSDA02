---
name: check
description: "Перевірка без змін."
disable-model-invocation: true
---
# /check

**Передумови:** проєкт створено попередніми командами.

**Дії:**
1. Перевірити наявність manifest, 3 skills, 6 commands.
2. Виконати `python tools/verify.py`.
3. Виконати `ci.sh` / `ci.bat`: тест BasicAddition passed, файл hello створено.
4. `git status --ignored --short`: `.venv/ та build/` ігнорується.

**Очікувані файли:** нічого не змінює.

**Перевірка:** усі пункти PASS.

**Помилка:** перелік пунктів FAIL і ненульовий результат.

Повторний запуск безпечний: наявні файли не руйнуються, конфігурація не дублюється.
