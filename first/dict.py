people = {
    'Alice': {
        'phone': 2341,
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar Street'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name:')

request = input('Phone number or address?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
if name in people:
    print("%s's %s is %s." % (name, labels[key], people[name][key]))
