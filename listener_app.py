from panini import app as panini_app
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# # create logger
# logger = logging.getLogger('__name__')
# level = logging.INFO
# logger.setLevel(level)

# # create console handler and set level to debug
# console_handler = logging.StreamHandler()
# console_handler.setLevel(level)

# # add ch to logger
# logger.addHandler(console_handler)

app = panini_app.App(
        service_name='listener_app',
        host='nats_messanger',
        port=4222,
)

# Create a connection string
db_user = os.getenv('POSTGRES_USER', default='root')
db_password = os.getenv('POSTGRES_PASSWORD', default='example')
db_url = os.getenv('DATABASE_HOST', default='db')
db_port = int(os.getenv('PORT', default='5432'))
db_name = os.getenv('POSTGRES_DB', default='messages')
connection = "postgresql://{}:{}@{}:{}/{}".format(db_user,db_password, db_url,db_port, db_name)

# Connect to Postgres
engine = create_engine(connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM Model
Base = declarative_base()
##

class Message(Base):
    __tablename__ = db_name

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    data = Column(String)
Base.metadata.create_all(bind=engine)

@app.listen("request")
# async def request_listener(msg):
#     """ request endpoint """
#     print(f"request {msg.data} from {msg.subject} has been processed")
#     return {"success": True, "message": "request has been processed"}
async def message_handler(msg):
    """ request endpoint """
    print(f"request {msg.data} from {msg.subject} has been processed")
    # Handle message received from NATS
    session = SessionLocal()
    session.begin()
    print("session  begin success")
    try:
        # Parse message and save to Postgres
        print("entered to try")
        data = msg.data["data"]
        print(f"data is {data}")
        subject = msg.subject
        print(f"subject is {subject}")
        message = Message(subject=subject, data=data)
        print("entered the sub and mess to class message")
        # insert the message in the DB
        session.add(message)
        print('Massage has successfully added to DB') 
        # return (f"{subject}")
    except:
        print("entered to exept")        
        # Handle option to add to postgress
        # logging.error("Handle option to add to postgress")
        session.rollback()
    finally:
        print("entered to finally")                
        # logging.info("Sesssion closed")
        session.commit()
        session.close()
        print("session closed")
    return {"success": True, "message": "message handler session completed"}


# metrics.register_default(
#     metrics.counter(
#         'by_path_counter', 'Request count by request paths',
#         labels={'path': lambda: request.path}
#     )
# )




if __name__ == "__main__":
    app.start()