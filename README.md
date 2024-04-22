Build using:

```
docker build -t youracr.azurecr.io/simulator-api:latest .
```

Push using:

```
docker push youracr.azurecr.io/simulator-api:latest
```

Run using:

```
docker run -p 8000:8000 \
    -e SIMULATOR_MODE=generate \
    -e SIMULATOR_API_KEY=blablabla \
    -e MODE=embedding \
    -e AZURE_OPENAI_DEPLOYMENT=embedding \
    -e AZURE_OPENAI_KEY=blablabla \
    -e OPENAI_DEPLOYMENT_CONFIG_PATH=/app/openai_deployment_config.json \
    -e LOG_LEVEL=DEBUG \
    -e EXTENSION_PATH=/app/forwarders/api_forwarder.py \
    youracr.azurecr.io/simulator-api:latest

```