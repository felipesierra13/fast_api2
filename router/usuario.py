from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


class UsuarioEntrada(BaseModel):
    nombre: str
    correo: str


usuarios = [
    {"id": 1, "nombre": "Luis", "correo": "luis@gmail.com"},
    {"id": 2, "nombre": "Carlos", "correo": "carlos@gmail.com"}
]


@router.get("")
def listar_usuarios():
    return usuarios


@router.post("", status_code=201)
def ingresar_usuario(datos: UsuarioEntrada):
    id = len(usuarios) + 1

    nuevo_usuario = {
        "id": id,
        "nombre": datos.nombre,
        "correo": datos.correo
    }

    usuarios.append(nuevo_usuario)

    return {"Usuario creado": nuevo_usuario}