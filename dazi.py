import random
import os
import getch
zimu='abcdefghijklmnopqrstuvwyxyz'
while True:
    a=random.choice(zimu)
    print(a)
    b=getch.getch()
    os.system("clear")
    if(a==b):
        print("dui..",a)
    else:
        print("cuo..",a)
