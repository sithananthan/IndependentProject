name = input("Enter the string :")
name_in_caps = name.lower()
i = 0

for c in name_in_caps:
    num = ord(c)
    if num > 65 and num < 91 or num > 97 and num < 123 :
        if i % 2 == 0:
            print(c, end="")
        else:
            print(chr(num - 32), end="")
        i +=1
    else:
        print(c, end="")