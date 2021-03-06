from celery import Celery
from scoring_engine.engine.config import config


redis_server = 'redis://:' + config.redis_password + '@' + config.redis_host + ':' + str(config.redis_port)
celery_app = Celery('engine.worker', backend=redis_server, broker=redis_server + '/0')
