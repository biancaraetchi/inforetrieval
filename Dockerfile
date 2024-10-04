FROM --platform=linux/amd64 python:3.10.13

RUN pip install virtualenv
RUN virtualenv /venv

RUN apt update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN bash -c "source /venv/bin/activate && pip install -r requirements.txt"

COPY ./keras_vggface ./keras_vggface
RUN cp -r keras_vggface /venv/lib/python3.10/site-packages/keras_vggface

ENTRYPOINT [ "/bin/bash", "-c", "source /venv/bin/activate && python face_recognition.py > results.txt 2> stderr.txt"]