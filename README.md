# GOR AQA
***
## Требования:
* Необходима версия python: 3.9
* Установить все зависимости
> pip install -r requirements.txt
***

## Git Flow:
* Создать новую папку и проинициализировать git
> git init
* Склонировать репозиторий 
> git clone [https://git.astondevs.ru/aston/repo-gor/gor-aqa.git]
* Создать локальную ветку для работы
> git checkout -b feature/TASK_NAME
* После завершения работы, подготовить измененные файлы для следующей фиксации
> git add .
* Сделать коммит
> git commit -m 'added ui_test_[test_case_number]
* Сделать пуш
> git push --set-upstream feature/[TASK_NAME]
***

## В нашем фреймворке существует следующая архитектура:
 1) test_data:
	>* api. Здесь хранятся payload для отправки api запросов и базовый url;
	>* ui. Здесь хранятся базовые url-адреса.
 2) test_framework:
	>* api. Дата и шаги для api-тестов;
	>* database:
	   >>* checkers - чекеры для запросов в БД;
       >>* orm - описание таблиц через классы; 
	   >>* queries и steps - запросы и шаги для БД соответственно;
	>* helpers. Генераторы, логгеры, чекеры;
	>* ui. Данные, локаторы, бизнес шаги для ui тестов.
 3) tests:
	>* api. Реализация api-тестов разделенных по логике на разные папки;
	>* ui. Реализация ui-тестов разделенных по логике на разные папки.
***
###### Подключение к БД выполняется через SQL-алхимию.
***

## Руководство по именованию коммитов, веток и МР:
* Название ветки: feature/TASK_NAME, пример: feature/GOR-97
* Название коммита: summary description, пример: added ui_test_C9032531
* Название МР: Resolve/TASK_NAME, пример: Resolve: feature/GOR-97

## Установка линтеров(пре-коммитов):
>* pre-commit install

## Allure-отчеты:
* Сохранить результаты тестов в allure:
  * --alluredir=allure_report;
* Очистить результаты allure предыдущего запуска тестов:
  * --clean-alluredir;
* Генерация allure-отчета: 
  * allure serve allure_report.

# CI/CD
Запуск осуществляется:
- VARIABLE: видтеста_номертеста (напр: api_12345)
- PROCESS: число ранеров для запуска
- Результаты смотреть в Settings/Pages/Your pages are served under:...
-(Результаты появляются через 10-15 минут после запуска)