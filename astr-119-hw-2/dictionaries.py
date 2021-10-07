#define a dictonary data structure

#disctonaries have key : value for the elements (associate key and value)
example_dict = {
	"class"				:	"Astr 119",
	"prof"				:	"Brant",
	"awesome"			:	10			#last element does not have a comma
}
print(type(example_dict))		#will say dict

#get a value via key
course = example_dict["class"]
print(course)

#change a value via key
example_dict["awesome"] +=1 	#increase awesomeness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
		print(x,example_dict[x])