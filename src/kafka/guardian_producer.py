# Kafka imports
from kafka import KafkaProducer

# API call
import requests

#Logging
import logging as log

#Configuration
from general import env_vars

#Setting the basic logging to INFO
log.basicConfig(level=log.INFO)


def get_last_n_guardian_articles(n:int = 10, url=env_vars.GUARDIAN_URL, key=env_vars.GUARDIAN_KEY):
    """ 
    Makes an API call to the guardian and returns the N articles
        
    @param
        n: number of articles to collect. Default is 10

    @Returns:
        Response of the API call
    """
    content = {
        'api-key':key,
        'pageSize':n,
    }
    
    return requests.get(
        url=url,
        params=content,
    )


def create_producer(host=env_vars.KAFKA_HOST, port=env_vars.KAFKA_PORT) -> KafkaProducer:
    """ 
    Creates the producer

    @Returns:
        A KafkaProducer
    """
    return KafkaProducer(bootstrap_servers=[f'{host}:{port}'])


def send_messages_to_kafka(data:bytes, producer:KafkaProducer, topic=env_vars.GUARDIAN_TOPIC):
    """
    Sends the response of the API to the KafkaBroker

    @param:
        data: API call response converted to bytes
        producer: The Kafkaproducer

    """
    producer.send(topic, data).add_callback(on_send_success).add_errback(on_send_error)
    

def on_send_success(record_metadata):
    log.info(f"Producer sending to : {record_metadata.topic}")


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)


if __name__ == "__main__":
    response = get_last_n_guardian_articles()
    producer = create_producer()
    send_messages_to_kafka(response.content, producer)
    producer.close()
    