FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get install -y nginx gunicorn  python3-virtualenv
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /code
EXPOSE 8000
#CMD exec gunicorn superlists.wsgi:application - bind 0.0.0.0:8000
