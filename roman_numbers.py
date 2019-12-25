def arabic_to_roman():
    text_num = input("введите число от 0 до 3999: ")

    if int(text_num) < 0:
        print("введено число меньше 0")
    elif int(text_num) > 3999:
        print("введено число больше 3999")
    else:
        tmp = int(text_num)
        res = ''
        if tmp / 1000 > 1:
            res += "M"*int(tmp / 1000)
            tmp -= 1000*int(tmp / 1000)

        if int(tmp / 900) >= 1:
            res += "CM"
            tmp -= 900

        if tmp / 500 >= 1:
            res += "D" * int(tmp / 500)
            tmp -= 500 * int(tmp / 500)

        if int(tmp / 100) >= 4:
            res += "CD"
            tmp -= 400

        if tmp / 100 >= 1:
            res += "C" * int(tmp / 100)
            tmp -= 100 * int(tmp / 100)

        if tmp/90 >= 1:
            res += "XC"
            tmp -= 90

        if tmp / 50 >= 1:
            res += "L" * int(tmp / 50)
            tmp -= 50 * int(tmp / 50)

        if tmp / 10 >= 4:
            res += "XL"
            tmp -= 40

        if tmp / 10 >= 1:
            res += "X" * int(tmp / 10)
            tmp -= 10 * int(tmp / 10)

        if tmp / 9 >= 1:
            res += "IX"
            tmp -= 9

        if tmp / 5 >= 1:
            res += "V" * int(tmp / 5)
            tmp -= 5 * int(tmp / 5)

        if tmp >= 4:
            res += "IV"
            tmp -= 4

        if tmp >= 1:
            res += "I"*tmp
            tmp -= tmp

        print(res)
        return res

arabic_to_roman()