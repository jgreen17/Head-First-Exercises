#Transform the string "Freak out!" into the string "Fear"
phrase = "Freak out!"
plist = list(phrase)
print(phrase)
print(plist)
#Loop iterates 6 times, taking 6 objects out the list
for i in range(6):
    plist.pop()
#Takes out last 3 objects out the list and adds them back in 
#Takes out the object the the second location and places it in the first
plist.extend([plist.pop(), plist.pop(), plist.pop()])
plist.insert(1, plist.pop(2))
#Turns the list into a string and prints the results
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)