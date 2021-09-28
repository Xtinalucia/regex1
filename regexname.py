import re

with open('regex_test.txt') as f:
    contents = f.read()


pattern = re.compile(' ([A-Z][a-z]+)')
matches = pattern.finditer(contents)
for match in matches:
        
        if match:
            
            print(match.group())
            
            
        else:
            print(None)
                 