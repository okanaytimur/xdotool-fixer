import os
import subprocess

def desktop():
    komut="xdotool search --onlyvisible 'Masaüstü'"
    altkomut=subprocess.run(komut, stdout=subprocess.PIPE, shell=True)
    sonuc=altkomut.stdout.strip().decode('ascii')
    for i in sonuc.split("\n"):
        return i
   
def aktifpencereler():
    komut="xdotool getactivewindow"
    altkomut=subprocess.run(komut, stdout=subprocess.PIPE, shell=True)
    sonuc=altkomut.stdout.strip().decode('ascii')
    for i in sonuc.split("\n"):
        return i
    
if not desktop()==aktifpencereler():
    os.system("xdotool windowminimize "+aktifpencereler())
 

