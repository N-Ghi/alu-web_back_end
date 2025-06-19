#!/usr/bin/env python3
"""
Script to analyze Nginx logs stored in MongoDB and display statistics.
Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    """
    The function where it happens - Hamilton reference
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    
    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Display methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count GET requests to /status
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()