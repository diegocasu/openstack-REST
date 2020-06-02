FROM python:3-alpine

RUN mkdir -p /usr/src/web
WORKDIR /usr/src/web

COPY requirements.txt /usr/src/web

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/web

EXPOSE 5000

ENV FLASK_APP openstackr
ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]
