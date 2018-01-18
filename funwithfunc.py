#Odd and Even
def odd_even():
	for i in range(1, 2001):
		# print 'Number is '
		if i % 2==1:
			print 'Number is ' + str(i) + '. This is an odd number.'
		else:
			print 'Number is '+ str(i) + '. This is an even number.'
odd_even()	

# Multiply

def multiply(list, num):
	for i in range(0,len(list)):
		list[i]*=num
	return list

list=[2,4,10,16]

b=multiply(list, 5)
print b

# Hacker Challenge: 

def layered_multiples(arr):
	print arr
	new_arr=[]
	for x in arr:
		val_arr=[]
		for i in range(0,x):
			val_arr.append(1)
		new_arr.append(val_arr)
	return new_arr
# y=multiply([2,4,5],3)
y=layered_multiples(multiply([2,4,5],3))
print y

