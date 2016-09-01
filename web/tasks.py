from __future__ import absolute_import

from celery import task

@task
def test(param):
    return 'Listo esta es la tarea y el parametro es:  "%s" ' % param


@task
def test2(param):
    return 'Ok tarea 2 y el parametro es:  "%s" ' % param