FROM python:3.8

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "/opt/app/src/app.py"]