## RUN IMAGE FROM GHCR

```sh
docker run -it --env-file .env --gpus all ghcr.io/semantic-search/quartznet:latest

```

To build the docker image locally, run:

```git
    git clone --recurse-submodules https://github.com/semantic-search/new-nemo-quartznet.git
```

```
docker build -t quartznet .
```

```
docker run -it  --env-file .env --gpus all quartznet
```
