from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from config import collection  
from bson import ObjectId
import uuid
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
=======
from fastapi import FastAPI, HTTPException,Query
from typing import List,Optional
from config import collection  
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto al puerto de tu frontend
>>>>>>> d024079 (Displaying user data on the frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Modelo de datos para Pydantic
class User(BaseModel):
    first_name: str
    phone: str
    plasticidad: str
    permeabilidad: str
    densidad: str
    porosidad: str
    oleosidad: str
    hebra: str
    textura: str

    
def generate_unique_id():
    return str(uuid.uuid4())


=======
>>>>>>> d024079 (Displaying user data on the frontend)
@app.get("/clientes/", response_model=List[dict])
async def obtener_clientes():
    try:
        clientes = collection.find()
        lista_clientes = []

        async for cliente in clientes:
            cliente['_id'] = str(cliente['_id'])  # Convertir ObjectId a str
            lista_clientes.append(cliente)

        if not lista_clientes:
            raise HTTPException(status_code=404, detail="No se encontraron clientes en la base de datos")

        return lista_clientes

    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.post("/clientes/")
# async def crear_o_actualizar_usuario(user: User):
#     existing_user = await collection.find_one({"id":usuario.id})
#     if existing_user:
#         # Si el usuario existe, actualiza sus datos
#         await collection.update_one({"id": usuario.id}, {"$set": usuario.dict()})
#         return {"message": "Usuario actualizado", "data": usuario}
#     else:
#         # Si no existe, crea un nuevo usuario
#         await collection.insert_one(usuario.dict())
#         return {"message": "Usuario creado", "data":usuario}
    
    
@app.post("/clientes/", response_model=dict)
async def crear_o_actualizar_usuario(user: User):
    try:
        # Buscar si el usuario ya existe por el campo 'phone'
        existing_user = collection.find_one({"phone": user.phone})

        if existing_user:
            # Actualizar los datos del usuario existente
            updated_data = {k: v for k, v in user.dict().items() if v is not None}
            collection.update_one({"phone": user.phone}, {"$set": updated_data})
            return {"message": "Usuario actualizado exitosamente"}
        else:
            # Crear un nuevo usuario si no existe
            user_data = user.dict()
            user_data["unique_id"] = generate_unique_id()  # Generar unique_id
            collection.insert_one(user_data)
            return {"message": "Usuario creado exitosamente"}

    except Exception as e:
        print(f"Error al crear o actualizar usuario: {e}")
        raise HTTPException(status_code=500, detail=str(e))    


# Actualizar un usuario existente
@app.put("/clientes/{unique_id}", response_model=dict)
async def actualizar_usuario(unique_id: str, user: User):
    try:
        updated_data = {k: v for k, v in user.dict().items() if v is not None}
        result = await collection.update_one({"unique_id": unique_id}, {"$set": updated_data})

        if result.modified_count > 0:
            return {"message": "Usuario actualizado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="No se encontró el usuario o no hubo cambios")

    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Eliminar un usuario por ID
@app.delete("/clientes/{unique_id}", response_model=dict)
async def eliminar_usuario(unique_id: str):
    try:
        result = await collection.delete_one({"unique_id": unique_id})

        if result.deleted_count:
            return {"message": "Usuario eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="No se encontró el usuario")

    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/clientes/count", response_model=dict)
async def contar_clientes():
    try:
        total_clientes = await collection.count_documents({})
        return {"total_clientes": total_clientes}
    except Exception as e:
        print(f"Error al contar clientes: {e}")
        raise HTTPException(status_code=500, detail=str(e))
