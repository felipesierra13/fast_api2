from fastapi import APIRouter, HTTPException
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
def ListarUsuarios():
    return usuarios


@router.post("", status_code=201)
def IngresarUsuario(datos: UsuarioEntrada):
    id = len(usuarios) + 1

    nuevoUsuario = {
        "id": id,
        "nombre": datos.nombre,
        "correo": datos.correo
    }

    usuarios.append(nuevoUsuario)

    return {"Usuario creado": nuevoUsuario}


@router.put("/{id_usuario}")
def ActualizarUsuario(id_usuario: int, datos: UsuarioEntrada):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["nombre"] = datos.nombre
            usuario["correo"] = datos.correo

            return {"Usuario actualizado": usuario}

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@router.delete("/{id_usuario}")
def EliminarUsuario(id_usuario: int):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuarios.remove(usuario)

            return {"Usuario eliminado": usuario}

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )