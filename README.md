# Базовый шаблон приложения на FastAPI

Запуск через докер, будет открыт на localhost:8000
```bash
docker-compose down
docker-compose up --build -d
```

---

Запуск без докера: <br>
Настройте файл `.env` под себя и далее:
```bash
python -m venv .venv
.venv\scripts\activate  # для windows
source .venv/bin/activate  # для linux
pip install -r requirements.txt
```

Запуск зависимостей в докере:
```bash
docker run -d --name postgresql -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=Database postgres
```

Запуск самого приложения:
```bash
.venv\scripts\activate  # для windows
source .venv/bin/activate  # для linux
python main.py
```

---

Структура файлов:
```
│   .env  # переменные для работы
│   config.py  # настройки, доступ к .env
│   docker-compose.yml
│   main.py  # основной файл fastapi
│   requirements.txt  # необходимые для работы библеотеки
│
├───app
│   │   limiter.py  # RateLimit
│   │
│   ├───database  # работа с бд
│   │   │   base.py  # базовый класс
│   │   │
│   │   └───models  # модели sqlaclhemy и запросы в бд
│   │
│   ├───routers  # роутеры
│   │
│   ├───schemas  # схемы pydantic
│   │
│   └───utils
│       │   enums.py  # все Enum'ы
│       │
│       └───rabbitmq  # consumer и producer rabbitmq
│
├───migration   # файлы alembic'a
│
├───tests  # тесты 
│
└───workers
    └───rabbitmq  # запуск consumer'а rabbitmq
```

Автор: Yarovich
