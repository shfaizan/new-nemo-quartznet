FROM nvcr.io/nvidia/nemo:v1.0.0b1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
