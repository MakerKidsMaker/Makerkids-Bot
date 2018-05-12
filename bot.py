import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio





bot = commands.Bot(command_prefix='!')

print (discord.__version__)
client = discord.Client()

@bot.event
async def on_ready():
    print ("Ready when you are.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Say !cmds for commands."))

     
        
   

@bot.command(pass_context=True)
async def ping(ctx):
        await bot.say(":ping_pong: Pong!!")
        print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="__**{}'s info**__".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Tim.K")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Creator")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. KICKED!".format(user.name))
    await bot.kick(user)
@bot.command(pass_context=True)
@commands.has_role("Creator")
async def login(ctx):
   embed.add_field(name="__**Loading database...**__", color=0x00ff00)
   await bot.say(embed=embed)

       
@bot.command(pass_context = True)
@commands.has_role("Creator")
async def btalk(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
@bot.command(pass_context = True)
@commands.has_role("Creator")
async def clear(ctx, number):
    mgs = [] 
    number = int(number) 
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)
@bot.command(pass_context=True)
async def cmds(ctx):
  embed = discord.Embed(name="COMMANDS", color=0x00ff00)
  embed.add_field(name="CMDS", value="Here are the commands I found.", inline=False)
  embed.add_field(name="Prefix", value="!", inline=False)
  embed.add_field(name="Info", value="!info (USERNAME HERE)", inline=False)
  embed.add_field(name="Server Info", value="!serverinfo", inline=False)
  embed.add_field(name="Ping Pong!", value="!ping", inline=True)
  await bot.say(embed=embed)
@bot.command(pass_context=True)
async def fban(ctx, user: discord.Member):
    await bot.say("__**=-=BAN=-=**__")
    await bot.say("**Banned By**")
    await bot.say("Tim.K")
    await bot.say("**User Banned**")
    await bot.say("{0}".format(user.name))
@bot.command(pass_context=True)
async def staff(ctx):
    embed = (discord.Embed(title=":regional_indicator_s: :regional_indicator_t: :regional_indicator_a: :regional_indicator_f: :regional_indicator_f:", color=0x00ff00))
    embed.add_field(name="__**BOT CREATOR**__", value="Tim.K", inline=False)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
@commands.has_role("Creator")
async def addrole(ctx, myrole):
    author = ctx.message.author
    await bot.create_role(author.server, name=myrole)
@bot.command(pass_context=True)
@commands.has_role("Creator")
async def giverole(ctx, user: discord.Member, myrole):
    role = discord.utils.get(user.server.roles, name=myrole)
    await bot.add_roles(user, role)
@bot.command(pass_context=True)
@commands.has_role("Creator")
async def remrole(ctx, user: discord.Member, myrole):
    role = discord.utils.get(user.server.roles, name=myrole)
    await bot.remove_roles(user, role)

 




    

bot.run('NDQxMzM0NDY4MjMwMzgxNTY4.DcuwRw.HhgA_od4PvvGdeAW52q6ToqYceM')
