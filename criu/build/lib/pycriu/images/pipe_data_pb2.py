# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipe-data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipe-data.proto',
  package='',
  serialized_pb=_b('\n\x0fpipe-data.proto\"?\n\x0fpipe_data_entry\x12\x0f\n\x07pipe_id\x18\x01 \x02(\r\x12\r\n\x05\x62ytes\x18\x02 \x02(\r\x12\x0c\n\x04size\x18\x03 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PIPE_DATA_ENTRY = _descriptor.Descriptor(
  name='pipe_data_entry',
  full_name='pipe_data_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipe_id', full_name='pipe_data_entry.pipe_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='pipe_data_entry.bytes', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='pipe_data_entry.size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['pipe_data_entry'] = _PIPE_DATA_ENTRY

pipe_data_entry = _reflection.GeneratedProtocolMessageType('pipe_data_entry', (_message.Message,), dict(
  DESCRIPTOR = _PIPE_DATA_ENTRY,
  __module__ = 'pipe_data_pb2'
  # @@protoc_insertion_point(class_scope:pipe_data_entry)
  ))
_sym_db.RegisterMessage(pipe_data_entry)


# @@protoc_insertion_point(module_scope)
