class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if i not in t:
                return False
            s_counter = 0
            t_counter = 0
            for count in range(len(s)):
                if s[count] == i:
                    s_counter += 1
            for count in range(len(t)):
                if t[count] == i:
                    t_counter += 1
            if s_counter != t_counter:
                return False
        return True


s = "anagraam"
"rat"
t = "nagaram"
"car"

print(Solution().isAnagram(s,t))