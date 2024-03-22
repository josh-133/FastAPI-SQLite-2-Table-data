import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# need check_same_thread set to False because SQLite only allows one thread to communicate with it
# This is required if you want to use multiple threads with SQLite in Python
engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This creates a session factory which are used to interact with the database
# autocommit and autoflush are set to control the behaviour of sessions, and
# bind_engine specifies that this session factory will bind to the database engine
# created earlier.
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This declares a Base class for declarative class definitions, which will be used
# to create ORM classes representing database tables.
# ORM = Object-Relational Mapping  
Base = _declarative.declarative_base()