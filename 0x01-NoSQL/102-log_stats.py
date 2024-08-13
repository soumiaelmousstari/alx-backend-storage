#!/usr/bin/env python3
"""A Python script that provides some stats about
Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def print_log_stats():
    """print log stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    GET = client.logs.nginx.count_documents({"method": "GET"})
    POST = client.logs.nginx.count_documents({"method": "POST"})
    PUT = client.logs.nginx.count_documents({"method": "PUT"})
    PATCH = client.logs.nginx.count_documents({"method": "PATCH"})
    DELETE = client.logs.nginx.count_documents({"method": "DELETE"})
    PATH = client.logs.nginx.count_documents({"method": "GET",
                                              "PATH": "/status"})
    print(f"{client.logs.nginx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {GET}")
    print(f"\tmethod POST: {POST}")
    print(f"\tmethod PUT: {PUT}")
    print(f"\tmethod PATCH: {PATCH}")
    print(f"\tmethod DELETE: {DELETE}")
    print(f"{PATH} status chek")
    print("IPs:")
    sort = client.logs.nginx.aggregate(
            [{"$group": {"_id": "$ip", "count": {"$sun": 1}}},
             {"$sort": {"count": -1}}])
    j = 0
    for i in sort:
        if j == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        j += 1


if __name__ == "__main__":
    printf_log_stats()
