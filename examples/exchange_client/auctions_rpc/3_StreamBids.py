import asyncio
import logging

from pyinjective.async_client import AsyncClient
from pyinjective.constant import Network

async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)
    bids = await client.stream_bids()
    async for bid in bids:
        print(bid)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
