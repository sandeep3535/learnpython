import time
import asyncio
import aiohttp

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
LIST_ISBN = [
    '9780002005883',
    '9780002238304',
    '9780002261982',
    '9780006163831',
    '9780006178736',
    '9780006280897',
    '9780006280934',
    '9780006353287',
    '9780006380832',
    '9780006470229',
]

# start = time.time()
# Books = []
# for isbn in LIST_ISBN:
#     response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
#     Books.append(response.json())
# end = time.time()
start = time.time()

async def book_list(isbn):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}", ssl=False)
        r_json = await response.json()
        return r_json


async def main():
    task = await asyncio.gather(*[book_list(isbn) for isbn in LIST_ISBN])
    print(task)


asyncio.run(main())
end = time.time()

print(end - start)
