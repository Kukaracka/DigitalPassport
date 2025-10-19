
FROM python:3.13-slim

WORKDIR /app

# Установка Poetry и зависимостей (без dev)

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY backend/src ./src

WORKDIR /app/src

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

