FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Copy and install python deps
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

# Copy project
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

ENV PORT 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
