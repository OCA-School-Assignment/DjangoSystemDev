FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    npm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]