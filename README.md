Blogapp
Using Flask to build blog that .

Integration with mongo DB.

Extension:
MONGODB: mongo DB for the users and the posts that are posted in the blog.

Testing: E2E test using curl for all the features in the blog.

Installation
Install with pip:

$ pip install -r requirements.txt
Flask Application Structure
.
├── microblog
│   ├── app
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   ├── delete_edit.html
│   │   │   ├── index.html
│   │   │   ├── login.html
│   │   │   └── posts.html


Run Flask
flask run
In flask, Default port is 5000



DB structure
 id | subject |           data            
----+---------+---------------------------


               List of relations
 Schema |      Name       |   Type   |  Owner   
--------+-----------------+----------+----------
 public | messages        | table    | postgres
 public | messages_id_seq | sequence | postgres
