#### topic 1 : 람다활용 
def hap(x,y):
    return x + y 

print(hap(10,20))

## 람다 형식은 함수를 딱 한줄만으로 만들게 해주는 방식 
# lambda 매개변수 : 표현식 

print((lambda x,y: x + y)(10, 20))

#### topic 2 : 나눗셈, 나머지, 몫 
# 1. 단순 나눗셈 
a = 5 
b = 3 
print(a/b)

# 2. 나눗셈의 몫 
print(a // b)

# 3. 나눗셈의 나머지 
print(a % b)

# 4. 나눗셈의 몫과 나머지 (튜플형식)
result = divmod(a,b)
print(result)
print(result[0]) # 몫
print(result[1]) # 나머지 

# 다른 사람 풀이 
    """
    def solution(num1, num2):
    answer = num1//num2
    return answer
def solution(num1, num2):
    a,b = divmod(num1,num2)
    return a


def solution(num1, num2):
    answer = divmod(num1, num2)
    return answer[0]

    """
    
#### 정수, 소수 부분만 return 하기
# 1. 정수부분만 return 
def solution(num1, num2):
    answer = (num1 / num2) * 1000
    return int(answer)
# math 활용법 
# 참고로 math.trunc()함수는 int()와 같이 결과를 반환한다.
"""
import math

def solution(num1, num2):
    return math.trunc(num1 / num2 * 1000) 

import math 

def solution(num1, num2):
    answer = num1/num2 * 1000
    return math.floor(answer)

"""
"""
>>> math.trunc(-3.14)   #결과는 -3
>>> math.floor(-3.14)   #결과는 -4

"""
# 다른 풀이 
import math 
def solution(num1, num2):
    answer = num1/num2 * 1000
    return math.trunc(answer)

import math 
def solution(num1, num2):
    answer = num1/num2 * 1000
    return math.modf(answer)[1]


# 2. 소수 부분만 return 
# math.modf()를 사용하여 숫자의 정수 및 소수 부분을 동시에 가져옵니다.
import math

print(math.modf(1.5))
print(type(math.modf(1.5)))
# (0.5, 1.0)
# <class 'tuple'>

#### 비교하기 
def solution(num1, num2):
    if num1 == num2 :
        return 1
    else :
        return -1

# 다른 풀이 
def solution(num1, num2):
    return 1 if num1==num2 else -1

def solution(num1, num2):
    return -1 if num1 != num2 else 1

def solution(num1, num2):
    answer = 0

    if num1 == num2:
        answer = 1
    else:
        answer = -1

    return answer

#### 기약분수 분수의 합 
# 1. math.gcd 최대공약수 구하기 
# math.lcm은 최소공배수 구하기 

import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]


from math import gcd

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    return [denum // gcd(denum, num), num // gcd(denum, num)]


from math import gcd
def solution(denum1, num1, denum2, num2):
    d = num1*num2
    n = denum1*num2+denum2*num1
    return [n//gcd(n,d),d//gcd(n,d)]

# 2. fractions fractions(분자,분모)
# numerator --> 분자의 값 
# denominator --> 분모의 값 

from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

#### 배열 두배 만들기 
# 리스트에 곱하기 2를 하면 두개를 이어붙힌 형태가 된다 
# 원소들의 값 자체를 두배씩으로 바꾸고 싶다면 반복문 쓰기 
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer