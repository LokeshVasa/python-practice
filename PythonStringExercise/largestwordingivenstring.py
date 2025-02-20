'''
string1='used as an informal greeting, usually to people who you know'

'''
string1='used as an informal greeting, usually to people who you know'
words=string1.split(' ')
#print(words)   
maxx=0
max_word=''
for word in words:
    #print(word,len(word))
    length=len(word)
    if length>maxx:
        max_word=word
        maxx=length
print(max_word)