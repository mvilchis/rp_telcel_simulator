import os
import time
from celery import Celery
import ast, json, requests
from constants import *

env=os.environ
REDIS_HOST = os.getenv('REDIS_PORT_6379_TCP_ADDR')
REDIS_PORT = int(os.getenv('REDIS_PORT_6379_TCP_PORT'))
redis = "redis://%s:%s/0" % (REDIS_HOST, REDIS_PORT)

CELERY_BROKER_URL=redis
CELERY_RESULT_BACKEND=redis

RP_URL= os.getenv('RP_URL', "")

celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.send_response')
def send_response(contact_cel, answer_constant):
    payload={"backend":"Telcel","sender":"+52"+contact_cel, "message":answer_constant,"ts":"1", "id":"758af0a175f8a86"}
    r = requests.get(RP_URL, params = payload)
    return payload
