#! /usr/bin/env sh

# Exit in case of error
set -e

docker-compose -f docker-compose.yml pull

TAG=${TAG?Variable not set} \
FRONTEND_ENV=${FRONTEND_ENV-production} \
docker-compose \
-f docker-compose.yml \
build
