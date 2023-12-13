FROM python:3.9-slim

WORKDIR /app

COPY . /app
# COPY app.py .
# COPY templates .
# COPY templates/index.html .
# COPY requirements.txt .
# COPY *.yaml .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]