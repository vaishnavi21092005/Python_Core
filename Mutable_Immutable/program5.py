ls=[10,20,30,40]
print(ls)
print(id(ls))
ls[0]=60
print(ls)
print(id(ls))

#[10, 20, 30, 40]
#2483063560576
#[60, 20, 30, 40]
#2483063560576

#List have same address in same value.
#It modified therefore it is Mutable type.