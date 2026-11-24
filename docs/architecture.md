# Архітектура агента

## Яку проблему вирішує агент
Ручне створення проєкту, складання, тестів і CI для трьох ОС займає час і легко дає помилки (забутий .gitignore,
тести, що не запускаються в CI). Агент виконує ці кроки за фіксованим сценарієм і перевіряє кожен з них.

## Компоненти
| Файл | Роль |
|---|---|
| `.github/agents/build-engineer.agent.md` | manifest: роль, правила, заборони, критерії завершення |
| `.github/skills/project-scaffold/SKILL.md` | skill: структура проєкту, Hello World, README, .gitignore |
| `.github/skills/build-and-test/SKILL.md` | skill: venv + скрипт запуску, функція додавання, тест BasicAddition |
| `.github/skills/github-actions/SKILL.md` | skill: `ci.yml` з матрицею трьох ОС |
| `.github/prompts/git-init.prompt.md` | command: Git і .gitignore |
| `.github/prompts/create-project.prompt.md` | command → project-scaffold |
| `.github/prompts/create-build.prompt.md` | command → build-and-test |
| `.github/prompts/create-actions.prompt.md` | command → github-actions |
| `.github/prompts/check.prompt.md` | command: перевірка без змін |
| `.github/prompts/init.prompt.md` | orchestrator |

У GitHub Copilot для VS Code команди (commands) реалізуються як prompt-файли `*.prompt.md` і викликаються в чаті
через `/<назва>`; skills – як файли `SKILL.md` у `.github/skills/`; manifest – як custom agent `*.agent.md`.

## Дані між етапами
Етапи обмінюються даними через файлову систему: кожна наступна команда перевіряє наявність файлів попередньої
(наприклад, `create-build` вимагає вихідного файлу програми, `create-actions` – робочих скриптів `ci.sh`/`ci.bat`).

## Обробка помилок оркестратором
`init` зупиняється на першому кроці з ненульовим результатом, показує вивід і причину; наступні кроки не
виконуються. Повторний запуск після виправлення продовжує з перевірки вже створених файлів.
