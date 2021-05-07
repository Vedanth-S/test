word=input("Enter a word: ")
if (word[0].isalpha()==True) and ((word[0] in "bcdfghjklmnpqrstvwxyz") or (word[0] in "BCDFGHJKLMNPQRSTVWXYZ")==True):
        print("The Pig latin equivalent of the word is",word[1:len(word)+1]+word[0]+"ay")
else:
    print("The Pig latin equivalent of the word is",word+"yay")

print("hello")

            
    
