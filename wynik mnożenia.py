import sys
import random
score = 0
while score < 20:
    factor_1 = random.randint(0, 10)
    factor_2 = random.randint(0, 10)
    print("ile wynosi:", factor_1, "razy", factor_2, ":")
    input_number = input()
    input_number = int(input_number)
    result = factor_1 * factor_2
#pętla dla prawidłowych wyników
    while result == input_number:
        print("dobrze! :D")
        print(f"otrzymałeś {2} punkty!")
        score = score + 2
        if score >= 20:
            print("WYGRAŁEŚ!")
            sys.exit(0)
        print("obecnie posiadasz", score, "punktów")
        factor_1 = random.randint(0, 10)
        factor_2 = random.randint(0, 10)
        print("ile wynosi:", factor_1, "razy", factor_2, ":")
        input_number = input()
        input_number = int(input_number)
        result = factor_1 * factor_2
#pętla dla nieprawidłowych wyników
    while result != input_number:
        print(f"straciłeś {1} punkt!")
        score = score - 1
        print("obecnie posiadasz", score, "punktów")
        print("źle :/, spróbuj jescze raz:")
        input_number = input()
        input_number = int(input_number)
        if result == input_number:
            if score >= 20:
                print("WYGRAŁEŚ!")
                sys.exit(0)
            print("dobrze! :D")
            print(f"otrzymałeś {2} punkty!")
            score = score + 2
            if score >= 20:
                print("WYGRAŁEŚ!")
                sys.exit(0)
            print("obecnie posiadasz", score, "punktów")

#POZAMIENIAĆ POWTARZAJĄCE SIĘ CZĘŚCI KODU NA FUNKCJE