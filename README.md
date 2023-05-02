# GitHookAPI
## This is the API created to work with Arqmeds gitHook
### installation guide:
- 1: first make sure you create a file called .env in the root of your project.
Use [this one](.env-example) as an example.
- 2: make sure you have [Docker](https://www.docker.com/) installed and running on your machine.
- 3: run the following command to create a shared network between the containers:
    ```python
    docker network create mynetwork
    ```
- 4: Run the following command in the root:
    ```python
    docker compose up --build
    ```
    This command will build and get up the application's container.

- Make sure the api is running with the command:
    ```python
    docker ps
    ```
#### The project is already running in a container on port 8000.
## Tests:
#### to run tests inside a container:
```python
docker exec -it api-container-id bash
```
**(remember to replace the id of the container correctly)**
##### Container id:
```python
docker ps
```
##### (then you copy and replace it)

### Another way:
**in a terminal, navigate to the root of the project:**
```python
pip install -r requirements.txt
```
#### In another terminal:
```python
python manage.py test api/tests/**
```

## The project is already running.
### Now it's time to install and run [OpenAIWorker](https://github.com/kaiqueBellmont/openAPIWorker/blob/master/README.md).
### [Click Here](https://github.com/kaiqueBellmont/openAPIWorker/blob/master/README.md) to finally finish it.