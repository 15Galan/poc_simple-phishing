Ejemplo simple de un phishing donde "la cuenta ha sido comprometida porque el correo se envía desde dentro".

# Funcionamiento

1. Crear un entorno virtual de Python (`.venv`) y aislar el proyecto.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar las dependencias necesarias del proyecto usando `requirements.txt`.

```bash
pip install -r requirements.txt
```

3. Personalizar el fichero `.env_template` y renombrarlo a `.env`.

```bash
mv .env_template .env
```

4. Ejecutar `phishing.py`, 2 opciones:
    - Usando `python3`.
    - Como ejecutable `./python.py` (requiere permisos de ejecución).
    
```bash
# Usando 'python3'
python3 phishing.py

# Haciéndolo ejecutable
sudo chmod +x phishing.py
./phishing.py
```

