# Copyright 2021 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Injective Exchange API client for Python. Example only."""

import asyncio
import logging
import grpc


from injective.exchange_api import injective_accounts_rpc_pb2 as accounts_rpc_pb
from injective.exchange_api import injective_accounts_rpc_pb2_grpc as accounts_rpc_grpc
from injective.exchange_api import injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
from injective.exchange_api import injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc
from injective.exchange_api import injective_exchange_rpc_pb2 as exchange_rpc_pb
from injective.exchange_api import injective_exchange_rpc_pb2_grpc as exchange_rpc_grpc
from injective.exchange_api import injective_insurance_rpc_pb2 as insurance_rpc_pb
from injective.exchange_api import injective_insurance_rpc_pb2_grpc as insurance_rpc_grpc
from injective.exchange_api import injective_oracle_rpc_pb2 as oracle_rpc_pb
from injective.exchange_api import injective_oracle_rpc_pb2_grpc as oracle_rpc_grpc
from injective.exchange_api import injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
from injective.exchange_api import injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:9910') as channel:
        exchange_rpc = exchange_rpc_grpc.InjectiveExchangeRPCStub(channel)
        spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)
        

        resp = await exchange_rpc.Version(exchange_rpc_pb.VersionRequest())
        print("-- Connected to Injective Exchange (version: %s, built %s)" % (resp.version, resp.meta_data["BuildDate"]))

        resp = await spot_exchange_rpc.Markets(spot_exchange_rpc_pb.MarketsRequest())
        print("\n-- Available markets:")
        for m in resp.markets:
            print(m.ticker, "=", m.market_id)

        selected_market = resp.markets[0]

        mkt_id = "0x17d9b5fb67666df72a5a858eb9b81104b99da760e3036a8243e05532d50e1c7c" #INJ/USDT Spot
        acct_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
        
        print("\n-- Watching for order updates on market %s" % selected_market.ticker)
        stream_req = spot_exchange_rpc_pb.StreamOrdersRequest(market_id=mkt_id) #Request
        
        orders_stream = spot_exchange_rpc.StreamOrders(stream_req)
        async for order in orders_stream:
            print("\n\033[1;34;40m API Response  \n")
            print("\033[0;37;40m\n-- Order Update:", order)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())








