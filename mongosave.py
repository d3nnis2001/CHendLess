import requests
from pymongo import MongoClient

def scrape_and_store():
    # Perform web scraping
    scraped_data = {'example_key': 'example_value'}
    
    # Connect to MongoDB and store data
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection']
    collection.insert_one(scraped_data)

if __name__ == "__main__":
    scrape_and_store()