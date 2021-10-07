import numpy as np #numpy is the library that we are uploading and np is its atlas

def main(): 
		i = 0 			#i is an interger, declared with the number 0 (real number)
		n = 10  		#n is another integer
		x = 119.0 		#this is a floating number, floating numbers are declared with a zero 
		
		# using numpy we can declare arrays quickly
		
		y = np.zeros(n,dtype=float) #declare the array with y, using numpy, and setting it to zero to create an array of 0s

		#we can use loops to iterate with a variable

		for i in range(n): # i in range [0,n-1]
			y[i]=2.0 * float(i) + 1.0 # set y=2*i+1 as floats

		#we can simply iterate through a variable array
		for y_element in y:
				print(y_element)

#execute the main function
if __name__ == "__main__":
		main()
