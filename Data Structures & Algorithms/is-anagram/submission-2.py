class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_string = list(t)
        counter = 0
        for s_char in s:
            for t_char in t_string:
                if s_char == t_char:
                    t_string.remove(t_char)
                    counter += 1
                    break
        if len(s) == counter:
            return True
        return False
