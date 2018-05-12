import grpc
import time
import calculator

from concurrent import futures
from portal_api import portal_api_pb2
from portal_api import portal_api_pb2_grpc
#from server.server import  *

class PlayerServicer(portal_api_pb2_grpc.PlayServicer):

    def EnrolPlayer(self, request, context):
        response = portal_api_pb2.Status()
        response.value = 200
        response.port = 9999
        return response
