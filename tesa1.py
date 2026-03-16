import discord
from discord.ext import commands
import asyncio
import sys
import json
import msg
from dotenv import load_dotenv
import os
import time
import requests  

load_dotenv()
bot1 = os.getenv('bot1')
GH_TOKEN = os.getenv('GH_TOKEN')         
GH_REPO  = os.getenv('GH_REPO')           

if len(sys.argv) < 2:
    print("Error: JSON config tidak diberikan.")
    sys.exit(1)

raw_config = sys.argv[1]
config = json.loads(raw_config)

place = config["place"]
channel_ids = {
    "bg"         : config["channel_idbg"],
    "sign"       : config["channel_idsign"],
    "plat"       : config["channel_idplat"],
    "consumable" : config["channel_idconsumable"],
    "block"      : config["channel_idblock"],
    "guild"      : config["channel_idguild"],
    "door"       : config["channel_iddoor"],
    "winterfest" : config["channel_winterfest"],
    "ubiweek"    : config["channel_ubiweek"],
    "carni"      : config["channel_carni"],
    "valentine"  : config["channel_valentine"],
    "test"       : config["channel_test"],
}

msgs = {
    "bg"         : msg.msg_bg.replace("{place}", place),
    "sign"       : msg.msg_sign.replace("{place}", place),
    "plat"       : msg.msg_plat.replace("{place}", place),
    "consumable" : msg.msg_consumable.replace("{place}", place),
    "block"      : msg.msg_block.replace("{place}", place),
    "guild"      : msg.msg_guild.replace("{place}", place),
    "door"       : msg.msg_door.replace("{place}", place),
    "winterfest" : msg.msg_winterfest.replace("{place}", place),
    "ubiweek"    : msg.msg_ubiweek.replace("{place}", place),
    "carnival"   : msg.msg_carnival.replace("{place}", place),
    "valentine"  : msg.msg_valen.replace("{place}", place),
    "test"       : msg.msg_test.replace("{place}", place),
}

BLOCK_COOLDOWN = 6 * 3600
VAR_NAME = f"BLOCK_LAST_SENT_{place.upper()}"  # nama variable di GitHub, misal BLOCK_LAST_SENT_KMWQ

def get_block_timestamp():
    """Ambil timestamp dari GitHub repo variable."""
    if not GH_TOKEN or not GH_REPO:
        return None
    url = f"https://api.github.com/repos/{GH_REPO}/actions/variables/{VAR_NAME}"
    headers = {"Authorization": f"Bearer {GH_TOKEN}", "Accept": "application/vnd.github+json"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return float(r.json()["value"])
    return None  # belum ada = belum pernah kirim

def save_block_timestamp():
    """Simpan timestamp ke GitHub repo variable."""
    if not GH_TOKEN or not GH_REPO:
        print(f"[{place}] GH_TOKEN/GH_REPO tidak ada, skip save timestamp.")
        return
    url_check = f"https://api.github.com/repos/{GH_REPO}/actions/variables/{VAR_NAME}"
    headers = {"Authorization": f"Bearer {GH_TOKEN}", "Accept": "application/vnd.github+json"}
    data = {"name": VAR_NAME, "value": str(time.time())}
    # Coba update dulu, kalau 404 baru create
    r = requests.patch(url_check, headers=headers, json=data)
    if r.status_code == 404:
        base_url = f"https://api.github.com/repos/{GH_REPO}/actions/variables"
        requests.post(base_url, headers=headers, json=data)

def can_send_block():
    last = get_block_timestamp()
    if last is None:
        return True
    return (time.time() - last) >= BLOCK_COOLDOWN

bot = commands.Bot(command_prefix="!")

async def send_msg(d):
    await asyncio.sleep(5)
    try:
        channel = bot.get_channel(channel_ids[d])
        if channel:
            await channel.send(msgs[d])
            print(f"[{place}] Sent [{d}]")
        else:
            print(f"[{place}] Channel not found: {d}")
    except discord.HTTPException as e:
        if e.status == 429:
            print(f"[{place}] Rate limited on {d}, skipping...")
        else:
            print(f"[{place}] HTTP error on {d}: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
    print(f"[{place}] {bot.user.name} is online")
    try:
        ds = ["bg", "sign", "plat", "consumable", "guild", "door", "winterfest", "ubiweek", "valentine"]
        for d in ds:
            await send_msg(d)

        if can_send_block():
            await send_msg("block")
            save_block_timestamp()
            print(f"[{place}] Block sent and timestamp saved.")
        else:
            last = get_block_timestamp()
            sisa = BLOCK_COOLDOWN - (time.time() - last)
            print(f"[{place}] Block skipped. Cooldown sisa {sisa/3600:.1f} jam.")

        print(f"[{place}] All done.")
    finally:
        await bot.close()

bot.run(bot1)