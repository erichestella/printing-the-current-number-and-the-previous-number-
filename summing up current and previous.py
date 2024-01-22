#putting some title 
print('\nPrinting current and previous in a range (10)\n')

#making a list of number
current_number= list()
previous_number= list()

#list of current number
current_number.append('0')
current_number.append('1')
current_number.append('2')
current_number.append('3')
current_number.append('4')
current_number.append('5')
current_number.append('6')
current_number.append('7')
current_number.append('8')
current_number.append('9')

#list of previous number
previous_number.append('0')
previous_number.append('0')
previous_number.append('1')
previous_number.append('2')
previous_number.append('3')
previous_number.append('4')
previous_number.append('5')
previous_number.append('6')
previous_number.append('7')
previous_number.append('8')

#it controls the current and previous number to add up 
for current, prev, in zip(previous_number, current_number): 
     total_sum = int(current) + int(prev)
     print('The current number:', prev, 'The previous number: ', current, 'Sum: ', total_sum)

