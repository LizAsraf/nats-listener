FROM python:3.8.16-slim-bullseye
WORKDIR /serviceB
COPY ./requirements.txt ./
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt  
COPY ./listener_app.py ./
ENTRYPOINT [ "python3", "listener_app.py"]