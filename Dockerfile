FROM python:3.12-slim

# Java (javac/java) and a C++ toolchain (g++) are required by the code judge
# in app.py — this is why the app can't run on Vercel's serverless Python
# functions, which only ship a bare Python runtime.
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jdk \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 2 --timeout 60 app:app"]
