#!/bin/bash
docker run -it --gpus all --shm-size=32g -p 8888:8888 -v "${PWD}":/code -v $HOME/.fastai:/root/.fastai -v $HOME/.cache:/root/.cache seemeai/fastai:pt-2.4.1-fa-2.7.17
# docker run --gpus all -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work egineering/fastai:fastai-basic-dev-latest
