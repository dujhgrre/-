import random
zut = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
zur = int(input("нужная длина пароля"))
zud = ""
for i in range(zur):
    u = random.choice(zut)
    zud += u
print(zud)
