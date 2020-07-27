import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.storage.init_storage import init_storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)
    init_storage()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
