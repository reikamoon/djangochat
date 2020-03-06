FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /chatapp
WORKDIR /chatapp
COPY /requirements.txt /chatapp/
RUN pip3 install -r requirements.txt
COPY . /chatapp/
