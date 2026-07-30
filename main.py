from fastapi import FastAPI
from router import producto
from router import categoria


app = FastAPI(
    title="API de la Tienda",
    description="CRUD de productos y categorias organizado en varios archivos",
    version="2.0.0"
)

app.include_router(producto.router)
app.include_router(categoria.router)



@app.get("/", tags=["Inicio"])
def inicio():
    return {"Mensaje": "Api Tienda"}