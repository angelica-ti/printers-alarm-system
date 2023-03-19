FROM python:3.9.13-slim-bullseye as deploy

ARG APP_NAME
ARG DEPLOYMENT_USER=angelica
ARG WORK_DIR=/project

ARG USER=angelica

LABEL app=${APP_NAME}

RUN mkdir -p /producer-alarm

COPY . /producer-alarm

WORKDIR /producer-alarm

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN addgroup --system ${USER} \
    && adduser --system --disabled-password --disabled-login  --gecos "" --group ${USER} \
    && chown -R ${USER} /producer-alarm

COPY --chown=${USER}:${USER} . .

USER ${USER}

CMD [ "gunicorn", "-w","1", "-k" ,"uvicorn.workers.UvicornH11Worker", "--chdir", ".", "-b", "0.0.0.0:8000", "main:app" ]


