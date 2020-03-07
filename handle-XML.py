import xml.etree.ElementTree as ET 

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input) 
lst = stuff.findall('users/user')
print('Users count: ', len(lst) )

for user in lst: 
    print('Name: ', user.find('name').text)
    print('id: ', user.find('id').text)
    print('Attribute: ', user.get("x"))


