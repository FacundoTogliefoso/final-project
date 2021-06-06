FROM python:3.8-buster
ENV PYTHONBUFFERED 1

# RUN apt update-y
# RUN apt upgrade -y
# RUN apt install --no-install-recommends -y build-essential python3-dev
# RUN pip install --upgrade pip
# RUN apt autoremove -y
# RUN apt clean && rm -rf /var/lib/apt/lists/*

RUN set -ex && mkdir /app

WORKDIR /app
# COPY ["requirements.txt", "/app/"]

# RUN pip install -r requirements.txt