# 📄 Plain Text Extractor API

API desarrollada en Python con FastAPI que permite procesar múltiples archivos `.txt` o de texto plano comprimidos en un archivo `.zip`. Une el contenido de todos los archivos y lo devuelve en un solo campo JSON respetando los saltos de línea.

---

## 📌 ¿Qué hace esta API? / What does this API do?

**Español:**

- Recibe un archivo `.zip` que contiene múltiples archivos `.txt` o planos dentro de una **carpeta**.  
  Ejemplo: `archivo.zip → carpeta → archivos.txt` o archivos sin extensión.
- La API une el contenido de todos los archivos en una sola respuesta de texto.
- Los saltos de línea se respetan en el campo `"text"`.
- Útil para unir contenido plano de archivos masivos como logs, notas, resultados, etc.

**English:**

- Accepts a `.zip` file containing multiple `.txt` or plain text files inside a **folder**.  
  Example: `file.zip → folder → .txt files` or files without extensions.
- The API concatenates the contents of all files into a single response.
- Line breaks are preserved in the `"text"` field.
- Useful to merge large amounts of raw plain text data from logs, notes, results, etc.

---

## 🚀 ¿Cómo usarla? / How to use it?

1. Ejecuta el servidor localmente:
   ```bash
   uvicorn main:app --reload
   ```

2. Accede a la documentación interactiva de Swagger:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Prueba el endpoint `POST /procesar-zip-texto/`:
   - Sube un archivo `.zip` que contenga una **carpeta** con uno o varios archivos `.txt` o planos.  
     Ejemplo: `archivo.zip → carpeta → archivos.txt`
   - Recibirás una respuesta JSON con una sola clave:

     ```json
     {
       "text": "Contenido completo unido\ncon saltos de línea\npreservados."
     }
     ```

---

## 🔧 Requisitos / Requirements

```txt
fastapi
uvicorn
python-multipart
```

Instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## 📁 Estructura esperada del proyecto

```
txt-extractor-api/
├── main.py
├── requirements.txt
└── README.md
```

---

## 👤 Autor / Author

**Ricardo Orlando Castillo Olivera**  
Ingeniero en Sistemas / Software Engineer  
Email: `ricaror@hotmail.com`  
Versión: `1.0.0`
