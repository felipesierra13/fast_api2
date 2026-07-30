from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/categoria", tags=["Categorias"])


class CategoriaEntrada(BaseModel):
    nombre: str


categorias = [
    {"id": 1, "nombre": "Perifericos"},
    {"id": 2, "nombre": "Pantallas"},
    {"id": 3, "nombre": "Audio"},
]

@router.get("")
def listar_categorias():
    return categorias

@router.post("", status_code=201)
def crear_categoria(categoria: CategoriaEntrada):

    for c in categorias:
        if c["nombre"].lower() == categoria.nombre.lower():
            raise HTTPException(status_code=404, detail="La categoria ya existe")

    nueva = {
        "id": len(categorias) + 1,
        "nombre": categoria.nombre
    }

    categorias.append(nueva)

    return nueva

@router.put("/{categoria_id}")
def actualizar_categoria(categoria_id: int, categoria: CategoriaEntrada):

    for c in categorias:
        if c["id"] == categoria_id:
            c["nombre"] = categoria.nombre
            return c

    raise HTTPException(status_code=404, detail="Categoria no encontrada")

@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int):

    for c in categorias:
        if c["id"] == categoria_id:
            categorias.remove(c)
            return {"mensaje": "Categoria eliminada"}

    raise HTTPException(status_code=404, detail="Categoria no encontrada")