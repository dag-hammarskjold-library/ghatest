FROM python:3.9-alpine
RUN apk update

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# ENV FLASK_ENV=dev

EXPOSE 5000
CMD ["flask", "--app", "app.app", "run", "--host", "0.0.0.0"]