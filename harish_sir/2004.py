'''p=open("harish_sir/3.png","rb")
d=p.read()'''
# print(d)
# print("================")
# for i in d:
#     print(i)
# for byte in d:
#     print(format(byte,"08b"))
'''p1=open("newimage.jpg","wb")
p1.write(d)
p.close()
p1.close()
print("reference of thr image has created")'''
'''p=open("name.txt","rb")
d=p.read()
# for i in d:
#     print(i,end="")
# for i in d:
#     print(format(i,"08b"),end="")
p1=open("name2.txt","wb")
p1.write(d)
p.close()
p1.close()'''
'''import pickle
class emp:
    def __init__(self,id,name,sal,add):
        self.id=id
        self.name=name
        self.sla=sal
        self.addr=add
    def dispay(self):
        print(self.id)
        print(self.name)
        print(self.sla)
        print(self.add)
# e=emp(1,"p",10,"k")
# f=open("name12.txt","wb")
# pickle.dump(e,f)
# f.close()
# print("object is  saved into the txt file")'''
import pickle
f=open("name12.txt","rb")
e=pickle.load(f)
e.display()
f.close()
print("object is  saved into the txt file")
