
class d:
    pass
class e:
    pass
class f:
    pass
class b(d,e):
    pass
class c(d,f):
    pass
class a(b,c):
    pass
print(d.mro())
print(e.mro())
print(f.mro())
print(b.mro())
print(c.mro())
print(a .mro())






import sys
sys.exit()
class A:
    def m1(self):
        print("method inside A")
class B:
    def m1(self):
        print("method inside B")
class C:
    def m1(self):
        print("method inside C")
class X(A,B):
    def m1(self):
        print("method inside X")
class Y(B,C):
    def m1(self):
        print("method inside Y")
class P(X,Y,C):
    def m1(self):
        print("method inside P")
v= (A)
print(A.mro())
v = B()
print(B.mro())
v = C()
print(C.mro())
v = X()
print(X.mro())
v = Y()
print(Y.mro())
v = P()
print(P.mro())

import sys
sys.exit()


class D:
    def m1(self):
        print("method inside D")
class E:
    def m1(self):
        print("method inside E")
class F:
    def m1(self):
        print("method inside F")
class B(D,E):
    def m1(self):
        print("method inside B")
class C(D,F):
    def m1(self):
        print("method inside C")
class A(B,C):
    def m1(self):
        print("method inside A")
v=(D)
print(D.mro())
v=E()
print(E.mro())
v=F()
print(F.mro())
v=B()
print(B.mro())
v=C()
print(C.mro())
v=A()
print(A.mro())



