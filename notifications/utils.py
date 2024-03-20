import os
from pymongo import MongoClient

def get_db_handle(company, type):
    print("Soltase: Attempting to get database handle...")

    # Validate company string against preset values
    valid_companies = ["soltase", "addermatt"] # Add more companies if needed
    if company.lower() not in valid_companies:
        raise ValueError(f"Invalid company '{company}'.")

    # Validate type string against preset values
    valid_types = ["store1", "store2", "store3", "store4", "users"] # Add more types if needed
    if type.lower() not in valid_types:
        raise ValueError(f"Invalid type '{type}'.")

    # Define a map to store environment variables based on company and type
    env_variables = {
        "addermatt": {
            "store1": os.getenv("ADDERMATT_STORE1", ""),
            "store2": os.getenv("ADDERMATT_STORE2", ""),
            "store3": os.getenv("ADDERMATT_STORE3", ""),
            "store4": os.getenv("ADDERMATT_STORE4", ""),
            "users": os.getenv("ADDERMATT_USERS", ""),
            "default": os.getenv("MONGODB_URL", ""),
        },
        "soltase": {
            "store1": os.getenv("SOLTASE_STORE1", ""),
            "store2": os.getenv("SOLTASE_STORE2", ""),
            "store3": os.getenv("SOLTASE_STORE3", ""),
            "store4": os.getenv("SOLTASE_STORE4", ""),
            "users": os.getenv("SOLTASE_USERS", ""),
            "default": os.getenv("MONGODB_URL", ""),
        },
        "default": {
            "default": os.getenv("MONGODB_URL", ""),
        },
    }

    # Get the corresponding environment variable based on company and type
    dynamic_url = env_variables.get(company.lower(), {}).get(type.lower(), env_variables["default"]["default"])

    if not dynamic_url:
        raise ValueError(f"No MongoDB URI found for the given '{company}' and '{type}'.")

    print(f"Soltase: MongoDB URI found: {dynamic_url}")

    # Create a MongoClient instance
    client = MongoClient(dynamic_url)
    print("Soltase: MongoClient instance created.")
        
    # Access the specified database
    # The database name is part of the URI, so you don't need to specify it separately
    db_handle = client.get_database() # This assumes the database name is included in the URI
    print("Soltase: Database handle obtained.")

    return db_handle, client
