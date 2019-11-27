==================================
Provisionamento de um novo site
==================================

## Pacotes necessarios

* nginx
* Python 3.7
* virtualenv + pip3
* Git

sudo yum install nginx git python37 python3.7-venv

## Config do Nginx Virtual Host

* Veja nginx.template.conf
* Substitua SITENAME, por exemplo, por emersonsm.pythonanywhere.com/

## Servico Systemd

* Veja gunicorn-systemd.template.service
* Substitua SITENAME, por exemplo, por emersonsm.pythonanywhere.com/

## Estrutura de pastas:

Suponha que temos uma conta de usuario em /home/username

/home/username
|___ sites
     |____ SITENAME
        |____ database
        |____ source
        |____ static
        |____ virtualenv

