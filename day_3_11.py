# 2주차

#step 1
def grade(score: int) -> str:
    """
    점수에 따라 학점을 리턴해주는 함수
    :param score: 0~100의 점수
    :return: grade(A+, A, B+, B, C+, C, D+, D, F)
    """
    if score <= 100 and score >= 95:
        return "A+"
    elif score <= 94 and score >= 90:
        return "A"
    elif score <= 89 and score >= 85:
        return "B+"
    elif score <= 84 and score >= 80:
        return "B"
    elif score <= 79 and score >= 75:
        return "C+"
    elif score <= 74 and score >= 70:
        return "C"
    elif score <= 69 and score >= 65:
        return "D+"
    elif score <= 64 and score >= 60:
        return "D"
    else: # elif score < 60:
        return "F"

def run_test():
    """
    테스트를 진행하고 점수를 출력하는 함수
    """
    while True:
        score = input("점수를 입력하세요: ")
        if score == "stop":
            break
        else:
            print(grade(int(score)))

# run_test()

#step 3

def step3():
    """음수 양수 판별"""
    x = -3
    if x < 0:
        print("it's negative")

    if x<0:
        print("it's negative")
    elif x == 0:
        print("it's zero")
    elif 0 < x < 5:
        print("Positive but smaller than 5")
    else:
        print("Positive and larger than or equal to 5")

#step 4
def step4():
    # 5번 반복하는 함수
    for i in range(5):
        print(i)
    # 특정 list를 사용해야 하는 경우
    dates = ['0302','0309','0316','0323','0323']
    for date in dates:
        print("the lecture is held on" + date)

#strp 5
def step5():
    """continue를 사용한 1부터 5까지의 합 구하기"""
    sequence = [1,2,None,4,None,5]
    total = 0
    for value in sequence:
        if value is None:
            continue # 다음 loop로 넘어감
        total += value
    print(total)

#step 6
def step6():
    """break를 사용한 1부터 5까지의 합 구하기"""
    sequence = [1,2,0,4,6,5,2,1]
    total_until_5 = 0
    for value in sequence:
        if value == 5:
            break # for loop을 빠져나감
        total_until_5 += value
    print(total_until_5)

#step 7
def step7():
    """enumerate를 사용한 1부터 5까지의 합 구하기"""
    i=0
    collection = ["a","b","c","d","e","f","g","h","i","j"]
    for value in collection:
        i+=1
    for i, value in enumerate(collection):
        print(i, value) # index와 value를 함께 출력

    # #test
    # dates = ['0302','0309','0316','0323','0323']
    # for i, date in enumerate(dates):
    #     print(f"The {i}th lecture is held on {date}")

#step 8
def step8():
    """enumerate를 사용한 리스트 출력"""
    # 특정한 list를 사용해야 하는 경우
    dates = ['0302','0309','0316','0323','0323']
    for i, date in enumerate(dates):
        print(f"The {i}th lecture is held on {date}")

#step 9
def step9():
    """라스트 내포"""
    # 리스트 내포
    expr = "data"
    condition = True
    collection = ["a","b","c","d","e","f","g","h","i","j"]
    result_1 = [expr for val in collection if condition]
    print(result_1)

    strings = ['a','as','bat','car','dove','python']
    result_2 = [x.upper() for x in strings if len(x) > 2]
    print(result_2)

#quiz
def quiz():
    """
    lee 씨로 사작하는 사람들로 list를 만들어주는 함수
    :return: lee 씨로 시작하는 사람들의 list
    """
    Names = ['leebyunghun', 'leehyolee', 'kangdongwon', 'Yoojaesuk', 'leeyoungja']

    #ans1
    result = []
    for name in Names:
        if name[:3] == 'lee':
            result.append(name)
    #ans2
    result = [name for name in Names if name[:3] == 'lee']
    #ans3
    result = [name for name in Names if name.startswith('lee')]

#step 13
def step13():
    """5!을 구하는 함수"""
    x = 0
    while x < 5:
        x+=1
        print(x)

#step 14
def step14():
    """range 사용법"""
    for i in range(10):
        print(i)
    for i in range(2,20,2):
        print(i)

#step 15
def step15():
    """0 에서 9999 까지 숫자 중 3이나 5의 배수 값의 합"""
    sum = 0
    for i in range(10000):
        #  % is the modulo operator
        if i % 3 == 0 or i % 5 == 0:
            sum += i

def step16():
    """def 함수 사용법"""
    def my_function(x,y,z=1.5):
        if z > 1:
            return z * (x + y)
        else:
            return z / (x + y)
    print(my_function(5,6,z=0.7))
    print(my_function(3.14,7,3.5))

#step 17
def step17():
    """일반적인 함수"""
    def add(x:int,y:int)->int:
        """
        두 수를 더해주는 함수
        :param x: 매개변수
        :param y: 매개변수
        :return: 결과
        """
        result = x + y
        return result
    a = add(3,4)
    print(a)

#step 18
def step18():
    """입력값이 없는 함수"""
    def say()->str:
        """
        입력값이 없는 함수
        :return: string
        """
        return 'Hi'
    a = say()
    print(a)

#step 19
def step19():
    """"입력값의 수가 미정일때"""
    def add_many(*args):
        result = 0
        for i in args:
            result += i
        return result
    result = add_many(1,2,3)
    print(result)

#step 20
def step20():
    """전역변수 지역변수"""
    def func():
        a = []
        for i in range(5):
            a.append(i)
    a = []
    func()
    print(a) # []

    a = []
    def func2():
        for i in range(5):
            a.append(i)
    func2()
    print(a) # [0,1,2,3,4]

#step 21
def step21():
    """여러 값 반환하기"""
    def f()->tuple:
        a = 5
        b = 6
        c = 7
        return a,b,c
    a,b,c = f()
    print(a,b,c) # 5 6 7

    def f2()->dict:
        a = 5
        b = 6
        c = 7
        return {'a':a,'b':b,'c':c}
    result = f2()
    print(result) # {'a':5,'b':6,'c':7}