# DOS

Asynchronous and distributed DOS attack through TOR.

## About

An asynchronous and distributed denial-of-service attack through the TOR network.

## Built with

- [Python](https://www.python.org/)
- [Threading](https://docs.python.org/3/library/threading.html)
- [Async IO](https://docs.python.org/3/library/asyncio.html)
- [AIO HTTP](https://docs.aiohttp.org/en/stable/)
- [Ray](https://www.ray.io/)
- [TOR](https://www.torproject.org/)

## Installation

Use the package manager APT to install the general dependencies.

```sh
apt install python3 python3-dev python3-pip python3-venv
```

Use the package manager APT to install the TOR dependency.

```sh
apt-get install tor=0.4.2.7-1
```

Use any text editor to uncomment the two lines where `ControlPort 9051` and `CookieAuthentication 1` appear to enable new TOR identity via script.

```sh
sudo xed /etc/tor/torrc
```

Use the Python 3 CLI to create a virtual environment.

```sh
python3 -m venv venv
```

Activate the virtual estartnvironment.

```sh
source ./venv/bin/activate
```

Use the package manager [Pip](https://pypi.org/project/pip/) to install the dependencies.

```sh
sudo pip3 install -r requirements.txt
```

## Usage

Start the TOR network.

```sh
sudo service tor start
```

Execute the script.

```sh
sudo -u debian-tor python3 main.py
```

## Test

Test if the TOR is working.

```sh
python3 -m unittest
```

## Documentation

### Parameters

The available CLI arguments are.

- --url The attack target (default `ident.me`)

- --proxy_host The proxy host (optional, default `localhost`)

- --proxy_port The proxy port, available on proxy host (optional, default `9050`)

- --workers Number of threads, one event loop will be executed in each thread (optional, default `8`)

For Cloud Flare targets check [AIO Scrape](https://github.com/pavlodvornikov/aiocfscrape) or [CloudScraper](https://github.com/VeNoMouS/cloudscraper).

### Distributed

Start a [Ray](https://docs.ray.io/en/latest/ray-overview/installation.html) server in N machines.

```sh
ray start --head --redis-password="att@ck&r"
```

> Use the same Python 3 version and Ray version across all machines

Set the URL, proxy host, proxy port and number of requests inside *distributed.py*, aside from Redis password that needs to mach the Ray servers.

Execute the script.

```sh
python3 distributed.py
```

For more configurations check [configure](https://docs.ray.io/en/latest/configure.html) and for cloud check [clusters](https://docs.ray.io/en/master/cluster/cloud.html#cluster-cloud).

## Contributing

Pull requests are welcome. Please, consider the following.

1. Make sure you code have quality, a.k.a standards
2. Make sure your code is secure
3. Make sure your code has no performance issues
4. Make sure your code is documented, if necessary
5. Describe the changes that were done

> No issue or PR template required, but be informative

## License

[MIT](./LICENSE.md)
