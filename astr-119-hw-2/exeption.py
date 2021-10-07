#python exceptions let yo deal with
#unexpected results

try:
	print(a)		#this will throw an exception since a is nt defined
except:
	print("a is not defined!")

#there are specific errors to help with cases
try:
	print(a) 	#this will throw an exception since a is not defined
except NameError:
	print("a is still not defined!")
except:
	pint("Something else went wrong.")

#this wll break our program
#since a is not defined
print(a)
