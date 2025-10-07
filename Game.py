# Sambungkan modul yang kamu butuhkan
from turtle import *
from time import sleep
from random import randint
# Buat objek "kura-kura", pasang bentuk, warna, dan kecepatan
t = Turtle()
t.color('red')
w = 200
h = 150
v = 100
t.poin = 0
t.penup()
t.shape('turtle')
t.speed(v)
# Buat fungsi gerak_acak() untuk menggerak kura-kura ke titik acak
def gerak_acak():
    t.goto(randint(-w,w),(randint(-h,h)))
# Buat fungsi penanganan tangkap(x, y) yang akan menangani klik di kura-kura
def tangkap(x, y):
    t.write('A!', font=('Arial', 14,'normal'))
    t.poin += 1
    gerak_acak()
# (klik berurutan akan terkumpul di properti t.poin)
# Buat langganan ke event «click on the turtle»
t.onclick(tangkap)
# Buat loop yang berjalan selama klik di t.poin di bawah 3
while t.poin < 3:
    sleep(1.5)
    gerak_acak()
t.write('WOW!', font=('Arial', 16,'Bold'))
t.hideturtle()