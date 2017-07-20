# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remap-file-path.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='remap-file-path.proto',
  package='',
  serialized_pb=_b('\n\x15remap-file-path.proto\"[\n\x15remap_file_path_entry\x12\x0f\n\x07orig_id\x18\x01 \x02(\r\x12\x10\n\x08remap_id\x18\x02 \x02(\r\x12\x1f\n\nremap_type\x18\x03 \x01(\x0e\x32\x0b.remap_type*/\n\nremap_type\x12\n\n\x06LINKED\x10\x00\x12\t\n\x05GHOST\x10\x01\x12\n\n\x06PROCFS\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REMAP_TYPE = _descriptor.EnumDescriptor(
  name='remap_type',
  full_name='remap_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LINKED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GHOST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCFS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=118,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_REMAP_TYPE)

remap_type = enum_type_wrapper.EnumTypeWrapper(_REMAP_TYPE)
LINKED = 0
GHOST = 1
PROCFS = 2



_REMAP_FILE_PATH_ENTRY = _descriptor.Descriptor(
  name='remap_file_path_entry',
  full_name='remap_file_path_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orig_id', full_name='remap_file_path_entry.orig_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remap_id', full_name='remap_file_path_entry.remap_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remap_type', full_name='remap_file_path_entry.remap_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=25,
  serialized_end=116,
)

_REMAP_FILE_PATH_ENTRY.fields_by_name['remap_type'].enum_type = _REMAP_TYPE
DESCRIPTOR.message_types_by_name['remap_file_path_entry'] = _REMAP_FILE_PATH_ENTRY
DESCRIPTOR.enum_types_by_name['remap_type'] = _REMAP_TYPE

remap_file_path_entry = _reflection.GeneratedProtocolMessageType('remap_file_path_entry', (_message.Message,), dict(
  DESCRIPTOR = _REMAP_FILE_PATH_ENTRY,
  __module__ = 'remap_file_path_pb2'
  # @@protoc_insertion_point(class_scope:remap_file_path_entry)
  ))
_sym_db.RegisterMessage(remap_file_path_entry)


# @@protoc_insertion_point(module_scope)