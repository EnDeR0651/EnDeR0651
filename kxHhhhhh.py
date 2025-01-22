import random

ss = int(input("Напиши диапозон "))

ntg = random.randint(1, ss)

sch = 0

l = int(input("Напиши количество жизней "))

guess = None
print("Угадай число! ")

while guess != ntg:
    guess = int(input())
    if guess < ntg:
        print("Слишком мало! ")
    if guess > ntg:
        print("Слишком много! ")
    if guess != ntg:
        l = l - 1
    print("У вас", l, "жизней! ")

    sch = sch + 1

    if l <= 0:
        print("Вы проиграли")
        break

    if guess == ntg:
        print("Ты угадал число! ")
        print(ntg)
        print("Ты потратил на это", sch, "попыток! ")

