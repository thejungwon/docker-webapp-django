#!/bin/sh
# If it's the first time running this script or changes are present in the code
# it builds/rebuilds the images, otherwise it uses the cached ones
docker-compose -f container/docker-compose.yml up --build