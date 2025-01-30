FROM python:3.10-bookworm

RUN apt-get update && apt-get install -y can-utils
RUN pip install python-can

WORKDIR /can_stresstest
COPY . .

