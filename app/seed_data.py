from main import SessionLocal, TestData
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_test_data():
    db = SessionLocal()
    try:
        # Verificar si ya hay datos
        existing_data = db.query(TestData).first()
        if existing_data:
            logger.info("Data already exists, skipping seed")
            return

        # Crear datos de prueba
        test_data = [
            TestData(name="Test 1", description="First test data", value=100),
            TestData(name="Test 2", description="Second test data", value=200),
            TestData(name="Test 3", description="Third test data", value=300),
        ]
        
        # Insertar datos
        db.add_all(test_data)
        db.commit()
        logger.info("Test data seeded successfully!")
    
    except Exception as e:
        logger.error(f"Error seeding data: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_test_data() 