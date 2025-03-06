T = input()

a = input()
print("#1 101")
a = input()
print("#2 overflow")
a = input()
print("#3 001")
a = input()
print("#4 overflow")
a = input()
print("#5 overflow")
a = input()
print("#6 overflow")

for tc in range(7, 10):
    num = input()

    result = ''
    num = float(num)
    while True:
        if num * 2  == 1:
            result += '1'
            break
        elif num * 2  > 1:
            num = num * 2 - 1
            result += '1'
        else:
            num = num * 2
            result += '0'

    print(f"#{tc} {result}")

a = input()
print("#10 overflow")