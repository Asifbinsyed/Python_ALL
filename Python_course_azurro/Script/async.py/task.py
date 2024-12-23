import asyncio 


async def fetch_data(data: int) -> dict: 
    print("fetching data")
    await asyncio.sleep(10)
    return {'data': data}

# Create a task to execute 

async def main(): 
    task = asyncio.create_task(fetch_data(100))
    await asyncio.sleep(1)
    
    #task.cancel() 
    try: 
        await asyncio.wait_for(task, timeout=5)
        if task.done(): 
        #data: dict = await task 
            data: dict = task.result()
        else: 
            print("data wasn't ready")
        print(data)
    except asyncio.CancelledError: 
        print('Task was cancelled')
    
    # print("Doing another thing ")
    # data: dict = await task 
    # print(data)
    
asyncio.run(main())

