FROM python:3.9
ENV PYTHONYNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD python3 manage.py runserver 0.0.0.0:8000

#TODO optimize and remove CMD 