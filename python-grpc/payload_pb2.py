# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rpayload.proto\"\x0c\n\nPayloadReq\"\x1b\n\x0bPayloadResp\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t24\n\x07Payload\x12)\n\nGetPayload\x12\x0b.PayloadReq\x1a\x0c.PayloadResp\"\x00\x62\x06proto3')
)




_PAYLOADREQ = _descriptor.Descriptor(
  name='PayloadReq',
  full_name='PayloadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=29,
)


_PAYLOADRESP = _descriptor.Descriptor(
  name='PayloadResp',
  full_name='PayloadResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PayloadResp.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=58,
)

DESCRIPTOR.message_types_by_name['PayloadReq'] = _PAYLOADREQ
DESCRIPTOR.message_types_by_name['PayloadResp'] = _PAYLOADRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PayloadReq = _reflection.GeneratedProtocolMessageType('PayloadReq', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADREQ,
  '__module__' : 'payload_pb2'
  # @@protoc_insertion_point(class_scope:PayloadReq)
  })
_sym_db.RegisterMessage(PayloadReq)

PayloadResp = _reflection.GeneratedProtocolMessageType('PayloadResp', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADRESP,
  '__module__' : 'payload_pb2'
  # @@protoc_insertion_point(class_scope:PayloadResp)
  })
_sym_db.RegisterMessage(PayloadResp)



_PAYLOAD = _descriptor.ServiceDescriptor(
  name='Payload',
  full_name='Payload',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=60,
  serialized_end=112,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPayload',
    full_name='Payload.GetPayload',
    index=0,
    containing_service=None,
    input_type=_PAYLOADREQ,
    output_type=_PAYLOADRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYLOAD)

DESCRIPTOR.services_by_name['Payload'] = _PAYLOAD

# @@protoc_insertion_point(module_scope)
