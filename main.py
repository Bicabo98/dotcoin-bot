import httpx
import asyncio
import json
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init
import time
import datetime

init()
load_dotenv()

class Color:
    green = Fore.GREEN
    yellow = Fore.YELLOW
    reset = Style.RESET_ALL

# coroutine to get token
async def getToken(session, query):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/functions/v1/getToken"

    payload = json.dumps({
        "initData": f"{query}"
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getToken, HTTP error, try again... {e}")
            continue

# coroutine to get user info
async def getUserInfo(session, token):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_user_info"

    payload = json.dumps({})

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2',
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getUserInfo, HTTP error, try again... {e}")
            continue

# coroutine to claim coins
async def saveCoins(session, token, amount):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/save_coins"

    payload = json.dumps({
        "coins": amount
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 400:
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to saveCoins, HTTP error, try again... {e}")
            continue

# coroutine to get task
async def getTasks(session, token, ispremium):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_filtered_tasks"

    payload = json.dumps({
        "platform": "",
        "locale": "",
        "is_premium": ispremium
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getTasks, HTTP error, try again... {e}")
            continue

# coroutine to claim task
async def claimTask(session, token, idtask):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/complete_task"

    payload = json.dumps({
        "oid": idtask
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimTask, HTTP error, try again... {e}")
            continue

# coroutine to upgrade multitap
async def addMultitap(session, token, lvl):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/add_multitap"

    payload = json.dumps({
        "lvl": lvl+1
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to addMultitap, HTTP error, try again... {e}")
            continue

# coroutine to upgrade attemps
async def addAttemps(session, token, lvl):
    url = "https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/add_attempts"

    payload = json.dumps({
        "lvl": lvl
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impqdm5tb3luY21jZXdudXlreWlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3MDE5ODIsImV4cCI6MjAyNDI3Nzk4Mn0.oZh_ECA6fA2NlwoUamf1TqF45lrMC0uIdJXvVitDbZ8',
        'authorization': f'Bearer {token}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to addAttemps, HTTP error, try again... {e}")
            continue

# coroutine to run get token
async def runGetToken():        
    try:
        with open('query.txt', 'r') as qf:
            querys = qf.readlines()
            async with httpx.AsyncClient() as session:
                for i in range(len(querys)):
                    # print(querys[i].strip())
                    query = querys[i].strip()

                    token = await getToken(session, query)
                    token = token['token']

                    querys[i] = f"{token}\n"

                    with open('tokens.txt', 'w+') as tf:
                        tf.writelines(querys)
        print("Create token success!")
    except FileNotFoundError:
        qf = open('query.txt', 'w')
        print("Fill the query.txt first!")
        qf.write("query1\nquery2\netc...")
        qf.close()
        exit()

# coroutine to run all
async def runAll(token):
    async with httpx.AsyncClient() as session:
        userinfo = await getUserInfo(session, token)

        userid = userinfo['id']
        user_level = userinfo['level']
        balance = userinfo['balance']
        user_dailyattemps = userinfo['daily_attempts']
        
        # taptap
        stat_farming = "-"
        amount = int(os.getenv("PER_CLAIM_AMOUNT"))
        if user_dailyattemps > 0: 
            stat_save = await saveCoins(session, token, amount) 
            if 'success' in stat_save:
                if stat_save['success'] == True:
                    stat_farming = f"{Color.green}Success{Color.reset}"
                else:
                    stat_farming = f"{Color.yellow}Wait for energy{Color.reset}"
            else:
                stat_farming = f"{Color.red}Wrong amount!{Color.reset}"
        else:
            stat_farming = f"{Color.yellow}Low energy{Color.reset}"
                
        # tasks
        success_task = 0
        if os.getenv("AUTO_TASK") == "true":
            is_premium = userinfo['is_premium']
            list_task = await getTasks(session, token, is_premium)
            for i in list_task:
                if i['is_completed'] != True:
                    # print(i['id'])
                    idtask = i['id']
                    await claimTask(session, token, idtask)
                else:
                    success_task +=1
        else:
            success_task = "Off"

        if success_task != "Off":
            if success_task > 0:
                success_task = f"{Color.green}{success_task}{Color.reset}"
            else:
                pass

        lvl_now = "-"
        attemps_now = "-"
        if os.getenv("AUTO_BOOSTER") == "true":
            # upgrade multitap
            lvl_now = int(userinfo['multiple_clicks'])
            await addMultitap(session, token, lvl_now)
            userinfo = await getUserInfo(session, token)
            lvl_now = f"{Color.green}{int(userinfo['multiple_clicks'])}{Color.reset}"

            # upgrade energy/attemps
            attemps_now = int(userinfo['limit_attempts']) - 9
            await addAttemps(session, token, attemps_now)
            userinfo = await getUserInfo(session, token)
            attemps_now = f"{Color.green}{int(userinfo['limit_attempts']) - 9}{Color.reset}"
        else:
            lvl_now = "Off"
            attemps_now = "Off"
        
        # print all
        if os.getenv("AUTO_TASK") == "true" and os.getenv("AUTO_BOOSTER") == "false":
            print(f"[{userid}] | Level : {user_level} | Balance : {Color.green}{balance}{Color.reset} | Status : {stat_farming} | Task completed : {success_task}")
        elif os.getenv("AUTO_TASK") == "false" and os.getenv("AUTO_BOOSTER") == "true":
            print(f"[{userid}] | Level : {user_level} | Balance : {Color.green}{balance}{Color.reset} | Status : {stat_farming} | Multitap level : {lvl_now} | Attemps level : {attemps_now}")
        elif os.getenv("AUTO_TASK") == "false" and os.getenv("AUTO_BOOSTER") == "false":
            print(f"[{userid}] | Level : {user_level} | Balance : {Color.green}{balance}{Color.reset} | Status : {stat_farming}")
        else:
            print(f"[{userid}] | Level : {user_level} | Balance : {Color.green}{balance}{Color.reset} | Status : {stat_farming} | Task completed : {success_task} | Multitap level : {lvl_now} | Attemps level : {attemps_now}")

    return int(balance)

async def main():
    # query = ""
    
    os.system("cls" if os.name == "nt" else "clear") # remove the printed 

    print("Create token started")
    await runGetToken()

    sekarang = time.time()
    nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))

    while sekarang < nanti:
        print("""
     _       _            _         _           _   
  __| | ___ | |_ ___ ___ (_)_ __   | |__   ___ | |_ 
 / _` |/ _ \| __/ __/ _ \| | '_ \  | '_ \ / _ \| __|
| (_| | (_) | || (_| (_) | | | | | | |_) | (_) | |_ 
 \__,_|\___/ \__\___\___/|_|_| |_| |_.__/ \___/ \__|
        """)
        print(f"Auto claim task :", f"{Fore.GREEN}On{Style.RESET_ALL}" if os.getenv("AUTO_TASK") == "true" else "Off")
        print(f"Auto upgrade booster :", f"{Fore.GREEN}On{Style.RESET_ALL}" if os.getenv("AUTO_BOOSTER") == "true" else "Off")
        print("")
        start = time.time()
        schedules = []
        with open('tokens.txt', 'r') as tf:
            tokens = tf.readlines()
            for i in range(len(tokens)):
                # print(tokens[i].strip())
                token = tokens[i].strip()
                schedules.append(asyncio.create_task(runAll(token)))

        # gather to run concurently
        hasilakhir = await asyncio.gather(*schedules) # BOOOMMMM TO RUN

        totalallacc = 0
        for i in hasilakhir:
            totalallacc = totalallacc + i
        
        # delay before next running
        print("")
        print(f"Total balance : {Fore.GREEN}{totalallacc}{Style.RESET_ALL}")
        finish = time.time()-start
        #################### CHANGE THE REFRESH HERE ####################
        claim_remaining = int(os.getenv("REFRESH_CLAIM")) # set to 2 menit or 120 seconds
        refresh_token_at = datetime.datetime.fromtimestamp(nanti).strftime("%H:%M:%S")
        ###############################################################

        while claim_remaining:
            hour, secs = divmod(claim_remaining, 60) 
            timer = '{:02d}'.format(secs) 
            print(f"Execution time : {Fore.YELLOW}{round(finish, 2)}{Style.RESET_ALL} seconds | Refresh tokens : {Fore.YELLOW}{refresh_token_at}{Style.RESET_ALL} | Refresh after : {Fore.YELLOW}{timer}{Style.RESET_ALL} seconds", end="\r")
            time.sleep(1) 
            claim_remaining -= 1
    
        sekarang = time.time() + int(os.getenv("REFRESH_CLAIM"))
        if sekarang >= nanti:
            print("")
            print("Refresh tokens started!")
            await runGetToken()
            time.sleep(2)
            nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))
            
        os.system("cls" if os.name == "nt" else "clear") # remove the printed 

if __name__ == "__main__":
    # Set the policy to prevent "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        pass
    asyncio.run(main())