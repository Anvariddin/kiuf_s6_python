# n=int(input("n="))
N=int(input("N="))
s=0.0
i=1
# for i in range(1, n+1):
while(s<N):
    s=s+1.0/i
    i+=1
print(f"s={s}\ni={i}")