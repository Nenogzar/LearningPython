N = int(input())
end = [print("*" * N) if (i == 0 or i == (N-1)) else print("*"+" "*(N-2)+"*") for i in range(N)]
# 6
# ******
# *    *
# *    *
# *    *
# *    *
# ******
