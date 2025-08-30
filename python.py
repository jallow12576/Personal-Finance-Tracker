name = 'Yaya Jallow'
new_list = []

#for loop to iterate through the name element
for i in range(len(name)):
    new_list.append(name[i])


#list function
name1 = 'Oliver Davis', 'Abubacarr Jaiteh', 'Lamin Bah'
result = list(name1)

hey = name[0:5] #slice method
hi = name.index('y') #index method
new_list.insert(0, 'Hello') #insert method
print(new_list)
print(hey)
print(hi)
print(result)
