import asyncio
import time
import random

start = time.time()


def take_time():
    return "%1.2f秒" % (time.time() - start)


async def long_time_task(task):
    print(f"执行耗时任务:{task}")
    await asyncio.sleep(1)
    print(f"任务结束:{task}")


async def task_A():
    print("运行task_A")
    # await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    await long_time_task('A')
    print(f"task_A结束!!耗时{take_time()}")


async def task_B():
    print("运行task_B")
    await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    print(f"task_B结束!!耗时{take_time()}")


async def task_C():
    print("运行task_C")
    await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    print(f"task_C结束!!耗时{take_time()}")


async def task_exect():
    tasks = [task_A(), task_B(), task_C()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(task_exect())
