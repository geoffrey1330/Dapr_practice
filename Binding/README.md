# Dapr binding


### make sure to have Docker running on your machine 

### setup dapr on your machine through this [guide](https://docs.dapr.io/getting-started/install-dapr-cli/)

- initialize dapr and allow it to config with the docker in your machine by running the command

``` dapr init ```
- Verify Dapr version run the command

``` dapr --version ```


Run Kafka Docker Container Locally

1. To run the container locally, run command:

``` docker-compose -f ./docker-compose-single-kafka.yml up -d ```



Verify containers are running the dapr instance run command

``` docker ps ```

- Expected output 
```
CONTAINER ID   IMAGE                      COMMAND                  CREATED      STATUS                  PORTS                                                  NAMES
4184a175d085   openzipkin/zipkin          "start-zipkin"           3 days ago   Up 20 hours (healthy)   9410/tcp, 0.0.0.0:9411->9411/tcp                       dapr_zipkin
663e13b2fb1c   daprio/dapr:1.5.1          "./placement"            3 days ago   Up 20 hours             0.0.0.0:50005->50005/tcp                               dapr_placement
50a3806a0038   redis                      "docker-entrypoint.s…"   3 days ago   Up 20 hours             0.0.0.0:6379->6379/tcp                                 dapr_redis
e9fc6cf63c71   bitnami/kafka:latest       "/opt/bitnami/script…"   5 days ago   Up About an hour        0.0.0.0:9092->9092/tcp                                 test_kafka_kafka_1
00b053841419   bitnami/zookeeper:latest   "/opt/bitnami/script…"   5 days ago   Up About an hour        2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp, 8080/tcp   test_kafka_zookeeper_1


```

### Start Receiver (expose gRPC server receiver on port 3000)
- open another terminal and move into the Binding folder
```
cd python2

dapr run --app-id receiver --app-protocol grpc --app-port 3000 --components-path ../components python3 app.py
```

### Start second Receiver (expose gRPC server receiver on port 50059)

- open another terminal and move into the Binding folder
```
cd python3

dapr run --app-id receiver2 --app-protocol grpc --app-port 50059 --components-path ../components python3 app.py

```

### Start the Publisher
- open another terminal and move into the Binding folder

```
dapr run --app-id publisher --app-protocol grpc --components-path ../components python3 app.py

```

### Cleanup

- The dapr apps can be stopped by calling stop or terminating the process:
```
dapr stop --app-id publisher
dapr stop --app-id receiver
dapr stop --app-id receiver2
```
- For kafka cleanup, run the following code:
```
docker-compose -f ./docker-compose-single-kafka.yml down
```