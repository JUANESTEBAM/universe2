import uuid
from config import collection 
from motor.motor_asyncio import AsyncIOMotorClient

# Función para generar un ID único
def generate_unique_id():
    return str(uuid.uuid4())

async def assign_unique_ids():
    try:
        # Obtener todos los documentos que no tienen `unique_id`
        documentos_sin_unique_id = collection.find({"unique_id": {"$exists": False}})
        
        async for doc in documentos_sin_unique_id:
            new_id = generate_unique_id()
            # Asignar un nuevo `unique_id` al documento
            result = await collection.update_one(
                {"_id": doc["_id"]},  # Usar `_id` para identificar el documento
                {"$set": {"unique_id": new_id}}
            )
            if result.modified_count:
                print(f"Asignado unique_id {new_id} a documento con _id {doc['_id']}")
            else:
                print(f"No se pudo asignar unique_id a documento con _id {doc['_id']}")

        print("Asignación de unique_ids completada.")
    except Exception as e:
        print(f"Error al asignar unique_ids: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(assign_unique_ids())