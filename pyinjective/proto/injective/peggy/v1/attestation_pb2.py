# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/attestation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/peggy/v1/attestation.proto',
  package='injective.peggy.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$injective/peggy/v1/attestation.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"c\n\x0b\x41ttestation\x12\x10\n\x08observed\x18\x01 \x01(\x08\x12\r\n\x05votes\x18\x02 \x03(\t\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12#\n\x05\x63laim\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"^\n\nERC20Token\x12\x10\n\x08\x63ontract\x18\x01 \x01(\t\x12>\n\x06\x61mount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00*\x9f\x02\n\tClaimType\x12.\n\x12\x43LAIM_TYPE_UNKNOWN\x10\x00\x1a\x16\x8a\x9d \x12\x43LAIM_TYPE_UNKNOWN\x12.\n\x12\x43LAIM_TYPE_DEPOSIT\x10\x01\x1a\x16\x8a\x9d \x12\x43LAIM_TYPE_DEPOSIT\x12\x30\n\x13\x43LAIM_TYPE_WITHDRAW\x10\x02\x1a\x17\x8a\x9d \x13\x43LAIM_TYPE_WITHDRAW\x12<\n\x19\x43LAIM_TYPE_ERC20_DEPLOYED\x10\x03\x1a\x1d\x8a\x9d \x19\x43LAIM_TYPE_ERC20_DEPLOYED\x12<\n\x19\x43LAIM_TYPE_VALSET_UPDATED\x10\x04\x1a\x1d\x8a\x9d \x19\x43LAIM_TYPE_VALSET_UPDATED\x1a\x04\x88\xa3\x1e\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_CLAIMTYPE = _descriptor.EnumDescriptor(
  name='ClaimType',
  full_name='injective.peggy.v1.ClaimType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLAIM_TYPE_UNKNOWN', index=0, number=0,
      serialized_options=b'\212\235 \022CLAIM_TYPE_UNKNOWN',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_TYPE_DEPOSIT', index=1, number=1,
      serialized_options=b'\212\235 \022CLAIM_TYPE_DEPOSIT',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_TYPE_WITHDRAW', index=2, number=2,
      serialized_options=b'\212\235 \023CLAIM_TYPE_WITHDRAW',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_TYPE_ERC20_DEPLOYED', index=3, number=3,
      serialized_options=b'\212\235 \031CLAIM_TYPE_ERC20_DEPLOYED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_TYPE_VALSET_UPDATED', index=4, number=4,
      serialized_options=b'\212\235 \031CLAIM_TYPE_VALSET_UPDATED',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=307,
  serialized_end=594,
)
_sym_db.RegisterEnumDescriptor(_CLAIMTYPE)

ClaimType = enum_type_wrapper.EnumTypeWrapper(_CLAIMTYPE)
CLAIM_TYPE_UNKNOWN = 0
CLAIM_TYPE_DEPOSIT = 1
CLAIM_TYPE_WITHDRAW = 2
CLAIM_TYPE_ERC20_DEPLOYED = 3
CLAIM_TYPE_VALSET_UPDATED = 4



_ATTESTATION = _descriptor.Descriptor(
  name='Attestation',
  full_name='injective.peggy.v1.Attestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='observed', full_name='injective.peggy.v1.Attestation.observed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='votes', full_name='injective.peggy.v1.Attestation.votes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='injective.peggy.v1.Attestation.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claim', full_name='injective.peggy.v1.Attestation.claim', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=109,
  serialized_end=208,
)


_ERC20TOKEN = _descriptor.Descriptor(
  name='ERC20Token',
  full_name='injective.peggy.v1.ERC20Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract', full_name='injective.peggy.v1.ERC20Token.contract', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='injective.peggy.v1.ERC20Token.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=210,
  serialized_end=304,
)

_ATTESTATION.fields_by_name['claim'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Attestation'] = _ATTESTATION
DESCRIPTOR.message_types_by_name['ERC20Token'] = _ERC20TOKEN
DESCRIPTOR.enum_types_by_name['ClaimType'] = _CLAIMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attestation = _reflection.GeneratedProtocolMessageType('Attestation', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTATION,
  '__module__' : 'injective.peggy.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.Attestation)
  })
_sym_db.RegisterMessage(Attestation)

ERC20Token = _reflection.GeneratedProtocolMessageType('ERC20Token', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TOKEN,
  '__module__' : 'injective.peggy.v1.attestation_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.ERC20Token)
  })
_sym_db.RegisterMessage(ERC20Token)


DESCRIPTOR._options = None
_CLAIMTYPE._options = None
_CLAIMTYPE.values_by_name["CLAIM_TYPE_UNKNOWN"]._options = None
_CLAIMTYPE.values_by_name["CLAIM_TYPE_DEPOSIT"]._options = None
_CLAIMTYPE.values_by_name["CLAIM_TYPE_WITHDRAW"]._options = None
_CLAIMTYPE.values_by_name["CLAIM_TYPE_ERC20_DEPLOYED"]._options = None
_CLAIMTYPE.values_by_name["CLAIM_TYPE_VALSET_UPDATED"]._options = None
_ERC20TOKEN.fields_by_name['amount']._options = None
# @@protoc_insertion_point(module_scope)
