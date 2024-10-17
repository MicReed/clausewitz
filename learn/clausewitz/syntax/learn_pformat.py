from pprint import pformat

data = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': {'nestedKey1': 'nestedValue1', 'nestedKey2': 'nestedValue2'}}
# The indent parameter specifies the number of spaces to use for each indentation level, 
# and the width parameter controls the maximum width of the output, influencing how the structure is broken into multiple lines for readability.
formatted_data = pformat(data, indent=4, width=1)

print(formatted_data)
'''
{   'key1': 'value1',
    'key2': [   1,
                2,
                3],
    'key3': {   'nestedKey1': 'nestedValue1',
                'nestedKey2': 'nestedValue2'}}
'''