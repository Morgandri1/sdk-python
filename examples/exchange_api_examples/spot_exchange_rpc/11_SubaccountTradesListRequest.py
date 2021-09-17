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

import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2 as spot_exchange_rpc_pb
import pyinjective.proto.exchange.injective_spot_exchange_rpc_pb2_grpc as spot_exchange_rpc_grpc

from pyinjective.constant import Network

network = Network.testnet()

async def main() -> None:
    async with grpc.aio.insecure_channel(network.grpc_exchange_endpoint) as channel:
        spot_exchange_rpc = spot_exchange_rpc_grpc.InjectiveSpotExchangeRPCStub(channel)

        mkt_id = "0xa508cb32923323679f29a032c70342c147c17d0145625922b0ef22e955c844c0"
        subacc_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"

        traderesp = await spot_exchange_rpc.SubaccountTradesList(spot_exchange_rpc_pb.SubaccountTradesListRequest(subaccount_id=subacc_id, market_id=mkt_id))
        print("\n-- Subaccount Trades Update:\n", traderesp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
