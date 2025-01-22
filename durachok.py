import time
ooo = 1
per = int(input("Взнос: "))
proc = int(input("Процент: "))

while True:
    ot1 = per // 100
    ot2 = ot1 * proc
    otv = ot2 + per

    print("Вы получите ", otv, "деняк за ", ooo, "лет")

    ooo = ooo + 1

    per = otv
    time.sleep(0.5)
