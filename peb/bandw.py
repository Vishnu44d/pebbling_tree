import hashlib
k=input()
z=[]; q=k; y=hashlib.sha256("").digest()
for h in range(1<<k,1,-1):
    if h==1<<q: z.insert(0,y); q-=1
    y=hashlib.sha256(y).digest()
print(str(y).encode('hex'))
for r in range((1<<k)-1,0,-1):
    print(str(z[0]).encode('hex'))
    c=r
    i=0
    while ~c&1: z[i]=z[i+1]; i+=1; c>>=1
    i+=1; c>>=1
    m=i; s=0
    while c: 
        l=i
        while ~c&1: i+=1; c>>=1
        j=r&((1<<i)-1)
        p=i&1^j&1
        h=p+j*(i-m)+(m+3-l)*(1<<l)-(1<<m)>>1
        q=h.bit_length()-1
        for _ in range(p+i+1-s>>1):
            y=z[q]
            if h==1<<q: q-=1
            z[q]=hashlib.sha256(y).digest()
            h-=1
        m=i; s=m+1
        while c&1: i+=1; c>>=1