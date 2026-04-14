Set={10,20,30,30}
print(Set)
print(id(Set))#100
Set={10,20,30,30}
print(Set)
print(id(Set))#200

Set[-1]=5
print(Set)
print(id(Set))

#'set' object does not support item assignment
#Set datatype is can't modified therefore it is Immutable type.

