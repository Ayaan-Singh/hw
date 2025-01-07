
def int_to_roman(num):
    roman_numerals = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC"
    }
    result = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result


num = int(input("Enter a number between 1 and 100: "))
print(int_to_roman(num))

