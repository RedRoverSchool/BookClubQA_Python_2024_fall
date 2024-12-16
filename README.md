# 1. Полезное 
➣ [Ручное тестирование сейчас проводим на проде](https://misleplav.ru/)

➣ [Автотесты будут проходить на тесте](http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/)

➣ [Баги оставляем в таблице](https://docs.google.com/spreadsheets/d/1NBimEWDxPNVlMtWHc_IML7hvNlYtQSe7i8AkilXUl6A/edit?gid=0#gid=0)

➣ Общая инструкция по работе с доской

[<img src="https://github.com/user-attachments/assets/14d75fbd-a1f0-4058-b4f5-05914851e78c" width="90" height="90">](https://docs.google.com/document/d/1ob1So07HGUwlMcEEHpgEYTBLBQzAZ6laPCRItndNJqU/edit?tab=t.0)

## 2. Требования

Для запуска проекта вам нужно установить следующие библиотеки:

- `pytest` — тестовый фреймворк.
- `pytest-playwright` — интеграция Playwright с Pytest.
- `playwright` — для автоматизации браузера.
- `pytest-xdist` — для параллельного выполнения тестов.
- `Faker` — для генерации поддельных данных.
- `pydantic` — для валидации данных.
- `Ruff` - [инструмент для анализа Python-кода](https://docs.astral.sh/ruff/installation/) 
  - Если вы хотите увидеть список доступных подкоманд и опций, используйте:
  ```bash
  ruff --help
  ```
  - Если вы хотите проверить весь проект на ошибки форматирования, выполните:
  ```bash
  ruff check .
  ```
  - Для форматирования кода:
  ```bash
  ruff format .
  ```

## 3. Как работаем с репозиторием

1. Клонируем 
2. Создаем ветку для своих тестов 
3. Пушим ветку в Github 
4. Открываем запрос на слияние с main
5. Отправляем запрос в slack в чат [#qa_python_project](https://redroverschool.slack.com/archives/C05US8RLPFU) или в свою группу
6. Обязательно удаляем свою ветку после слияния с main

## 4. Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https:https://github.com/RedRoverSchool/BookClubQA_Python_2024_fall.git
   cd BookClubQA_Python_2024_fall
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS/Linux
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Для запуска тестов, убедитесь, что у вас установлен Playwright:
   ```bash
   playwright install
   ```
   ```bash
   playwright --version
   ```
После этого ваш проект будет готов к запуску.

_________
## 5. Отчеты
Чтобы получить отчет о тестах в формате Allure, выполните команду:

```bash
pytest --alluredir=allure-results
```
```bash
allure serve allure-results
```
После этого Allure откроет отчет в браузере.
____________

## 6. Как пишем тесты 

1. Тесты пишем в соответствии с шаблоном
 - Локаторы храним в components
 - Тест должен начинаться с авторизации
2. Соблюдаем правила кода [PEP8](https://letpy.com/python-guide/pep8/)    
3. Тесты НЕ должны повторяться 
4. Перед пушем в репозиторий тесты необходимо проверить на работоспособность 
5. Не работаем в одной ветке долго, чтобы уменьшить количество конфликтов
6. Не самые важные тесты стоит помечать маркером slow (@pytest.mark.slow)

## 7. Swagger доступен только на тестовом окружении. Чтобы получить доступ нужно:
1. Открыть тестовое окружение
2. Войти в аккаунт
3. Открыть http://testing.misleplav.ru/api/swagger/

