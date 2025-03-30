from typing import List 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# Carregar les dades dels alumnes des del fitxer alumnes.json
def carregar_dades():
    if os.path.exists("alumnes.json"):
        with open("alumnes.json", "r") as f:
            return json.load(f)
    # Si no existeix el fitxer, retornem una llista buida
    return []

# Desar les dades al fitxer alumnes.json
def desar_dades(alumnes):
    with open("alumnes.json", "w") as f:
        json.dump(alumnes, f, indent=4)

# Definim el model de dades per un alumne
class Alumne(BaseModel):
    id: int          
    nom: str         
    cognom: str      
    data: dict      
    email: str       
    feina: bool     
    curs: str        

# Creem l'app FastAPI
app = FastAPI()

# Carregar les dades dels alumnes al començar l'aplicació
alumnes = carregar_dades()

# Ruta per llegir un missatge de benvinguda
@app.get("/")
def llegir_institut():
    return {"message": "Institut TIC de Barcelona"}

# Ruta per obtenir el nombre total d'alumnes
@app.get("/alumnes/")
def contar_alumnes():
    return {"total_alumnes": len(alumnes)}

# Ruta per veure les dades d'un alumne específic mitjançant el seu ID
@app.get("/id/{alumne_id}")
def veure_alumne(alumne_id: int):
    alumne_trobat = next((a for a in alumnes if a["id"] == alumne_id), None)
    if alumne_trobat is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne_trobat

# Ruta per esborrar un alumne basant-se en el seu ID
@app.delete("/del/{alumne_id}")
def esborrar_alumne(alumne_id: int):
    global alumnes
    alumnes = [a for a in alumnes if a["id"] != alumne_id]
    desar_dades(alumnes)
    return {"message": f"Alumne amb id {alumne_id} eliminat"}

# Ruta per afegir un nou alumne
@app.post("/alumne/")
def afegir_alumne(alumne: Alumne):
    alumnes.append(alumne.dict())
    desar_dades(alumnes)
    return {"message": "Alumne afegit correctament", "alumne": alumne}
