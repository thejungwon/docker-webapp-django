FROM python:3


RUN mkdir ./code
WORKDIR ./code
ADD requirements.txt ./code
RUN pip install -r requirements.txt
ADD . ./code
RUN chmod +x entry_point.sh
EXPOSE 8000
