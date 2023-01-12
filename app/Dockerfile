FROM python:3.8

#RUN mkdir /app
#COPY ./app /app
WORKDIR /app
COPY . .

RUN pip3 install -r /app/requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS /app/airy-runway-344101-9fb121fbeb28.json