# Vodafone-Ziggo Assignment

####


## Overview

## Requirements
Python 3.8+

## Install Requirements
```bash
pip3 install -r requirements.txt
```
## Usage
Please ensure before running tests swagger server is up and running


Local:

```
http://localhost:8080/mdenhoedt/PetStore/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/mdenhoedt/PetStore/1.0.0/swagger.json
```

## Running with Docker

```bash
# starting up a container
docker run -p 8080:8080 swagger_server
```

## Running with Kubernetes
```bash
#Fetch kubernetes external IP of running service:
externalip=$(kubectl get svc swagger-server --template="{{range .status.loadBalancer.ingress}}{{.ip}}{{end}}")
```

## Command to run tests
```bash
BASE_URI=<BASE_URI> pytest -rA tests --junitxml="result.xml"
```
