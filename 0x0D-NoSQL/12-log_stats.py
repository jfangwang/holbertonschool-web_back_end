#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

cli = MongoClient()
log = cli.logs.nginx

total = log.count_documents({})
get = log.count_documents({"method": "GET"})
post = log.count_documents({"method": "POST"})
put = log.count_documents({"method": "PUT"})
patch = log.count_documents({"method": "PATCH"})
delete = log.count_documents({"method": "DELETE"})
status_check = log.count_documents({"method": "GET", "path": "/status"})

print(f"{total} logs")
print("Methods:")
print(f"\tmethod GET: {get}")
print(f"\tmethod POST: {post}")
print(f"\tmethod PUT: {put}")
print(f"\tmethod PATCH: {patch}")
print(f"\tmethod DELETE: {delete}")
print(f"{status_check} status check")
