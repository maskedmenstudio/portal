#!/bin/python

import grpc
import time
import portal_api.portal_api_pb2 as portal_api_pb2
import portal_api.portal_api_pb2_grpc as portal_api_pb2_grpc

from concurrent import futures
from server import calculator
from server.server import *

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
portal_api_pb2_grpc.add_PlayServicer_to_server(
        PlayerServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
