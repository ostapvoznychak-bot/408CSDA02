# Використання

## Агент
- Copilot Chat → агент `build-engineer` → `/init` – повний сценарій;
- `/check` – лише перевірка (нічого не змінює).

## Локальна перевірка
```
./ci.sh   (Windows: ci.bat)
python tools/verify.py
git status --ignored --short
```

## Запуск програми
.venv/bin/hello (Windows: .venv\Scripts\hello.exe)

[Після виконання /init замінити цей розділ точними командами й виводом, які були використані.]
