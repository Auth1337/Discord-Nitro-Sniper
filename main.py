import discord
import re
import threading
import os
import sys
import requests
from discord.ext import commands
from dhooks import Webhook



session = requests.Session()

os.system("clear||cls")

def rmv_dpy():
  print("[+] Installing Discord.Py-Self")
  if "discord" or "discord.py" in sys.modules:
    os.system("pip uninstall discord.py -y && pip uninstall discord -y && pip uninstall discord.py-self -y && pip install git+https://github.com/dolfies/discord.py-self && clear||cls")

rmv_dpy()

token = input("Token: ")
web_hook = input("Webhook(Optional Press Enter To Skip Or Add Webhook):")

os.system("clear||cls")

if web_hook.startswith("https://"):
  client = Webhook(web_hook)
else:
  class client:
    def send(*args, **kwargs):
      pass





def snap(code):
  r = session.post(f"https://discord.com/api/v10/entitlements/gift-codes/{code}/redeem", headers={"Authorization": token})
  res = r.text.lower()
  if "already" in res:
    print(f"https://discord.gift/{code}, Already Redeemed")
  elif "subscription_plan" in res:
    print(f"Auth#1337 | Nitro Claimed\nhttps://discord.gift/{code}")
    client.send(f"@everyone https://discord.gift/{code} Claimed!")
  elif "unknown" in res:
    print("Unknown Gift Code Or Invalid.")
  print(res)
  print(code)
  

    




client = commands.Bot(command_prefix="nitro-sniper", self_bot=True, help_command=None)


@client.event
async def on_ready():
  print(f"Connected To {client.user}")


@client.event
async def on_message(message):
  if 'discord.gift/' in message.content.lower() or 'discord.com/gifts/' in message.content.lower() or 'discordapp.com/gifts/' in message.content.lower():
    if "discord.gift/" in message.content.lower():
      code = re.findall("discord[.]gift/(\w+)", message.content.lower())
    elif "discordapp.com/gifts/" in message.content.lower():
      code = re.findall("discordapp[.]com/gifts/(\w+)", message.content.lower())
    elif 'discord.com/gifts/' in message.content.lower():
      code = re.findall("discord[.]com/gifts/(\w+)", message.content.lower())
    try:
      for code_ in code:
        if len(code_) == 16 or len(code_) == 24:
          threading.Thread(target=snap, args=(code_,)).start()
    except:
      pass
  await client.process_commands(message)
      
      

    
client.run(token, reconnect=True)
