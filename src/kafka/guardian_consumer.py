from kafka import KafkaConsumer

import json 
from typing import List, Set

# general imports
import logging as log
from general import env_vars
from general import database as db
from datetime import datetime

log.basicConfig(level=log.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

groupid = env_vars.GUARDIAN_GROUP_ID

datetime_format = '%Y-%m-%dT%H:%M:%S%z'  # Format guardian 2019-05-08T11:33:13Z


def create_consumer(
    host=env_vars.KAFKA_HOST,
    port=env_vars.KAFKA_PORT,
    topic=env_vars.GUARDIAN_TOPIC,
    groupid=env_vars.GUARDIAN_GROUP_ID) -> KafkaConsumer:
    """
    Creates a consumer

    Returns:
        A Kafkaconsumer
    """
    return KafkaConsumer(
        topic,
        group_id=groupid,
        bootstrap_servers=[f'{host}:{port}'],
    )


def get_message_from_consumer(consumer:KafkaConsumer):
    """
    Gets the messages from the consumer

    @param:
        consumer: The KafkaConsumer you want to read messages from 
    """
    for message in consumer:
        db.init_db()
        log.info(f'New message from the {message.topic}')
        articles = transform_to_list_of_json_objects(message.value)
        count = 0
        for article in articles:
            count += db.insert_data(
                    article_id = article['id'],
                    article_section = article['id'].split('/')[0],
                    article_type = article['type'],
                    article_publication_date = datetime.strptime(article['webPublicationDate'], datetime_format),
                    article_title = article['webTitle'],
                    article_url = article['webUrl'],
                ) 
            
        log.info(f'There are {count} new articles. ')
        
      
def transform_to_list_of_json_objects(data:bytes) -> List:
    json_data = json.loads(data)
    return [result for result in json_data['response']['results']]


if __name__ == "__main__":
    consumer = create_consumer()
    get_message_from_consumer(consumer)
