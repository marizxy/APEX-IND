from pathlib import Path
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "apaar_ultimate_enterprise.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EnterpriseStudent(Base):
    __tablename__ = "enterprise_students"
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, index=True)
    permanent_id = Column(String, index=True)
    student_name = Column(String, index=True)
    apaar_id = Column(String, unique=True, index=True)
    course = Column(String)
    category = Column(String)
    ai_risk_score = Column(String)
    dropout_risk = Column(String)
    scholarship_status = Column(String)
    status = Column(String)

class EnterpriseLog(Base):
    __tablename__ = "enterprise_logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    action = Column(String)
    actor = Column(String)
    block_hash = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
