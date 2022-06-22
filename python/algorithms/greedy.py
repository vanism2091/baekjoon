
problems = [1789, 1026, 1049, 1541]

def sol_1789():
    import math
    n = int(input())
    print(math.floor((-1 + math.sqrt(1+8*n))/2))

    # int((2*int(input())+.25)**.5-.5)

def sol_1026():
    # 어차피 출력은 B 정렬과 무관하므로 a, b를 정렬 작은수X큰수
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum([ i*j for i in a.sort() for j in b.sort(reverse=True)]))

    # B를 바꾸지 않고 답을 구하는 방법을 생각/구현해보자

def sol_1049():
    # 브랜드별 패키지 가격, 개당 가격 list에서 min을 구함
    # 패키지, 개별 = [(0, n), (1, n-6), ... (k, n-k*6) ],
    #   단 k는 n <= 6*k인 k 중 최소
    # tuple 순회하며 min_cost를 구한다
    n, m = map(int, input().split())
    packs = []
    eachs = []
    for _ in range(m):
        a, b = map(int, input().split())
        packs.append(a)
        eachs.append(b)
    # O(M)
    # O(M) + O(M)
    p, e = min(packs), min(eachs)
    min_cost = 1000*100 + 1
    # O(logN)
    for i in range(n//6+2):
        curr_cost =  p*i + e* (n-i*6 if n-i*6 > 0 else 0)
        if min_cost > curr_cost:
            min_cost = curr_cost 
    return min_cost
    # O(M+logN)

def other_1049():
    N,M=map(int,input().split())
    value=[]
    for i in range(M):
        value.extend(map(int,input().split()))
        a,b=min(value[::2]),min(value[1::2])
    # value에 다 넣고, 2칸씩 건너 뛰어서 slicing한 후 min을 구한다.. 
    # 오! 리스트가 1개라 공간 복잡도 측면에서 더 좋을듯.

    # 생각해보면 당연함. 개별로 6개 구매하는 것이 묶음 6개보다 더 싸면 전체 개별만 사면 됨
    # 이런 조건을 찾음으로써 평균 시간 복잡도 더 줄일 수 있음
    # 생각해보니.. 남은 경우는 두 가지밖에 없음
    #   1. 넘치는 한이 있어도 다 묶음으로 사거나
    #   2. 넘치기 전까지 묶음으로 + 개별로 사거나
    # 1, 2 중 min을 찾으면 됨
    # 문제를 읽고 더 생각하자 :)
    if 6*b<a:
        print(b*N)
    else:
        print(min((N//6+1)*a,N//6*a+b*(N-N//6*6)))


# 잃어버린 괄호
# 식을 하나씩 순회하다가 '-'를 만났을 때, 
# 괄호를 이전에 열었다면 닫고 - 뒤에 열고, 
# 안열었다면 - 뒤에 열고
# eval() 사용
def sol_1541():
    exp = input()
    res = []
    is_open = False
    is_leading = True
    for c in exp:
        if c == '-':
            if is_open:
                res.append(")")
            res.append(c)
            res.append("(")
            is_open = True
            is_leading = True
        elif c == '+':
            is_leading = True
            res.append(c)
        else:
            if not is_leading or c != '0':
                res.append(c)
                is_leading = False
    if is_open:
        res.append(")")
    print(eval("".join(res)))
    # 처음에 런타임에러났는데, 0으로 시작하는 숫자가 eval에 들어가서 oct 취급되었기 때문.

def other_1541():
    e = [sum(map(int, x.split('+'))) for x in input().split('-')]
    print(e[0]-sum(e[1:]))
