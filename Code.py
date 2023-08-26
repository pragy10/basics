a=6
a=a+5
print(a)

a=6
a+=5
print(a)

a=10
b=12
c=a+b
print(c)

a="Hello"
print(a*10)

a=15
b=4
print(a/b,a//b)

x=2
y=3
x+=y
print(x,y)

x=8
y=2
x+=y
y-=x
print(x,y)

a=5
b=10
a+=a+b
b*a+b
print(a,b)

p=10
q=20
p*=q//3
q+=p+q**2
print(p,q)

p=2/5
q=p*4
r=p*q
p+=p+q-r
r*=p-q+r
q+=p+q
print(p,q,r)

first=2
second=3
third=first*second
print(first,second,third)
third=second*first
print(first,second,third)

a=5
b=2*a
a+=a+b
b*=a+b
print(a,b)

p=10
q=20
p*=q/3
q+= p+q*2
print(p,q)

p=5%2
q=p**4
r=p//q
p+=p+q+r
r+=p+q+r
q-=p+q*r
print(p,q,r)

p=21//5
q=p%4
r=p*q
p+=p+q-r
r*=p-q+r
q+= p+q
print(p,q,r)
