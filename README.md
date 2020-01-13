# Enrollment Microservice

An enrollment microservice for nanodegrees.


## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Testing](#testing)
1. [Swagger](#swagger)
1. [Web Client](#web-client)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/MahmoudWael/enrollment.git <my-project-name>
$ cd <my-project-name>
```

Then install dependencies and check that it works

```bash
$ make server.install      # Install the pip dependencies on the docker container
$ make server.start        # Run the container containing your local python server
```

The available routes [here](http://127.0.0.1:5000/spec).

## Commands

You can display availables make commands using `make`.

While developing, you will probably rely mostly on `make server.start`; however, there are additional scripts at your disposal:

| `make <script>`      | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `server.install`     | Install the pip dependencies on the server's container.                      |
| `server.start`       | Run your local server in its own docker container.                           |
| `server.upgrade`     | Upgrade pip packages interactively.                                          |
| `database.connect`   | Connect to your docker database.                                             |
| `database.migrate`   | Generate a database migration file using alembic, based on your model files. |
| `database.upgrade`   | Run the migrations until your database is up to date.                        |
| `database.downgrade` | Downgrade your database by one migration.                                    |
| `test`               | Run unit tests with pytest in its own container.                             |
| `test.coverage`      | Run test coverage using pytest-cov.                                          |
| `test.lint`          | Run flake8 on the `src` and `test` directories.                              |
| `test.safety`        | Run safety to check if your vendors have security issues.                    |
| `client.start`       | Start react app in its docker container
| `client.stop`        | Stop react app container
                                  

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :

```bash
$ make database.connect
```



## Application Structure


```
.
├── migrations               # Database's migrations settings
│   └── versions             # Database's migrations versions generated by alembic
├── src                      # Application source code
│   ├── models               # Python classes modeling the database
│   │   ├── abc.py           # Abstract base class model
│   │   └── enrollment.py    # Definition of the enrollment model
│   ├── repositories         # Python classes allowing you to interact with your models
│   │   └── enrollment.py    # Methods to easily handle enrollment models
│   ├── resources            # Python classes containing the HTTP verbs of your routes
│   │   └── enrollment.py    # Rest verbs related to the enrollment routes
│   ├── routes               # Routes definitions and links to their associated resources
│   │   ├── __init__.py      # Contains every blueprint of your API
│   │   └── enrollment.py    # The blueprint related to the enrollment
│   ├── swagger              # Resources documentation
│   │   └── enrollment       # Documentation of the enrollment resource
│   │       └── GET.yml      # Documentation of the GET method on the enrollment resource
│   ├── config.py            # Project configuration settings
│   ├── manage.py            # Project commands
│   └── server.py            # Server configuration
└── test                     # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make server.start           # Create the containers containing your python server in your terminal
```
You can check the logs in the `./server.log` file.

## Testing

You can run your tests in their own container with the command:

```bash
$ make test
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make test.lint
```

## Swagger

The API description will be available [here](http://127.0.0.1:5000/spec).
The Swagger UI will be available [here](http://127.0.0.1:5000/apidocs/).

## Web Client

The client directory has a react app to consume available and open for enrollment nanodegrees and send a request to our back-end to enroll user to
those nanodegrees.

No UI libraries are being used with the web app.

React app will be available [here](http://127.0.0.1:3000).

```bash
$ make client.start
```


![](https://media.giphy.com/media/MEvcqlB1dpfCq6r6TX/giphy.gif)
