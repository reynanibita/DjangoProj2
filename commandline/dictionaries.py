participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
#print Ola
print(participant['name'])

#Eror because value doent exist
#print(participant['age'])

#number of letters
print(len(participant))

#new key-value
participant['favorite_language'] = 'Python'

#display the numbers 7,42,92
print(participant.pop('favorite_numbers'))

#display all info
print(participant)

#change key value of country to germany
participant['country'] = 'Germany'

#display all new info
print(participant)
