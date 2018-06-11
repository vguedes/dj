 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 RUN mkdir /code/wait-for-it
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
