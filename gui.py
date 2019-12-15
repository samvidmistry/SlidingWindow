import sys
import vlc
import easygui

if(len(sys.argv) < 2):
    print("Please enter file name as command line argument")
    exit(0)

media = vlc.MediaPlayer(sys.argv[1])
media.play()
while True:
    pass
