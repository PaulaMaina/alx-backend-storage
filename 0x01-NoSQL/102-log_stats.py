#!/usr/bin/env python3
"""NGINX log stats"""
from pymongo import MongoClient


def nginx_stats(nginx):
    """Provides some stats about Nginx logs"""
    print('{} logs'.format(nginx.count_documents({})))
    print('Methods:')
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for met in method:
        total = len(list(nginx.find({'method': met})))
        print('\tmethod {}: {}'.format(met, total))

    stat_check = len(list(nginx.find({'method': 'GET', 'path': '/status'})))
    print('{} status check'.format(stat_check))


def top_ips(server):
    """Printss the most present IPs in the nginx collection"""
    print('IPs:')
    logs = server.aggregate(
        [
            {
                '$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for log in logs:
        ip = log['_id']
        ip_count = log['totalRequests']
        print('\t{}: {}'.format(ip, ip_count))


def stats():
    """Main program"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_stats(client.logs.nginx)


if __name__ == '__main__':
    stats()
