import grpc
import time
import calculator

from concurrent import futures
from portal_api import portal_api_pb2
from portal_api import portal_api_pb2_grpc

class CalculatorServicer(portal_api_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = portal_api_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response
