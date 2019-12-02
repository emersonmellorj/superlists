FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip
RUN echo "deb http://download.unesp.br/linux/debian sid main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nginx gunicorn firefox python3-virtualenv tcpdump vim
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /code
EXPOSE 8000
EXPOSE 80
#RUN python manage.py collectstatic --noinput
COPY ./deploy_tools/nginx.conf /etc/nginx/nginx.conf
#CMD exec gunicorn superlists.wsgi:application - bind 0.0.0.0:8000
