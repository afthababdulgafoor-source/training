import logging


logging.basicConfig(
    filename="app.log",          
    level=logging.INFO,       
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.debug("This is a debug message")
logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical error!")