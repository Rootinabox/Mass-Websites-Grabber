import requests,random,re,os,time,sys
import colorama
import threading
from colorama import *
from threading import Thread

try:
 os.system("title @rootinabox Grabber | More : t.me/Rootinabox_Channel ")
except:pass
init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN

try:
    if os.name == 'nt':os.system('cls')
    else:os.system('clear')
except:
        pass
        
try:
    import requests
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install requests')
    print('   [-] you need to install requests Module')
    sys.exit()

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
 

  _____             _   _             _               
 |  __ \           | | (_)           | |              
 | |__) |___   ___ | |_ _ _ __   __ _| |__   _____  __
 |  _  // _ \ / _ \| __| | '_ \ / _` | '_ \ / _ \ \/ /
 | | \ \ (_) | (_) | |_| | | | | (_| | |_) | (_) >  < 
 |_|  \_\___/ \___/ \__|_|_| |_|\__,_|_.__/ \___/_/\_\
                                                      
                                                             
 Websites Grabber V1.0    |   Priv8 method    | |  Coded by Rootinabox                           
                 Greetz to : Bajatax         
                      
 [+] Telegram : @rootinabox
 [+] Channel  : https://t.me/Rootinabox_Channel

+-------- With Great Power Comes Great Responsibilities! --------+

			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


logo()

old_ip=[]
old_website=[]
total=0
total_f=0
f=0
total_f2=0
f2=0

def generat_ip():
   global old_ip
   while True:
     ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(2))))
     try:
      if ip in open('list_ip.txt','r').read():
         continue
     except:
        pass
     if ip not in old_ip:
        old_ip.append(ip)
        open('list_ip.txt','a').write(ip+'\n')
        break
   return ip
def subnet(i,n='y'):
   i=int(i)
   if n=='y':
      start=23
   else:
      start=15
   if i<128:
      return '/'+str(start+1)
   if i<192:
      return '/'+str(start+2)
   if i<224:
      return '/'+str(start+3)
   if i<240:
      return '/'+str(start+4)
   if i<248:
      return '/'+str(start+5)
   if i<252:
      return '/'+str(start+6)
   if i<254:
      return '/'+str(start+7)
   if i<255:
      return '/'+str(start+8)
   else:
      return False
def for_by_rang(rang):
    if rang=='/16':
       return [range(0,256),range(0,256)]
    elif rang=='/17':
       return [range(128,256),range(0,256)]
    elif rang=='/18':
       return [range(192,256),range(0,256)]
    elif rang=='/19':
       return [range(224,256),range(0,256)]
    elif rang=='/20':
       return [range(240,256),range(0,256)]
    elif rang=='/21':
       return [range(248,256),range(0,256)]
    elif rang=='/22':
       return [range(252,256),range(0,256)]
    elif rang=='/23':
       return [range(254,256),range(0,256)]
    elif rang=='/24':
       return [range(1),range(0,256)]
    elif rang=='/25':
       return [range(1),range(128,256)]
    elif rang=='/26':
       return [range(1),range(192,256)]
    elif rang=='/27':
       return [range(1),range(224,256)]
    elif rang=='/28':
       return [range(1),range(240,256)]
    elif rang=='/29':
       return [range(1),range(248,256)]
    elif rang=='/30':
       return [range(1),range(252,256)]
    elif rang=='/31':
       return [range(1),range(254,256)]
    return False
def next_range(i,y):
   if y!=255:
        this_rang=subnet(y)
        next_rang=subnet(y+1)
        if this_rang!=next_rang and next_rang!=False:
           return next_rang
        else:
           return False
   elif i!=255:
        this_rang=subnet(i,'i')
        next_rang=subnet(i+1,'i')
        if this_rang!=next_rang and next_rang!=False:
           return next_rang
        else:
           return False
   return False
def reverse_ip_random():
   global old_ip,old_website,total,total_f,f,total_f2,f2
   while True:
    try:
     ip2=generat_ip()
     ip=ip2+'.0.0'
     rang='/16'
     last_global_rang=[]
     last_global_rang.append(rang)
     ip_range_old=False
     while True:
      print('scan ->'+ip+rang)
      if ip+rang==ip_range_old:
          iplast22=ip_range_old.split('.')[-1].split('/')[0]
          iplast[0]=int(iplast22)
      re1=requests.get('https://sonar.omnisint.io/reverse/'+ip+rang)
      ip_range_old=ip+rang
      if '{"error":"no results found"}' in str(re1.content):
           print('[0] No Rsult '+ip)
           if rang=='/16':
              break
           else:
              if iplast[0]+1==255:
                 break
              rang="/24"
              print('iplast : '+str(iplast[0]))

              i_last=iplast[0]+1                  
              iplast=[i_last,0]
              ip=ip2+'.'+str(iplast[0]+1)+'.0'
              continue
      result=re1.json()
      print('[+] Fond '+str(len(result))+' Ip Work')
      total_this=0
      rang_boucl=for_by_rang(rang)
      if rang_boucl[0]==range(1):
         i_start=range(i_last,i_last+1)
      else:
         i_start=rang_boucl[0]
      for i in i_start:
       for y in rang_boucl[1]:
        try:
            ip_one=ip2+'.'+str(i)+'.'+str(y)
            nm=len(result[ip_one])
            total+=nm
            total_this+=nm
            if nm>0:
               iplast=[i,y,ip2]
            print('[+] '+ip_one+' FOND '+str(nm)+' Website')
            try:
               if total_f2>=10000000:
                      f2+=1
                      total_f2=0
               total_f2+=nm
               open('all_info/'+str(f2)+'.txt','a').write('\n'.join(result[ip_one])+'\n')
            except:
               pass
            
            domaine=re.findall('(?P<domain>[a-z0-9][a-z0-9\-]{1,63}\.[a-z\.]{2,6}),',','.join(result[ip_one])+',')
            domaine=set(domaine)
            if len(domaine)==0:
                   continue
            if total_f>=10000000:
                      f+=1
                      total_f=0
            open(str(f)+'.txt','a').write('\n'.join(domaine)+'\n')
            total_f+=len(domaine)
            if total_this>=99900:
               break
        except Exception as E:
             pass
      print('[+] Total Last ip '+str(total_this))
      print('[+] Total website '+str(total))
      print('[+] Range '+str(rang))
      if total_this<99900 and i==255 and y==255:
          break
      elif total_this<99900:
          check_next_range=next_range(iplast[0],255)
          if check_next_range!=False and check_next_range not in last_global_rang:
             last_global_rang.append(check_next_range)
             rang=check_next_range
          else:
             rang="/24"
          i_last=iplast[0]+1
          ip=ip2+'.'+str(iplast[0]+1)+'.0'
          continue
      sort=False
      i=iplast[0]
      first_max=False
      for y in range(iplast[1],255):
         try:
            ip_one=ip2+'.'+str(i)+'.'+str(y)
            re1=requests.get('https://sonar.omnisint.io/reverse/'+ip_one)
            if '{"error":"no results found"}' in str(re1.content):
              print('[0] No Rsult '+ip_one+'.0')
              continue
            result=re1.json()
            total_this+=len(result)
            total+=len(result)
            if first_max==False and len(result)<70000:
                   if y+1!=255:
                      rang=subnet(y+1)
                   else:
                      rang=subnet(i+1,'i')
                   sort=True
                   last_Y=y
            first_max=True
            if len(result)==100000:
               print('[++] best IP Added : '+ip_one)
               open('best_ip.txt','a').write(ip_one+'\n')
            print('[+]2 '+ip_one+' FOND '+str(len(result))+' Website')
            try:
               if total_f2>=10000000:
                      f2+=1
                      total_f2=0
               total_f2+=total_this
               open('all_info/'+str(f2)+'.txt','a').write('\n'.join(result)+'\n')
            except:
               pass
            domaine=re.findall('(?P<domain>[a-z0-9][a-z0-9\-]{1,63}\.[a-z\.]{2,6}),',','.join(result)+',')
            domaine=set(domaine)
            if len(domaine)==0:
                   continue
            if total_f>=10000000:
                      f+=1
                      total_f=0
            open(str(f)+'.txt','a').write('\n'.join(domaine)+'\n')
            total_f+=len(domaine)
            check_next_range=next_range(i,y)
            if check_next_range!=False:
                   rang=check_next_range
                   sort=True
                   last_Y=y
            if sort==True:
                break
         except:
            pass
      print('[+] Total Last ip '+str(total_this))
      print('[+] Total website '+str(total))
      i_last=iplast[0]+1
      if i==255 and y==255:
            break
      if sort==False:
          ip=ip2+'.'+str(iplast[0]+1)+'.0'
          rang="/24"
      elif sort==True:
          ip=ip2+'.'+str(iplast[0]+1)+'.'+str(last_Y+1)
    except Exception as E:
       print(E)
speed=input('Choose your speed : ')
thrd={}
for spd in range(int(speed)):
   print('Start thread Num :'+str(spd))
   thrd[spd]=Thread(target = reverse_ip_random)
   thrd[spd].setDaemon(True)
   thrd[spd].start()
while True:
        time.sleep(10000)
print('Finish')