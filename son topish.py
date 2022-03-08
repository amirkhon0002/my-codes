import random

def sontop(x = 10):
    tasodifiy_son = random.randint(1, x)
    print(f"1 dan {x} gacha son o'ylaganman, topa olasizmi? ")
    taxminlar = 0

    while True:
        taxminlar += 1
        taxmin = int(input(">>>>"))
        if taxmin < tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana urinib ko'ring: ")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana urinib ko'ring: ")
        else:
            break


    print(f"Tabriklaymiz, siz {taxminlar} ta urinishda to'g'ri topdingiz.")
    return taxminlar
print(sontop())

def sontop_pc(x = 10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing, Men uni topaman. ")
    quyi = 1
    yuqori = x
    taxminlar = 0

    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'ylagansiz:  to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta urinishda topdim!!!")
    return taxminlar
print(sontop_pc())
def play(x = 10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!!!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!!!")
        else:
            print("Durrang!!!")
        yana = int(input("Yana o'ynaysizmi: Ha(1)/ Yo'q(0): "))