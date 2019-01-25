
# Базовый контейнер - тот контейнер с docker-hub, на основе которого создается данный контейнер
FROM debian:unstable

# Локаль
ENV LANG=C.UTF-8

RUN apt-get -qqy update
RUN apt-get -qqy install python3 python3-pip
# Очистка кеша apt-get
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install Django==2 pillow transliterate django-widget-tweaks django-bootstrap-modal-forms

RUN mkdir /src
# . - текущий каталог
COPY . /src
WORKDIR /src

RUN rm -f db.sqlite3
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

