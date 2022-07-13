def factorial(num):
    if num == 1:
        return 1
    else:
        answer = num * factorial(num - 1)
        return answer

input = input("Number to count down from: ")
factorial(int(input))