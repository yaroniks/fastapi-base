# Базовый шаблон приложения на FastAPI

Установка без докера:

```bash
git clone https://github.com/yaroniks/fastapi-base.git
cd fastapi-base
```

Настройте файл `.env` под себя и далее:

```bash
python -m venv .venv
.venv\scripts\activate  # для windows
source .venv/bin/activate  # для linux
pip install -r requirements.txt
alembic upgrade head
```

---

Структура файлов:

```
│   .env  # все переменные
│   alembic.ini
│   config.py
│   docker-compose.yml
│   Dockerfile
│   main.py  # основной файл fast api
│   requirements.txt
│
├───app
│   │   limiter.py  # RateLimit
│   │
│   ├───common
│   │   │   enums.py  # все Enum'ы
│   │   │
│   │   ├───rabbitmq  # consumer и producer rabbitmq
│   │   │
│   │   └───schemas  # схемы pydantic
│   │
│   ├───database  # работа с бд
│   │   │   database.py  # базовый класс
│   │   │   models.py  # таблицы
│   │   │
│   │   └───requests  # запросы к бд
│   │
│   └───routers  # роутеры
│       │
│       └───example
│               router.py
│
├───migration   # файлы alembic'a
│
├───tests  # тесты 
│
└───workers
    └───rabbitmq  # запуск consumer'а и producer'а rabbitmq
            Dockerfile
            main.py
            requirements.txt
```
