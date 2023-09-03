# Django project with postgres all based on docker
It's about a simple django project with one view returning simple information fetched from postgres db



### how to run the project

Pour lancer le projet correctement suivez l'ordre ci-dessous de lancement des services:

0. first clone the project
1. make sure you have docker and docker compose installed , up and running
2. inside docker-compose.yml file location run `docker-compose up --build`
3. wait the web server to start and try to access to http://localhost:8000/user-list/
4. You should normally get a json with some data

# Django Application Deployment on Kubernetes with PostgreSQL

This guide will walk you through the process of deploying your Django application on Kubernetes with a PostgreSQL database.

## Prerequisites

Before you begin, ensure you have the following prerequisites:
- A running Kubernetes cluster
- `kubectl` command-line tool installed
- Docker image of your Django application
- Docker image of PostgreSQL (official image)

## Step 1: Create Kubernetes Deployment for PostgreSQL

1. Create a Kubernetes Deployment YAML file for PostgreSQL (e.g., `postgres-deployment.yaml`).

2. Define the PostgreSQL configuration, such as database name, user, and password.

3. Apply the PostgreSQL Deployment to your Kubernetes cluster:
kubectl apply -f postgres-deployment.yaml

4. Verify that the PostgreSQL database is running:
kubectl get pods


## Step 2: Create Kubernetes Service for PostgreSQL

1. Create a Kubernetes Service YAML file for PostgreSQL (e.g., `postgres-service.yaml`).

2. Define the PostgreSQL port (5432).

3. Apply the PostgreSQL Service to your Kubernetes cluster:
kubectl apply -f postgres-service.yaml


## Step 3: Update Django Application Settings

1. Update your Django application settings to use the PostgreSQL database.

2. Configure the PostgreSQL host as the `postgres-service` DNS name (e.g., `postgres-service`).

3. Provide the database name, user, and password as configured in the Deployment YAML.

## Step 4: Deploy Django Application on Kubernetes

1. Create a Kubernetes Deployment YAML file for your Django application (e.g., `django-deployment.yaml`).

2. Define the number of replicas, Docker image, and container port (8000).

3. Apply the Django Deployment to your Kubernetes cluster:
kubectl apply -f django-deployment.yaml

4. Create a Kubernetes Service YAML file to expose your Django application (e.g., `django-service.yaml`).

5. Apply the Django Service to your Kubernetes cluster:
kubectl apply -f django-service.yaml

6. Wait for the external IP (if using LoadBalancer) to be assigned to the Django Service:
kubectl get services

## Step 5: Access Your Django Application

1. Once the external IP is assigned, access your Django application in your web browser using the external IP.

2. You can now access your Django application at the specified URL ( `/user-list/`).

That's it! Your Django application is now deployed on Kubernetes with PostgreSQL.

