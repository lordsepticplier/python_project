words=input("the string you want to change")
result=[]
change=int(input("and by how much"))
for I in range(len(words)):
       letter=words[I]
       num=ord(letter)+change
       dif=chr(num)     
       result.append(dif)
output="".join(result)
print(output)