**Тестовое задание**

**Сборка и запуск образа**:
Копируем файл .env: sudo cp .example-env .env
sudo docker-compose -f docker-compose.yml build
sudo docker-compose -f docker-compose.yml up

**Запуск сервера**: 
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
python backend/manager.py runserver

API:

**[GET]**
/api/v1/division/ - список подразделений (без иерархии).
Параметры сортировки: ?ord=[id, title] или [-id, -title] для обратного порядка 

**[GET]**
/api/v1/division/ - список подразделений (без иерархии).
Параметры сортировки: ?ord=[id, title]

**[GET]**
/api/v1/division/<pk>/ - деталка подразделения и список всех дочерних с учетом иерархии.
Параметры сортировки: ?ord=[id, title]

**[GET]**
/api/v1/division/<pk>/staff/ - список сотрудников подразделения (без учета иерархии).
Параметры сортировки: ?ord=[id, first_name, last_name, patronymic]

**[GET]**
/api/v1/staff/<pk>/ - деталка сотрудника.

**[GET]**
/api/v1/staff/<pk>/subordinates/ - список подчиненных данного сотрудника с учетом иерархии.
Параметры сортировки: ?ord=[id, first_name, last_name, patronymic]


