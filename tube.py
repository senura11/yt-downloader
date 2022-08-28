import os
import time
import platform
import termcolor
import sys
try:  
   import pytube
   import pyfiglet
except:
     os.system('pip install pytube')
     os.system('pip install pyfiglet')
     import pytube
     import pyfiglet
def yt(): 
 text=input("\033[1;31;40menter text = ")
 try:
   global inpu
   from pytube import Search
   time.sleep(0.2)
   s = Search(text)
   time.sleep(0.2)
   for i in s.results:
    inpu=i.watch_url
    print(inpu)
    t='main'
    if t==t:
      break
 except:
     print("\033[1;32;40mcheck your internet connection and try again")
     exit()
 v=pytube.YouTube(inpu)
 mode=input("\033[1;33;40menter your mode (mp4 or video) = ")
 if mode=='mp4':
  s=v.streams.get_audio_only('mp4')
  os.mkdir('/storage/emulated/0','yt-music')
  path='/storage/emulated/0/yt-music'
  print('downloading your audio -',v.title)
  s.download(path)
  print('your audio download complete... \n','audio saved in ',path)
 elif mode=='video':
    g=v.streams.get_highest_resolution()
    path2='/storage/emulated/0/yt-music'
    print('downloading your video ',v.title)
    g.download(path2)
    print('your video download complete..\n','video saved in ',path2)
 else:
    quit()
os.system('termux-setup-storage')
os.system('clear')
time.sleep(0.5)
words = "This tool written by senupama isuranda"
words=termcolor.colored(words,color='yellow')
for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print()
os.system('clear')
s=pyfiglet.Figlet()
t=s.renderText('yt-downloader')
print(termcolor.colored(t,color='green'))
time.sleep(0.1)
print()
time.sleep(0.5)
yt()
