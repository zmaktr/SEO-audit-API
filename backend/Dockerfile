FROM python:3.9.14-bullseye
ENV PYTHONUNBUFFERED=1
RUN apt-get update 
WORKDIR /seo-audit
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8001"]