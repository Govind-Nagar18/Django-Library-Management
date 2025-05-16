set -o errexit

pip install -r requirements.txt

pythom manage.py collectstatic --no-input 

pythom manage.py migrate