# --------------------------------------------------------------------------------
# Nathan Juman - CSC175
# This program takes a text file and finds the total number of characters, total number of lines, total number of lowercase letters, total number of uppercase letters, and total number of each letter.
# --------------------------------------------------------------------------------
def totalChar(data):
    '''
    This function returns the total number of characters in the txt file.

    Input:
    data (txt): string from the text file

    Return:
    len(answer): total number of characters in the txt file
    '''
    return len(data)

def totalLines(data):
    '''
    This function returns the total number of lines in the txt file.

    Input:
    data (txt): string from the text file

    Return:
    len(answer): total number of lines in the txt file
    '''
    answer = 0
    
    for n in data:
        if n == '\n':
            answer += 1
    return answer + 1

def totalLowercase(data):
    '''
    This function returns the total number of lowercase letters in the txt file.

    Input:
    data (txt): string from the text file

    Return:
    len(answer): total number of lowercase letters in the txt file
    '''
    answer = 0

    for char in data:
        if char.islower():
            answer += 1
    return answer

def totalUppercase(data):
    '''
    This function returns the total number of uppercase letters in the txt file.

    Input:
    data (txt): string from the text file

    Return:
    len(answer): total number of uppercase letters in the txt file
    '''
    answer = 0

    for char in data:
        if char.isupper():
            answer += 1
    return answer

def letterTotal(data):
    '''
    This function returns the frequency of each letter in the txt file, with uppercase and lowercase letter counted together.

    Input:
    data (txt): string from the text file

    Return:
    len(answer): frequency of each letter in the txt file
    '''
    letterCount = {}
    line = data.split()

    for word in line:
        for char in word:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in letterCount:
                    letterCount[char_lower] += 1
                else:
                    letterCount[char_lower] = 1 
    return letterCount

def main():
    # print the total number of characters
    with open('MA_01.txt', 'r') as file:
        data = file.read()
        print("Total number of characters:", totalChar(data))

    # print the total number of text lines
        print("Total number of text lines:", totalLines(data))

    # print the total number of lowercase letters
        print("Total number of lowercase letters:", totalLowercase(data))
        
    # print the total number of uppercase letters
        print("Total number of uppercase letters:", totalUppercase(data))

    # print the total number of each letter
        print(letterTotal(data))

main()