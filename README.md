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
```

Запуск:

```bash
python main.py
```

---

Структура файлов:

```
│   .env
│   alembic.ini
│   config.py  # настройки, доступ к .env
│   docker-compose.yml
│   Dockerfile
│   main.py  # основной файл fastapi
│   requirements.txt
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
            Dockerfile
            main.py
            requirements.txt
```

Автор: Yarovich
