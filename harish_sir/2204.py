# regular expresssion[RegEx]:
#match
import re
text="python is super super easy"
regex=r"python"
data=re.match(regex,text)
print(data)
#super
import re
text="python is super super easy"
regex=r"super"
data=re.search(regex,text)
print(data)
#findall
import re
text="python is super super easy"
regex=r"super"
data=re.findall(regex,text)
print(data)
#.dot metacharacter
import re
text="python is super super easy"
regex=r"."
data=re.findall(regex,text)
print(data)
# \ escap metacharacter
import re
text="python is super.  super.    . easy"
regex=r"\."
data=re.findall(regex,text)
print(data)
#|pipe metacharacter
import re
text="python is super super easy"
regex=r"is|super"
data=re.findall(regex,text)
print(data)
#* star metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"p*ython"
data=re.findall(regex,text)
print(data)
# + plus metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"p+ython"
data=re.findall(regex,text)
print(data)
# ? question mark metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"p?ython"
data=re.findall(regex,text)
print(data)
# ^ hat metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"^a"
data=re.findall(regex,text)
print(data)
# $doller metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"pppppython$"
data=re.findall(regex,text)
print(data)
# []character class metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"[p]"
data=re.findall(regex,text)
print(data)
# {} metacharacter
import re
text="a python is ython not pppython and pppppython"
regex=r"p{1,3}ython"
data=re.findall(regex,text)
print(data)