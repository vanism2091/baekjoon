# TODO: 타인 코드 확인 ㄱ
# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# 88 / 52 한 번 확인 ㄱㄱ
def sol_2775():
    n = int(input())
    for i in range(n):
        k = int(input())
        n = int(input())
        res = [[col for col in range(1, n+1)] for row in range(k+1)]
        for j in range(1, k+1):
            # j = 1 ... k 층
            for l in range(1, n+1):
                res[j][l-1] = sum(res[j-1][:l])
        print(res[k][n-1])
        
        