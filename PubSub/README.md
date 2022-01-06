# Dapr Pub-Sub 

### make sure to have Docker running on your machine 

### setup dapr on your machine through this [guide](https://docs.dapr.io/getting-started/install-dapr-cli/)

- initialize dapr and allow it to config with the docker in your machine by running the command

``` dapr init ```
- Verify Dapr version run the command

``` dapr --version ```

Verify containers are running the dapr instance run command

``` docker ps ```

- Expected output 
```
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS                              NAMES
0dda6684dc2e   openzipkin/zipkin        "/busybox/sh run.sh"     2 minutes ago   Up 2 minutes   9410/tcp, 0.0.0.0:9411->9411/tcp   dapr_zipkin
9bf6ef339f50   redis                    "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:6379->6379/tcp             dapr_redis
8d993e514150   daprio/dapr              "./placement"            2 minutes ago   Up 2 minutes   0.0.0.0:6050->50005/tcp            dapr_placement

```


### To Run Node message subscriber with Dapr 

1. Navigate to Node App directory in your CLI run the command:

```
cd nodeapp
```
2. Install dependencies:

```
npm install
```
3. Run the Nodeapp  ``` app.js ``` with Dapr:

```
dapr run --app-id nodeapp --app-port 3000 node app.js
```

- app-id which can be any unique identifier for the microservice. app-port, is the port that the Node application is running on. Finally, the command to run the app node app.js is passed last.


### Run Python message subscriber with Dapr

1. Open another CLI and Navigate to Python App directory in your CLI run the command:

```
cd pythonapp
```
2. Install dependencies:

```
pip3 install -r requirements.txt 

```

3. Run the Pythonapp  ``` app.py ``` with Dapr:

```
dapr run --app-id pythonapp --app-port 5000 python3 app.py
```


### RUN the Publisher

- Now to run the publisher which will send messages for our subscriber to consume


1. Run the Dapr sidecar 

``` dapr run --app-id myapp --dapr-http-port 3500 ```

2. Sending Messages
- for the order subscriber
```
dapr publish --publish-app-id myapp --pubsub pubsub --topic order --data-file order.json

```
- for the email subscriber
```
dapr publish --publish-app-id myapp --pubsub pubsub --topic email --data-file email.json

```

- for the cart subscriber
```
dapr publish --publish-app-id myapp --pubsub pubsub --topic cart --data-file cart.json

```