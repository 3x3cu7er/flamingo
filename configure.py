from importlib.abc import Loader
from unittest import loader
from jinja2 import Environment,FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

temp = env.get_template('config.j2')

networks = [
    {
        "name": "cisco",
        "mode": "wireless",
        "port": "80",
        "status": "active",
        "ip": "127.0.0.1"
    }
]

print(temp.render(network=networks[0]))


