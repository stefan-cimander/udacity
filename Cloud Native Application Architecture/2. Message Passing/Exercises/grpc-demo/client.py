import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

print("Getting existing orders...")

response = stub.Get(order_pb2.Empty())
print(response)


print("Sending new sample order...")

newOrder = order_pb2.OrderMessage(
    id="3",
    created_by="User3",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at="2021-06-20T21:48:23",
    equipment=[order_pb2.OrderMessage.Equipment.WEBCAM]
)

response = stub.Create(newOrder)