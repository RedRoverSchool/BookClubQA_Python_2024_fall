# Полезное 
➣ [Ручное тестирование сейчас проводим на проде](https://misleplav.ru/)

➣ [Автотесты будут проходить на тесте](http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/)

➣ [Баги оставляем в таблице](https://docs.google.com/spreadsheets/d/1NBimEWDxPNVlMtWHc_IML7hvNlYtQSe7i8AkilXUl6A/edit?gid=0#gid=0)

## Как работаем с репозиторием

1. Клонируем 
2. Создаем ветку для своих тестов 
3. Пушим ветку в Github 
4. Открываем запрос на слияние с main
5. Отправляем запрос в slack в чат [#qa_python_project](https://redroverschool.slack.com/archives/C05US8RLPFU) или в свою группу
6. Обязательно удаляем свою ветку после слияния с main

## Как пишем тесты 

1. Тесты пишем в соответствии с шаблоном
 - Локаторы храним в components
2. Соблюдаем правила кода [PEP8](https://letpy.com/python-guide/pep8/)    
3. Тесты НЕ должны повторяться 
4. Перед пушем в репозиторий тесты необходимо проверить на работоспособность 
5. Не работаем в одной ветке долго, чтобы уменьшить количество конфликтов
6. Не самые важные тесты стоит помечать маркером slow (@pytest.mark.slow)

## Общая инструкция по работе с доской


[<img src="https://github.com/user-attachments/assets/14d75fbd-a1f0-4058-b4f5-05914851e78c" width="90" height="90">](https://docs.google.com/document/d/1ob1So07HGUwlMcEEHpgEYTBLBQzAZ6laPCRItndNJqU/edit?tab=t.0)


## Установки:

<img src="https://docs.astral.sh/ruff/assets/bolt.svg" width="20" height="20">[Install Ruff](https://docs.astral.sh/ruff/installation/) инструмент для анализа Python-кода  
- Если вы хотите увидеть список доступных подкоманд и опций, используйте:
```ruff --help```
- Если вы хотите проверить весь проект на ошибки форматирования, выполните:
```ruff check .```
- Для форматирования кода:
```ruff format .```



