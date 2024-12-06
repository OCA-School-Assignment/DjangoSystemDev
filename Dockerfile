FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc postgresql-client \
    && apt-get clean

WORKDIR /code/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]