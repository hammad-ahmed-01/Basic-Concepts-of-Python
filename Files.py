# The following program is designed to count the number of times a certain word appears in a file:'filen.txt'
print('\n A program to count the occurences of a word in the file filen.txt .... ')
print()
# A function 'get_word_frequencies()' is defined 
def get_word_frequencies():
    # The file is opened in read mode
    file=open('filen.txt','r')
    # Data is read from the file and stored in variable data
    data=file.read()
    # All the words are converted to lower case by using a built-in function 'lower()' and stored in variable 'proper_data' to make it easy to apply functions on it
    # also the program should'nt consider full stops and commas, so we replaced that by empty space using a built-in function 'replace()' 
    proper_data=data.lower().replace('.','').replace(',','')
    # The file is spilited into basic words in the form of list called list_of_words 
    list_of_words=proper_data.split()
    # common words like the,and,a are listed down in a list 
    common_words=['the','a','is','and']
    # an empty dictionary named 'dic_count' is created  
    dic_count={}
    # list_of_words is iterated through for loop to judge each word
    for i in list_of_words:
        # a condition is put to ignore the common words defined above in the list 'common_words'
        if i not in common_words:
            # a buit_in function 'count()' is used to count the number of time a certain word appears in the give list 
            count_of_word=list_of_words.count(i)
            # the count is added to the dictionary 'dic_count'
            dic_count[i]=count_of_word
    # the final dictionary is then printed after all the iterations
    print(dic_count)
# the function is then called in order to be executed  
get_word_frequencies()

    
    
        
    

