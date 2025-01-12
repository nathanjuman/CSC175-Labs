def average(n):
    '''
    This function prompts the user for a certain amount of numbers and calculates the average of those numbers. 

    Inputs:
    n (int): the amount of numbers the user wants to input
    value (int): number that is included in the average calculation
    
    Return:
    avg (int): the average of all inputted numbers
    '''
    sum = 0
    for i in range(n):
        value = int(input("Enter a number: "))
        sum = sum + value
    avg = sum / n
    return avg

def definiteFib(n):
    '''
    This function finds the nth value in the Fibonacci Sequence using a for loop. 

    Inputs:
    n (int): the value in the Fibonacci Sequence to display

    Return:
    answer (int): the value of n in the Fibonacci Sequence
    '''
    first = 1
    second = 1
    answer = first

    if n <= 2:
        return answer
    else:
        for i in range(n - 2):
            answer = first + second
            first = second
            second = answer
            n -= 1
        return answer

def indefiniteFib(n):
    '''
    This function finds the nth value in the Fibonacci Sequence using a while loop. 

    Inputs:
    n (int): the value in the Fibonacci Sequence to display

    Return:
    answer (int): the value of n in the Fibonacci Sequence
    '''
    first = 1
    second = 1
    answer = first

    if n <= 2:
        return answer
    else:
        while n > 2:
            answer = first + second
            first = second
            second = answer
            n -= 1
        return answer

def main():
    #compute average of n numbers
    howMany = int(input("How many numbers are being entered? "))
    if howMany < 1:
        print("Please choose a positive number.")
    else: 
        print(average(howMany))
   
   #Fibonacci Sequence
    n = int(input("Digit in the Fibonacci Sequence to display: "))
    print(definiteFib(n))
    print(indefiniteFib(n))

main()

#Test Case 1:
#Input: howMany = 5, value = 5, 2, 3, 4, 2
#Output: 3.2
#Input: n = 5
#Output: 5, 5
#-----------------------------------------------------
#Test Case 2:
#Input: howMany = 6, value = 2, 6, 8, 5, 3, 5
#Output: 4.833333333333
#Input: n = 10
#Output: 55, 55