# Игры разума (Python)

[![hexlet-check](https://github.com/penguin-astronaut/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/penguin-astronaut/devops-engineer-from-scratch-project-49/actions)

Пять математических игр для терминала: проверка чётности, калькулятор, НОД, арифметическая прогрессия и проверка простоты числа. Введите имя и отвечайте на вопросы. Три правильных ответа подряд приносят победу; первая ошибка завершает игру и показывает правильный ответ.

## Требования

- Python 3.13 или новее
- Менеджер пакетов uv
- Make для команд сборки и установки

## Установка

```bash
git clone https://github.com/penguin-astronaut/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
uv sync
make build
make package-install
```

После установки команды игр доступны напрямую, например `brain-even`. Если команда не найдена, выполните `uv tool update-shell` и перезапустите терминал. Для обновления ранее установленного пакета выполните `uv tool install --force dist/*.whl`.

Запись установки зависимостей, сборки и установки пакета:

[![Установка игр разума](https://asciinema.org/a/Agu0dJXjB5xoyxTm.svg)](https://asciinema.org/a/Agu0dJXjB5xoyxTm)

## Использование

Из каталога проекта игры также можно запускать через `uv run`, как показано ниже.

### Проверка на чётность (brain-even)

Ответьте `yes`, если число чётное, и `no`, если нечётное.

```bash
uv run brain-even
```

[![Демонстрация brain-even](https://asciinema.org/a/HmucaRWhKxxARmXG.svg)](https://asciinema.org/a/HmucaRWhKxxARmXG)

### Калькулятор (brain-calc)

Вычислите результат сложения, вычитания или умножения двух чисел и введите целое число.

```bash
uv run brain-calc
```

[![Демонстрация brain-calc](https://asciinema.org/a/jwT7rAFAWFfEIpFg.svg)](https://asciinema.org/a/jwT7rAFAWFfEIpFg)

### Наибольший общий делитель (brain-gcd)

Найдите НОД двух чисел. Для победы нужно правильно ответить три раза подряд.

```bash
uv run brain-gcd
```

Запуск игры, победа и поражение:

[![Демонстрация brain-gcd](https://asciinema.org/a/SFlBNUgQgY5X5a5F.svg)](https://asciinema.org/a/SFlBNUgQgY5X5a5F)

### Арифметическая прогрессия (brain-progression)

Найдите число, скрытое за двумя точками в прогрессии. Для победы нужно правильно ответить три раза подряд.

```bash
uv run brain-progression
```

Запуск игры, победа и поражение:

[![Демонстрация brain-progression](https://asciinema.org/a/0DF95odETYuVaF3Z.svg)](https://asciinema.org/a/0DF95odETYuVaF3Z)

### Простое ли число? (brain-prime)

Ответьте `yes`, если число простое, и `no`, если нет. Для победы нужно правильно ответить три раза подряд.

```bash
uv run brain-prime
```

Запуск игры, победа и поражение:

[![Демонстрация brain-prime](https://asciinema.org/a/Ua5AjlPBXaDpnFzq.svg)](https://asciinema.org/a/Ua5AjlPBXaDpnFzq)

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
