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


