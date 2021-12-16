"""
A very deep and good educational stuff to learn 'asyncio'
- https://www.youtube.com/watch?v=Xbl7XjFYsN4

"""

import asyncio

async def test(n):
    temp = 0
    while temp < n:
        print(temp)
        await asyncio.sleep(0.25)
        temp += 1

async def breaker():
    await asyncio.sleep(2)
    print("break")

async def main():
    print("Inside main")
    task1 = asyncio.create_task(breaker())
    task2 = asyncio.create_task(test(10))
    await task1
    await task2
    print("End")

asyncio.run(main())