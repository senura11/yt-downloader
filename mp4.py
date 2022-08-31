def mp4():
    import time,pytube,os
    text=input('\033[1;35;40menter youtube link or text : ')
    time.sleep(0.2)
    try:
        search=pytube.Search(text)
        watch_url=search.results[0].watch_url
    except:
        print('\033[1;31;40mcheck your internet connection and try again...')
        exit()
    mp4=pytube.YouTube(watch_url)
    dmp4=mp4.streams.get_audio_only('mp4')
    os.system('termux-setup-storage')
    os.chdir('/sdcard')#path
    if 'yt-music' in os.listdir():#path
        None
    else:
        os.mkdir('yt-music')#path
    print('\033[1;31;40mdownloading your audio - '+str(mp4.title))
    path='/sdcard/yt-music'#path
    dmp4.download(path)
    print('your audio download complete...')
    print('your audio saved ',path)
if __name__=='__main__':
    mp4()
