class C(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,c):
        return C(c.b[::-1]+self.a[::-1],self.b+c.b)
    def __repr__(self):
        return self.a+self.b

print(C("ABC","DEF")+C("foo","bar"))