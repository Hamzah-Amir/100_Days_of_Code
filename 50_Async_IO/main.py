import asyncio
import requests


async def func1():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(r.content)
async def func2():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
async def func3():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google3.ico', 'wb').write(r.content)

async def main():
   l = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
   print(l)
asyncio.run(main())