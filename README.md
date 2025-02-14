Ejemplo simple de un phishing donde "fuiste hackeado, porque el correo lo envíé desde dentro".

> [!IMPORTANT]
> Esto es una **prueba de concepto** y no tiene intenciones maliciosas; de hecho, aunque las
> tuviera, el script es demasiado básico para hacer nada.

# Funcionamiento

> [!NOTE]
> Se ha usado una cuenta de pruebas en [Mailtrap](https://mailtrap.io), de forma que todos los
> datos necesarios para el fichero **.env** los proporciona la misma página.

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
    - Por ejemplo, usando [Mailtrap](https://mailtrap.io).

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

