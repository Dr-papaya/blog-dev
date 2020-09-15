FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# start django here
# Django key. CHANGEME
# ENV SECRET_KEY supersecretkey
# Until we serve media files properly (django dev server doesn't serve media files with with debug=false)
# ENV DEBUG true

RUN python manage.py migrate
#RUN python manage.py runserver
#ENTRYPOINT ./entrypoint.sh
