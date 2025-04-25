# app/__init__.py

# Optional: Initialize package-level variables
DB_ENGINE = "sqlite:///tasks.db"

# Optional: Define public exports
__all__ = ["models", "schemas"]  # Controls `from app import *`

# Optional: Run setup code
print(f"Initializing 'app' package with DB: {DB_ENGINE}")