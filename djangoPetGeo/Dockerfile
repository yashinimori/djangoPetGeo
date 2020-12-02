# pull official base image
FROM python:3.8.6

# set work directory
WORKDIR /usr/src/djangoPetGeo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libgdal-dev gdal-bin netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .

ENTRYPOINT ["/usr/src/djangoPetGeo/entrypoint.sh"]