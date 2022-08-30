import mp4
import video
import os
import sys
import time
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet ')
    import pyfiglet

os.system('clear')#os command
words = "\033[1;31;40mThis tool by dark devil \n"
for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(0.2)
os.system('clear')#os command
print('\n','\n')
time.sleep(0.2) 
banner=pyfiglet.Figlet('banner')
banner=banner.renderText('yt-down')
print('\033[1;32;40m'+str(banner)+'\033[1;34;40m')
print('       Tool by dark devil     ')
print('\n\n')
print('\033[1;33;40m[1] \033[1;31;40mstart                      \033[1;33;40m[2] \033[1;31;40mupdate tool')
print()
choice=input('\033[1;34;40menter your choice : ')
if choice=='1' or choice=='start':
    os.system('clear')#os command
    try:
        import pytube
    except:
        os.system('pip install pytube')
        import pytube
    print('\033[1;33;40m[1] \033[1;31;40mmp4                    \033[1;33;40m[2] \033[1;31;40mvideo') 
    print()
    choice=input('\033[1;34;40menter your choice : ')
    os.system('clear')#os command
    #mp4 download
    if choice=='1' or choice=='mp4':
        mp4.mp4()
        
     #video download
    elif choice=='2' or choice=='video':
        video.video()

        
        
        
        
        
