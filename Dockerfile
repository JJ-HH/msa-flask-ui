FROM python:3.10.2

RUN pip install -U pip
RUN pip install flask requests

WORKDIR /app

COPY . /app/

ENTRYPOINT ["python", "app.py"]
