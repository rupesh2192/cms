# CMS: Customer Management System

The purpose of the project is to demonstrate the knowledge of below modules:
* Django
* Django REST Framework
* API Documentation
* Clean & Scalable Code
* Unit test
* API & Database Design

### Run on Local
##### Pre-Requisite:
* [Docker](https://docs.docker.com/engine/install/)

##### Command
```
docker build -t cms . && docker run -p 8000:8000 cms
```
##### Important Links
* API Swagger: http://localhost:8000/swagger/
* API Documentation: http://localhost:8000/redoc/
* DRF Browsable API: http://localhost:8000/


#### Run Unit Tests
* ```python manage.py test```

#### Block Diagram
![block_diagram](https://github.com/rupesh2192/cms/blob/master/Django.png)
