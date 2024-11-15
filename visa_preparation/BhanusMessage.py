number = input().strip()

number = number.replace(" ","")
if len(number) == 10 and number.isdigit():
    print("Corrct")
elif len(number) == 13 and number.startswith("+91") and number[3:].isdigit():
        print("Correct")
else:
    print("Incorrect")
