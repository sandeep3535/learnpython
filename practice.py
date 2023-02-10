"""
import pyotp
totp = pyotp.TOTP(s="BVYCKZ3BRCX5KNGVMOOR56DAUM").now()
print(totp)

"""

"""
import requests
client_ip = requests.get('https://api.ipify.org').text
print(client_ip)
"""

"""
import socket
hostname = socket.gethostname()
clientLocalIp = socket.gethostbyname(hostname)
print(clientLocalIp)
"""

"""
import re
import uuid
clientMacAddress = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
print(clientMacAddress)
"""

"""
import asyncio
import datetime


async def print_no(a):
    n = 0
    for i in range(a):
        n = n + 1
        await asyncio.sleep(2)
        print(datetime.datetime.now(), '|', n)


async def print_no_2(b):
    for i in range(b):
        await asyncio.sleep(1)
        print(datetime.datetime.now(), '|', "*")


async def main():
    task1 = print_no(100)
    task2 = print_no_2(100)
    await asyncio.gather(task1, task2)
"""

"""
import asyncio


async def generate_value(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i


async def iterate_value():
    async for value in generate_value(50):
        print(value)


async def main():
    await iterate_value()

asyncio.run(main())
"""

"""
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(filename)s : %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

"""
class Test:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        if Test.__instance is None:
            Test.__instance = self
        else:
            raise Exception("You can not Create Multiple Instance of Angel Instrument Class")


n_obj = Test()
l_obj = Test()


print(n_obj.__str__())
print(l_obj.__str__())
"""

"""
import asyncio

async def put_nowait_queue(word):
    q = asyncio.Queue(maxsize=2)
    q.put_nowait(word)
    q.put_nowait(word)
    que = q.get_nowait()
    print(que)

async def put_queue(word):
    q = asyncio.Queue(maxsize=2)
    await q.put(word)
    await q.put(word)
    await q.put(word)
    print(q)

async def main():
    await put_nowait_queue("sandeep")


asyncio.run(main())
"""


