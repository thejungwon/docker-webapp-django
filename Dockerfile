FROM python:3


WORKDIR /usr/src/app

ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . ./src/
RUN chmod +x entry_point.sh
EXPOSE 8000
