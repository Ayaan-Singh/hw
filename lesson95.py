num = float(input("Enter decimal number: "))
whole = int(num)
fraction = num - whole
print(f"{num} is {bin(whole)[2:]}.{bin(int(fraction*2**32))[2:][:32]} in binary")

                