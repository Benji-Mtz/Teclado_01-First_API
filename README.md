# Flask

A continuación se describen algunos pasos basicos para la ejecución del proyecto.

## Installation

Use el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar Flask.

```bash
python3 -m venv env

env\Scripts\activate.bat (windows)
source venv/bin/activate (linux)

(env) pip install flask

ó

(env) pip3 install -r requirements.txt

```

## Uso

```python
from flask import Flask, request

app = Flask('__name__')
```
## Corra la app con:

```sh
(env) flask run
```

## Guardar dependencias en un archivo txt

```sh
(env) pip freeze > requirements.txt
```
