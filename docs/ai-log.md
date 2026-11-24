# Журнал взаємодії з AI

| № | Запит | Важлива відповідь / дія агента | Помилка | Рішення |
|---|---|---|---|---|
| 1 | `/init` | Відновлено шість `.prompt.md` команд; виконано git-init, створено Python-каркас, збірку, тести та matrix-CI; перевірка завершена успішно | Частина `.github/prompts/*.prompt.md` була відсутня у робочому дереві | Відновлено відсутні prompt-файли без видалення/зміни наявного стану репозиторію |
| 2 | `/check` | `tools/verify.py` пройшов усі перевірки; окремий `test_BasicAddition` passed; повна збірка `ci.bat` passed | Перший повторний запуск збірки мав помилку формування команди оболонки | Повторний запуск виконано через коректний виклик `.\\ci.bat` |

Щонайменше одна помилка та її виправлення через зміну інструкцій агента (не ручною правкою результату).

## Помилка та виправлення

- Симптом: на `ubuntu-latest` і `macos-latest` виконання `ci.sh` закінчувалося `ci.sh: line 7: hello: command not found` із кодом виходу `127`, хоча тести проходили.
- Причина: скрипт викликав `hello` без шляху, а virtual environment не активувався в `ci.sh`, тому shell не знаходив executable у PATH.
- Змінена інструкція: у `.github/skills/build-and-test/SKILL.md` вказано запуск застосунку через `.venv/bin/hello` у `ci.sh`, а `.venv\Scripts\hello.exe` — у `ci.bat`.
- Результат: `.github/skills/build-and-test/SKILL.md` і `ci.sh` тепер використовують явний шлях до executable всередині `.venv`.

На `ubuntu-latest` та `macos-latest` CI падав на `Permission denied`, тому що `ci.sh` був закомічений з режимом `100644`. Виправлення: у skill `build-and-test` додано обов’язкові команди `git update-index --chmod=+x ci.sh` та перевірку `git ls-files -s ci.sh`; у skill `github-actions` і `.github/workflows/ci.yml` запуск Unix-сценарію змінено з `bash ./ci.sh` на `bash ci.sh`. Також перевірка `tools/verify.py` тепер очікує саме `bash ci.sh`.
