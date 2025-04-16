from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Pydantic model for response
class TestDataResponse(BaseModel):
    id: int
    name: str
    description: str
    value: int

    class Config:
        from_attributes = True

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL environment variable found")

logger.info(f"Connecting to database...")

# Create engine with echo=True to see SQL queries
engine = create_engine(DATABASE_URL, echo=True)

# Test database connection
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        logger.info("Successfully connected to the database!")
except Exception as e:
    logger.error(f"Error connecting to the database: {str(e)}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class
Base = declarative_base()

# Create test table model
class TestData(Base):
    __tablename__ = "test_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    value = Column(Integer)

# Create tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully!")
except Exception as e:
    logger.error(f"Error creating tables: {str(e)}")
    raise

# Create FastAPI app
app = FastAPI(title="Quantycs API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Quantycs API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/test-data", response_model=list[TestDataResponse])
async def get_test_data():
    try:
        # Create a new session
        db = SessionLocal()
        logger.info("Executing query to fetch test data...")
        
        # Use SQLAlchemy ORM to query the data
        result = db.query(TestData).all()
        logger.info(f"Successfully retrieved {len(result)} records")
        return result
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

def start():
    """Start the server"""
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    start() 