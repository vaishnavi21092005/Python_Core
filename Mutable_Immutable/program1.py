#Mutability=Modified 
#Immutabily=Doesn't Modified
#Int is Immutable Datatype
a=10;
print(a);
#o/p=10

print(id(a));
#It gives address of variable

a=10;
print(id(a));
a=20;
print(id(a));

#o/p=140719214815960
     #140719214816280
#It is immutable it doesn't change variable address.
#And when Reinitialize the variable new address is created.

a=10;
print(id(a));#140719214815960
b=20;
print(id(b));#140719214816280

a=10;
print(id(a));
b=10;
print(id(b));
#140719214815960
#140719214815960
#Because of int datatype id Immutable.

a=10;
print(id(a));#140719203085016
b=20;
print(id(b));#140719203085336
c=30;
print(id(c));#140719203085656
d=30;
print(id(c));#140719203085656









