---
name: init
description: "Оркестратор повного сценарію"
disable-model-invocation: true
---
# /init

1. `/git-init`
2. `/create-project`
3. `/create-build`
4. `/create-actions`
5. `/check`

Після кожного кроку перевір результат. На помилці зупинись і виведи: крок, команду, вивід, причину. Наприкінці – таблиця «крок – статус» і запис у docs/ai-log.md.
