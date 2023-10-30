FROM python:3.9
RUN apt-get update

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /apprendre-django-tenant
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . $APP_HOME
COPY apprendre-django-tenant.conf /etc/nginx/conf.d/
CMD ["gunicorn", "platform_evaluation.wsgi:application", "-b", "0:8000", "-w", "10", "--log-level", "DEBUG", "--reload"]
