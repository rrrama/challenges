import sys

def piDigits(n):
    d=[]
    m = 10*n//3
    current = [2 for _ in range(m+1)]
    num = [i+1 for i in range(m)]
    den = [2*(i+1)+1 for i in range(m)]
    for i in range(n):
        current = [10*i for i in current]
        carry = [0 for _ in range(m+1)]
        for a in range(m,0,-1):
            q = (current[a]+carry[a])//den[a-1]
            r = (current[a]+carry[a])%den[a-1]
            current[a] = r
            carry[a-1] = q*num[a-1]
            #print(current)
            #print(carry)
            #print()
        d.append((current[0]+carry[0])//10)
        current[0] = (current[0]+carry[0])%10
    return d


if __name__ == "__main__":
    n=int(sys.argv[1])
    print("3."+"".join([str(i) for i in piDigits(n)[1:]]))
