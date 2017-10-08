FROM debian:jessie-slim

MAINTAINER dev@corykey.com

RUN apt-get update -y \
	&& apt-get install -y --force-yes python2.7 apt-utils git screen wget

RUN apt-get install -y --force-yes python-bs4 \
	&& apt-get install -y --force-yes libmysqlclient-dev \
	&& apt-get install -y --force-yes python-dev \
	&& apt-get install -y --force-yes python-pip

RUN wget https://bootstrap.pypa.io/get-pip.py \
	&& python ./get-pip.py

RUN pip install --upgrade google-api-python-client \
	&& pip install --upgrade google-cloud-pubsub \
	&& pip install memory-profiler \
	&& pip install beautifulsoup4 \
	&& pip install elasticsearch \
	&& pip install riot_observer \
	&& pip install MySQL-python \
	&& pip install feedparser \
	&& pip install rethinkdb \
	&& pip install pygoogle \
	&& pip install googlemaps \
	&& pip install httplib2 \
	&& pip install tornado \
	&& pip install requests \
	&& pip install twitter \
	&& pip install psutil \
	&& pip install redis \
	&& pip install pymysql


VOLUME ["/code"]
EXPOSE 9999 9999

CMD ["sleep", "99999"]
