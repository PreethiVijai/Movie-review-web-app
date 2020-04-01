FROM python:3

# Dir setup
ENV APP_DIR /app
RUN mkdir ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# expose http port
EXPOSE 80

# copy config files into filesystem
COPY src .

CMD [ "python3", "search.py", "-u" ]
