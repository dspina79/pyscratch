import re

pattern = '[abc]'
text = 'ac'

result = re.match(pattern, text)

if result:
    print(result)
else:
    print('No result found.')