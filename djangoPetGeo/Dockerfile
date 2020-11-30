# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /usr/src/djangoPetGeo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing gdal-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt && \
    pip install gdal --no-cache-dir

# copy project
COPY . .

ENTRYPOINT ["/usr/src/djangoPetGeo/entrypoint.sh"]