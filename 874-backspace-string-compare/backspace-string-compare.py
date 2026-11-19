class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = self.process(s)
        new_t = self.process(t)
        return new_s == new_t
    
    def process(self, a: str) -> str:
        stack = []
        for char in a:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)