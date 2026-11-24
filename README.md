# Лабораторна робота 1 – AI-агент для автоматизації розробки та CI/CD

**Виконав:** Возничак Остап Маркіянович, група КІ-408, варіант 2
**Мова / складання / тести:** Python / venv + скрипт запуску / pytest

Репозиторій містить AI-агента `build-engineer` для GitHub Copilot (VS Code), який створює кросплатформний
проєкт Hello World, систему складання, юніт-тести та CI для Windows, Linux і macOS.

## Запуск агента
1. Відкрити репозиторій у VS Code з увімкненим GitHub Copilot.
2. У Copilot Chat вибрати агента **build-engineer**.
3. Ввести команду `/init` (або окремі `/git-init`, `/create-project`, `/create-build`, `/create-actions`, `/check`).

## Локальна збірка та тести
`./ci.sh   (Windows: ci.bat)` – збирає проєкт, запускає тести й програму `hello`.

Детальніше: [docs/usage.md](docs/usage.md), архітектура – [docs/architecture.md](docs/architecture.md),
журнал роботи з AI – [docs/ai-log.md](docs/ai-log.md).
