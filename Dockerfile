FROM python:3


RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
ADD . /src/
RUN chmod +x entry_point.sh
EXPOSE 8000
