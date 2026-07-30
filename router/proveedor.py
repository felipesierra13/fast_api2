from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])


class ProveedorEntrada(BaseModel):
    nombre: str
    telefono: str


proveedores = [
    {"id": 1, "nombre": "Tech Colombia", "telefono": "3001234567"},
    {"id": 2, "nombre": "CompuStore", "telefono": "3017654321"}
]


@router.get("")
def ListarProveedores():
    return proveedores


@router.post("", status_code=201)
def IngresarProveedores(datos: ProveedorEntrada):
    id = len(proveedores) + 1

    nuevoProveedor = {
        "id": id,
        "nombre": datos.nombre,
        "telefono": datos.telefono
    }

    proveedores.append(nuevoProveedor)

    return {"Proveedor Creado": nuevoProveedor}


@router.put("/{id_proveedor}")
def ActualizarProveedores(id_proveedor: int, datos: ProveedorEntrada):
    for proveedor in proveedores:
        if proveedor["id"] == id_proveedor:
            proveedor["nombre"] = datos.nombre
            proveedor["telefono"] = datos.telefono

            return {"Proveedor actualizado": proveedor}

    raise HTTPException(
        status_code=404,
        detail="Proveedor no encontrado"
    )


@router.delete("/{id_proveedor}")
def EliminarProveedores(id_proveedor: int):
    for proveedor in proveedores:
        if proveedor["id"] == id_proveedor:
            proveedores.remove(proveedor)

            return {"Proveedor eliminado": proveedor}

    raise HTTPException(
        status_code=404,
        detail="Proveedor no encontrado"
    )