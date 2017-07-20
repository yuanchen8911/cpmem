# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fh.proto

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


import opts_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fh.proto',
  package='',
  serialized_pb=_b('\n\x08\x66h.proto\x1a\nopts.proto\"U\n\x08\x66h_entry\x12\r\n\x05\x62ytes\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\r\x12\x0e\n\x06handle\x18\x03 \x03(\x04\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0e\n\x06mnt_id\x18\x05 \x01(\r\"I\n\x11irmap_cache_entry\x12\x17\n\x03\x64\x65v\x18\x01 \x02(\rB\n\xd2?\x02 \x01\xd2?\x02(\x01\x12\r\n\x05inode\x18\x02 \x02(\x04\x12\x0c\n\x04path\x18\x03 \x02(\t*!\n\x0e\x66h_entry_sizes\x12\x0f\n\x0bmin_entries\x10\x10')
  ,
  dependencies=[opts_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FH_ENTRY_SIZES = _descriptor.EnumDescriptor(
  name='fh_entry_sizes',
  full_name='fh_entry_sizes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='min_entries', index=0, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=186,
  serialized_end=219,
)
_sym_db.RegisterEnumDescriptor(_FH_ENTRY_SIZES)

fh_entry_sizes = enum_type_wrapper.EnumTypeWrapper(_FH_ENTRY_SIZES)
min_entries = 16



_FH_ENTRY = _descriptor.Descriptor(
  name='fh_entry',
  full_name='fh_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='fh_entry.bytes', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='fh_entry.type', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handle', full_name='fh_entry.handle', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='fh_entry.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnt_id', full_name='fh_entry.mnt_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=24,
  serialized_end=109,
)


_IRMAP_CACHE_ENTRY = _descriptor.Descriptor(
  name='irmap_cache_entry',
  full_name='irmap_cache_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev', full_name='irmap_cache_entry.dev', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002 \001\322?\002(\001'))),
    _descriptor.FieldDescriptor(
      name='inode', full_name='irmap_cache_entry.inode', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='irmap_cache_entry.path', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=111,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['fh_entry'] = _FH_ENTRY
DESCRIPTOR.message_types_by_name['irmap_cache_entry'] = _IRMAP_CACHE_ENTRY
DESCRIPTOR.enum_types_by_name['fh_entry_sizes'] = _FH_ENTRY_SIZES

fh_entry = _reflection.GeneratedProtocolMessageType('fh_entry', (_message.Message,), dict(
  DESCRIPTOR = _FH_ENTRY,
  __module__ = 'fh_pb2'
  # @@protoc_insertion_point(class_scope:fh_entry)
  ))
_sym_db.RegisterMessage(fh_entry)

irmap_cache_entry = _reflection.GeneratedProtocolMessageType('irmap_cache_entry', (_message.Message,), dict(
  DESCRIPTOR = _IRMAP_CACHE_ENTRY,
  __module__ = 'fh_pb2'
  # @@protoc_insertion_point(class_scope:irmap_cache_entry)
  ))
_sym_db.RegisterMessage(irmap_cache_entry)


_IRMAP_CACHE_ENTRY.fields_by_name['dev'].has_options = True
_IRMAP_CACHE_ENTRY.fields_by_name['dev']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002 \001\322?\002(\001'))
# @@protoc_insertion_point(module_scope)