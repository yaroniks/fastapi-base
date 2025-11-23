# Базовый шаблон приложения на FastAPI

Установка и запуск, будет работать на localhost:8000/api/v1
```bash
git clone https://github.com/yaroniks/fastapi-base.git
cd fastapi-base
docker compose up --build -d
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
