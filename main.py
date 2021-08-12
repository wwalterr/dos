import asyncio

import aiohttp

from aiohttp_socks import ProxyType, ProxyConnector

from fake_useragent import UserAgent

import argparse


URL = 'https://ident.me/'

PROXY_HOST = 'localhost'

PROXY_PORT = 9050


async def main(url, proxy_host, proxy_port):
    connector = ProxyConnector(
        proxy_type=ProxyType.SOCKS5,
        host=proxy_host,
        port=proxy_port,
        rdns=True
    )

    session = aiohttp.ClientSession(connector=connector)

    headers = {'User-Agent': UserAgent().random}

    async with session.get(url, headers=headers) as response:
        print(response.status, await response.text())

    await session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Asynchronous Denial-of-service attack through TOR.')

    parser.add_argument(
        '--url',
        default=URL,
        type=str
    )
    parser.add_argument(
        '--proxy_host',
        default=PROXY_HOST,
        type=str
    )
    parser.add_argument(
        '--proxy_port',
        default=PROXY_PORT,
        type=int
    )

    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(args.url, args.proxy_host, args.proxy_port))
