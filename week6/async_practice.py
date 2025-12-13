import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='async_log.txt', filemode='a')

async def fetch(session, url):
        try:
            async with session.get(url) as response:
                logging.info(f"GET {url} - Status Code: {response.status}")
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    logging.warning(f"GET {url} - Status Code: {response.status}")
        except Exception as e:
            logging.error(e)

async def main():
    urls= [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments"
    ]
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*(fetch(session, url) for url in urls))
        for url, data in zip(urls, result):
            if data is not None:
                logging.info(f"Fetched {len(data)} items from {url}")

asyncio.run(main())





        # if users:
        #     logging.info(f"Fetched {len(users)} users")
        # if posts:
        #     logging.info(f"Fetched {len(posts)} posts")
        # if comments:
        #     logging.info(f"Fetched {len(comments)} comments")