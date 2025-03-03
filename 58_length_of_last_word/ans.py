# # a = 'string  '
# # print(len(a.rstrip()))

# a = lengthOfLastWord(s="hello   ")
# print(a)
# # i=10
# # while i > 0: 
# #     print(i)
# #     i-=1 


def lengthOfLastWordSol_2(s):
    s = s.strip()
    for i in range(1,len(s)):
        if(s[i*-1] == " "): 
            return i - 1
    return len(s)


def lengthOfLastWord(s):

        s = s.rstrip()
        if len(s) == 1: 
            return 1
        answer = 0
        i = len(s)
        while i > 0:
            i -= 1
            if s[i] == " ":
                break
            else:
                answer += 1
            
        return answer


print(lengthOfLastWord('hello there my name is       '))