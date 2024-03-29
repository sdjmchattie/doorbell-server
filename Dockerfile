FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pipenv

WORKDIR /code

COPY . .

RUN pipenv sync --dev --system

CMD ["python3", "DoorbellServer.py"]
