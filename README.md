# Install

# Develop
Crear un entorno virtual en python3.

```
PATH_PYTHON3=$(which python3)
virtualenv -p $PATH_PYTHON3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Ejecutar prueba.
```
python3 src/main.py
```
