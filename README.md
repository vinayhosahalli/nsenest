# NSENEST

## steps to dev run
## 1.update env file
## 2. install dependency
> pipenv install
## 3. migrate database
> python manage.py migrate
## 4. run server
> python manage.py runserver
## 5 run celery workers
> celery -A nsenest beat -l info --logfile=celery.beat.log --detach
> celery -A nsenest worker -l info --logfile=celery.log --detach
# index
![Alt text](https://github.com/vinayhosahalli/nsenest/blob/master/docs/1.png?raw=true "Title")

# celary task logs
![Alt text](https://github.com/vinayhosahalli/nsenest/blob/master/docs/2.png?raw=true "Title")

# API
![Alt text](https://github.com/vinayhosahalli/nsenest/blob/master/docs/3.png?raw=true "Title")


