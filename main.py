import time 
from playsound import playsound 


mins = 25
break_time = 5
set = 0

while True:
    set +=1
    mins = 25
    time.sleep(3)
    playsound("Study_Timer/bell.mp3")
    #Ders Sayacı
    while mins != 0:
        print("{}. Ders Bitimine Kalan Süre: {} dakika".format(set,mins))
        time.sleep(60)
        mins -=1
    playsound("Study_Timer/bell.mp3")
    #Mola Sayacı
    if(set%4 == 0):
        break_time = 30
        playsound("Study_Timer/bell.mp3")
    else:
        break_time = 5
    while break_time != 0:
        print("{}. Mola Bitimine Kalan Süre: {} dakika".format(set,break_time))
        time.sleep(60)
        break_time = -1

    playsound("Study_Timer/bell.mp3")
    
    devam_mi = input("Tamam mı Devam mı ? (T/D): ")
    devam_mi.upper()
    if(devam_mi == 'T'):
        break
    elif(devam_mi =='D'):
        playsound("Study_Timer/bell.mp3")
        print("Diğer Set'e geçiliyor")
