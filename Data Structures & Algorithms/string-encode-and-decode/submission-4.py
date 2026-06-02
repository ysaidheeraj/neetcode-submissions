class Solution:

    def encode(self, strs: List[str]) -> str:
        #Adding length of string followed by # for each string
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
            #Reconstructing string once # is found
            if poundSeen:
                if length == 0:
                    strs.append(string)
                    string = ""
                    poundSeen = False
                    length = -1
                else:
                    string += s[i]
                    length -= 1
            #If # is not found, constructing the length number
            else:
                if s[i].isnumeric() and length > -1:
                    length = length * 10 + int(s[i])
                elif s[i] == "#":
                    poundSeen = True
            if length == -1 and s[i].isnumeric():
                length = int(s[i])
        #Appending the final string to the list
        if length == 0:
            strs.append(string)
        return strs