# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reservation.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11reservation.proto\x12\x0breservation\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"@\n\x12ReservationRequest\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x13\n\x0bseat_number\x18\x02 \x01(\x05\"7\n\x13ReservationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x11\n\x0fSeatListRequest\"1\n\nSeatStatus\x12\x13\n\x0bseat_number\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t2\xc0\x02\n\x12ReservationService\x12;\n\x04Ping\x12\x18.reservation.PingRequest\x1a\x19.reservation.PingResponse\x12P\n\x0bReserveSeat\x12\x1f.reservation.ReservationRequest\x1a .reservation.ReservationResponse\x12H\n\rGetSeatStatus\x12\x1c.reservation.SeatListRequest\x1a\x17.reservation.SeatStatus0\x01\x12Q\n\x0cUpdateStatus\x12\x1f.reservation.ReservationRequest\x1a .reservation.ReservationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reservation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PINGREQUEST']._serialized_start=34
  _globals['_PINGREQUEST']._serialized_end=47
  _globals['_PINGRESPONSE']._serialized_start=49
  _globals['_PINGRESPONSE']._serialized_end=63
  _globals['_RESERVATIONREQUEST']._serialized_start=65
  _globals['_RESERVATIONREQUEST']._serialized_end=129
  _globals['_RESERVATIONRESPONSE']._serialized_start=131
  _globals['_RESERVATIONRESPONSE']._serialized_end=186
  _globals['_SEATLISTREQUEST']._serialized_start=188
  _globals['_SEATLISTREQUEST']._serialized_end=205
  _globals['_SEATSTATUS']._serialized_start=207
  _globals['_SEATSTATUS']._serialized_end=256
  _globals['_RESERVATIONSERVICE']._serialized_start=259
  _globals['_RESERVATIONSERVICE']._serialized_end=579
# @@protoc_insertion_point(module_scope)
