import grpc

# import the generated classes
import portal_api.portal_api_pb2 as portal_api_pb2
import portal_api.portal_api_pb2_grpc as portal_api_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = portal_api_pb2_grpc.PlayStub(channel)

# create a valid request message
name = portal_api_pb2.Player(name="Lee")

# make the call
response = stub.EnrolPlayer(name)

# et voilà
print(response)
