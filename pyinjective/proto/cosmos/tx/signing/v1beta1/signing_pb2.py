# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/signing/v1beta1/signing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/tx/signing/v1beta1/signing.proto',
  package='cosmos.tx.signing.v1beta1',
  syntax='proto3',
  serialized_options=b'Z-github.com/cosmos/cosmos-sdk/types/tx/signing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'cosmos/tx/signing/v1beta1/signing.proto\x12\x19\x63osmos.tx.signing.v1beta1\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x19google/protobuf/any.proto\"Z\n\x14SignatureDescriptors\x12\x42\n\nsignatures\x18\x01 \x03(\x0b\x32..cosmos.tx.signing.v1beta1.SignatureDescriptor\"\xa4\x04\n\x13SignatureDescriptor\x12(\n\npublic_key\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x41\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x1a\x8d\x03\n\x04\x44\x61ta\x12L\n\x06single\x18\x01 \x01(\x0b\x32:.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.SingleH\x00\x12J\n\x05multi\x18\x02 \x01(\x0b\x32\x39.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.MultiH\x00\x1aN\n\x06Single\x12\x31\n\x04mode\x18\x01 \x01(\x0e\x32#.cosmos.tx.signing.v1beta1.SignMode\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1a\x93\x01\n\x05Multi\x12\x41\n\x08\x62itarray\x18\x01 \x01(\x0b\x32/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12G\n\nsignatures\x18\x02 \x03(\x0b\x32\x33.cosmos.tx.signing.v1beta1.SignatureDescriptor.DataB\x05\n\x03sum*\x8b\x01\n\x08SignMode\x12\x19\n\x15SIGN_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SIGN_MODE_DIRECT\x10\x01\x12\x15\n\x11SIGN_MODE_TEXTUAL\x10\x02\x12\x1f\n\x1bSIGN_MODE_LEGACY_AMINO_JSON\x10\x7f\x12\x16\n\x11SIGN_MODE_EIP_191\x10\xbf\x01\x42/Z-github.com/cosmos/cosmos-sdk/types/tx/signingb\x06proto3'
  ,
  dependencies=[cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_SIGNMODE = _descriptor.EnumDescriptor(
  name='SignMode',
  full_name='cosmos.tx.signing.v1beta1.SignMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_DIRECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_TEXTUAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_LEGACY_AMINO_JSON', index=3, number=127,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGN_MODE_EIP_191', index=4, number=191,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=788,
  serialized_end=927,
)
_sym_db.RegisterEnumDescriptor(_SIGNMODE)

SignMode = enum_type_wrapper.EnumTypeWrapper(_SIGNMODE)
SIGN_MODE_UNSPECIFIED = 0
SIGN_MODE_DIRECT = 1
SIGN_MODE_TEXTUAL = 2
SIGN_MODE_LEGACY_AMINO_JSON = 127
SIGN_MODE_EIP_191 = 191



_SIGNATUREDESCRIPTORS = _descriptor.Descriptor(
  name='SignatureDescriptors',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signatures', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptors.signatures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=144,
  serialized_end=234,
)


_SIGNATUREDESCRIPTOR_DATA_SINGLE = _descriptor.Descriptor(
  name='Single',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=550,
  serialized_end=628,
)

_SIGNATUREDESCRIPTOR_DATA_MULTI = _descriptor.Descriptor(
  name='Multi',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bitarray', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi.bitarray', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=631,
  serialized_end=778,
)

_SIGNATUREDESCRIPTOR_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.multi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDESCRIPTOR_DATA_SINGLE, _SIGNATUREDESCRIPTOR_DATA_MULTI, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sum', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=388,
  serialized_end=785,
)

_SIGNATUREDESCRIPTOR = _descriptor.Descriptor(
  name='SignatureDescriptor',
  full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.public_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='cosmos.tx.signing.v1beta1.SignatureDescriptor.sequence', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDESCRIPTOR_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=785,
)

_SIGNATUREDESCRIPTORS.fields_by_name['signatures'].message_type = _SIGNATUREDESCRIPTOR
_SIGNATUREDESCRIPTOR_DATA_SINGLE.fields_by_name['mode'].enum_type = _SIGNMODE
_SIGNATUREDESCRIPTOR_DATA_SINGLE.containing_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA_MULTI.fields_by_name['bitarray'].message_type = cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2._COMPACTBITARRAY
_SIGNATUREDESCRIPTOR_DATA_MULTI.fields_by_name['signatures'].message_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA_MULTI.containing_type = _SIGNATUREDESCRIPTOR_DATA
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'].message_type = _SIGNATUREDESCRIPTOR_DATA_SINGLE
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'].message_type = _SIGNATUREDESCRIPTOR_DATA_MULTI
_SIGNATUREDESCRIPTOR_DATA.containing_type = _SIGNATUREDESCRIPTOR
_SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum'].fields.append(
  _SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'])
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['single'].containing_oneof = _SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum']
_SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum'].fields.append(
  _SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'])
_SIGNATUREDESCRIPTOR_DATA.fields_by_name['multi'].containing_oneof = _SIGNATUREDESCRIPTOR_DATA.oneofs_by_name['sum']
_SIGNATUREDESCRIPTOR.fields_by_name['public_key'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SIGNATUREDESCRIPTOR.fields_by_name['data'].message_type = _SIGNATUREDESCRIPTOR_DATA
DESCRIPTOR.message_types_by_name['SignatureDescriptors'] = _SIGNATUREDESCRIPTORS
DESCRIPTOR.message_types_by_name['SignatureDescriptor'] = _SIGNATUREDESCRIPTOR
DESCRIPTOR.enum_types_by_name['SignMode'] = _SIGNMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignatureDescriptors = _reflection.GeneratedProtocolMessageType('SignatureDescriptors', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATUREDESCRIPTORS,
  '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptors)
  })
_sym_db.RegisterMessage(SignatureDescriptors)

SignatureDescriptor = _reflection.GeneratedProtocolMessageType('SignatureDescriptor', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

    'Single' : _reflection.GeneratedProtocolMessageType('Single', (_message.Message,), {
      'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA_SINGLE,
      '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
      # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Single)
      })
    ,

    'Multi' : _reflection.GeneratedProtocolMessageType('Multi', (_message.Message,), {
      'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA_MULTI,
      '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
      # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.Multi)
      })
    ,
    'DESCRIPTOR' : _SIGNATUREDESCRIPTOR_DATA,
    '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor.Data)
    })
  ,
  'DESCRIPTOR' : _SIGNATUREDESCRIPTOR,
  '__module__' : 'cosmos.tx.signing.v1beta1.signing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.tx.signing.v1beta1.SignatureDescriptor)
  })
_sym_db.RegisterMessage(SignatureDescriptor)
_sym_db.RegisterMessage(SignatureDescriptor.Data)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Single)
_sym_db.RegisterMessage(SignatureDescriptor.Data.Multi)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
