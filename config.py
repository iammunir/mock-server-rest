import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_PASSWORD = os.environ.get("DB_PASSWORD", "admin")
DB_USER = os.environ.get("DB_USER", "root")
DB_NAME = os.environ.get("DB_NAME", "customer_hub")