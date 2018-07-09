FROM python:3


RUN mkdir ./code
WORKDIR ./code
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
RUN chmod +x entry_point.sh
EXPOSE 8000
