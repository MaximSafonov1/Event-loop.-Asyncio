import asyncio
import aiosqlite
DB_NAME = 'contacts.db'


# async def read_db(db_name):
#     db = await aiosqlite.connect(db_name)
#     cursor = await db.execute('select first_name, last_name, email from contacts')
#     rows = await cursor.fetchall()
#     await cursor.close()
#     await db.close()
#     print(rows)
#     return await rows


async def create_mail(person):

    text = f'Здравствуйте {person[1]} {person[0]}!\nРады видеть вас на нашем сервисе объявлений.'
    print(text)
    return text


async def main():
    db = await aiosqlite.connect(DB_NAME)
    cursor = await db.execute('select first_name, last_name, email from contacts')
    rows = await cursor.fetchall()

    tasks = []
    for row in rows:
        task = asyncio.create_task(create_mail(row))
        tasks.append(task)
    emails = await asyncio.gather(*tasks)

    await cursor.close()
    await db.close()
    print(rows)


asyncio.run(main())
