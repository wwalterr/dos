# DOS

Asynchronous Denial-of-service attack through TOR.

## About

An asynchronous Denial-of-service attack through the TOR network and with fake User-Agent.

## Built with

- [Python](https://www.python.org/)
- [Async IO](https://docs.python.org/3/library/asyncio.html)
- [AIOHTTP](https://docs.aiohttp.org/en/stable/)

## Installation

Use the package manager APT to install the general dependencies.

```sh
apt install python3 python3-dev python3-pip python3-venv
```

Use the package manager APT to install the TOR dependency.

```sh
apt-get install tor
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
pip3 install -r requirements.txt
```

## Usage

Start the TOR network.

```sh
sudo service tor start
```

Change the url inside the *script.py* to the attack target.

Execute the script.

```sh
python3 main.py
```

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