sentence = input("Enter a sentence:").lower()
term = input("Enter the term to search :").lower()

position = sentence.find(term)

if position >=0:
    print(f" The term '{term}' index position is : {position}")
else:
    print("The term is not found.")