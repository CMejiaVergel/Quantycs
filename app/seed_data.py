import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import SessionLocal, TestData, engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_test_data():
    logger.info("Starting seed process...")
    
    # Verificar conexión a la base de datos
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1").scalar()
            logger.info(f"Database connection test successful: {result}")
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise

    db = SessionLocal()
    try:
        # Limpiar datos existentes
        db.query(TestData).delete()
        db.commit()
        logger.info("Cleaned existing data")

        # Crear nuevos datos de prueba
        test_data = [
            TestData(name="Test 1", description="First test data", value=100),
            TestData(name="Test 2", description="Second test data", value=200),
            TestData(name="Test 3", description="Third test data", value=300),
        ]
        
        # Insertar datos
        db.add_all(test_data)
        db.commit()
        
        # Verificar datos insertados
        count = db.query(TestData).count()
        logger.info(f"Test data seeded successfully! {count} records created")
    
    except Exception as e:
        logger.error(f"Error seeding data: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_test_data() 