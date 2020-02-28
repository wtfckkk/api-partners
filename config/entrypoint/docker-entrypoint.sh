#!/bin/bash 
set -e

_wait(){
    /bin/bash /entrypoint/wait-for-it.sh ${DB_HOST}:${DB_PORT} -s -t 30 -- "$@"
}

if [ "$1" == "bootstrap" ]; then
    _wait python manage.py migrate
elif [ "$1" == "migrate" ]; then
    _wait python manage.py migrate
elif [ "$1" == "loaddata" ]; then
    _wait python manage.py loaddata initial_data/*.json
elif [ "$1" == "sudo" ]; then
    _wait python manage.py sudo
elif [ "$1" == "test" ]; then
    _wait python manage.py test
elif [ "$1" == "./manage.py" ]; then
    _wait echo "DB Ready" 
    exec "$@"
elif [[ "$1" == "python" && "$2" == "manage.py" ]]; then
    _wait echo "DB Ready" 
    exec "$@"
else
    exec "$@"
fi
