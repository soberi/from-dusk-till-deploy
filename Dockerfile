FROM python:3.8-alpine

COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

EXPOSE 8000
CMD ["python", "main.py"]
