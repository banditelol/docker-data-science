FROM python:3.8

WORKDIR /opt/app

COPY src/ ./src/
COPY data/models/ ./data/models/
COPY requirements.txt .

RUN pip install -r requirements.txt

# CMD ["ls","src"]
CMD ["python", "/opt/app/src/app.py"]