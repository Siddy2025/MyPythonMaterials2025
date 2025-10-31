#variable length keyword arguments
def fun1(**k):    #dict
    print(k,type(k))


fun1(ajay=22,vijay=81,sumit=91)
fun1(name="Rakesh",age=18,height=175,roll=32,num="Number")
#fun1(11,22,w=33,z=44)


