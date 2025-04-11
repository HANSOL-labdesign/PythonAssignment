def read_single_digit(digit) :
    if digit == 0 :
        print("영", end=" ")
    elif digit == 1 :
        print("일", end=" ")
    elif digit == 2 :
        print("이", end=" ")
    elif digit == 3 :
        print("삼", end=" ")
    elif digit == 4 :
        print("사", end=" ")
    elif digit == 5 :
        print("오", end=" ")
    elif digit == 6 :
        print("육", end=" ")
    elif digit == 7 :
        print("칠", end=" ")
    elif digit == 8 :
        print("팔", end=" ")
    elif digit == 9 :
        print("구", end=" ")

def read_number(number) :
    if len(number) == 3 :
        read_single_digit(int(number[0]))
        read_single_digit(int(number[1]))
        read_single_digit(int(number[2]))
    elif len(number) == 2 :
        read_single_digit(int(number[0]))
        read_single_digit(int(number[1]))
    else :
        read_single_digit(int(number[0]))

number = input("세 자리 정수 입력 : ")

read_number(number)
