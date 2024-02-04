import threading
import requests
import time
import asyncio
import aiohttp

def get_data_sync(urls):
    json_array=[]
    st= time.time()
    for url in urls:
        json_array.append(requests.get(url).json())
    et=time.time()
    elapsed_time=et-st
    print("Execution time: ",elapsed_time)
    return json_array

urls=["https://postman-echo.com/delay/3"]*10


class ThreadingDownloader(threading.Thread):
    json_array=[]
    def __init__(self,url):
        super().__init__()
        self.url=url
    
    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json)
        return self.json_array


def get_data_threading(urls):
    st= time.time()
    threads=[]
    for url in urls:
        t=ThreadingDownloader(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
        print(t)
    et=time.time()
    elapsed_time=et-st
    print("Execution time: ",elapsed_time) 




async def get_data_async_but_as_wrapper(urls):
    st= time.time()
    json_array=[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())
    et=time.time()
    elapsed_time=et-st
    print("Execution time: ",elapsed_time)
    return json_array

async def get_data(json_array, session, url):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    st= time.time()
    json_array=[]

    async with aiohttp.ClientSession() as session:
        tasks=[]
        for url in urls:
            tasks.append(asyncio.create_task(get_data(json_array,session,url)))

        await asyncio.gather(*tasks)
    
    et=time.time()
    elapsed_time=et-st
    print("Execution time: ",elapsed_time)
    return json_array


#get_data_sync(urls)  40-45 sec
#get_data_threading(urls)  3-4 sec
#asyncio.run(get_data_async_but_as_wrapper(urls))  32 sec
#asyncio.run(get_data_async_concurrently(urls))   3-4 sec