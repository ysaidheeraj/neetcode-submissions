class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+= str(len(string))+"#"+string
        return res
    def decode(self, s: str) -> List[str]:
        strs = []
        length = -1
        poundSeen = False
        string = ""
        for i in range(len(s)):
            if poundSeen:
                if length == 0:
                    print(string)
                    strs.append(string)
                    string = ""
                    poundSeen = False
                    length = -1
                else:
                    string += s[i]
                    length -= 1
            else:
                if s[i].isnumeric() and length > -1:
                    length = length * 10 + int(s[i])
                elif s[i] == "#":
                    poundSeen = True
            print(s[i], length)
            if length == -1 and s[i].isnumeric():
                length = int(s[i])
        if length == 0:
            strs.append(string)
        return strs