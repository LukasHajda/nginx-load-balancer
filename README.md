# Multi-Container Flask Application with Nginx Round-Robin Load Balancer
This project demonstrates how to run multiple Flask applications in Docker containers with Nginx acting as a **round-robin** load balancer. Each Flask application runs in its own container, and Nginx is configured to distribute traffic across these containers in a round-robin fashion.

Getting Started
To get started with the project, follow these steps:

Step 1: Clone or Download the Repository
First, clone or download the repository to your local machine.

```
git clone <repository-url>
cd <repository-directory>
```

Step 2: Build and Run the Containers with Docker Compose
To build and start the containers, run the following command:

```docker-compose up -d --build```
This will build the necessary images and start the containers defined in the docker-compose.yml file. The `--build` flag ensures that the images are rebuilt if any changes were made.

Step 3: Access the Application
Once the containers are up and running, you can access the load-balanced application in your browser at:

```http://localhost:8080```
This URL will be served by Nginx, which is configured to distribute traffic across the `app1`, `app2`, `app3`, and `app4` Flask application containers.

Each container will return a message like:

```Hello from: app<CONTAINER_NAME>```
The `CONTAINER_NAME` environment variable will dynamically change based on the container handling the request.