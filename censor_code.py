sentence_input=input("Enter your sentence: ")
sentence_list=sentence_input.split()

censor_input=input("Enter the letters or words from your\nsentence you wish to censor: ")
print()

for word in sentence_list:
    if word==censor_input:
        print("***",end=" ")
        continue
    print(word,end=" ")
