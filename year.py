year1 = int(input("year"))
zodiac = ['dragon','snake','horse','sheep','monkey','rooster','dog','pig','rat','ox','tiger','hare']
year1 = (year1-2000)%12
print(year1,"is the year of the ",zodiac[year1])

year = int(input("year"))
#print(year)
year = (year-2000)%12
#print(year)
if year==0:
    print(year,"is the year of the dragon")
elif year==1:
    print(year,"is the year of the snake")
elif year==2:
    print(year,"is the year of the horse")
elif year==3:
    print(year,"is the year of the sheep")
elif year==4:
    print(year,"is the year of the monkey")
elif year==5:
    print(year,"is the year of the rooster")
elif year==6:
    print(year,"is the year of the dog")
elif year==7:
    print(year,"is the year of the pig")  
elif year==8:
    print(year,"is the year of the rat")
elif year==9:
    print(year,"is the year of the ox")
elif year==10:
    print(year,"is the year of the tiger")
elif year==11:
    print(year,"is the year of the hare")
else:
    print("is this within the parapters?")

