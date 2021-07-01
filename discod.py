import asyncio
from sys import audit
import discord
from discord import client
from discord import channel
from discord.ext import commands
from discord.message import Message
from discord.user import ClientUser
import requests
from bs4 import BeautifulSoup
import re
import random #랜덤함수
import time #딜레이 함수
from soupsieve import select
from datetime import datetime
import os
import json
import requests
app = commands.Bot(command_prefix='prefix that you want')



@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')    
    activity = discord.Game(name="모두에게 인사")
    
    await app.change_presence(status=discord.Status.idle, activity=activity)
    #await app.change_presence(status=discord.Status.online, activity=discord.Game("서술"))
    

@app.event
async def on_message(message):
    a = random.randint(1, 30)
    if(a==3):
        await message.add_reaction("👀")
    elif(a==14):
        await message.add_reaction("🤔")

 
            
    message_content=message.content
    bad=message_content.find("ㅅㅂ")

    if bad>=0:
        await message.delete()
        await message.channel.send('욕 감지')
    if message.content.startswith('삭제'): 
        await message.channel.purge(limit=5)
    if message.content.startswith("실행"):
        embed=discord.Embed(title="프로필", description="폴라 딱가리", color=0x00ff56)
        embed.set_author(name="폴라 딱가리", url="https://blog.naver.com/huntingbear21", icon_url="https://cdn.discordapp.com/avatars/655642548328726578/9912c169df4d463a2d28d9f9654bd597.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/655642548328726578/9912c169df4d463a2d28d9f9654bd597.png?size=256")
        embed.add_field(name="1", value="1", inline=False)
    
        embed.set_footer(text="안녕하세요!")
        await message.channel.send(embed=embed)    
    
    if message.content.startswith('시간표'): 
        a=datetime.today().weekday()      
        if(a==0):
            today="월"
            a="영어\n 수학\n일본어 \n 서버구축\n서버구축 \n자료구조\n자료구조" 
        elif(a==1):
            today="화"
            a="주제\n 한국사\n물리 \n 영어b\n문학a \n웹프\n웹프"   
        embed = discord.Embed(title="시간표",description=a, color=0x00aaaa)    
        await message.channel.send("6반 시간표", embed = discord.Embed(title=today+"요일 시간표",description=a, color=0x00aaaa)   )

    if message.content.startswith('안녕!'): 
        await message.channel.send('안녕하세요!👋')
    if message.content.startswith('아담'): 
        await message.channel.send('예쁘다!')    
    if message.content.startswith('사랑해'): 
        await message.channel.send('나도 엄청 사랑해❤❤❤')
        
        await message.add_reaction("❤") #step
    if message.content.startswith('고마워'): 
        await message.channel.send('웅><')
    if message.content.startswith('히히'): 
        await message.channel.send('😀')    
        



    if message.content.startswith('좋아'): 
        await message.add_reaction("👍")
    if message.content.startswith('id'): 
        await message.channel.send("<@"+str(message.author.id)+'>')
    if message.content.startswith('가위바위보!'):
        embed = discord.Embed(title="가위 바위 보 게임!",description="가위바위보 게임\n 선택해주세요!", color=0x00aaaa)
        embed.add_field(name="Scissors ✌️", value="가위!", inline=False)
        embed.add_field(name="Rock", value="바위!", inline=False)
        embed.add_field(name="Paper✋", value="보!", inline=False)
        
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("✌️") #step
        await msg.add_reaction("✊") #stun
        await msg.add_reaction("✋")

    if message.content.startswith('명령어 리스트'):
         await message.channel.send(message.channel, embed=discord.Embed(description="명령어 테스트",color=0x00ff00))

    if message.content.startswith('급식'):
         url = 'http://sunrint.hs.kr/index.do'
         s="#index_board_mlsv_03_195699 > div > div > div > div > ul:nth-child(1) > li > dl > dd"
         await message.channel.send( embed=discord.Embed(description=html(url,s),color=0x00ff00))     
    if message.content.startswith('코로나'):
         url="https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EC%BD%94%EB%A1%9C%EB%82%98%ED%98%B8&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90"
         s="#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_01 > p"
         s1="#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_01 > em"
         s2="#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_04 > p"
         await message.channel.send( embed=discord.Embed(title="대한 민국 확진자",description="💉확진자 수💉:"+html(url,s)+"\n증가수 :"+html(url,s1)+"\n사망자 수 : "+html(url,s2)+"\n마스크 착용을 의무화 합시다😷",color=0xFF0000))    
    if message.content.startswith('공부 어때?'):
         msg= await message.channel.send('으악 공부싫어')
         await asyncio.sleep(3.0)
         await msg.edit(content="ㅎㅎ...공부 좋아")
    
    if message.content.startswith('비밀'):
         msg= await message.channel.send('전 사실 사람이에요')
         await asyncio.sleep(1.0)
         await msg.delete()
    if message.content.startswith('움짤'):
         msg= await message.channel.send( "https://tenor.com/view/grrr-gif-18348448")
         await message.delete()
    if message.content.startswith('임티'):
         msg= await message.channel.send( "https://cdn.discordapp.com/emojis/835663623685668875.png?v=1")
         await message.delete()     
    if message.content.startswith('도배'):
        for i in range(1,10):

            msg= await message.channel.send( "https://cdn.discordapp.com/emojis/835663623685668875.png?v=1")
            await msg.delete()      
    if message.content.startswith('온라인클래스'):
        await message.channel.send( "https://www.ebsoc.co.kr/")
    if message.content.startswith('자가진단'):
       await message.channel.send( "https://hcs.eduro.go.kr/#/loginWithUserInfo")  
    if message.content.startswith('+검색 '):
        message.content = "https://www.google.com/search?q="+message.content.replace("+검색 ","").replace(" ","%20")
        msg = message.content
        await  message.channel.send( msg)
   
    if message.content.startswith('롤'):
       
       name= message.content.split("!")
       a=lol(name[1])
       await message.channel.send("솔로랭크" )  
       await message.channel.send("랭크 포인트"+str(a[0]) )  
       await message.channel.send("티어"+str(a[1]) )  
       await message.channel.send("티어 "+str(a[2]))  
      
       await message.channel.send( "승리한 게임"+str(a[3]) )  
       await message.channel.send( "패배한 게임"+str(a[4]) )  
   


client=commands.Bot(command_prefix='r!')
@client.command()
async def clear(ctx,amount:int):
    await ctx.channel.purege(limit=amount)

    
@app.event
async def on_member_join(member):
	await member.guild.get_channel("856064349055090691").send(member.mention + "님이 새롭게 접속했습니다. 환영해주세요!")
	return



 
@app.event
async def on_reaction_add(reaction, user):
    a = random.randint(1, 2)
    
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "✌️":
        await reaction.message.channel.send(user.name + "님이 가위를 선택했습니다")
        await reaction.message.channel.send("선택중🤔")
        time.sleep(5)
        if(a==1):
            await reaction.message.channel.send("✋\n"+user.name+"님이 승리했습니다")
        else:
            await reaction.message.channel.send("✊\n"+user.name+"님이 패배했습니다")    

    if str(reaction.emoji) == "✊":
        await reaction.message.channel.send("선택중🤔")
        time.sleep(5)
        await reaction.message.channel.send(user.name + "님이 주먹을 선택했습니다")
        if(a==1):
            await reaction.message.channel.send("✌️\n"+user.name+"님이 승리했습니다")
        else:
            await reaction.message.channel.send("✋\n"+user.name+"님이 패배했습니다")   
    if str(reaction.emoji) == "✋":
        await reaction.message.channel.send(user.name + "님이 보를 선택했습니다")
        await reaction.message.channel.send("선택중🤔")
        time.sleep(5)
        if(a==1):
            await reaction.message.channel.send("✊\n"+user.name+"님이 승리했습니다")
        else:
            await reaction.message.channel.send("✌️\n"+user.name+"님이 패배했습니다")   



def html(url,s):

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one(s)
        return title.get_text()
    else : 
        return "에러"

def lol(name):
    
    api_key = "RGAPI-b2148bfd-5897-4cbf-adab-d8b46816cca1"
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
       
        resobj = json.loads(res.text)
        URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        rankinfo = json.loads(res.text)
        print("소환사 이름: "+name)
        for i in rankinfo:
            if i["queueType"] == "RANKED_SOLO_5x5":
                #솔랭과 자랭중 솔랭
                print("솔로랭크:")
                print(f'포인트{i["leaguePoints"]}')
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
                a=[{i["leaguePoints"]}, {i["tier"]}, {i["rank"]},{i["wins"]},{i["losses"]}]
                return a
            else:
             # 솔랭과 자랭중 자랭
                print("자유랭크:")
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")

token=os.environ["BOT"]
app.run(token)

