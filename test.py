from unittest import IsolatedAsyncioTestCase

from aiohttp import ClientSession

from aiohttp_socks import ProxyType, ProxyConnector

import urllib.request

from dos import URL, HEADERS, PROXY_HOST, PROXY_PORT, dos


class TestDOS(IsolatedAsyncioTestCase):
    async def test_anonymity(self):
        # Proxy
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=PROXY_HOST,
            port=PROXY_PORT,
            # DNS resolution for Socket
            rdns=True
        )

        # HTTP proxy session
        session = ClientSession(connector=connector)

        ip_proxy = None

        async with session.get(URL, headers=HEADERS) as response:
            ip_proxy = await response.text()

        await session.close()

        # HTTP session
        ip = None

        with urllib.request.urlopen(URL) as response:
            ip = response.read().decode('utf-8')

        self.assertNotEqual(ip, ip_proxy)


if __name__ == '__main__':
    unittest.main()
