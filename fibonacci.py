#fibonacci series
a,b,=0,1
n=int(input("Enter the limit: "))
print("Fibonacci series:")
print(a)
print(b)
i=1
while i<n-1:
  c=a+b
  print(c)
  a=b
  b=c
  i=i+1
