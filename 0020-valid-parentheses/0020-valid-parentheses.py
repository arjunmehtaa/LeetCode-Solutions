mapping = {
    ")":"(", 
    "}": "{", 
    "]": "["
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in mapping:
                if len(stack) == 0 or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0