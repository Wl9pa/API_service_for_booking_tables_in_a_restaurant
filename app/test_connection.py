import asyncio
import asyncpg


async def test():
    try:
        conn = await asyncpg.connect(
            user="",
            password="",
            database="",
            host="localhost"
        )
        print("Подключение успешно!")
        await conn.close()
    except Exception as e:
        print(f"Ошибка подключения: {e}")


asyncio.run(test())
