#Program transform the string "Freak out!" into the string "tea"
phrase = "Freak out!"
plist = list(phrase)
print(plist)
print(phrase)
#Removes the letters from the list
plist.remove('F')
plist.remove('r')
plist.remove('k')
plist.remove('o')
plist.remove('u')
#Removes the last item in the list
plist.pop()
#Removes the last two items in the list and then extends 
#back in the into the list. 
plist.extend([plist.pop(), plist.pop()])
#Removes the last item in the list
plist.pop()
#Removes the last item in the list and inserts it in location 0
plist.insert(0, plist.pop())
#Turns plist back into a string and print the results
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

 
