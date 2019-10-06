#!/bin/sh

docker pull postgres:latest
cd container
docker build . -t pizza-django