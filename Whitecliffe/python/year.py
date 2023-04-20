year1 = int(input("year"))
zodiac = ['dragon','snake','horse','sheep','monkey','rooster','dog','pig','rat','ox','tiger','hare']
year1 = (year1-2000)%12
print(year1,"is the year of the ",zodiac[year1])


year = int(input("year"))
print(year)
year = (year-2000)%12
print(year)
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


mag = float(input("magnitude"))
#print(mag)
if mag<2.0:
    print(mag,"is micro")
elif mag<3.0:
    print(mag,"is very minor")
elif mag<4.0:
    print(mag,"is minor")
elif mag<5.0:
    print(mag,"is light")
elif mag<6.0:
    print(mag,"is moderate")
elif mag<7.0:
    print(mag,"is strong")
elif mag<8.0:
    print(mag,"is major")
elif mag<10.0:
    print(mag,"is great")
elif mag>=10.0:
    print(mag,"is meteoric")
else:
    print("is this within the parapters?")


sou = int(input("sound level"))
#print(sou)
if sou>130:
    print(sou,"is loader then even the mighty jackhammer")
elif sou==130:
    print("jackhammer")
elif sou>106:
    print(sou,"is between jackhammer and petrol lawnmower")
elif sou==106:
    print("petrol lawnmower")
elif sou>70:
    print(sou,"is between petrol lawnmower and alarm clock")
elif sou==70:
    print("alarm clock")
elif sou>40:
    print(sou,"is between alarm clock and quite room")
elif sou==40:
    print("quite room")
elif sou<40:
    print(sou,"is quiter then even the sly quite room")
else:
    print("is this within the parapters?")


voco = input("letter")
#print(voco)
if voco=="a":
    print(voco,"is vowel")
elif voco=="e":
    print(voco,"is vowel")
elif voco=="i":
    print(voco,"is vowel")
elif voco=="o":
    print(voco,"is vowel")
elif voco=="u":
    print(voco,"is vowel")
elif voco=="y":
    print(voco,"is vowel sometimes and other times a consonant")
else:
    print(voco,"is a consonant")
