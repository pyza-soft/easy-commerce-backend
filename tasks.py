import os
import time
from invoke import task

DEFAULT_DOCKER_COMPOSE_FILES = 'docker-compose.dev.yml,docker-compose.yml'


def docker_exec(c, command, executor='docker exec', container_name='web', pty=True, envs={}):
    run_command = executor.split(' ')
    if pty:
        run_command.append('-it')
    for env_key, env_value in envs.items():
        run_command += ["--env", f"{env_key}={env_value}"]
    run_command += [container_name, command]
    final_command = ' '.join(run_command)
    print(f"Executing: {final_command}")
    c.run(final_command, pty=pty)


def docker_compose(c, command, compose_files=DEFAULT_DOCKER_COMPOSE_FILES, detached=False):
    run_command = ['docker-compose']
    for compose_file in compose_files.split(','):
        run_command += ['-f', compose_file]
    run_command.append(command)
    if detached:
        run_command.append('-d')
    final_command = ' '.join(run_command)
    print(f"Executing: {final_command}")
    c.run(final_command)


@task
def build_docker(c, files=DEFAULT_DOCKER_COMPOSE_FILES, detached=False):
    docker_compose(c, command='build', compose_files=files, detached=detached)


@task
def start_docker(c, files=DEFAULT_DOCKER_COMPOSE_FILES, detached=True):
    docker_compose(c, command='up', compose_files=files, detached=detached)


@task
def stop_docker(c):
    docker_compose(c, command='down')


@task
def sleep(c, sleep_time=5):
    time.sleep(sleep_time)


@task
def migrate(c):
    docker_exec(c, "./manage.py migrate")


@task
def create_su(c, username="admin", email="admin@django.com"):
    docker_exec(
        c, f"./manage.py createsuperuser --username {username} --email {email}")


@task(pre=[build_docker, start_docker, sleep, migrate, create_su])
def setup_dev(c, sleep_time=5):
    time.sleep(sleep_time)


@task
def gunicorn(c):
    docker_exec(
        c, "/usr/local/bin/gunicorn --config /usr/local/app/gunicorn.conf.py "
        "--log-config /usr/local/app/logging.conf "
        "-b :8000 ggGameService.wsgi:application"
    )


@task
def runserver(c, port=8000):
    docker_exec(c, command=f'./manage.py runserver 0:{port}')


@task
def shell(c):
    docker_exec(c, "sh")


@task
def django_shell(c):
    docker_exec(c, "./manage.py shell")


@task
def test(c, app_name=""):
    docker_exec(c, f"./manage.py test {app_name}")
