import asyncio

async def fetch_data(source, delay):
    print(f"Fetching data from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def main():
    sources = [("API", 2), ("Database", 1), ("Cache", 0.5)]
    tasks = [fetch_data(source, delay) for source, delay in sources]
    
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

asyncio.run(main())