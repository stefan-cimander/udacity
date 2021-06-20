import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc

class OrderServicer(order_pb2_grpc.OrderServiceServicer):

    def Get(self, request, context):
        first_order = order_pb2.OrderMessage(
            id="1",
            created_by="User1",
            status=order_pb2.OrderMessage.Status.COMPLETED,
            created_at="2021-04-27T18:37:44",
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD],
        )

        second_order = order_pb2.OrderMessage(
            id="2",
            created_by="User2",
            status=order_pb2.OrderMessage.Status.PROCESSING,
            created_at="2021-05-30T04:21:58",
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE],
        )

        result = order_pb2.OrderMessageList()
        result.orders.extend([first_order, second_order])
        return result


    def Create(self, request, context):
        
        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": request.equipment,
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)