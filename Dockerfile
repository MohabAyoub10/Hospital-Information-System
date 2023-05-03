ARG PYTHON_VERSION=3.11.3

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install pipenv
COPY requirements.txt /code/
RUN pipenv install -r requirements.txt
RUN pipenv install --deploy --system
COPY . /code

ENV SECRET_KEY 'django-insecure-dnssfa#!j^xlhoz-7--wd2_g24q0^b*uyxh2yjw74$nfmej6s_'
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "HIS.wsgi"]
