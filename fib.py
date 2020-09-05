import time
def fib(n):
    preNum=0
    curNUm=1
    for i in range(1,n):
        ppNum=preNum
        preNum=curNUm
        curNUm=preNum+ppNum
    return curNUm

def fibrecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibrecur(n-1)+fibrecur(n-2)

if __name__ == "__main__":
    num=int(input("Enter Number:"))
    start=time.time()
    print(f"the fibonacci value of {num} is {fib(num)}")
    print(f"it took {time.time()-start} seconds")
    print(f"RECURSION METHOD: the fibonacci value of {num} is {fibrecur(num)}")
    print(f"it took {time.time()-start} seconds")