# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ibc/applications/transfer/v1/authz.proto\x12\x1cibc.applications.transfer.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xaf\x01\n\nAllocation\x12\x13\n\x0bsource_port\x18\x01 \x01(\t\x12\x16\n\x0esource_channel\x18\x02 \x01(\t\x12`\n\x0bspend_limit\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x12\n\nallow_list\x18\x04 \x03(\t\"\x84\x01\n\x15TransferAuthorization\x12\x43\n\x0b\x61llocations\x18\x01 \x03(\x0b\x32(.ibc.applications.transfer.v1.AllocationB\x04\xc8\xde\x1f\x00:&\xca\xb4-\"cosmos.authz.v1beta1.AuthorizationB9Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.authz_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _ALLOCATION.fields_by_name['spend_limit']._options = None
  _ALLOCATION.fields_by_name['spend_limit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _TRANSFERAUTHORIZATION.fields_by_name['allocations']._options = None
  _TRANSFERAUTHORIZATION.fields_by_name['allocations']._serialized_options = b'\310\336\037\000'
  _TRANSFERAUTHORIZATION._options = None
  _TRANSFERAUTHORIZATION._serialized_options = b'\312\264-\"cosmos.authz.v1beta1.Authorization'
  _ALLOCATION._serialized_start=156
  _ALLOCATION._serialized_end=331
  _TRANSFERAUTHORIZATION._serialized_start=334
  _TRANSFERAUTHORIZATION._serialized_end=466
# @@protoc_insertion_point(module_scope)
