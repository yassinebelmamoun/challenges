# Challenges

## Getting Started

### Prerequisites

- python3.6
- Docker
- docker-compose
- virtualenv
- Postgres

### Environment variables

| NAME                  | DEFAULT              | DESCRIPTION                                        |
| --------------------- | ---------            | -------------------------------------------------- |
| SECRET_KEY            | notasecret           | A secret key for a particular Django installation. |
| DEBUG                 | true                 | Flag that turns on debug mode. `true` or `false`   |
| DJANGO_SETTINGS_MODULE| test_assignment.settings| Name of the settings module                     |
| ALLOWED_HOSTS         | *                    | List of allowed hosts, separated by comma(,)       |
| POSTGRES_DB           | test_assignment      | PostgresQL Database Name                           |
| POSTGRES_PASSWORD     | postgres             | PostgresQL  User's password                        |
| POSTGRES_USER         | postgres             | PostgresQL  User's username                        |
| POSTGRES_HOST         | postgres             | Name of the host                                   |
| POSTGRES_PORT         | 5432                 | Port of the connection                             |

### Installing the project

Clone the project to your machine  
```
git clone git@github.com:katalyzator/challenges.git
```

Go into project directory  
```
cd challenges
```


### Running with Docker

Declare environment variables. You can find this information in **ENVIRONMENT VARIABLES** section.

Start services  
```
docker-compose up --build
```

Server is up and running on port 8000

### Documentation

After running project you can get through the link http://127.0.0.1:8000/documentation to see documentation

### Running with manage.py

Start postgres  
```
docker-compose up postgres
```

Create virtual environment  
```
virtualenv -p python3 venv
```

Activate your virtual environment  
```
source venv/bin/activate
```

Install requirements  
```
pip install -r requirements/dev.txt
```

Declare environment variables  
```
export <ENV_VAR>=<ENV_VALUE>
```

Apply new migrations if any  
```
python manage.py migrate
```

Start server  
```
python manage.py runserver 8000
```

Server is up and running on port 8000


## Basic commands

### Setting up your users

To create a superuser account, use this command:  
```
python manage.py createsuperuser
```

### Creating migrations
 
```
python manage.py makemigrations
```

### Applying migrations
 
```
python manage.py migrate
```

### If you are using docker to start the server, then you need to execute these commands

```
docker exec -it challenges_django sh
```

inside docker terminal

```commandline
python manage.py createsuperser
```

### Running tests

```
python manage.py test
```


## Data and Action flow

### View
This is basically a controller that invokes other components 
and does not contain any business logic inside.  
Usually it is an `APIView` that only knows about what authentication 
and permissions classes it should use.

### Service
This component is responsible for the business logic related stuff 
and contains some high-level API for the controller(view).  
Usually it is basic Python class with some `classmethods`.
If the method is/should not be used outside of the service
then make sure to mark it as private using `_` in the naming.  
You should always use [**type annotations**](https://docs.python.org/3/library/typing.html) when defining these methods, 
so everyone knows how to use them.

### Serializer
This component is responsible for validating user input and serializing `querysets` into native Python data types.  
Don't use `save()` method. It will give too much responsibility to this component. The only things it should do
are defined above. 

### Model
This is basically a representation of your database table.  
Thus, it should not contain any business logic here. Sometimes it may have some calculated fields(`@property`).
