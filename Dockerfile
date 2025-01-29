FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc postgresql-client \
    && apt-get clean

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash \
    && apt-get install -y nodejs \
    && apt-get install -y npm \
    && apt-get clean

WORKDIR /code/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY package.json /code/app/
RUN npm install

COPY . /code/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]