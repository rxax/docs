## How to set up rabbitmq as docker image

Pull the rabbitmq image

`docker pull rabbitmq:3-management`

Run the container

`docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

Navigate to the admin console in your browser

`http://localhost:15672`