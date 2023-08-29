import sys
import os
import asyncio
from telethon import events

@hell_cmd(pattern="ol(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await eod(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(5364964725,"/explore")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[5364964725]))
async def _(event):
    if 'Wait , a group of monster is approaching.... 

if monster not appearing in 10 seconds , press /captcha' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
   
    
   
