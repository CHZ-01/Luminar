# single inheritance
class A:
    pass
class B(A):
    pass

# multilevel inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass

# hierarchical inheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass

# multiple inheritance
class A:
    pass
class B:
    pass
class C(A,B):
    pass
