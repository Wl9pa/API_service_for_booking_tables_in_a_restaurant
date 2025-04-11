import asyncio
from app.backend.base import async_session_maker
from app.models.table import Table


async def create_test_data():
    async with async_session_maker() as session:
        session.add_all([
            Table(name="Стол у окна", seats=4, location="Зал"),
            Table(name="VIP-ложа", seats=6, location="Терраса")
        ])
        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_test_data())
