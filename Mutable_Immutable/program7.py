Dic={
	"Name":"Vaishnavi",
	"Matches":400,
	"runs":10000
	}
print(Dic)
print(id(Dic))//200

Dic={
	"Name":"Janu",
	"Matches":900,
	"runs":10000
	}
print(Dic)
print(id(Dic))//100

Dic["Name"]="Janvhi"

print(Dic)
print(id(Dic))//100

#Dictionary Datatype is modified therefore it is Muatable type.