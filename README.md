# Sprint_7

## Финальный проект 7 спринт: Автоматизированные тесты для сайта по заказу самокатов

Этот проект содержит автоматизированные тесты для веб-приложения по заказу самокатов. Тесты написаны с использованием Python, Pytest, Allure и Requests.

## Инструкции по запуску

Убедитесь, что у вас установлен Python и Mozilla Firefox.

### Запуск всех тестов

Выполните следующую команду:

```bash
pytest -v
```

Запуск отдельных тестов
Для запуска отдельных тестов выполните соответствующую команду:

Генерация отчета Allure
Для получения отчета Allure выполните следующие команды:

```bash
pytest --alluredir=allure_results
allure serve allure_results
```

**Описание файлов**

test_courier_creation.py: Тесты для создания курьеров.

test_create_courier_answer_correct_response_code: курьера можно создать и запрос возвращает правильный код ответа.
test_create_courier_double: нельзя создать двух одинаковых курьеров.
test_create_courier_missing_login: отсутствует поле login.
test_create_courier_missing_password: отсутствует поле password.
test_create_existing_login_courier_error: если создать пользователя с логином, который уже есть, возвращается ошибка.
test_courier_login.py: Тесты для входа курьеров.

test_courier_login_successfully: курьер может авторизоваться и успешный запрос возвращает id.
test_courier_login_error_login: ошибка в поле login.
test_courier_login_error_password: ошибка в поле password.
test_courier_login_missing_login_and_password: нет поля login_and_password.
test_courier_login_missing_login: нет поля login.
test_courier_login_missing_password: нет поля password.
test_order_creation.py: Тесты для создания заказов.

test_create_order: тестируем все варианты цветов заказа.
test_order_list.py: Тесты для получения списка заказов.

