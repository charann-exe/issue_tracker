from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# check_same_thread=False is needed only for SQLite to allow usage in FastAPI threads
engine = create_engine(
	SQLALCHEMY_DATABASE_URL,
	connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
	"""FastAPI dependency to provide a scoped SQLAlchemy session."""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

