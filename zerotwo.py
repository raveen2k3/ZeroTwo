
from pyrogram import Client , filters
import wget
import os
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
import psutil
import requests
import json
import subprocess
import configs

sudo_users = 1520625615 , 1871813121
owner_id = [1871813121]

ZeroTwo = Client(
    "my_bot",
    bot_token= configs.BOT_TOKEN,
    api_id=configs.API_ID,
    api_hash=configs.API_HASH
    
)



@ZeroTwo.on_message(filters.command(["start"]))
async def help (client , message):
    await message.reply_text(text = "fuck")

@ZeroTwo.on_message(filters.command(["id"]))
async def id (client , message):
    id_user = str(message.from_user.id)
    await message.reply_text(text ="**YOUR ID:**"+" \n\n " + id_user)

@ZeroTwo.on_message(filters.command(["neofetch"]))
async def neofetch (client , message):
    string2 = subprocess.run(["neofetch", "--stdout"] , capture_output=True , shell=False, text=None, env=None, universal_newlines=None)
    await message.reply_text(text = string2)



@ZeroTwo.on_message(filters.command(["neko"]))
async def anime (client , message):
    user_id = message.from_user.id
    if user_id in configs.owner_id:
        chat_id = message.chat.id
        r = requests.get(url = 'https://api.waifu.pics/sfw/neko')
        data = r.json()
        print(data)
        print(type(data))
        await message.reply(data['url'])
    else:
        await message.reply("only for my <a href=\"https://t.me/its_raveen/\">Darling</a> ")


@ZeroTwo.on_message(filters.command(["chat_id"]))
async def chatid (client , message):
    chatidee =str(message.chat.id)
    await message.reply_text(text="**GROUP'S ID: **"+ " \n\n" + chatidee)

@ZeroTwo.on_message(filters.command(["leavechat"]))
async def leave (client , message):
    chat_id = message.chat.id
    await message.reply_text(text = "As Per Your Request ill leave from here 🥺")
    await ZeroTwo.leave_chat(chat_id)

@ZeroTwo.on_message(filters.command(["stats"]))
async def stats (client , message):
    user_id = message.from_user.id
    if user_id in configs.sudo_users:
        chat_id = message.chat.id
        print(os.uname()) 
        os_unmae = str( os.uname())
        disk_stat =  str(psutil.disk_usage('/'))
        print(psutil.disk_usage('/'))
        status = str( "RUNNING WITH PROBLEMS")
        await message.reply_text(text = "**\n\nHOSTNAME:** " +os_unmae + " "+ " "  + " "+ " "+ "\n\n **STORAGE**:" + disk_stat +  " " + " " +" " + " "+"\n\n **RUNNING STATUS :**" + status )
    else:
        await message.reply_text(text= "you are not a sudo user of @Im_zeroTwo")



@ZeroTwo.on_message(filters.command(["ban"]))
async def ban (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            chat_id = message.chat.id
            user_id  = message.reply_to_message.from_user.id
            await ZeroTwo.ban_chat_member(chat_id, user_id)
            await message.reply_text(text= "**BANNED SUCCESFULLY**")
        else:
            await message.reply_text(text = "** YOU ARE NOT A ADMIN IN THIS CHAT **")
    except:
        await message.reply_text("**Error Occured Report in Support Group!!**")


@ZeroTwo.on_message(filters.command(["unban"]))
async def unban (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            chat_id = message.chat.id
            user_id  = message.reply_to_message.from_user.id
            await ZeroTwo.unban_chat_member(chat_id, user_id)
            await message.reply_text(text= "**UNBANNED SUCCESFULLY**")
        else:
            await message.reply_text(text = "** YOU ARE NOT A ADMIN IN THIS CHAT **")
    except:
        await message.reply_text("**Error Occured Report in Support Group!!**")






@ZeroTwo.on_message(filters.command(["promote"]))
async def promote (client , message):
    try:
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get. status 
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        cmd_user = ["administrator","creator"] 
        if status in cmd_user:
            user_id = message.reply_to_message.from_user.id
            await ZeroTwo.promote_chat_member(chat_id, user_id)
            await ZeroTwo.send_message(chat_id, "promoted successfully")
        else:
            await message.reply_text("You don't have enough rights!!")
    except:
        await message.reply_text("ERROR OCCURED TRY CONTACTING OUR SUPPORT GROUP")

@ZeroTwo.on_message(filters.command(["pin"]))
async def pin (client , message):
  try:
      get =await client.get_chat_member(message.chat.id,message.from_user.id) 
      status = get. status 
      chat_id = message.chat.id
      message_id = message.reply_to_message.message_id
      cmd_user = ["administrator","creator"] 
      if status in cmd_user:
          await ZeroTwo.pin_chat_message(chat_id, message_id)
          await message.reply_text(text = "Pinned to Top🥺")
      
      else:
          await message.reply_text('Only Admin Can Pin Messages')
  except:
        await message.reply_text("REPLY TO A MESSAGE TO PIN IT ")

@ZeroTwo.on_message(filters.command(["admintitle"]))
async def adminTITLE(client , message):
    chat_id = message.chat.id
    get =await client.get_chat_member(message.chat.id,message.from_user.id) 
    status = get.status
    cmd_user = ["administrator","creator"]
    msg = message.text
    title = msg.split(' ')[1]
    user_id = message.reply_to_message.from_user.id
    try:
        if status in cmd_user:
            await ZeroTwo.set_administrator_title(chat_id, user_id, title)
            await message.reply_text("title updated")
        else:
            await ZeroTwo.send_message(chat_id, "you dont have enough rights , to make changes!!")
    except:
            await message.reply_text("ERROR OCCURED TRY CONTACTING OUR SUPPORT GROUP")


@ZeroTwo.on_message(filters.command(["eval"]))
async def eval (client , message):
    chat_id = message.chat.id
    inputgot = message.text[0]
    string = subprocess.run([inputgot], capture_output=True)
    await message.reply(text = string)



@ZeroTwo.on_message(filters.command(["adminlist"]))
async def adminlist (client , message):
    chat_id = message.chat.id
    chat_name = message.chat.username
    async for member in ZeroTwo.iter_chat_members(chat_name, filter="administrators"):
        print(member.user.first_name + ' is admin!')
        await message.reply_text(text = member.user.first_name + ' is admin!')








ZeroTwo.run()
