# DOS

Asynchronous Denial-of-service attack through TOR.

## About

An asynchronous Denial-of-service attack through the TOR network.

## Built with

- [Python](https://www.python.org/)
- [Threading](https://docs.python.org/3/library/threading.html)
- [Async IO](https://docs.python.org/3/library/asyncio.html)
- [AIO HTTP](https://docs.aiohttp.org/en/stable/)
- [TOR](https://www.torproject.org/)

## Installation

Use the package manager APT to install the general dependencies.

```sh
apt install python3 python3-dev python3-pip python3-venv
```

Use the package manager APT to install the TOR dependency.

```sh
apt-get install tor
```

Use any text editor to uncomment the two lines where `ControlPort 9051` and `CookieAuthentication 1` appear, to enable new TOR identity via script.

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

Change the url inside the _script.py_ to the attack target.

Execute the script.

```sh
sudo -u debian-tor python3 main.py
```

## Documentation

The available CLI arguments are.

- --url The attack target (default `ident.me`)

- --proxy_host The proxy host (optional, default `localhost`)

- --proxy_port The proxy port, available on proxy host (optional, default `9050`)

- --workers Number of threads, one event loop will be executed in each thread (optional, default `8`) - [check](https://unix.stackexchange.com/a/351743) the amount of cores you have

For Cloud Flare targets. Please check [aiocfscrape](https://github.com/pavlodvornikov/aiocfscrape).

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
