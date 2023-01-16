# Listener App

This application is a simple service that listens for messages on a NATS messaging service and saves them to a Postgres database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- A running NATS messaging service
- A running Postgres database

## DB Structure

The application uses a Postgres database with the following table structure:

|id|subject|data|
|----|---------|---------------------------|

List of relations:


| Schema |      Name       |   Type   |  Owner   |
|--------|-----------------|----------|----------|
| public | messages        | table    | postgres|
| public | messages_id_seq | sequence | postgres|


**Note:** the application creates the Postgres database with the same schema and relations.

### Installing

1. Clone the repository
'''
    $ git clone git@github.com:LizAsraf/nats-listener.git
'''

2. Create a virtual environment and activate it
'''
    $ python3 -m venv env
    $ source env/bin/activate
'''

3. Install the dependencies
'''
    $ pip install -r requirements.txt
'''

4. Set the following environment variables:
- `POSTGRES_USER`: the username for the Postgres database
- `POSTGRES_PASSWORD`: the password for the Postgres database
- `DATABASE_HOST`: the hostname or IP address of the Postgres database
- `PORT`: the port number of the Postgres database
- `POSTGRES_DB`: the name of the Postgres database

5. Run the application
'''
    $ python listener_app.py
'''

## Usage

Once the application is running, it will listen for messages on the "request" subject and save them to the Postgres database.

## Built With

* [panini](https://pypi.org/project/panini/) - A library for easy integration with NATS messaging services
* [SQLAlchemy](https://www.sqlalchemy.org/) - A SQL toolkit and ORM

## Authors

* **Liz Asraf** - *Initial work* - [Your Github](https://github.com/LizAsraf/)
