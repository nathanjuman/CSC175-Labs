#-----------------------------------------
#Nathan Juman - CSC 175 with Paul Olsen
#Lab 8: Strings
#October 2024
#-----------------------------------------

def index_fnrc(s):
    '''
    This function accepts a string as a parameter and returns the first character in the string which appears only once.

    Input:
    s (str): string given by user to test

    Return:
    (char): first character in the string that appears only once.
    '''
    for idx in range(len(s)):
        if s.count(s[idx]) == 1: 
            return s[idx]

def validMonth(date):
    '''
    This function checks the month value of a date to see if it is valid. 

    Input:
    date (str): date that is given by the user to test

    Return:
    (bool): returns True if month is valid, False if not. 
    '''
    month = date[0:2]

    if month.isdigit():
        if (1 <= int(month) <= 12):
            return True
        else:
            return False
    else:
        return False

def validDay(date):
    '''
    This function checks the day value of a date to see if it is valid. 

    Input:
    date (str): date that is given by the user to test

    Return:
    (bool): returns True if the day is valid, False if not.
    '''
    day = date[3:5]

    if day.isdigit():
        if (1 <= int(day) <= 31):
            return True
        else:    
            return False
    else:
        return False
    
def validYear(date):
    '''
    This function checks the year value of a date to see if it is valid. 

    Input:
    date (str): date that is given by the user to test

    Return:
    (bool): returns True if the day is valid, False if not.
    '''
    year = date[6:10]

    if year.isdigit():
        if int(year) > 1999:
            return True
        else:
            return False
    else:
        return False

def isValidDate(date):
    '''
    This function uses previous functions that were validating date values, returns True if all functions were true, returns False if not all functions are true. 

    Input:
    date (str): date that is given by the user to test

    Return:
    (bool): returns True if the date is valid, False if the date is not valid. 
    '''
    
    if len(date) != 10:
        return False    
    elif validMonth(date) == False:
        return False
    elif validDay(date) == False:
        return False
    elif validYear(date) == False:
        return False
    else:
        return True

def main():
    stringOne = input("Enter a string: ") 
    print(index_fnrc(stringOne))

    date = input("Enter a date (mm/dd/yyyy): ") 
    invalid = "{} is an invalid date".format(date)
    valid = "{} is a valid date".format(date)

    if isValidDate(date) == False:
        print(invalid)
    else:
        print(valid)
main()