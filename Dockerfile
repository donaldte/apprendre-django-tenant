FROM python:3.9
RUN apt-get update
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME /apprendre-django-tenant
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . $APP_HOME
