def isValid(s: str) -> bool:
   
    stack = []
    
    
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    
    for char in s:
        
        if char in '({[':
            stack.append(char)
       
        elif char in ')}]':
           
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    

    return len(stack) == 0


print(isValid("()"))       
print(isValid("()[]{}"))   
print(isValid("(]"))      
