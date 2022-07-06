# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/consensus/wal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from tendermint.consensus import types_pb2 as tendermint_dot_consensus_dot_types__pb2
from tendermint.types import events_pb2 as tendermint_dot_types_dot_events__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tendermint/consensus/wal.proto',
  package='tendermint.consensus',
  syntax='proto3',
  serialized_options=b'Z;github.com/tendermint/tendermint/proto/tendermint/consensus',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1etendermint/consensus/wal.proto\x12\x14tendermint.consensus\x1a\x14gogoproto/gogo.proto\x1a tendermint/consensus/types.proto\x1a\x1dtendermint/types/events.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"X\n\x07MsgInfo\x12\x30\n\x03msg\x18\x01 \x01(\x0b\x32\x1d.tendermint.consensus.MessageB\x04\xc8\xde\x1f\x00\x12\x1b\n\x07peer_id\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06PeerID\"q\n\x0bTimeoutInfo\x12\x35\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x05\x12\x0c\n\x04step\x18\x04 \x01(\r\"\x1b\n\tEndHeight\x12\x0e\n\x06height\x18\x01 \x01(\x03\"\x81\x02\n\nWALMessage\x12G\n\x16\x65vent_data_round_state\x18\x01 \x01(\x0b\x32%.tendermint.types.EventDataRoundStateH\x00\x12\x31\n\x08msg_info\x18\x02 \x01(\x0b\x32\x1d.tendermint.consensus.MsgInfoH\x00\x12\x39\n\x0ctimeout_info\x18\x03 \x01(\x0b\x32!.tendermint.consensus.TimeoutInfoH\x00\x12\x35\n\nend_height\x18\x04 \x01(\x0b\x32\x1f.tendermint.consensus.EndHeightH\x00\x42\x05\n\x03sum\"t\n\x0fTimedWALMessage\x12\x32\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12-\n\x03msg\x18\x02 \x01(\x0b\x32 .tendermint.consensus.WALMessageB=Z;github.com/tendermint/tendermint/proto/tendermint/consensusb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,tendermint_dot_consensus_dot_types__pb2.DESCRIPTOR,tendermint_dot_types_dot_events__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_MSGINFO = _descriptor.Descriptor(
  name='MsgInfo',
  full_name='tendermint.consensus.MsgInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='tendermint.consensus.MsgInfo.msg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='tendermint.consensus.MsgInfo.peer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\006PeerID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=208,
  serialized_end=296,
)


_TIMEOUTINFO = _descriptor.Descriptor(
  name='TimeoutInfo',
  full_name='tendermint.consensus.TimeoutInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='tendermint.consensus.TimeoutInfo.duration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\230\337\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.consensus.TimeoutInfo.height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='tendermint.consensus.TimeoutInfo.round', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='step', full_name='tendermint.consensus.TimeoutInfo.step', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=298,
  serialized_end=411,
)


_ENDHEIGHT = _descriptor.Descriptor(
  name='EndHeight',
  full_name='tendermint.consensus.EndHeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='tendermint.consensus.EndHeight.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=413,
  serialized_end=440,
)


_WALMESSAGE = _descriptor.Descriptor(
  name='WALMessage',
  full_name='tendermint.consensus.WALMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_data_round_state', full_name='tendermint.consensus.WALMessage.event_data_round_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_info', full_name='tendermint.consensus.WALMessage.msg_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_info', full_name='tendermint.consensus.WALMessage.timeout_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_height', full_name='tendermint.consensus.WALMessage.end_height', index=3,
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
    _descriptor.OneofDescriptor(
      name='sum', full_name='tendermint.consensus.WALMessage.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=443,
  serialized_end=700,
)


_TIMEDWALMESSAGE = _descriptor.Descriptor(
  name='TimedWALMessage',
  full_name='tendermint.consensus.TimedWALMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tendermint.consensus.TimedWALMessage.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\220\337\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='tendermint.consensus.TimedWALMessage.msg', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=702,
  serialized_end=818,
)

_MSGINFO.fields_by_name['msg'].message_type = tendermint_dot_consensus_dot_types__pb2._MESSAGE
_TIMEOUTINFO.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_WALMESSAGE.fields_by_name['event_data_round_state'].message_type = tendermint_dot_types_dot_events__pb2._EVENTDATAROUNDSTATE
_WALMESSAGE.fields_by_name['msg_info'].message_type = _MSGINFO
_WALMESSAGE.fields_by_name['timeout_info'].message_type = _TIMEOUTINFO
_WALMESSAGE.fields_by_name['end_height'].message_type = _ENDHEIGHT
_WALMESSAGE.oneofs_by_name['sum'].fields.append(
  _WALMESSAGE.fields_by_name['event_data_round_state'])
_WALMESSAGE.fields_by_name['event_data_round_state'].containing_oneof = _WALMESSAGE.oneofs_by_name['sum']
_WALMESSAGE.oneofs_by_name['sum'].fields.append(
  _WALMESSAGE.fields_by_name['msg_info'])
_WALMESSAGE.fields_by_name['msg_info'].containing_oneof = _WALMESSAGE.oneofs_by_name['sum']
_WALMESSAGE.oneofs_by_name['sum'].fields.append(
  _WALMESSAGE.fields_by_name['timeout_info'])
_WALMESSAGE.fields_by_name['timeout_info'].containing_oneof = _WALMESSAGE.oneofs_by_name['sum']
_WALMESSAGE.oneofs_by_name['sum'].fields.append(
  _WALMESSAGE.fields_by_name['end_height'])
_WALMESSAGE.fields_by_name['end_height'].containing_oneof = _WALMESSAGE.oneofs_by_name['sum']
_TIMEDWALMESSAGE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEDWALMESSAGE.fields_by_name['msg'].message_type = _WALMESSAGE
DESCRIPTOR.message_types_by_name['MsgInfo'] = _MSGINFO
DESCRIPTOR.message_types_by_name['TimeoutInfo'] = _TIMEOUTINFO
DESCRIPTOR.message_types_by_name['EndHeight'] = _ENDHEIGHT
DESCRIPTOR.message_types_by_name['WALMessage'] = _WALMESSAGE
DESCRIPTOR.message_types_by_name['TimedWALMessage'] = _TIMEDWALMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgInfo = _reflection.GeneratedProtocolMessageType('MsgInfo', (_message.Message,), {
  'DESCRIPTOR' : _MSGINFO,
  '__module__' : 'tendermint.consensus.wal_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.consensus.MsgInfo)
  })
_sym_db.RegisterMessage(MsgInfo)

TimeoutInfo = _reflection.GeneratedProtocolMessageType('TimeoutInfo', (_message.Message,), {
  'DESCRIPTOR' : _TIMEOUTINFO,
  '__module__' : 'tendermint.consensus.wal_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.consensus.TimeoutInfo)
  })
_sym_db.RegisterMessage(TimeoutInfo)

EndHeight = _reflection.GeneratedProtocolMessageType('EndHeight', (_message.Message,), {
  'DESCRIPTOR' : _ENDHEIGHT,
  '__module__' : 'tendermint.consensus.wal_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.consensus.EndHeight)
  })
_sym_db.RegisterMessage(EndHeight)

WALMessage = _reflection.GeneratedProtocolMessageType('WALMessage', (_message.Message,), {
  'DESCRIPTOR' : _WALMESSAGE,
  '__module__' : 'tendermint.consensus.wal_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.consensus.WALMessage)
  })
_sym_db.RegisterMessage(WALMessage)

TimedWALMessage = _reflection.GeneratedProtocolMessageType('TimedWALMessage', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDWALMESSAGE,
  '__module__' : 'tendermint.consensus.wal_pb2'
  # @@protoc_insertion_point(class_scope:tendermint.consensus.TimedWALMessage)
  })
_sym_db.RegisterMessage(TimedWALMessage)


DESCRIPTOR._options = None
_MSGINFO.fields_by_name['msg']._options = None
_MSGINFO.fields_by_name['peer_id']._options = None
_TIMEOUTINFO.fields_by_name['duration']._options = None
_TIMEDWALMESSAGE.fields_by_name['time']._options = None
# @@protoc_insertion_point(module_scope)