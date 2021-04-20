FROM python:3.8.6

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install -y python3-dev musl-dev netcat

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt upgrade -y
COPY ./entrypoint.sh .
COPY . .
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
