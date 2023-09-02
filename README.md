# Django project with postgres all based on docker
It's about a simple django project with one view returning simple information fetched from postgres db



### how to run the project

Pour lancer le projet correctement suivez l'ordre ci-dessous de lancement des services:

0. first clone the project
1. make sure you have docker and docker compose installed , up and running
2. inside docker-compose.yml file location run `docker-compose up --build`
3. wait the web server to start and try to access to http://localhost:8000/user-list/
4. You should normally get a json with some data

