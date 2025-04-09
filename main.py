from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import zipfile
import io

app = FastAPI(
    title="Plain Text Extractor API",
    description="API que descomprime un archivo ZIP y une el contenido de todos los archivos .txt o de texto plano.",
    version="1.0.0",
    contact={
        "name": "Ricardo Orlando Castillo Olivera",
        "email": "ricaror@hotmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/procesar-zip-texto/", summary="Procesar ZIP de archivos .txt", tags=["Text Extractor"])
async def procesar_zip_texto(file: UploadFile = File(...)):
    """
    Procesa un archivo ZIP que contiene archivos .txt o planos y devuelve el contenido unido como texto.
    """
    if not file.filename.endswith(".zip"):
        return JSONResponse(status_code=400, content={"error": "El archivo debe ser un .zip"})

    content = await file.read()
    texto_total = ""

    with zipfile.ZipFile(io.BytesIO(content), "r") as zip_ref:
        for file_info in zip_ref.infolist():
            nombre = file_info.filename.lower()
            if not file_info.is_dir() and (nombre.endswith(".txt") or '.' not in nombre):
                with zip_ref.open(file_info) as f:
                    try:
                        contenido = f.read().decode("utf-8", errors="ignore")
                        texto_total += contenido + "\n"
                    except Exception as e:
                        texto_total += f"\n[ERROR AL LEER {file_info.filename}: {str(e)}]\n"

    return JSONResponse(content={"text": texto_total.strip()})
