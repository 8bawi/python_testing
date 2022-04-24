print("Please enter 3 numbers separated by ',' ")
value_keeper = []

#Save user input in a variable
user_input = input()
#Splitting the values and putting them in a list
user_input_toint = user_input.split(',')
#Converting the values to int
for index,value in enumerate(user_input_toint):
    user_input_toint[index]=int(value)
#Running the equation on the values
compute = user_input_toint[0] + user_input_toint[1] - user_input_toint[2]   
print(compute)    