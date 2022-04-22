'''
Sample functions
'''

def remove_letter(sentance,letter):
    '''
    Function to remove a leter from a string.

    Parameters
    ----------
    sentance : string
        string from which a letter has to be removed
    letter : string
        letter which has to be removed

    Returns  
    -------
    newstr : string
        sentance with given letter removed
    '''
    lst=sentance.split(letter)
    newstr=''
    
    for substr in lst:
        newstr+=substr
        
    return newstr


def capwords(args):
    '''
    Function to capitalize each word of string

    Parameters
    ----------
    args : string
        string whose each word has to be capitalized.

    Returns
    -------
    newstr : string
        given string with each word capitalized.
    '''
    lst=args.split()
    newstr=''
    
    for substr in lst:
        newstr=' '.join([newstr,substr.capitalize()])
        
    return newstr[1:]
    