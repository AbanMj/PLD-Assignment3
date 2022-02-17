def average():
    sum=0
    count=0
    more_data = 'yes'
    while more_data[0] == 'y':
        number = float(input('Enter number: '))
        sum += number
        count += 1
        more_data = input('Add another number? (y or n):    ')
    return count, sum/count


n, avg = average()
print(f'The average of {n} number(s) is {avg}')