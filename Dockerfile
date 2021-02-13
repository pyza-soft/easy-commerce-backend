FROM python:3-alpine

# Installs some utils for debugging
ARG DEV_ENV="0"

ENV DEV_ENV $DEV_ENV

RUN apk add build-base
RUN apk add libffi-dev
RUN apk add postgresql-dev
RUN apk add python3-dev openssl-dev cargo
RUN apk add jpeg-dev zlib-dev

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
ADD poetry.lock pyproject.toml /
RUN poetry install

ADD ./backend /usr/local/app/

WORKDIR /usr/local/app/

EXPOSE 8000

CMD ["/usr/local/bin/gunicorn", "--config", "/usr/local/app/gunicorn.conf.py", "--log-config", "/usr/local/app/logging.conf", "-b", ":8000", "ggUserService.wsgi:application"]
