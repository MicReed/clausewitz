def unescape(s: str) -> str:
    '''
    The purpose of this function is to convert escape sequences in the input string s into their corresponding characters, effectively "unescaping" any escaped characters in the string. 
    For example, if the input string is '\\n' (representing the escape sequence for a newline character as a literal string), the function returns '\n' (the actual newline character).
    
    '''
    return s.encode().decode('unicode-escape')

print('w\\ts')
unescaped = unescape('w\\ts')
print(unescaped) 
