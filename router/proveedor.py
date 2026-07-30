from fastapi import APIRouter
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
def listar_proveedores():
    return proveedores


@router.post("", status_code=201)
def ingresar_proveedor(datos: ProveedorEntrada):
    id = len(proveedores) + 1

    nuevo_proveedor = {
        "id": id,
        "nombre": datos.nombre,
        "telefono": datos.telefono
    }

    proveedores.append(nuevo_proveedor)

    return {"Proveedor creado": nuevo_proveedor}