## Dockerize a React App

### Local development

Do the following in the current working dir (where the react app was created):


Create a `Dockerfile`:

```html
# pull official base image
FROM node:16-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json .\
     package-lock.json .\
    ./

RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# add app
COPY . ./

# set env variable from build argument
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# start app
CMD ["npm", "run", "start"]
```

Crate the `.dockerignore` file:

```html
node_modules
build
.dockerignore
Dockerfile
Dockerfile.prod
```

Build the image:

`docker build -t reactapp1:dev .`

Run the container:

`docker run --name reactapp1_dev -it --rm -v %cd%:/app -v /app/node_modules -p 3001:3000 -e CHOKIDAR_USEPOLLING=true reactapp1:dev`

Create the `docker-compose.yml` file:

```html
version: '3.9'

services:
  frontend:
    container_name: react_frontend
    image: react_frontend
    build:
      context: .
      dockerfile: Dockerfile
      args:
        - NODE_ENV=production
        - REACT_APP_API_URL=http://localhost:5003
    volumes:
      - '.:/app'
      - '/app/node_modules'
    ports:
      - 3001:3000
    environment:
      - CHOKIDAR_USEPOLLING=true
```

Start container from docker-compose:

`docker-compose -f docker-compose.yml up -d --build`

## Production build

The `Dockerfile.prod`:

```html
# build environment
FROM node:16-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY . ./
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL
RUN npm run build

# production environment
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
# new
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

The `nginx/nginx.conf` file for React Router usage:

```html
server {

  listen 80;

  location / {
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
  }

  error_page   500 502 503 504  /50x.html;

  location = /50x.html {
    root   /usr/share/nginx/html;
  }

}
```

The `docker-compose.prod.yml` file:

```html
version: '3.9'

services:
  frontend-prod:
    container_name: react_frontend
    image: reactapp1:prod
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        - NODE_ENV=production
        - REACT_APP_API_URL=http://localhost:5002
    ports:
      - 1337:80
    environment:
      - CHOKIDAR_USEPOLLING=true
```

Start the container with docker-compose:

`docker-compose -f docker-compose.prod.yml up -d --build`