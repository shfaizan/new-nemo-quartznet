
FROM pytorch/pytorch:1.5.1-cuda10.1-cudnn7-devel

RUN apt-get update && apt-get install -y libsndfile1 ffmpeg

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
