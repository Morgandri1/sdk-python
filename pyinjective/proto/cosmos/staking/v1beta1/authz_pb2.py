# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/staking/v1beta1/authz.proto',
  package='cosmos.staking.v1beta1',
  syntax='proto3',
  serialized_options=b'Z,github.com/cosmos/cosmos-sdk/x/staking/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"cosmos/staking/v1beta1/authz.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x90\x03\n\x12StakeAuthorization\x12Z\n\nmax_tokens\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12K\n\nallow_list\x18\x02 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12J\n\tdeny_list\x18\x03 \x01(\x0b\x32\x35.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12\x45\n\x12\x61uthorization_type\x18\x04 \x01(\x0e\x32).cosmos.staking.v1beta1.AuthorizationType\x1a\x1d\n\nValidators\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t:\x11\xd2\xb4-\rAuthorizationB\x0c\n\nvalidators*\x9e\x01\n\x11\x41uthorizationType\x12\"\n\x1e\x41UTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41UTHORIZATION_TYPE_DELEGATE\x10\x01\x12!\n\x1d\x41UTHORIZATION_TYPE_UNDELEGATE\x10\x02\x12!\n\x1d\x41UTHORIZATION_TYPE_REDELEGATE\x10\x03\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])

_AUTHORIZATIONTYPE = _descriptor.EnumDescriptor(
  name='AuthorizationType',
  full_name='cosmos.staking.v1beta1.AuthorizationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_TYPE_DELEGATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_TYPE_UNDELEGATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_TYPE_REDELEGATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=547,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_AUTHORIZATIONTYPE)

AuthorizationType = enum_type_wrapper.EnumTypeWrapper(_AUTHORIZATIONTYPE)
AUTHORIZATION_TYPE_UNSPECIFIED = 0
AUTHORIZATION_TYPE_DELEGATE = 1
AUTHORIZATION_TYPE_UNDELEGATE = 2
AUTHORIZATION_TYPE_REDELEGATE = 3



_STAKEAUTHORIZATION_VALIDATORS = _descriptor.Descriptor(
  name='Validators',
  full_name='cosmos.staking.v1beta1.StakeAuthorization.Validators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.staking.v1beta1.StakeAuthorization.Validators.address', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=482,
  serialized_end=511,
)

_STAKEAUTHORIZATION = _descriptor.Descriptor(
  name='StakeAuthorization',
  full_name='cosmos.staking.v1beta1.StakeAuthorization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_tokens', full_name='cosmos.staking.v1beta1.StakeAuthorization.max_tokens', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037\'github.com/cosmos/cosmos-sdk/types.Coin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_list', full_name='cosmos.staking.v1beta1.StakeAuthorization.allow_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deny_list', full_name='cosmos.staking.v1beta1.StakeAuthorization.deny_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorization_type', full_name='cosmos.staking.v1beta1.StakeAuthorization.authorization_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STAKEAUTHORIZATION_VALIDATORS, ],
  enum_types=[
  ],
  serialized_options=b'\322\264-\rAuthorization',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='validators', full_name='cosmos.staking.v1beta1.StakeAuthorization.validators',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=144,
  serialized_end=544,
)

_STAKEAUTHORIZATION_VALIDATORS.containing_type = _STAKEAUTHORIZATION
_STAKEAUTHORIZATION.fields_by_name['max_tokens'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_STAKEAUTHORIZATION.fields_by_name['allow_list'].message_type = _STAKEAUTHORIZATION_VALIDATORS
_STAKEAUTHORIZATION.fields_by_name['deny_list'].message_type = _STAKEAUTHORIZATION_VALIDATORS
_STAKEAUTHORIZATION.fields_by_name['authorization_type'].enum_type = _AUTHORIZATIONTYPE
_STAKEAUTHORIZATION.oneofs_by_name['validators'].fields.append(
  _STAKEAUTHORIZATION.fields_by_name['allow_list'])
_STAKEAUTHORIZATION.fields_by_name['allow_list'].containing_oneof = _STAKEAUTHORIZATION.oneofs_by_name['validators']
_STAKEAUTHORIZATION.oneofs_by_name['validators'].fields.append(
  _STAKEAUTHORIZATION.fields_by_name['deny_list'])
_STAKEAUTHORIZATION.fields_by_name['deny_list'].containing_oneof = _STAKEAUTHORIZATION.oneofs_by_name['validators']
DESCRIPTOR.message_types_by_name['StakeAuthorization'] = _STAKEAUTHORIZATION
DESCRIPTOR.enum_types_by_name['AuthorizationType'] = _AUTHORIZATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StakeAuthorization = _reflection.GeneratedProtocolMessageType('StakeAuthorization', (_message.Message,), {

  'Validators' : _reflection.GeneratedProtocolMessageType('Validators', (_message.Message,), {
    'DESCRIPTOR' : _STAKEAUTHORIZATION_VALIDATORS,
    '__module__' : 'cosmos.staking.v1beta1.authz_pb2'
    # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.StakeAuthorization.Validators)
    })
  ,
  'DESCRIPTOR' : _STAKEAUTHORIZATION,
  '__module__' : 'cosmos.staking.v1beta1.authz_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.StakeAuthorization)
  })
_sym_db.RegisterMessage(StakeAuthorization)
_sym_db.RegisterMessage(StakeAuthorization.Validators)


DESCRIPTOR._options = None
_STAKEAUTHORIZATION.fields_by_name['max_tokens']._options = None
_STAKEAUTHORIZATION._options = None
# @@protoc_insertion_point(module_scope)
