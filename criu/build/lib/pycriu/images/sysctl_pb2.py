# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sysctl.proto

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
  name='sysctl.proto',
  package='',
  serialized_pb=_b('\n\x0csysctl.proto\"E\n\x0csysctl_entry\x12\x19\n\x04type\x18\x01 \x02(\x0e\x32\x0b.SysctlType\x12\x0c\n\x04iarg\x18\x02 \x01(\x05\x12\x0c\n\x04sarg\x18\x03 \x01(\t*%\n\nSysctlType\x12\x0b\n\x07\x43TL_STR\x10\x05\x12\n\n\x06\x43TL_32\x10\x06')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SYSCTLTYPE = _descriptor.EnumDescriptor(
  name='SysctlType',
  full_name='SysctlType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CTL_STR', index=0, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CTL_32', index=1, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=87,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_SYSCTLTYPE)

SysctlType = enum_type_wrapper.EnumTypeWrapper(_SYSCTLTYPE)
CTL_STR = 5
CTL_32 = 6



_SYSCTL_ENTRY = _descriptor.Descriptor(
  name='sysctl_entry',
  full_name='sysctl_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sysctl_entry.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iarg', full_name='sysctl_entry.iarg', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sarg', full_name='sysctl_entry.sarg', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=16,
  serialized_end=85,
)

_SYSCTL_ENTRY.fields_by_name['type'].enum_type = _SYSCTLTYPE
DESCRIPTOR.message_types_by_name['sysctl_entry'] = _SYSCTL_ENTRY
DESCRIPTOR.enum_types_by_name['SysctlType'] = _SYSCTLTYPE

sysctl_entry = _reflection.GeneratedProtocolMessageType('sysctl_entry', (_message.Message,), dict(
  DESCRIPTOR = _SYSCTL_ENTRY,
  __module__ = 'sysctl_pb2'
  # @@protoc_insertion_point(class_scope:sysctl_entry)
  ))
_sym_db.RegisterMessage(sysctl_entry)


# @@protoc_insertion_point(module_scope)