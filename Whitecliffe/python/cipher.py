words=input("the string you want to change")
result=[]
change=int(input("and by how much"))
for I in range(len(words)):
       letter=words[I]
       num=ord(letter)+change  # changes letter into it's numical number and adds the change
       dif=chr(num)  # changes num into what letter it's number represents     
       result.append(dif)  # adds it onto the results list
output="".join(result)  # combines all of the lists boxs into one string
print(output)