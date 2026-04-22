# class Solution:
#     def create(self,s):
#         ascii=[0]*26
#         occstr=""
#         for i in range(0,len(s)):
#             ascii[ord(s[i])-97]+=1
#         for i in range(0,len(ascii)):
#             if ascii[i]>0:
#                 occstr+=chr(i+97)
#                 occstr+=chr(ascii[i]+48)
#         return occstr
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict=defaultdict(list)
#         for i in range(0,len(strs)):
#             occstr =self.create(strs[i])
#             dict[occstr].append(strs[i])
#         res=[]
#         for key,val in dict.items():
#             res.append(val)
#         return res