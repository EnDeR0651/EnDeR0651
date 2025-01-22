import time
print("Запуск цикла")

i = int(input())

while True:
    time.sleep(1)
    i -= 1
    print(i)
    if i == 0:
        break

print("Конец")

