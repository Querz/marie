FROM debian:jessie-slim

MAINTAINER BlackForestCrafting <dev@corykey.com>

ENV NODE_VERSION 6.x # v0.10.40, v2.0.2, v3.x, v4.x, v5.x, v6.x

RUN apt-get update -y \
    && apt-get install -y wget screen curl nano \
    && curl -sL https://deb.nodesource.com/setup_${NODE_VERSION} | bash \
    && apt-get install -y nodejs \
    && npm install request

RUN npm install vue && npm install vue@csp \
    && npm install -g vue-cli \
    && npm install vue-router \
    && npm install vue-resource \
    && npm install material-design-icons \
    && npm install keen-ui --save \
    && npm update

WORKDIR /project_x

CMD ["sleep", "99999"]
