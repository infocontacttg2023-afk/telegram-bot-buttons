FROM python:3.10-slim

# Встановлюємо необхідні системні бібліотеки для компіляції
RUN apt-get update && apt-get install -y gcc libffi-dev

WORKDIR /app
COPY . .

# Оновлюємо pip і встановлюємо залежності
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8080"]
