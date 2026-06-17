## How to set up rabbitmq as docker image

Pull the rabbitmq image

`docker pull rabbitmq:3-management`

Run the container

`docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

Navigate to the admin console in your browser

`http://localhost:15672`


###Using Docker Compose to Load and Import Broker Definitions

`docker-compose.ym`

```yaml
version: '3.8'

services:
    rabbitmq:
        image: rabbitmq:3-management
        hostname: my-rabbit
        volumes:
            - ./rabbitmq/etc/definitions.json:/etc/rabbitmq/defu
            .json
            - ./rabbitmq/etc/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf
            - ./rabbitmq/data:/var/lib/rabbitmq/mnesia/rabbit@my-rabbit
            - ./rabbitmq/logs:/var/log/rabbitmq/log
        ports:
            - 5672:5672
            - 15672:15672
```