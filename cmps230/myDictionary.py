myDict = {
    'i':['hadret janebe'],
    'love':['b7ob','bebla3']
}

def translate(word=None):
    if word is None:
        word=input("please enter the source word you wanna translate:")
    if myDict.get(word) is not None:
        return myDict[word]
    else:
        print(f"{word} does not exist in dictionary")
        ans = input(f"do you want to add{word} to dictionary? ").strip().lower()
        while ans not in ['yes','no']:
            ans = input(f"do you want to add {word} to dictionary? ").strip().lower()
        if ans == 'yes':
             addWord(word)
             return myDict[word]
        else:
            return 'Translation not added'

def addWord (word = None,translation=None):
    if word is None:
        word = input("Enter the sourceWord you wanna add to dictionary: ")
    if translation is None:
        translation = input(f"Enter translation for {word}: ")
    
    if word in myDict :
        if translation in myDict[word]:
            return f"{translation} already exists in translations of {word}"
        else:
            myDict[word].append(translation)
            return f"{translation} is a new translation of {word}"
    else :
        myDict[word]=[translation]
        return f"{word} translates into: {translation} "
        
        
#print(f"i translate into : {translate('i')}")
#print(translate()) #the hell?
print(addWord('you','hadret janebak'))
print(addWord('you','hadret janebak'))
print(addWord('you','entaaaaaaaaaaaaaaaaaaaa'))
print()
def displayDictionary(Dict):
    for key, value in Dict.items():
        print(f"{key}---->{value}")
    print()
    
def menu():
    l1='1.Translate a word'
    l2='2.Add a Word to dictionary'
    l2_1='3.Display dictionary'
    l2_2='4.Translate a sentence'
    l3='5.Exist'
    while True:
        print(l1,l2,l2_1,l2_2,l3,sep='\n')
        choice=int(input().strip())
        if choice ==1:
            translate()
        elif choice==2:
            addWord()
        elif choice==3:
            displayDictionary(myDict)
        elif choice==4:
            sentence = input("Enter a sentence: ").split()
            for individualWord in sentence:
                print(f"{individualWord} translates into {translate(individualWord)}")
        elif choice==5:
            break
        else:
            print('Error in input!')
    

menu()

    
        






