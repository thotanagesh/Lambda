#lambda 
#sum=lambda x,y:x+y
#print(sum(10,5))

#import fn
#print(fn.gen_password())

l1=[]

n=int(input())
for i in range(n):
  l1.append(list(map(int,input().split())))
  
a=b=i=p=0
c=d=n-1
k=m=n-1
y=0
z=0
t=0
s=0
cnt=0

while(cnt<((2*n)-1)):
  while(i<=a):
    for j in range(0+s,n-1):
      print(l1[j][i],end=' ')
    i+=1
    s+=1
  cnt+=1
  if(cnt<((2*n)-1)):
    while(k<=c):
      for l in range(0+y,n-1):
        print(l1[k][l],end=' ')
      k+=1
      y+=2
    cnt+=1
  if(cnt<((2*n)-1)):
    while(m<=d):
      for o in range(n-1-z,0,-1):
        print(l1[o][m],end=' ')
      m+=1
      z+=2
    cnt+=1
  if(cnt<((2*n)-1)):
    while(p<=b):
      for q in range(n-1-t,0,-1):
        print(l1[p][q],end=' ')
      t+=2
      p+=1
  
  
  a+=1
  b+=1
  k-=2
  m-=2
  c-=1
  d-=1
  cnt+=1
