#a chainloader for e2dengine
import sys, os, random
sys.path.insert(0, 'engine2d')
from e2druntime import *


#initialize highscore
#reset highscore when starting up
f = open("assets/data/highscore.txt", "r+")
hs = int(f.readline())
f.seek(0)
f.truncate()
f.write(str('0'))
f.close()

print('-----------------------[q7engine chainloader]--------------------------')
print('launching flappybird')
print('q7e2d (questandachievementengine2d) based on opensource engine made by PopAdi and ramremo')
print('https://github.com/ramremo/Flappybird (ramremo repo)')
print('https://github.com/PopAdi/python-flappy-bird (PopAdi repo)')
print('q7e2d Alpha state Bug may happen')
print('developed by Rachel Hera and Wahyu Suryo Samudro')
print('https://github.com/rachelhera (Rachelhera repo)')
print('https://github.com/questandachievement (Samudro Repo)')
print('-----------------------------------------------------------------------')

main()
