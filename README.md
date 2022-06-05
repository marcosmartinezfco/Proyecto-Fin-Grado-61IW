# AI-nance: Stocks Prediction

Final thesis diploma for the Software Engineering Degree of the Universidad Politecnica de Madrid.

# Overview

The goal is to build an entire infrastructure using a micro-services pattern, focusing on automation and deployment, to serve NASDAQ stock prices predictions.

## Architecture
![Architecture](https://github.com/marcosmartinezfco/TFG-61IW-memory/blob/main/figures/architecture.png)

# How to run
### Tensorflow Server
You need to export the environment variable ```$MODELPATH``` in order for Tensorflow Server to be able to find the prediction model. Tensorflow Server will automatically pick the models from ```/predictionModule/mlp_model```, save your models there to be able to access them.

```bash
export MODELPATH="/repo-location/predictionModule"
```

### Docker Compose
After installing Docker and Docker compose, you can run the compose command in the same location as the ```docker-compose.yml``` file.

```bash
docker-compose up
```
Once all the containers are up and running you can request price predictions by specifiying the desired company ticker.

```
localhost:8000/predition/<str>:ticker
```
