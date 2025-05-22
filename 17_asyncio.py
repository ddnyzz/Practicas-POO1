##06/05/25
### asyncio es una librería de Python para escribir código concurrente usando la sintaxis async/await.

import asyncio

async def tarea(nombre):
    print(f"Tarea {nombre} iniciada.")
    await asyncio.sleep(2)  # Simula una tarea que toma tiempo
    print(f"Tarea {nombre} terminada.")
    
async def main():
    await asyncio.gather(
        tarea("tarea 1"),
        tarea("tarea 2"),
    )
    
asyncio.run(main())
