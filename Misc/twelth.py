fp=open("a.txt","r")
while True:
    k=fp.readline()
    if k=='':
        break
    print(k,end='')
#l1=["Pune\n","Nashik\n","Beed\n","Akola\n","Jalgaon\n"]
#fp.writelines(l1)
#n1=input("Enter Your name:")
#fp.write(n1)
'''print(fp.name)
print(fp.mode)
print(fp.closed)
print(fp.readable())
print(fp.writable())
print(fp)'''
fp.close()
