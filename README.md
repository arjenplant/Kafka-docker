# Kafka-docker

## Deploying this project.

Navigate to the directory. 

`docker-compose up `

`docker build -f GuardProdDockerfile -t guard_producer:1.0.0 . `

`docker build -f GuardConsDockerfile -t guard_consumer:1.0.0 . `

It could be that your network name is different if you have it in a different folder. So check the network name with: `docker network ls` and copy paste the network name. 

`docker run --rm --network news_data_kafka_default guard_producer:1.0.0` 

`docker run --rm --network news_data_kafka_default guard_consumer:1.0.0`