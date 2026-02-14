
'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

14/02/2026

Version - 0.4.3

mail - navtejsingh15032011@gmail.com

'''


import asyncio
import aiohttp
import time
import sys
import os
from FILES.brand import intro
import shutil
from FILES.color import *


os.system('clear')


def slowprint(s):
        for c in s + '\n' :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 100)


async def check_url(session, url, stats):

    try:
        headers = ""
        async with session.head(url, timeout=5, ssl=False, allow_redirects=True) as response:
            stats['checked'] += 1
            

            sys.stdout.write( GREEN + f'\r[*]' +RED+f"\r Progress: {stats['checked']}/{stats['total']} | Status: {response.status}")
            sys.stdout.flush()

            if response.status == 200:
                print("")
                print(GREEN + "[+]" + RED + "FOUND" + GREEN + url)
            elif response.status == 403:
                print("")
                print(GREEN + "[!]" + RED + " RESTRICTED (403): " + GREEN + url)
                
            return response.status
    except Exception:
        stats['checked'] += 1
        return None

async def main():
    

    list_path = "DATA/backdoor_list.txt"

    if not os.path.exists(list_path):
        print(f"File {list_path} not found!")
        return
    
    with open(list_path, 'r') as f:
        paths = [line.strip() for line in f if line.strip()]


    print(RED + "")
    slowprint(intro)
    slowprint(GREEN+"                                                -By Navtej-Singh-1503")
    slowprint(GREEN+"                                                -Contact : navtejsingh15032011@gmail.com")

    print(RESET + "")
    target = input(GREEN + '[*]' + RESET +'Enter Target..>>> ').strip()
    if not target.startswith('http'):
        target = f"https://{target}"
    target = target.rstrip('/')

    print(f"[*] Analyzing {target} with {len(paths)} paths...")
    print("-" * 50)
    
    stats = {'checked': 0, 'total': len(paths)}
    start_time = time.perf_counter()


    connector = aiohttp.TCPConnector(limit=200, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [check_url(session, f"{target}/{p.lstrip('/')}", stats) for p in paths]
        await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    print(f"\n" + "-" * 50)
    print(f"[!] Scan Completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(RED+"\n[!]"+RESET+" User Interrupted.")
