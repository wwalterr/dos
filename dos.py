import asyncio

import aiohttp

from aiohttp_socks import ProxyType, ProxyConnector

from fake_useragent import UserAgent


URL = 'https://ident.me/'

PROXY_HOST = 'localhost'

PROXY_PORT = 9050


async def main():
    connector = ProxyConnector(
        proxy_type=ProxyType.SOCKS5,
        host=PROXY_HOST,
        port=PROXY_PORT,
        rdns=True
    )

    session = aiohttp.ClientSession(connector=connector)

    headers = {'User-Agent': UserAgent().random}

    async with session.get(URL, headers=headers) as response:
        print(response.status, await response.text())

    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())
