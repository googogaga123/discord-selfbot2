import discord
from discord.ext import commands, tasks
import asyncio
import sys
import json
import msg
from dotenv import load_dotenv
import os

load_dotenv()
bot3 = os.getenv('bot3')

if len(sys.argv) < 2:
    print("Error: JSON config tidak diberikan.")
    sys.exit(1)

raw_config = sys.argv[1]
config = json.loads(raw_config)


place = config["place"]
channel_ids = {
    "bg" : config["channel_idbg"],
    "sign" : config["channel_idsign"],
    "plat" : config["channel_idplat"],
    "consumable" : config["channel_idconsumable"],
    "block" : config["channel_idblock"],
    "guild" : config["channel_idguild"],
    "door" : config["channel_iddoor"],
    "winterfest" : config["channel_winterfest"],
    "ubiweek" : config["channel_ubiweek"],
    "carni" : config["channel_carni"],
    "valentine" : config["channel_valentine"],
    "test" : config["channel_test"],
}

msgs ={
    "bg" : msg.msg_bg.replace("{place}", place),
    "sign" : msg.msg_sign.replace("{place}", place),
    "plat" : msg.msg_plat.replace("{place}", place),
    "consumable" : msg.msg_consumable.replace("{place}", place),
    "block" : msg.msg_block.replace("{place}", place),
    "guild" : msg.msg_guild.replace("{place}", place),
    "door" : msg.msg_door.replace("{place}", place),
    "winterfest" : msg.msg_winterfest.replace("{place}", place),
    "ubiweek" : msg.msg_ubiweek.replace("{place}", place),
    "carnival" : msg.msg_carnival.replace("{place}", place),
    "valentine" : msg.msg_valen.replace("{place}", place),
    "test" : msg.msg_test.replace("{place}", place),
    
}



bot = commands.Bot(command_prefix="!")

async def send_msg(d):
    await asyncio.sleep(5)
    try:
        channel = bot.get_channel(channel_ids[d])
        if channel  :
            await channel.send(msgs[d])
            print(f"[{place}] Sent[{d}]")
        else:
            print(f"[{place}] Channel not found: {d}")
    except discord.HTTPException:
        print(f"[{place}] Cooldown on {d}, waiting 20s...")
        await asyncio.sleep(20)

@bot.event
async def on_ready():
    print(f"[{place}] {bot.user.name} is online")
    try:
        ds = ["bg", "sign", "plat", "consumable", "guild", "door", "winterfest", "ubiweek", "valentine", "block"]
        for d in ds:
            await send_msg(d)
        print(f"[{place}] All done.")
    finally:
        await bot.close()  # always closes, even if error occurs\

    # send_loop.start()
    # send_loop1.start()


# @tasks.loop(hours=2)
# async def send_loop():

#     ds = ["bg", "sign", "plat", "consumable", "guild", "door", "winterfest", "ubiweek", "valentine"]
#     for d in ds:
#         await send_msg(d)

# @tasks.loop(seconds=0, hours=6)
# async def send_loop1():
#         ds = ["block"]
#         for d in ds :
#              await send_msg(d)

# token

bot.run(bot3)  
