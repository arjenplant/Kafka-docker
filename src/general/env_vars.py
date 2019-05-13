
from pyhocon import ConfigFactory
import logging as logging
import os

conf = ConfigFactory.parse_file('config.conf')


#KAFKA configuration
KAFKA_HOST = os.environ.get('KAFKA_HOST') or conf.get('kafka.host')
KAFKA_PORT = os.environ.get('KAFKA_PORT') or conf.get('kafka.port')

#GUARDIAN configuration
GUARDIAN_TOPIC = conf.get('guardian.topic')
GUARDIAN_KEY = conf.get('guardian.key')
GUARDIAN_URL = conf.get('guardian.url')
GUARDIAN_GROUP_ID = conf.get('guardian.groupid')    

#DATABASE configuration
POSTGRES_HOST = os.environ.get('POSTGRES_HOST') or conf.get('database.host')
POSTGRES_PASSWORD = conf.get('database.password')
POSTGRES_USER = conf.get('database.user')
POSTGRES_DATABASE = conf.get('database.database')