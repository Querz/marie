#!/bin/bash

# docker-machine create -d virtualbox local

# docker run swarm create

# eval "$(docker-machine env local)"


D_TOKEN="64bcdc5229b1b62dc4a1750dce024666"

docker-machine create \
        -d virtualbox \
        --swarm \
        --swarm-master \
        --swarm-discovery token://$D_TOKEN \
        swarm-master