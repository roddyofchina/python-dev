
def Getdata(*args,**kwargs):
    print type(args)
    print type(kwargs)
    print args,kwargs


Getdata(1,2,3,4,'dddd', a=1,b=2,c=3)
