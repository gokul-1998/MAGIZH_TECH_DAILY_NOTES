import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Database query executed")
logging.info("User logged in")
logging.warning("Rate limit almost reached")
logging.error("Payment failed")
logging.critical("Database server is down")


# print("Logging complete")
