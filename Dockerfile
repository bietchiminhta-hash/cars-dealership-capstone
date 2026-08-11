FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Sua ALLOWED_HOSTS truoc khi deploy that (khong dung '*' cho production)
ENV PORT=8080
EXPOSE 8080

CMD gunicorn djangoproj.wsgi:application --bind 0.0.0.0:$PORT
