#!/usr/bin/env python3
# A phone number database.

people = {
    'talen':{
        'phone': '12345',
        'addr': 'china'
    },
    'alex':{
        'phone': '3455',
        'addr': 'us'
    },
    'lina':{
        'phone': '5678',
        'addr': 'en'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name:')

request = input('Phone[p] or address[a]?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

# 4.1
if name in people:
    print("{}'s {} is {}".format(name, labels[key], people[name][key]))

person = people.get(name, {})
print(person)
label = labels.get(key, key)
result = person.get(key, 'not available.')

print("{}'s {} is {}".format(name, label, result))
print(people.items())
