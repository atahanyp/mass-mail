import os

comps = []
mails = []
with open("mails.txt","r",encoding="utf-8") as f:
    for a in f.readlines():
        a = a.replace("\n","")
        a = a.replace("  ","")
        mails.append(a)
  
print(mails)  

with open("isims.txt","r",encoding="utf-8") as f:
    for a in f.readlines():
        a = a.replace("\n","")
        a = a.replace("  ","")
        comps.append(a)


print(comps)



   
    



