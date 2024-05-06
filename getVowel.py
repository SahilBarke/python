def getVowel():
    vowel = ['a' , 'e' , 'i' , 'o', 'u']
    string = input("enter the string:")
    match = []
    for char in string:
        for item in vowel:
            if char == item:
                match.append(char)
    print("The matched vowels with the string are:", ", ".join(match))
        
getVowel()

