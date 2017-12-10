FROM python:3.6

RUN  apt-get update && apt-get -y install postgresql-client

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend
ADD . /var/www/backend

# Install dependencies from requirments.txt
RUN pip install -r requirements.txt
RUN python -m unittest -v

EXPOSE 5000

CMD ["python","backend.py"]
