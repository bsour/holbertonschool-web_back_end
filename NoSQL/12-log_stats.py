#!/usr/bin/env python3
"""
Python script to provide statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Retrieve and display statistics about Nginx

    Args:
         None
    Returns:
            None
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Count the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Count the number of documents with method=GET and path=/status
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
