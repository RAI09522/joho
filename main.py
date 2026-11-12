Ten = []
Ten[0][0] = 88
Ten[0][1] = 92
Ten[0][2] = 75
Ten[1][0] = 90
Ten[1][1] = 85
Ten[1][2] = 99

saikou = -1
kekka = 0
h = 0
while h < 6:
    g = 0
    while k <= 2:
        g = g + Ten[h][k]
    print(g)
    if g > saikou:
        saikou = g
        katta = h
print("勝ったのは",(katta+1),"人目")





