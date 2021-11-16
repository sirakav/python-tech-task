FROM python:3.9.7-slim

RUN groupadd --gid 1000 app && \
    useradd --create-home --gid 1000 --uid 1000 app

RUN mkdir -p /home/app/src

COPY docker/gunicorn.py /home/app/gunicorn.py

COPY run.py /home/app

WORKDIR /home/app/

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

USER app
COPY ./app ./app

ENTRYPOINT ["gunicorn"]

CMD ["--config=/home/app/gunicorn.py", "run:app"]
