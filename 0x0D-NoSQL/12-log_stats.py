#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
import pymongo
from pymongo import MongoClient

cli = MongoClient()
log = cli.logs.nginx

print("{} logs".format(log.count_documents({})))
print("Methods")
print("    method GET: {}".format(log.count_documents({"method":"GET"})))
print("    method POST: {}".format(log.count_documents({"method":"POST"})))
print("    method PUT: {}".format(log.count_documents({"method":"PUT"})))
print("    method PATCH: {}".format(log.count_documents({"method":"PATCH"})))
print("    method DELETE: {}".format(log.count_documents({"method":"DELETE"})))
print("{} status check".format(log.count_documents({"method":"GET", "path": "/status"})))
