# Backend Challenge
## Stack
- Django 2.1.5
- MySQL 5.7

## Requirements
- Git (https://git-scm.com/downloads)
- Docker (https://www.docker.com/)

## Installation
```
git clone https://github.com/wtfckkk/api-partners.git api-partners && cd api-partners
docker-compose build && docker-compose up
```

## Endpoints

File api-partners.postman_collection.json has a collection with the requests for an easy use

```
POST: localhost:8070/partners/
GET:  localhost:8070/partners/{id}/
POST:  localhost:8070/partners/nearest/
```

