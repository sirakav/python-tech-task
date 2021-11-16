# example-api
This project aims to evaluate Python code design skills and overall technical knowledge for containerized cloud-native application development, deployment and management.
## How to start the project
This project can be deployed locally in three different ways, choose one that is acceptable and meets your demands.
### Minikube
 
Build docker image
```sh
eval $(minikube docker-env)
docker build -t gunicorn:latest .
```
Deploy using helm
```sh
helm upgrade --install --create-namespace -n example-api -f helm-charts/values-staging.yaml example-api helm-charts/
```
Expose service for testing using Minikube
```sh
minikube service --url -n example-api gunicorn
```
### Docker
Setup environment variables
```sh
cp .env.dist .env
```
Build Docker image
```sh
docker build -t gunicorn:latest .
```
Start application with Gunicorn
```sh
docker run -i -p8000:8000 --env-file .env gunicorn:latest
```
Start application with development server
```sh
docker run -i -p5000:5000 --env-file .env --entrypoint python gunicorn:latest run.py
```
### Shell
Create virtual environment and activate it
```sh
python3 -m venv .venv
source .venv/bin/activate
```
Install requirements
```sh
pip3 install -r requirements.txt
```
Start the development server
```sh
python3 run.py
```
## Tasks and questions
### Questions
 
Start by going through the project and answer these questions:
- What Python framework does this project use?
- What endpoints does this application currently have?
- Why are there two requirement files?
- How code style and testing is enforced in this project?
- Looking at the provided Dockerfile answer these questions:
  - Why is `app` user used instead of the default one?
  - How can we reduce the final image size?
- What steps are described in `.gitlab-ci.yml`?
- Describe the deployment process of this project:
  - In what environment this application is meant to run?
  - What tool is used to help and assist the deployment process?
- This README defines tree distinct ways to deploy this example application for local development:
  - How are they different?
  - Which one would you choose if you wanted to:
      - Add extra code?
      - Test application deployment?
### Tasks
- Every secure application must have authentication:
  - What authentication methods can be used?
  - What other Python web framework would make it a lot easier to integrate ACL?
  - Integrate REST API authentication tokens
- Now you have a working authentication, test it using unit tests:
  - What Python unit testing frameworks are available and are commonly used?
  - Write a simple unit test that ensures authentication functionality
- Application which are exposed to the internet suffer various attacks that can reduce QoS:
  - Integrate rate limiting
  - What rate limiting backends can be used and what are the benefits?
  
#### Additional task
 
- Add an endpoint that returns weather forecast from `https://www.weatherapi.com/`
   - The endpoint should be able to return a weather forecast for a given city and country
   - API key will be provided
 

