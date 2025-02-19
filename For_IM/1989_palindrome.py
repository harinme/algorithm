import sys
sys.stdin = open('1989_palindrome.txt')

def reverse_string(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string(string[:-1])


t = int(input())
for tc in range(1, t+1):
    string = input()

    result = reverse_string(string)
    if string == result:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')

    # palindrome
    # def is_palindrome(string):
    #     if string == string[::-1]:
    #         return 1
    #     return 0