def fun1(*g):
    print(g)
    h=list(g)
    print(h)


fun1(10)
fun1(10,20)
fun1(10,20,30)
fun1(10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180)




'''def fun1(x,y,z=0):
    print(x+y+z)
    print(z)

fun1(z=11,x=22,y=33)'''






'''def add(p,q):   #formal parameters  function definition
    z=p+q
    print("Addition is",z)
    #return z
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
result=add(x,y)  #actual parameters    function calling
print("Addition is",result)'''
