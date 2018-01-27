FROM python:3.6

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  apt-key add -

RUN  apt-get update && apt-get upgrade -y && apt-get -y install postgresql-client

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend
ADD . /var/www/backend

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt
RUN python -m unittest discover --verbose

EXPOSE 80

CMD ["python","backend.py"]
