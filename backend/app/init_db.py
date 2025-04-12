from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import logging
from main import SessionLocal, TestData, engine, Base

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL environment variable found")

logger.info(f"Connecting to database...")

# Create engine with echo=True to see SQL queries
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully")

        # Create session
        db = SessionLocal()

        # Check if data already exists
        if db.query(TestData).count() == 0:
            # Add test data
            test_data = [
                TestData(name="Test 1", description="First test item", value=100),
                TestData(name="Test 2", description="Second test item", value=200),
                TestData(name="Test 3", description="Third test item", value=300),
            ]
            
            db.add_all(test_data)
            db.commit()
            logger.info("Test data inserted successfully")
        else:
            logger.info("Test data already exists")

    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 