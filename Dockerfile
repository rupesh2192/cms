FROM python:3.9-slim

ENV DJANGO_SETTINGS_MODULE cms.settings
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
RUN python manage.py migrate
RUN python3 manage.py loaddata initial.json
EXPOSE 8000:8000
CMD ["/bin/bash", "entrypoint.sh"]
