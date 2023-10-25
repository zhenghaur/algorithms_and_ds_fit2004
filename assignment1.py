"""
Name: Lim Zheng Haur
Student ID: 32023952
Assignment 1
FIT2004
"""

# remember, no codes outside

def trainer(wordlist, word, marker):
    """
    This function returns a list of strings in lexicographical order containing valid words based on the input provided.

    Precondition: each element of wordlist is of length M. word and marker is of length M as well
    Postcondition: list is sorted

    Input:
        wordlist: a list of N strings of length M, with each character at the range of 
        lower case {a - z}
        word: a string of length M
        marker: a list with element in the range {0, 1} of length M
    Return:
        answer: a list of strings of length M 

    Time complexity: 
        Best: O(NM) where N is the length of wordlist and M is the length of word
        Worst: O(NM) where N is the length of wordlist and M is the length of word
    Space complexity: 
        Input: O(NM) where N is the length of new_list and M is length of word
        Aux: O(NM) where N is the length of new_list and M is length of word

    """
    # append all item in wordlist containing same characters with word into answer
    # done by sorting all character in each item and comparing to the word
    answer = []
    temp = word_sort(word)
    for i in range(len(wordlist)):
        if word_sort(wordlist[i]) == temp:
            answer.append(wordlist[i])

    # loop through marker and removing words from answer
    i = 0
    while len(answer) != 0 and i < len(word):
        # sort answer by character at position i
        answer = counting_sort(answer, i)
        # search for first occurence of character at position i
        start = binary_search_first(answer, word[i], i)
        # search for last occurence of character at position i
        end = binary_search_last(answer, word[i], i)
        temp = []
        # remove all words that is does not have character of word[i] at position i 
        if marker[i] == 1:
            if start is not None:
                for j in range(start,end+1):
                    temp.append(answer[j])
                answer = temp
            else:
                answer = []
        # remove all words that have character of word[i] at position i
        else:
            if start is not None:
                for j in range(start):
                    temp.append(answer[j])
                for j in range(end+1, len(answer)):
                    temp.append(answer[j])
                answer = temp
        i += 1
    # sort answer 
    if len(answer) != 0:
        radix_sort(answer)
    return answer
            

def radix_sort(new_list):
    """
    This function sorts the new_list

    Precondition: strings of new_list must be of length M. new_list is not empty
    Postcondition: the return list is sorted

    Input:
        new_list: a list of N strings, with each character at the range of 
        lower case {a - z}

    Return:
        new_list: a list of N strings sorted

    Time complexity: 
        Best: O(NM) where N is the length of new_list
        Worst: O(NM) where N is the length of new_list
        loop of count_arr is constant with maximum of 26
    Space complexity: 
        Input: O(NM) where N is the length of new_list and M is length of word
        Aux: O(NM) where N is the length of new_list and M is length of word
        size of count_arr is constant with maximum of 26

    """
    # i = last index
    i = len(new_list[0]) - 1
    # iterate through every character and perform counting sort
    while i >= 0:
        new_list = counting_sort(new_list, i)
        i -= 1
    return new_list


def counting_sort(new_list, pos):
    """
    This function sorts the new_list by the character at index pos.

    Precondition: pos must be < len(word in new_list), new_list have strings of same length
    Postcondition: the return list is sorted by character at index 'pos'

    Input:
        new_list: a list of N strings, with each character at the range of 
        lower case {a - z}
        pos: the index of the character to be sorted

    Return:
        new_list: a list of N strings sorted by the character at index position

    Time complexity: 
        Best: O(N) where N is the length of new_list
        Worst: O(N) where N is the length of new_list
        loop of count_arr is constant with maximum of 26
    Space complexity: 
        Input: O(NM) where N is the length of new_list and M is length of word
        Aux: O(NM) where N is the length of new_list and M is length of word
        size of count_arr is constant with maximum of 26

    """
    # find max
    max_item = ord(new_list[0][pos])-97
    for item in new_list:
        if ord(item[pos])-97 > max_item:
            max_item = ord(item[pos])-97

    # initialize count_arr
    count_arr = [None] * (max_item + 1)
    for i in range(len(count_arr)):
        count_arr[i] = []

    # update count_arr
    for item in new_list:
        count_arr[ord(item[pos])-97].append(item)

    # update input list
    index = 0
    for i in range(len(count_arr)):
        freq = count_arr[i]
        for j in range(len(freq)):
            new_list[index] = count_arr[i][j]
            index += 1

    # new list will be sorted
    return new_list


def word_sort(word):
    """
    This function returns a string with sorted characters of the input string.

    Precondition: 
    Postcondition: 

    Input:
        word: a string of length M
    Return:
        ret: a string of length M with each character in sorted order

    Time complexity:
        Best: O(N + M) where N is the length of word and M is the maximum character of word (size of count_arr)
        Worst: O(N + M) where N is the length of word and M is the maximum character of word (size of count_arr)
    Space complexity: 
        Input: O(1)
        Aux: O(N) where N is the length of word 
        size of count_arr is constant with maximum of 26
    
    """
    # transform word into list of characters
    word = [char for char in word]

    # sort word using counting sort
    word = counting_sort(word, 0)

    # transform character list back into word
    ret = ""
    for char in word:
        ret += char
    return ret


def binary_search_first(wordlist, char, pos):
    """
    This function returns an integer which represents the index of the first occurence of the input character in the pos-th index 
    within the wordlist or None if it the character is not found

    Precondition: pos must be <len(word in wordlist)
    Postcondition: 

    Input:
        wordlist: a list of N strings of length M, with each character at the range of 
        lower case {a - z}
        word: a string of length M
        pos: an integer of the n-th position to search
    Return:
        c + 1: an integer representing the index of the first occurence of input character
        None: if character is not found

    Time complexity: 
        Best: O(1) where the first occurence is found on first iteration
        Worst: O(N) where N is the length of wordlist
    Space complexity: 
        Input: O(NM) where N is the length of wordlist and M is length of word
        Aux: O(1)

    """
    # lower boundary
    a = 0
    # upper boundary
    b = len(wordlist) - 1
    # while boundary have not crossed each other
    while a <= b:
        # c = midpoint
        c = (a + b) // 2
        # if found:
        if wordlist[c][pos] == char:
            # find last occurence
            while c >= 0 and wordlist[c][pos] == char:
                c -= 1
            # return index
            return c + 1
        # if not found and value at c greater than target
        elif wordlist[c][pos] > char:
            # update upper boundary
            b = c - 1
        # if not found and value at c lesser than target
        else:
            # update lower boundary
            a = c + 1
    # if not in list return None
    return None


def binary_search_last(wordlist, char, pos):
    """
    This function returns an integer which represents the index of the last occurence of the input character in the pos-th index 
    within the wordlist or None if it the character is not found

    Precondition: pos must be <len(word in wordlist)
    Postcondition: 

    Input:
        wordlist: a list of N strings of length M, with each character at the range of 
        lower case {a - z}
        word: a string of length M
        pos: an integer of the n-th position to search
    Return:
        c - 1: an integer representing the index of the last occurence of input character
        None: if character is not found

    Time complexity: 
        Best: O(1) where the last occurence is found on first iteration
        Worst: O(N) where N is the length of wordlist
    Space complexity: 
        Input: O(N) where N is the length of wordlist
        Aux: O(1)

    """
    # lower boundary
    a = 0
    # upper boundary
    b = len(wordlist) - 1
    # while boundary have not crossed each other
    while a <= b:
        # c = midpoint
        c = (a + b) // 2
        # if found:
        if wordlist[c][pos] == char:
            # find first occurence
            while c < len(wordlist) and wordlist[c][pos] == char:
                c += 1
            # return index
            return c - 1
        # if not found and value at c greater than target
        elif wordlist[c][pos] > char:
            # update upper boundary
            b = c - 1
        # if not found and value at c lesser than target
        else:
            # update lower boundary
            a = c + 1
    # if not in list return None
    return None


def local_maxmum(M):
    """
    Returns the coordinate of a local maximum from the input matrix

    Precondition: matrix has to be N x N
    Postcondition:

    Input:
        M: N x N matrix
    Return:
        max: coordinates of a local maximum 
    Time complexity: 
        Best: O(N) where N = len(M)
        Worst: O(N) where N = len(M)
    Space complexity: 
        Input: O(N^2) where N = len(M)
        Aux: O(1)

    """

    # creating border
    row = len(M) // 2
    col = len(M[row]) // 2

    # finding max coordinates of border
    max = [row, col]
    for i in range(len(M)):
        if M[i][col] > M[max[0]][max[1]]:
            max = [i, col]
    for i in range(len(M[row])):
        if M[row][i] > M[max[0]][max[1]]:
            max = [row, i]

    # stepping into quadrant to find max coordinates
    next = next_coord(max, M)
    while next != max:
        max = next
        next = next_coord(max, M)

    # return max coordinates
    return max


def next_coord(current, M):
    """
    Returns the next coordinate to search

    Precondition: matrix has to be N x N, current must be coordinate of M
    Postcondition:

    Input:
        M: N x N matrix
    Return:
        max: coordinates of a the next row and column to search
    Time complexity: 
        Best: O(1)
        Worst: O(1)
    Space complexity: 
        Input: O(N^2) where N is the length of M
        Aux: O(1)

    """
    # initialize max
    max = current
    
    # initialize up down left right coordinates
    # if does not exist, store as empty list 
    up = []
    if current[1]-1 >= 0:
        up = [current[0], current[1]-1]
    right = []
    if current[0] + 1 < len(M):
        right = [current[0]+1, current[1]]
    left = []
    if current[0] - 1 >= 0:
        left = [current[0]-1, current[1]]
    down = []
    if current[1] + 1 < len(M[0]):
        down = [current[0], current[1]+1]
        
    # compare with up down left right
    # update max respectively
    if len(up) != 0 and M[up[0]][up[1]] > M[max[0]][max[1]]:
        max = up
    if len(down) != 0 and M[down[0]][down[1]] > M[max[0]][max[1]]:
        max = down
    if len(right) != 0 and M[right[0]][right[1]] > M[max[0]][max[1]]:
        max = right
    if len(left) != 0 and M[left[0]][left[1]] > M[max[0]][max[1]]:
        max = left
    
    # return max coordinate
    return max


if __name__ == "__main__":
    wordlist = ["hello", "helps", "harpy"]
    word = "hello"
    marker = [1,0,0,1,0]
    trainer(wordlist, word, marker)

