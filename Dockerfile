FROM python:3


WORKDIR /usr/src/app

ADD requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./src/app/
RUN chmod +x entry_point.sh
EXPOSE 8000
