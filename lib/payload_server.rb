require 'grpc'
require '/Users/mekari/learn/comparing-rest-grpc/lib/payload_pb.rb'
require '/Users/mekari/learn/comparing-rest-grpc/lib/payload_services_pb'

class PayloadServer < Payload::Service
  def get_payload(payload_req, _unused_call)
    PayloadResp.new(data: "Hello World")
  end
end

def main 
  s = GRPC::RpcServer.new
  s.add_http2_port('0.0.0.0:50051', :this_port_is_insecure)
  s.handle(PayloadServer)
  # Runs the server with SIGHUP, SIGINT and SIGQUIT signal handlers to 
  #   gracefully shutdown.
  # User could also choose to run server via call to run_till_terminated
  s.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
end

main