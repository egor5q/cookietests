# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize


from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
vip=[441399484, 55888804]
games={}
skills=[]

client1=os.environ['database']
client=MongoClient(client1)
db=client.cookiewars
users=db.users

client2=os.environ['database2']
client3=MongoClient(client2)
db2=client3.trug
userstrug=db2.users


@bot.message_handler(commands=['referal'])
def ref(m):
   bot.send_message(m.chat.id, 'Присоединяйся к игре CookieWars! Прокачай своего бойца, отправь в бой и наслаждайся тем, как он сам уничтожает соперника!\n'+
                    'https://telegram.me/cookiewarsbot?start='+str(m.from_user.id))

         
         

@bot.message_handler(commands=['dropname'])
def dropname(m):
   try:
       x=users.find_one({'id':m.reply_to_message.from_user.id})
       if x!=None:
           users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.name':None}})
           bot.send_message(m.chat.id, 'Имя пользователя успешно удалено!')
   except:
    pass

vetki={'hp':['skill "shieldgen"', 'skill "medic"', 'skill "liveful"', 'skill "dvuzhil"', 'skill "undead"'],          
       'dmg':['skill "pricel"', 'skill "berserk"','skill ""','skill "assasin"'],
       'different':['skill "zombie"', 'skill "hypnos"', 'skill "cube"', 'paukovod'],
       'skins':['oracle']
}

skills=[]

items=['flash', 'knife']
            


@bot.message_handler(commands=['donate'])
def donate(m):
   bot.send_message(m.chat.id, 'Донат - покупка игровых ресурсов за реальные деньги.\n'+
                    'Курс: 1000⚛ за 100 рублей. Для совершения платежа, переведите желаемую сумму (не меньше 50р) на карту:\n'+
                    '`5336 6900 5562 4037`, указав свой ник (через @).\nКак только я зайду в сеть, то начислю поинты в соответствии с курсом.\n'+
                    'При покупке от 500р начисляется бонус - дополнительные 1000⚛. При сумме покупок больше, чем на 800р - уникальные смайлики для хп в подарок!\nТак же их можно купить за 300 рублей.', parse_mode='markdown')
            


def createboss(id):
    return{'name': 'Босс',
              'weapon':'light',
              'skills':[],
              'team':None,
              'hp':5000,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':0,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':15,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'gipnoz':0,
              'weapons':['hand']}


def createpauk(id):
    return{id-(id*2):{'name': 'Паук',
              'weapon':'bite',
              'skills':[],
              'team':None,
              'hp':2,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':-id,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':7,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'gipnoz':0,
              'maxhp':2,
              'weapons':['hand']}}


       
           


@bot.message_handler(commands=['clear'])
def clear(m):
    if m.from_user.id==441399484:
        try:
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.bought':[]}})
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.skills':[]}})
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.skin':[]}})
            bot.send_message(m.chat.id, 'Инвентарь юзера успешно очищен!')
        except:
            pass
              


@bot.message_handler(commands=['me'])
def me(m):
  x=users.find_one({'id':m.from_user.id})
  if x!=None:
      exp=x['bot']['exp']
      if exp<=100:
         rang='Новичок'
      elif exp<=200:
         rang='Эсквайер'
      elif exp<=500:
         rang='Оруженосец'
      elif exp<=800:
         rang='Солдат'
      elif exp<=1500:
         rang='Опытный боец'
      elif exp<=2000:
         rang='Офицер'
      elif exp<=3000:
         rang='Подполковник'
      elif exp<=3500:
         rang='Полковник'
      elif exp<=5000:
         rang='Генерал'
      elif exp<=7000:
         rang='Оракул'
      elif exp<=8500:
         rang='Повелитель'
      elif exp<=10000:
         rang='Машина для убийств'
      elif exp<=15000:
         rang='Бессмертный'
      elif exp<=50000:
         rang='Мутант'
      elif exp<=100000:
         rang='Бог'
      else:
         rang='Пасюк'
  if m.reply_to_message==None:
    try:
      x=users.find_one({'id':m.from_user.id})
      bot.send_message(m.chat.id, 'Ваши поинты: '+str(x['cookie'])+'⚛️\nОпыт бойца: '+str(x['bot']['exp'])+'❇️\nДжоин боты: '+str(x['joinbots'])+'🤖\nСыграно матчей: '+str(x['games'])+'\n🎖Ранг: '+rang)
    except:
      pass
  else:
      try:
        x=users.find_one({'id':m.reply_to_message.from_user.id})
        bot.send_message(m.chat.id, 'Ваши поинты: '+str(x['cookie'])+'⚛️\nОпыт бойца: '+str(x['bot']['exp'])+'❇️\nДжоин боты: '+str(x['joinbots'])+'🤖\nСыграно матчей: '+str(x['games']))#+'\n🎖Ранг: '+rang)
      except:
        pass

@bot.message_handler(commands=['p'])
def k(m):
  if m.from_user.id==441399484 or m.from_user.id==55888804:
    x=m.text.split('/p')
    try:
      int(x[1])
      users.update_one({'id':m.reply_to_message.from_user.id}, {'$inc':{'cookie':int(x[1])}})
      bot.send_message(m.chat.id, x[1]+'⚛️ поинтов успешно выдано!')
    except:
        pass

      
      
@bot.message_handler(commands=['j'])
def j(m):
  if m.from_user.id==441399484 or m.from_user.id==55888804:
    x=m.text.split('/j')
    try:
      int(x[1])
      users.update_one({'id':m.reply_to_message.from_user.id}, {'$inc':{'joinbots':int(x[1])}})
      bot.send_message(m.chat.id, x[1]+'🤖 джойн-ботов успешно выдано!')
    except:
        pass
                

@bot.message_handler(commands=['dailybox'])
def buy(m):
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
     if x['dailybox']==1:
      try:
         y=random.randint(25,75)
         users.update_one({'id':m.from_user.id}, {'$inc':{'cookie':y}})
         users.update_one({'id':m.from_user.id}, {'$set':{'dailybox':0}})
         bot.send_message(m.chat.id, 'Вы открыли Поинтбокс и получили '+str(y)+'⚛️ поинтов!')
      except:
         bot.send_message(m.chat.id, 'Вас нет в списке бота! Сначала напишите ему в личку /start.')
     else:
      bot.send_message(m.chat.id, 'Вы уже открывали Поинтбокс сегодня! Приходите завтра после 00:00 по МСК.')
    
  
  
@bot.message_handler(commands=['delete'])
def delete(m):
    if m.from_user.id==441399484 or m.from_user.id==60727377 or m.from_user.id==137499781:
        if m.chat.id in games:
            del games[m.chat.id]
            bot.send_message(m.chat.id, 'Игра была удалена!')
        
        
@bot.message_handler(commands=['name'])
def name(m):
    text=m.text.split(' ')
    if len(text)==2:
     if len(text[1])<=12:
      x=users.find_one({'id':m.from_user.id})
      users.update_one({'id':m.from_user.id}, {'$set':{'bot.name':text[1]}})
      bot.send_message(m.chat.id, 'Вы успешно изменили имя бойца на '+text[1]+'!')
     else:
            bot.send_message(m.chat.id, 'Длина ника не должна превышать 12 символов!')
    else:
       bot.send_message(m.chat.id, 'Для переименования используйте формат:\n/name *имя*, где *имя* - имя вашего бойца.', parse_mode='markdown')
        
  
def itemselect():
    x=[]
    i=0
    while i<2:
        item=random.choice(items)
        x.append(item)
        i+=1
    return x
    

            
        
    
              
  
      

def giveitems(game):
    for ids in game['bots']:
      if game['bots'][ids]['id']!=0:
        game['bots'][ids]['items'].append(random.choice(items))
        game['bots'][ids]['items'].append(random.choice(items))
  

                   
def battle(id):  
  for bots in games[id]['bots']:
   if games[id]['bots'][bots]['die']!=1:
    if games[id]['bots'][bots]['stun']<=0:
     games[id]['bots'][bots][act(bots, id)]=1
  results(id)

def results(id):           
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['yvorot']==1:
        yvorot(games[id]['bots'][bots], id)
        
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['skill']==1:
        skill(games[id]['bots'][bots], id)   
              
  for bots in games[id]['bots']:
      if games[id]['bots'][bots]['item']==1:
          item(games[id]['bots'][bots], id) 
              
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['reload']==1:
        reload(games[id]['bots'][bots], id)          
              
  for bots in games[id]['bots']:
      if games[id]['bots'][bots]['attack']==1:
        attack(games[id]['bots'][bots],id)
                     
  for ids in games[id]['bots']:
    if games[id]['bots'][ids]['shield']>=1:
        games[id]['bots'][ids]['takendmg']=0
  dmgs(id)
  z=0
  bot.send_message(id, 'Результаты хода '+str(games[id]['xod'])+':\n'+games[id]['res']+'\n\n')
  bot.send_message(id, games[id]['secondres'])
  die=0    
  games[id]['xod']+=1
  for mobs in games[id]['bots']:
    if games[id]['bots'][mobs]['hp']>games[id]['bots'][mobs]['maxhp']:
        games[id]['bots'][mobs]['hp']=games[id]['bots'][mobs]['maxhp']
    games[id]['bots'][mobs]['attack']=0
    games[id]['bots'][mobs]['yvorot']=0 
    games[id]['bots'][mobs]['reload']=0 
    games[id]['bots'][mobs]['item']=0
    games[id]['bots'][mobs]['miss']=0
    if 'nindza' in games[id]['bots'][mobs]['skills']:
      games[id]['bots'][mobs]['miss']=20
    games[id]['bots'][mobs]['skill']=0
    games[id]['bots'][mobs]['shield']=0
    games[id]['bots'][mobs]['takendmg']=0
    games[id]['bots'][mobs]['yvorotkd']-=1
    games[id]['bots'][mobs]['shield']-=1
    games[id]['bots'][mobs]['shieldgen']-=1
    games[id]['bots'][mobs]['target']=None
    games[id]['bots'][mobs]['gipnoz']-=1
    games[id]['bots'][mobs]['mainskill']=[]
    games[id]['bots'][mobs]['mainitem']=[]
    if games[id]['bots'][mobs]['heal']!=0:
        games[id]['bots'][mobs]['heal']-=1
    if games[id]['bots'][mobs]['die']!=1:
     if games[id]['bots'][mobs]['hp']<1:
      games[id]['bots'][mobs]['die']=1
  diedungs=0
  dieplayers=0
  for ids in games[id]['bots']:
      if games[id]['bots'][ids]['id']==0 and games[id]['bots'][ids]['die']==1:
            diedungs+=1
  for ids in games[id]['bots']:
      if games[id]['bots'][ids]['id']!=0 and games[id]['bots'][ids]['die']==1:
            dieplayers+=1
  if diedungs==games[id]['enemies']:
      bot.send_message(id, 'Подземелье пройдено!')
      z=1
  elif dieplayers==games[id]['players']:
      bot.send_message(id, 'Бойцы проиграли!')
      z=1
  
  games[id]['results']=''
  games[id]['res']=''
  games[id]['secondres']=''
  if z==0:
    t=threading.Timer(12.0, battle, args=[id])
    t.start()
  else:
    del games[id]
                   
def dmgs(id):
    c=0
    for ids in games[id]['bots']:
        if games[id]['bots'][ids]['takendmg']>c:
            c=games[id]['bots'][ids]['takendmg']
    text=''
    for mob in games[id]['bots']:
        games[id]['bots'][mob]['stun']-=1
        if games[id]['bots'][mob]['stun']==0 and games[id]['bots'][mob]['die']!=1:
            text+='🌀'+games[id]['bots'][mob]['name']+' приходит в себя.\n'
        if games[id]['bots'][mob]['blood']!=0:
              games[id]['bots'][mob]['blood']-=1
              if games[id]['bots'][mob]['blood']==0 and games[id]['bots'][mob]['die']!=1 and games[id]['bots'][mob]['zombie']<=0:
                     games[id]['bots'][mob]['hp']-=1
                     text+='💔'+games[id]['bots'][mob]['name']+' истекает кровью и теряет жизнь!\n'
        if 'vampire' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
            if games[id]['bots'][mob]['target']!=None:
                print('1')
                print(games[id]['bots'][mob]['target']['takendmg'])
                if games[id]['bots'][mob]['target']['takendmg']==c and c>0:
                  a=random.randint(1,100)
                  if a<=5:
                    games[id]['bots'][mob]['hp']+=1
                    text+='😈Вампир '+games[id]['bots'][mob]['name']+' восстанавливает себе ❤️хп!\n'
    
                     
        if 'zeus' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
            x=random.randint(1,100)
            if x<=2:
                for ids in games[id]['bots']:
                    if games[id]['bots'][ids]['id']!=games[id]['bots'][mob]['id']:
                        games[id]['bots'][ids]['hp']-=1
                text+='⚠️Зевс '+games[id]['bots'][mob]['name']+' вызывает молнию! Все его враги теряют ❤️хп.\n'
        
                        
        if games[id]['bots'][mob]['zombie']!=0:
            games[id]['bots'][mob]['zombie']-=1
            if games[id]['bots'][mob]['zombie']==0:
                games[id]['bots'][mob]['die']=1     
                games[id]['bots'][mob]['energy']=0
                text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
                
    pauk=[]
    for mob in games[id]['bots']:
     if games[id]['bots'][mob]['takendmg']==c:
      if games[id]['bots'][mob]['takendmg']>0:
       if games[id]['bots'][mob]['takendmg']<games[id]['bots'][mob]['damagelimit']:
        a=1
       else:
        a=1
        ff=0
        while a<games[id]['bots'][mob]['takendmg'] and ff!=1:
            if games[id]['bots'][mob]['takendmg']>=games[id]['bots'][mob]['damagelimit']:
                a+=1
                games[id]['bots'][mob]['takendmg']-=games[id]['bots'][mob]['damagelimit']
            else:
               ff=1
       if games[id]['bots'][mob]['zombie']==0:
         if games[id]['bots'][mob]['die']!=1:
           if 'oracle' not in games[id]['bots'][mob]['skin']:
             games[id]['bots'][mob]['hp']-=a
           else:
            xx=random.randint(1,100)
            if games[id]['bots'][mob]['oracle']==1 and games[id]['bots'][mob]['hp']-a<=0 and xx<=30:
                   text+='🔮Оракул '+games[id]['bots'][mob]['name']+' предотвращает свою смерть!\n'
                   games[id]['bots'][mob]['oracle']=0
            else:
                games[id]['bots'][mob]['hp']-=a
       else:
           pass
       pop=emojize(':poop:', use_aliases=True)
       if games[id]['bots'][mob]['hp']<100:
         if games[id]['bots'][mob]['id']==581167827:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'💙'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
         elif games[id]['bots'][mob]['id']==256659642:
            text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+pop*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
         else:
            text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'            
       else:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+str(games[id]['bots'][mob]['hp'])+'хп!\n'
       if games[id]['bots'][mob]['hp']==1 and 'berserk' in games[id]['bots'][mob]['skills']:
         text+='😡Берсерк '+games[id]['bots'][mob]['name']+' входит в ярость и получает +2 урона!\n'
     if games[id]['bots'][mob]['hp']<=0:
           if 'zombie' not in games[id]['bots'][mob]['skills']:
             if games[id]['bots'][mob]['die']!=1:
              if 'bloodmage' not in games[id]['bots'][mob]['skills']:
                  text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
              else:
                 randd=random.randint(1,100)
                 if randd<=50:
                  a=[]
                  for ids in games[id]['bots']:
                     if games[id]['bots'][ids]['die']!=1 and games[id]['bots'][ids]['hp']>0 and games[id]['bots'][ids]['zombie']<=0:
                        a.append(games[id]['bots'][ids])
                  if len(a)>0:
                   x1=random.choice(a)
                   x2=None
                   
     
                   x2=None
                   x1['hp']-=1
                   if x2!=None:
                     x2['hp']-=1
                   if x2!=None:
                     if x2['hp']<=0 or x1['hp']<=0:
                        text+='🔥Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает по жизни у '+x1['name']+' и '+x2['name']+', и воскресает с 1❤️!\n'
                        games[id]['bots'][mob]['hp']=1
                        if x1['hp']<=0:
                           text+='👹'+x1['name']+' теперь зомби!\n'
                           x1['zombie']=1
                        if x2['hp']<=0:
                           text+='☠️'+x2['name']+' теперь зомби!\n'
                           x2['zombie']=3
                     else:
                        text+='😵Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает по жизни у '+x1['name']+' и '+x2['name']+', но никого не убивает, и погибает окончательно.\n'
                   else:
                     if x1['hp']<=0:
                        text+='🔥Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает жизнь у '+x1['name']+', и воскресает с 1❤️!\n'
                        games[id]['bots'][mob]['hp']=1
                        text+='👹'+x1['name']+' теперь зомби!\n'
                        x1['zombie']=1
                        x1['hp']=1
                     else:
                        text+='😵Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает жизнь у '+x1['name']+', но не убивает цель, и погибает окончательно.\n'
                  else:
                     text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
                 else:
                  text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
           else:
              games[id]['bots'][mob]['zombie']=2
              games[id]['bots'][mob]['hp']=1
              text+='👹'+games[id]['bots'][mob]['name']+' теперь зомби!\n'
           if 'paukovod' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
                  text+='🕷Паук бойца '+games[id]['bots'][mob]['name']+' в ярости! Он присоединяется к бою.\n'
                  pauk.append(games[id]['bots'][mob]['id'])
     if games[id]['xod']%5==0:
       if games[id]['bots'][mob]['id']==87651712:
          if games[id]['bots'][mob]['die']!=1 and games[id]['bots'][mob]['hp']>0:
              text+=games[id]['bots'][mob]['name']+' сосёт!\n'
    for itemss in pauk:
       games[id]['bots'].update(createpauk(itemss))
       print('pauk')
       print(games[id]['bots'])
    games[id]['secondres']='Эффекты:\n'+text
   
    
  
  
  
def rockchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=95
  elif energy==4:
    chance=80
  elif energy==3:
    chance=70
  elif energy==2:
    chance=50
  elif energy==1:
    chance=20
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(2, 3)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='☄️'+bot1['name']+' Кидает камень в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          stun=random.randint(1, 100)
          if stun<=20:
            target['stun']=2
            games[id]['res']+='🌀Цель оглушена!\n'
          
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
          
          
def akchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=80
  elif energy==4:
    chance=70
  elif energy==3:
    chance=50
  elif energy==2:
    chance=30
  elif energy==1:
    chance=5
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(3, 4)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='🔫'+bot1['name']+' Стреляет в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'        
          target['takendmg']+=damage
          bot1['energy']-=random.randint(2,3)
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=random.randint(2,3)
        
        
        
def handchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=99
  elif energy==4:
    chance=90
  elif energy==3:
    chance=80
  elif energy==2:
    chance=70
  elif energy==1:
    chance=60
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(1,3)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='🤜'+bot1['name']+' Бьет '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=random.randint(1,2)
                
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=random.randint(1,2)
       
       
def sawchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=97
  elif energy==4:
    chance=90
  elif energy==3:
    chance=80
  elif energy==2:
    chance=65
  elif energy==1:
    chance=30
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(1,2)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='⚙️'+bot1['name']+' Стреляет в '+target['name']+' из Пилострела! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          blood=random.randint(1, 100)
          if blood<=35:
            if target['blood']==0:
              target['blood']=4
              games[id]['res']+='❣️Цель истекает кровью!\n'
            elif target['blood']==1:
              games[id]['res']+='❣️Кровотечение усиливается!\n'
            else:
                target['blood']-=1
                games[id]['res']+='❣️Кровотечение усиливается!\n'
                
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
       
       
def kinzhalchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=95
  elif energy==4:
    chance=80
  elif energy==3:
    chance=75
  elif energy==2:
    chance=40
  elif energy==1:
    chance=25
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=1
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          if target['reload']!=1:
              games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
              target['takendmg']+=damage
              bot1['energy']-=2
          else:
              a=random.randint(1,100)
              if a<=100:
                   damage=6
                   games[id]['res']+='⚡️'+bot1['name']+' Наносит критический удар по '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
                   bot1['energy']-=5
                   target['takendmg']+=damage
              else:
                  games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
                  target['takendmg']+=damage
                  bot1['energy']-=2               
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
                
             
def lightchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=50
  elif energy==4:
    chance=50
  elif energy==3:
    chance=10
  elif energy==2:
    chance=1
  elif energy==1:
    chance=1
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=100
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='⚠️'+bot1['name']+' Бъет '+target['name']+' Молнией! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=5
        
    else:
        games[id]['res']+='💨Молния босса ударила мимо '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=5
        
def bitechance(energy, target, x, id, bot1):
  if energy>=5:
    chance=90
  elif energy==4:
    chance=60
  elif energy==3:
    chance=50
  elif energy==2:
    chance=40
  elif energy==1:
    chance=20
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💀Голодный Паук доедает ослабевшего '+target['name']+'!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=5
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          x=random.randint(1,100)
          stun=0
          if x<=50:
                stun=1
          games[id]['res']+='🕷'+bot1['name']+' кусает '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          if stun==1:
                games[id]['res']+='🤢Цель поражена ядом! Её энергия снижена на 2.'
                target['energy']-=2
          target['takendmg']+=damage
          bot1['energy']-=5
        
    else:
        games[id]['res']+='💨'+bot1['name']+' промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=5
    
              


      
      
def attack(bot, id):
  a=[]
  if 0 not in games[id]['bots']:
    if bot['id']!=0:
      for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']==0:
            a.append(games[id]['bots'][bots])
    else:
         for bots in games[id]['bots']:
            if games[id]['bots'][bots]['id']!=0:
               a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    dd=0
    while a[x-1]['die']==1 and dd<100:
       x=random.randint(1,len(a))
       dd+=1
    if a[x-1]['id']!=0:
      target=games[id]['bots'][a[x-1]['id']]
    else:
      target=games[id]['bots'][a[x-1]['code']]
    if bot['target']!=None:
        target=bot['target']
    bot['target']=target
    x=random.randint(1,100)
  
  x=random.randint(1,100)

  if bot['weapon']=='rock':
      rockchance(bot['energy'], target, x, id, bot)          
      
  elif bot['weapon']=='hand':
      handchance(bot['energy'], target, x, id, bot)          

  
  elif bot['weapon']=='ak':
      akchance(bot['energy'], target, x, id, bot)  

  elif bot['weapon']=='saw':
      sawchance(bot['energy'], target, x, id, bot)
      
  elif bot['weapon']=='kinzhal':
    kinzhalchance(bot['energy'], target, x, id, bot)

  elif bot['weapon']=='light':
    lightchance(bot['energy'], target, x, id, bot)
   
  elif bot['weapon']=='bite':
    bitechance(bot['energy'], target, x, id, bot)
                                     

def yvorot(bot, id):
  if 'shieldgen' in bot['skills'] and bot['shieldgen']<=0:
       games[id]['res']+='🛡'+bot['name']+' использует щит. Урон заблокирован!\n'
       bot['shield']=1
       bot['shieldgen']=6
  else:
       bot['miss']=+30
       bot['yvorotkd']=7
       games[id]['res']+='💨'+bot['name']+' Уворачивается!\n'
    

def reload(bot2, id):
   bot2['energy']=bot2['maxenergy']
   games[id]['res']+='🕓'+bot2['name']+' Перезаряжается. Энергия восстановлена до '+str(bot2['maxenergy'])+'!\n'
    
def skill(bot,id):
  i=0
  skills=[]
  a=[]
  if 0 not in games[id]['bots']:
      if bot['id']!=0:
         for bots in games[id]['bots']:
            if games[id]['bots'][bots]['id']==0:
               a.append(games[id]['bots'][bots])
      else:
         for bots in games[id]['bots']:
            if games[id]['bots'][bots]['id']!=0:
               a.append(games[id]['bots'][bots])
      x=random.randint(1,len(a))
      if bot['mainskill']==[]:
        while a[x-1]['die']==1:
            print('while1')
            x=random.randint(1,len(a))
      elif 'gipnoz' in bot['mainskill']:
       for ii in games[id]['bots']:
              if games[id]['bots'][ii]['energy']>=3:
                  yes=1
       x=random.randint(1,len(a))
       if yes==1:
        zz=[]
        live=0
        for ids in a:
            if ids['die']!=1:
               zz.append(ids)
               live=1
        if live==1:
          dd=0
          x=random.randint(1, len(zz))
          while zz[x-1]['energy']<=2 and dd<100:
                print('while2')
                x=random.randint(1,len(zz))
                dd+=1
       else:
         bot.send_message(id, '@Loshadkin, баг с гипнозом, приди!')

      target=games[id]['bots'][a[x-1]['id']]
   
  else:    
    target=games[id]['bots'][0]
  for item in bot['skills']:
      skills.append(item)
  if bot['mainskill']==[]:
      choice=random.choice(skills)
  else:       
      choice=random.choice(bot['mainskill'])
  if choice=='medic':
       if bot['heal']<=0:
         a=random.randint(1,100)
         if a<60:
           bot['heal']=10
           bot['hp']+=1
           bot['energy']=0
           games[id]['res']+='⛑'+bot['name']+' восстанавливает себе ❤️хп!\n'
           i=1
         else:
              games[id]['res']+='⛑Медику '+bot['name']+' не удалось восстановить хп!\n'
              bot['heal']=10
               
  elif choice=='gipnoz':
             games[id]['res']+='👁‍🗨'+bot['name']+' использует гипноз на '+target['name']+'!\n'
             target['target']=target
             bot['energy']-=1
             bot['gipnoz']=6
             i=1
              
            
                       
            
    
    

def item(bot, id):
  if 0 not in games[id]['bots']:
    a=[]
    if bot['id']!=0:
      for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']==0 and games[id]['bots'][bots]['die']!=1:
            a.append(games[id]['bots'][bots])
    else:
      for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=0 and games[id]['bots'][bots]['die']!=1:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    if bot['mainitem']==[]:
        dd=0
        while a[x-1]['die']==1 and dd<100:
            print('while4')
            dd+=1
            x=random.randint(1,len(a))
    else:
        livex=0
        if 'flash' in bot['mainitem']:
          yes=0
          for ii in games[id]['bots']:
             if games[id]['bots'][ii]['energy']>=3 and games[id]['bots'][ii]['die']!=1:
                  yes=1
          if yes==1:        
            dd=0
            x=random.randint(1, len(a))
            while a[x-1]['energy']<=2 and a[x-1]['die']==1 and dd<=100:
                print('while5')
                x=random.randint(1,len(a))
                dd+=1
            livex=1
          else:
         
              while a[x-1]['die']==1:
                  print('while6')
                  x=random.randint(1,len(a))
    target=games[id]['bots'][a[x-1]['id']]
    if bot['target']!=None:
        target=bot['target']
    bot['target']=target                                            
  else:
    target=games[id]['bots'][0]
  x=[]
  i=1
  for items in bot['items']:
      x.append(items)
  if bot['mainitem']==[]:
    z=random.choice(x)
  else:
    z=random.choice(bot['mainitem'])
  if z=='flash':
          games[id]['res']+='🏮'+bot['name']+' Кидает флешку в '+target['name']+'!\n'
          target['energy']=0
          bot['items'].remove('flash')
          bot['target']=None

  elif z=='knife':
          x=random.randint(1,100)
          bot['energy']-=2
          z=random.randint(1, len(a))
          ddd=0
          while a[z-1]['die']==1 and ddd<100:
            z=random.randint(1,len(a))
            ddd+=1
          if x>target['miss']:
              games[id]['res']+='🔪'+bot['name']+' Кидает нож в '+target['name']+'! Нанесено 3 урона.\n'
              target['takendmg']+=3
              bot['items'].remove('knife')
          else:
            games[id]['res']+='💨'+bot['name']+' Не попадает ножом в '+target['name']+'!\n'
            bot['items'].remove('knife')

        
        
              
                
                
                
    

    

def actnumber(bot, id):  
  a=[]
  npc=games[id]['bots'][bot]
  if npc['energy']>0 and npc['energy']<=2:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
     if x<=20:
       attack=1
     else:
       attack=0
    else:
     if npc['accuracy']>=-5:
      if x<=75:
        attack=1
      else:
        attack=0
     else:
       if x<=30:
         attack=1
       else:
         attack=0
  elif npc['energy']>=3:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
      if x<=75:
        attack=1
      else:
        attack=0
    else:
      attack=1
  else:
    attack=0
    
  x=random.randint(1,100)  
  low=0
  enemy=[]
  if npc['id']!=0:
      for mob in games[id]['bots']:
              if games[id]['bots'][mob]['id']==0:
                     enemy.append(games[id]['bots'][mob])
  else:
     for mob in games[id]['bots']:
              if games[id]['bots'][mob]['id']!=0:
                     enemy.append(games[id]['bots'][mob])
  for mob in enemy:
   if mob['energy']<=2 or mob['stun']>0 or mob['die']==1:
    low+=1
  if low>=len(enemy):
   yvorot=0
  else:
   if npc['energy']<=2:
    if x<=50 and npc['yvorotkd']<=0:
      yvorot=1
    else:
      yvorot=0
   elif npc['energy']>=3:
      x=random.randint(1,100)
      if x<=25 and npc['yvorotkd']<=0:
        yvorot=1
      else:
        yvorot=0
   if 'shieldgen' in npc['skills'] and npc['shieldgen']<=0 and low<len(enemy):
      yvorot=1
        
  x=random.randint(1,100)
  if len(npc['skills'])>0 and 'active' in npc['skills']:
    if 'gipnoz' in npc['skills'] and npc['gipnoz']<=0:
        if low==len(enemy):
           gipn=0
        else:
            gipn=1
            npc['mainskill'].append('gipnoz')
            skill=1
    else:
        gipn=0
    if gipn==0:
        skill=0
    else:
        skill=1       
  else:
    skill=0
  if 'medic' in npc['skills'] and npc['heal']<=0:
      skill=1
      npc['mainskill'].append('medic')
        
  if len(npc['items'])>0:
    knife=0
    flash=0
    if 'flash' in npc['items']:
        if low>=len(enemy):
            flash=0
        else:
            flash=1
            npc['mainitem'].append('flash')
    if 'knife' in npc['items'] and npc['energy']>=2:
        knife=1
        npc['mainitem'].append('knife')
    if knife==1 or flash==1:      
        x=random.randint(1,100)
        if x<=50:
            item=1
        else:
            item=0
    else:
       item=0
  else:
    item=0
  reload=0
  if attack==0 and yvorot==0 and item==0 and skill==0:
    if npc['energy']>=3:
      attack=1
    else:
      reload=1
  else:
    reload=0
    
  return{'attack':{'name':'attack', 'x':attack}, 'yvorot':{'name':'yvorot', 'x':yvorot}, 'item':{'name':'item', 'x':item}, 'reload':{'name':'reload', 'x':reload},'skill':{'name':'skill', 'x':skill}}
         
      
      
 

def act(bot, id):
  actions=actnumber(bot, id)
  curact=[]
  for item in actions:
    if actions[item]['x']==1:
      curact.append(actions[item]['name'])
  x=random.randint(1, len(curact))
  return curact[x-1]
  


@bot.message_handler(commands=['help'])
def helpp(m):
  if m.from_user.id==m.chat.id:
    bot.send_message(m.chat.id, '''Игра "CookieWars". Главная суть игры в том, что вам в процессе игры делать ничего не надо - боец сам 
выбирает оптимальные действия. Вы только должны будете экипировать ему скиллы и оружие, и отправить в бой.\n\n
*Как отправить бойца на арену?*\nДля этого надо начать игру в чате @cookiewarsru, нажав команду /begin. После этого другие игроки жмут 
кнопку "Присоединиться", которая появится после начала игры в чате, пуская своих бойцов на арену. Когда все желающие присоединятся, 
кто-то должен будет нажать команду /go, и игра начнётся. Если в игре участвует больше, чем 2 бойца, они сами будут решать, какую 
цель атаковать.\n\n*Теперь про самого бойца.*\nКаждый боец имеет следующие характеристики:\nЗдоровье\nЭнергия\nОружие\nСкиллы
Скин\n\nТеперь обо всём по порядку.\n*Здоровье* - показатель количества жизней бойца. Стандартно у всех 4 жизни, но с помощью 
скиллов можно увеличить этот предел. Потеря здоровья происходит по такому принципу: кто за ход получил урона больше остальных, тот и теряет жизни. 
Если несколько бойцов получили одинаково много урона, то все они потеряют здоровье. Сколько единиц - зависит от принятого урона.
Стандартно, за каждые 6 единиц урона по бойцу он теряет дополнительную жизнь. То есть, получив 1-5 урона, боец потеряет 1 хп. Но получив 6 урона, 
боец потеряет 2 хп, а получив 12 - 3. Предел урона можно увеличить с помощью скиллов. Разберём пример:\n
Боец Вася, Петя и Игорь бьют друг друга. Вася нанёс Пете 3 урона, Петя нанёс Васе 2 урона, а Игорь нанёс 3 урона Васе. Считаем полученный бойцами урон:\n
Вася: 5\nПетя:3\nИгорь:0\nВ итоге Вася потеряет 1 хп, а остальные не потеряют ничего, кроме потраченной на атаку энергии. Об этом позже.\n
*Энергия*\nПочти на каждое действие бойцы тратят энергию. Стандартно её у всех по 5 единиц. Каждое оружие тратит определённое количество 
энергии за атаку, некоторые скиллы тоже. Чем меньше энергии в данный момент, тем меньше шанс промахнуться по врагу. Иногда боец должен 
тратить ход на перезарядку, восстанавливая всю энергию.\n
*Оружие*\nКаждое оружие в игре уникально и имеет свои особенности. Про них можно узнать в Траг боте, выбивая оружие из лутбоксов.\n
*Скиллы* - Важная часть игры. За заработанные в боях или выбитые в Траг ⚛️поинты вы можете приобрести полезные скиллы для вашего бойца. О них в /upgrade.
Но купить скилл мало - его надо *экипировать*. Делается это командой /inventory. Максимум можно надеть на себя 2 скилла.\n
*Скины*\nСкины - личность вашего бойца, дающая дополнительную способность, не конкурирующую со скиллами. Подробнее: /upgrade.\n
Зовите друзей, выпускайте бойцов на арену - и наслаждайтесь зрелищем!
''', parse_mode='markdown')
  else:
      bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')
       
       
@bot.message_handler(commands=['start'])
def start(m):
  x=m.text.split('/start')
  print(x)
  try:
     if int(x[1]) in games:
      if games[int(x[1])]['started']==0:
        y=users.find_one({'id':m.from_user.id})
        if y!=None:
         if y['bot']['id'] not in games[int(x[1])]['ids']:
          if y['bot']['name']!=None:
           if games[int(x[1])]['started']==0:
            games[int(x[1])]['bots'].update(createbott(m.from_user.id, y['bot']))
            games[int(x[1])]['players']+=1
            users.update_one({'id':m.from_user.id}, {'$set':{'name':m.from_user.first_name}})
            bot.send_message(m.chat.id, 'Вы присоединились! Игра начнётся в чате, когда кто-нибудь нажмёт /go.')
            bot.send_message(int(x[1]), m.from_user.first_name+' (боец '+y['bot']['name']+') присоединился!')
            games[int(x[1])]['ids'].append(m.from_user.id)
          else:
             bot.send_message(m.chat.id, 'Сначала назовите своего бойца! (команда /name).')
  except:
        pass
  if users.find_one({'id':m.from_user.id})==None:
        try:
            bot.send_message(m.from_user.id, 'Здраствуйте, вы попали в игру "CookieWars"! Вам был выдан начальный персонаж. В будущем вы можете улучшить его за куки! Подробнее об игре можно узнать с помощью команды /help.')
            users.insert_one(createuser(m.from_user.id, m.from_user.username, m.from_user.first_name))
        except:
            bot.send_message(m.chat.id, 'Напишите боту в личку!')
        x=users.find({})
        z=m.text.split('/start')
        print(z)
        i=0
        for ids in x:
            if ids['id']==int(z[1]):
               i=1
        if i==1:
           print('i=1')
           users.update_one({'id':int(z[1])}, {'$push':{'referals':m.from_user.id}})
           users.update_one({'id':m.from_user.id}, {'$set':{'inviter':int(z[1])}})
           try:
             bot.send_message(int(z[1]), 'По вашей ссылке зашёл пользователь '+m.from_user.first_name+'! По мере достижения им званий вы будете получать за него бонус - половину от его награды за звание.')
           except:
             pass
    
  
def createmonsters(id, name):
   i=1
   if name=='drakozavrik':
      z=[]
      while i<4:
         x=random.randint(1,10000)
         while x in z:
            x=random.randint(1,10000)
         word=str(x)
         code=''
         for ids in word:
            if ids=='0':
               code+='a'
            if ids=='1':
               code+='b'
            if ids=='2':
               code+='c'
            if ids=='3':
               code+='d'
            if ids=='4':
               code+='e'
            if ids=='5':
               code+='f'
            if ids=='6':
               code+='g'
            if ids=='7':
               code+='h'
            if ids=='8':
               code+='i'
            if ids=='9':
               code+='g'
         name2='Дракозаврик '+str(i)
         print(code)
         games[id]['bots'].update(createdrakozavrik(code, name2))
         games[id]['enemies']+=1
         i+=1
         
def createdrakozavrik(code, name):
   return {code:{'name': name,
              'code':code,
              'weapon':'hand',
              'skills':[],
              'team':None,
              'hp':2,
              'maxhp':0,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':0,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':3,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'rank':0,
              'mainskill':[],
              'mainitem':[],
              'weapons':['hand'],
              'gipnoz':0
}}
                                  
                                  
                                  

@bot.message_handler(commands=['go'])
def goo(m):
    if m.chat.id in games:
        if len(games[m.chat.id]['bots'])>=1:
         if games[m.chat.id]['started']==0:
           monsters=['drakozavrik']
           x=random.choice(monsters)
           createmonsters(m.chat.id, x)
           begingame(m.chat.id)
           games[m.chat.id]['started']=1
        else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
    

@bot.message_handler(commands=['begin'])
def begin(m):
  if m.chat.id==-229396706:
     if m.chat.id not in games:
        games.update(creategame(m.chat.id))
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Присоединиться', url='telegram.me/cookietestsbot?start='+str(m.chat.id)))
        bot.send_message(m.chat.id, 'Игра началась!\n\n', reply_markup=kb)
        x=users.find({})
        if m.chat.id==-1001208357368:
         text=''
         for ids in x:
          if ids['id']!=0:
            if ids['enablejoin']==1 and ids['joinbots']>0:
               games[m.chat.id]['bots'].update(createbott(ids['id'], ids['bot']))
               games[m.chat.id]['ids'].append(ids['id'])
               users.update_one({'id':ids['id']}, {'$inc':{'joinbots':-1}})
               text+=ids['name']+' (боец '+ids['bot']['name']+') присоединился! (🤖Автоджоин)\n'
         bot.send_message(m.chat.id, text)
         x=users.find({})
         for idss in x:
          if idss['id']!=0:
            if idss['ping']==1:
              
               try:
                  bot.send_message(idss['id'], 'В чате @cookiewarsru началась игра!') 
               except:
                  pass
               
        if m.chat.id!=-1001208357368:
         bot.send_message(441399484, 'Где-то началась игра!')
             
   
   
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)        
        

def begingame(id):
 if games[id]['started2']!=1:
    spisok=['kinzhal','rock', 'hand', 'ak', 'saw']
    for ids in games[id]['bots']:
        if games[id]['bots'][ids]['weapon']==None:
            games[id]['bots'][ids]['weapon']='hand'
        active=['shieldgen', 'medic', 'gipnoz']
        yes=0
        for i in active:
            if i in games[id]['bots'][ids]['skills']:
                yes=1  
        if yes==1:
              games[id]['bots'][ids]['skills'].append('active')
        if 'cube' in games[id]['bots'][ids]['skills']:
            a=['medic', 'liveful', 'dvuzhil', 'pricel', 'cazn', 'berserk', 'zombie', 'gipnoz', 'paukovod', 'vampire', 'zeus', 'nindza']
            z=(random.choice(a))
            while z in games[id]['bots'][ids]['skills']:
               z=(random.choice(a))
            games[id]['bots'][ids]['skills'].append(z)
        if 'liveful' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=2
            games[id]['bots'][ids]['accuracy']-=15
        if 'dvuzhil' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=0
            games[id]['bots'][ids]['damagelimit']+=3
        if 'medic' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['heal']=9
        if 'pricel' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['accuracy']+=15
        if 'paukovod' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']-=2
        if 'nindza' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['miss']+=20
        games[id]['bots'][ids]['maxhp']=games[id]['bots'][ids]['hp']
        if 'robot' in games[id]['bots'][ids]['skin']:
            games[id]['bots'][ids]['maxenergy']+=1
    text=''
    
    for ids in games[id]['bots']: 
        randomm=0
        text+=games[id]['bots'][ids]['name']+':\n'
        for skill in games[id]['bots'][ids]['skills']:
          if randomm==0:
            bots=games[id]['bots'][ids]
            if skill!='cube' and skill!='active':
                text+=skilltoname(skill)+'\n'
            else:
                if skill!='active':
                    randomm=bots['skills'][len(bots['skills'])-1]
                    text+=skilltoname(skill)+'('+skilltoname(bots['skills'][len(bots['skills'])-1])+')\n'
          else:
              if skill!=randomm and skill!='active':
                    text+=skilltoname(skill)+'\n'
        text+='\n'
    bot.send_message(id, 'Экипированные скиллы:\n\n'+text)
    giveitems(games[id])
    games[id]['started2']=1
    battle(id)
 else:
   pass

def skilltoname(x):
    if x=='shieldgen':
        return 'Генератор щитов'
    elif x=='medic':
        return 'Медик'
    elif x=='liveful':
        return 'Живучий'
    elif x=='dvuzhil':
        return 'Стойкий'
    elif x=='pricel':
        return 'Прицел'
    elif x=='cazn':
        return 'Ассасин'
    elif x=='berserk':
        return 'Берсерк'
    elif x=='zombie':
        return 'Зомби'
    elif x=='gipnoz':
        return 'Гипнотизёр'
    elif x=='cube':
       return 'Куб рандома'
    elif x=='paukovod':
       return 'Пауковод'
    elif x=='vampire':
       return 'Вампир'
    elif x=='zeus':
       return 'Зевс'
    elif x=='nindza':
       return 'Ниндзя'
    elif x=='bloodmage':
       return 'Маг крови'

 
def createbott(id, y):
        return{id:y}

def createuser(id, username, name):
    return{'id':id,
           'bot':createbot(id),
           'username':username,
           'name':name,
           'cookie':0,
           'cookiecoef':0.10,
           'joinbots':0,
           'enablejoin':0,
           'currentjoinbots':0,
           'dailybox':1,
           'games':0,
           'ping':0,
           'referals':[],
           'inviter':None,
           'prize1':0,
           'prize2':0,
           'prize3':0,
           'prize4':0,
           'prize5':0,
           'prize6':0,
           'prize7':0
          }
    
        
def creategame(id):
    return {id:{
        'chatid':id,
        'ids':[],
        'bots':{},
        'results':'',
        'secondres':'',
        'res':'',
        'started':0,
        'xod':1,
        'started2':0,
        'dung':0,
        'enemies':0,
        'players':0
        
             }
           }
   
            
def createbot(id):
  return {'name': None,
              'weapon':'hand',
              'skills':[],
              'team':None,
              'hp':4,
              'maxhp':0,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':id,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':6,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'rank':0,
              'mainskill':[],
              'mainitem':[],
              'weapons':['hand'],
              'gipnoz':0
}

  



  
if True:
 try:
   print('7777')
   bot.polling(none_stop=True,timeout=600)
 except (requests.ReadTimeout):
        print('!!! READTIME OUT !!!')           
        bot.stop_polling()
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except (requests.exceptions.ConnectionError):
            time.sleep(1)
   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(0.1)
