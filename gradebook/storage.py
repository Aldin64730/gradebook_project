import json
import os
import logging

DEFAULT_PATH = "data/gradebook.json"

def save_data(data,filepath=DEFAULT_PATH):
    """
    Saves the current data dictionary to a JSON file.
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w') as f:
            json.dump(data,f,indent=4)
        
        logging.info(f"Data successfully saved to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save data to: {e}")
        print(f"Error saving data: {e}")


def load_data(filepath=DEFAULT_PATH):
    """
    Loads data from JSON file. Returns empty structure if file is missing or invalid.
    """
    if not os.path.exists(filepath):
        logging.info("No storage file found. Starting with empty data.")
        return {"students": [], "courses": [], "enrollments": []}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        msg = "Warning: The data file is corrupted or invalid. Starting with a clean slate"
        print(msg)
        logging.error(msg)
        return {"students": [], "courses": [], "enrollments": []}
    except Exception as e:
        logging.error(f"Unexpected error during load: {e}")
        return {"students": [], "courses": [], "enrollments": []}