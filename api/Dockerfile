FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip3 install Flask psycopg2-binary

CMD ["python", "app.py"]
