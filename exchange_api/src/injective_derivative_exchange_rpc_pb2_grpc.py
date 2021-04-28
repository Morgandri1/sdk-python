# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import injective_derivative_exchange_rpc_pb2 as injective__derivative__exchange__rpc__pb2


class InjectiveDerivativeExchangeRPCStub(object):
    """InjectiveDerivativeExchangeRPC defines gRPC API of Derivative Markets
    provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Markets = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Markets',
                request_serializer=injective__derivative__exchange__rpc__pb2.MarketsRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.MarketsResponse.FromString,
                )
        self.Market = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Market',
                request_serializer=injective__derivative__exchange__rpc__pb2.MarketRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.MarketResponse.FromString,
                )
        self.StreamMarket = channel.unary_stream(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamMarket',
                request_serializer=injective__derivative__exchange__rpc__pb2.StreamMarketRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.StreamMarketResponse.FromString,
                )
        self.Orderbook = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Orderbook',
                request_serializer=injective__derivative__exchange__rpc__pb2.OrderbookRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.OrderbookResponse.FromString,
                )
        self.StreamOrderbook = channel.unary_stream(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamOrderbook',
                request_serializer=injective__derivative__exchange__rpc__pb2.StreamOrderbookRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.StreamOrderbookResponse.FromString,
                )
        self.Orders = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Orders',
                request_serializer=injective__derivative__exchange__rpc__pb2.OrdersRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.OrdersResponse.FromString,
                )
        self.Positions = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Positions',
                request_serializer=injective__derivative__exchange__rpc__pb2.PositionsRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.PositionsResponse.FromString,
                )
        self.StreamOrders = channel.unary_stream(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamOrders',
                request_serializer=injective__derivative__exchange__rpc__pb2.StreamOrdersRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.StreamOrdersResponse.FromString,
                )
        self.Trades = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Trades',
                request_serializer=injective__derivative__exchange__rpc__pb2.TradesRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.TradesResponse.FromString,
                )
        self.StreamTrades = channel.unary_stream(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamTrades',
                request_serializer=injective__derivative__exchange__rpc__pb2.StreamTradesRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.StreamTradesResponse.FromString,
                )
        self.SubaccountOrdersList = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/SubaccountOrdersList',
                request_serializer=injective__derivative__exchange__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.SubaccountOrdersListResponse.FromString,
                )
        self.SubaccountTradesList = channel.unary_unary(
                '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/SubaccountTradesList',
                request_serializer=injective__derivative__exchange__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
                response_deserializer=injective__derivative__exchange__rpc__pb2.SubaccountTradesListResponse.FromString,
                )


class InjectiveDerivativeExchangeRPCServicer(object):
    """InjectiveDerivativeExchangeRPC defines gRPC API of Derivative Markets
    provider.
    """

    def Markets(self, request, context):
        """Markets gets a list of Derivative Markets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Market(self, request, context):
        """Market gets details of a single derivative market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMarket(self, request, context):
        """StreamMarket streams live updates of selected derivative markets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Orderbook(self, request, context):
        """Orderbook gets the Orderbook of a Derivative Market
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamOrderbook(self, request, context):
        """StreamOrderbook streams live updates of selected derivative market orderbook.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Orders(self, request, context):
        """DerivativeLimitOrders gets the limit orders of a Derivative Market.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Positions(self, request, context):
        """Positions gets the positions for a trader.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamOrders(self, request, context):
        """StreamOrders streams updates to individual orders of a Derivative Market.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Trades(self, request, context):
        """Trades gets the trades of a Derivative Market.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamTrades(self, request, context):
        """StreamTrades streams newly executed trades from Derivative Market.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountOrdersList(self, request, context):
        """SubaccountOrdersList lists orders posted from this subaccount.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubaccountTradesList(self, request, context):
        """SubaccountTradesList gets a list of derivatives trades executed by this
        subaccount.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveDerivativeExchangeRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Markets': grpc.unary_unary_rpc_method_handler(
                    servicer.Markets,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.MarketsRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.MarketsResponse.SerializeToString,
            ),
            'Market': grpc.unary_unary_rpc_method_handler(
                    servicer.Market,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.MarketRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.MarketResponse.SerializeToString,
            ),
            'StreamMarket': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMarket,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.StreamMarketRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.StreamMarketResponse.SerializeToString,
            ),
            'Orderbook': grpc.unary_unary_rpc_method_handler(
                    servicer.Orderbook,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.OrderbookRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.OrderbookResponse.SerializeToString,
            ),
            'StreamOrderbook': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamOrderbook,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.StreamOrderbookRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.StreamOrderbookResponse.SerializeToString,
            ),
            'Orders': grpc.unary_unary_rpc_method_handler(
                    servicer.Orders,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.OrdersRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.OrdersResponse.SerializeToString,
            ),
            'Positions': grpc.unary_unary_rpc_method_handler(
                    servicer.Positions,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.PositionsRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.PositionsResponse.SerializeToString,
            ),
            'StreamOrders': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamOrders,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.StreamOrdersRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.StreamOrdersResponse.SerializeToString,
            ),
            'Trades': grpc.unary_unary_rpc_method_handler(
                    servicer.Trades,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.TradesRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.TradesResponse.SerializeToString,
            ),
            'StreamTrades': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamTrades,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.StreamTradesRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.StreamTradesResponse.SerializeToString,
            ),
            'SubaccountOrdersList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountOrdersList,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.SubaccountOrdersListRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.SubaccountOrdersListResponse.SerializeToString,
            ),
            'SubaccountTradesList': grpc.unary_unary_rpc_method_handler(
                    servicer.SubaccountTradesList,
                    request_deserializer=injective__derivative__exchange__rpc__pb2.SubaccountTradesListRequest.FromString,
                    response_serializer=injective__derivative__exchange__rpc__pb2.SubaccountTradesListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveDerivativeExchangeRPC(object):
    """InjectiveDerivativeExchangeRPC defines gRPC API of Derivative Markets
    provider.
    """

    @staticmethod
    def Markets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Markets',
            injective__derivative__exchange__rpc__pb2.MarketsRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.MarketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Market(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Market',
            injective__derivative__exchange__rpc__pb2.MarketRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.MarketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMarket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamMarket',
            injective__derivative__exchange__rpc__pb2.StreamMarketRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.StreamMarketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Orderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Orderbook',
            injective__derivative__exchange__rpc__pb2.OrderbookRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.OrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamOrderbook',
            injective__derivative__exchange__rpc__pb2.StreamOrderbookRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.StreamOrderbookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Orders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Orders',
            injective__derivative__exchange__rpc__pb2.OrdersRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.OrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Positions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Positions',
            injective__derivative__exchange__rpc__pb2.PositionsRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.PositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamOrders',
            injective__derivative__exchange__rpc__pb2.StreamOrdersRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.StreamOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Trades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/Trades',
            injective__derivative__exchange__rpc__pb2.TradesRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.TradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/StreamTrades',
            injective__derivative__exchange__rpc__pb2.StreamTradesRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.StreamTradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountOrdersList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/SubaccountOrdersList',
            injective__derivative__exchange__rpc__pb2.SubaccountOrdersListRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.SubaccountOrdersListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubaccountTradesList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_derivative_exchange_rpc.InjectiveDerivativeExchangeRPC/SubaccountTradesList',
            injective__derivative__exchange__rpc__pb2.SubaccountTradesListRequest.SerializeToString,
            injective__derivative__exchange__rpc__pb2.SubaccountTradesListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
