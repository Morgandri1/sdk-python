# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/p2p/conn.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19tendermint/p2p/conn.proto\x12\x0etendermint.p2p\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/crypto/keys.proto\"\x0c\n\nPacketPing\"\x0c\n\nPacketPong\"R\n\tPacketMsg\x12!\n\nchannel_id\x18\x01 \x01(\x05\x42\r\xe2\xde\x1f\tChannelID\x12\x14\n\x03\x65of\x18\x02 \x01(\x08\x42\x07\xe2\xde\x1f\x03\x45OF\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xa6\x01\n\x06Packet\x12\x31\n\x0bpacket_ping\x18\x01 \x01(\x0b\x32\x1a.tendermint.p2p.PacketPingH\x00\x12\x31\n\x0bpacket_pong\x18\x02 \x01(\x0b\x32\x1a.tendermint.p2p.PacketPongH\x00\x12/\n\npacket_msg\x18\x03 \x01(\x0b\x32\x19.tendermint.p2p.PacketMsgH\x00\x42\x05\n\x03sum\"R\n\x0e\x41uthSigMessage\x12\x33\n\x07pub_key\x18\x01 \x01(\x0b\x32\x1c.tendermint.crypto.PublicKeyB\x04\xc8\xde\x1f\x00\x12\x0b\n\x03sig\x18\x02 \x01(\x0c\x42\x33Z1github.com/cometbft/cometbft/proto/tendermint/p2pb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.p2p.conn_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cometbft/cometbft/proto/tendermint/p2p'
  _PACKETMSG.fields_by_name['channel_id']._options = None
  _PACKETMSG.fields_by_name['channel_id']._serialized_options = b'\342\336\037\tChannelID'
  _PACKETMSG.fields_by_name['eof']._options = None
  _PACKETMSG.fields_by_name['eof']._serialized_options = b'\342\336\037\003EOF'
  _AUTHSIGMESSAGE.fields_by_name['pub_key']._options = None
  _AUTHSIGMESSAGE.fields_by_name['pub_key']._serialized_options = b'\310\336\037\000'
  _PACKETPING._serialized_start=97
  _PACKETPING._serialized_end=109
  _PACKETPONG._serialized_start=111
  _PACKETPONG._serialized_end=123
  _PACKETMSG._serialized_start=125
  _PACKETMSG._serialized_end=207
  _PACKET._serialized_start=210
  _PACKET._serialized_end=376
  _AUTHSIGMESSAGE._serialized_start=378
  _AUTHSIGMESSAGE._serialized_end=460
# @@protoc_insertion_point(module_scope)
