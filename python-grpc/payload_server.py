from concurrent import futures
import logging

import grpc

import payload_pb2
import payload_pb2_grpc

class Payload(payload_pb2_grpc.PayloadServicer):

  def GetPayload(self, request, context):
    return payload_pb2.PayloadResp(data="Hello World!")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  payload_pb2_grpc.add_PayloadServicer_to_server(Payload(), server)
  server.add_insecure_port('[::]:50053')
  server.start()
  server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()