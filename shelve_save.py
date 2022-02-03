import shelve
shelfile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfile['cats'] = cats
print(shelfile['cats'])
print(shelfile.keys())
print(shelfile.values())
shelfile.close()
