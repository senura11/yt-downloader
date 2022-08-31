def video():
    import os,time,pytube
    text=input('\033[1;35;40menter youtube link or text : ')
    time.sleep(0.2)
    try:
     search=pytube.Search(text)
     watch_url=search.results[0].watch_url
    except:
        print('\033[1;31;40munknown error --- please check your internet connection and and tool run again.....')
        
    video=pytube.YouTube(watch_url)
    os.system('clear')
    print('------------- video quality --------------')
    videod=video.streams.all()
    qv=list(enumerate(videod))
    for i,j in qv:
        if i==13:
            break
        print(str([i]),'---',j.resolution)
    print()
    cho=int(input('Enter No : '))
    os.system('termux-setup-storage')
    os.chdir('/sdcard')#path
    if 'yt-music' in os.listdir():#path
        None
    else:
        os.mkdir('yt-music')#path
    print('\033[1;31;40mdownloading your video - ',video.title)
    path='/sdcard/yt-music'
    videod[cho].download(path)
    print('your video download complete...')
    print('your video saved ',path)
if __name__=='__main__':
    video()
