FROM python:3


RUN mkdir /src/code
WORKDIR /src/code
ADD requirements.txt /src/code/
RUN pip install -r requirements.txt
ADD . /src/code/
RUN chmod +x entry_point.sh
EXPOSE 8000
