FROM python:3.9.13-slim-bullseye as deploy

ARG APP_NAME
ARG DEPLOYMENT_USER=angelica
ARG WORK_DIR=/project

ARG USER=angelica

LABEL app=${APP_NAME}

RUN mkdir -p /consumer-alarm

COPY . /consumer-alarm

WORKDIR /consumer-alarm

RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

RUN addgroup --system ${USER} \
    && adduser --system --disabled-password --disabled-login  --gecos "" --group ${USER} \
    && chown -R ${USER} /consumer-alarm

COPY --chown=${USER}:${USER} . .

USER ${USER}

CMD [ "gunicorn", "-w","1", "-k" ,"uvicorn.workers.UvicornH11Worker", "--chdir", ".", "-b", "0.0.0.0:8001", "app.main:app" ]



