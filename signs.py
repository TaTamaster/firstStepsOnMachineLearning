from fastapi import FastAPI, File, UploadFile, HTTPException
import cv2
import numpy as np
import uvicorn

app = FastAPI()

def compare_signatures_bytes(image1_bytes, image2_bytes):
    # Convertir los bytes a matrices NumPy
    nparr1 = np.frombuffer(image1_bytes, np.uint8)
    nparr2 = np.frombuffer(image2_bytes, np.uint8)

    # Decodificar las matrices en imágenes
    img1 = cv2.imdecode(nparr1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imdecode(nparr2, cv2.IMREAD_GRAYSCALE)

    # Verificar si las imágenes se cargaron correctamente
    if img1 is None or img2 is None:
        return 0.0  # Retorna 0 si las imágenes no son válidas

    # Redimensionar las imágenes a un tamaño estándar
    img1 = cv2.resize(img1, (500, 200))
    img2 = cv2.resize(img2, (500, 200))

    # Aplicar umbral para binarizar las imágenes
    _, img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
    _, img2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY_INV)

    # Inicializar el detector ORB
    orb = cv2.ORB_create()

    # Encontrar puntos clave y descriptores
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Verificar si se encontraron descriptores
    if des1 is None or des2 is None:
        return 0.0  # No se encontraron características para comparar

    # Inicializar BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Emparejar descriptores
    matches = bf.match(des1, des2)

    # Ordenar los emparejamientos basados en la distancia
    matches = sorted(matches, key=lambda x: x.distance)

    # Calcular el puntaje de similitud
    total_matches = len(matches)
    good_matches = [m for m in matches if m.distance < 50]
    good_matches_count = len(good_matches)

    # Evitar división por cero
    if total_matches == 0:
        return 0.0

    # La similitud es la proporción de buenos emparejamientos
    similarity = good_matches_count / total_matches

    # Asegurar que la similitud esté entre 0 y 1
    similarity = max(0.0, min(1.0, similarity))

    return similarity

@app.post("/comparar_firmas/")
async def comparar_firmas(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    try:
        image1_bytes = await file1.read()
        image2_bytes = await file2.read()

        similarity_score = compare_signatures_bytes(image1_bytes, image2_bytes)

        return {"similaridad": similarity_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
