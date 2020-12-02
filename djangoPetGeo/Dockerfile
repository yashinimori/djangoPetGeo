# pull official base image
FROM python:3.8.6-slim

# set work directory
WORKDIR /usr/src/djangoPetGeo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev libgdal-dev gdal-bin

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir && \
    pip install gdal --no-cache-dir

# copy project
COPY . .

ENTRYPOINT ["/usr/src/djangoPetGeo/entrypoint.sh"]