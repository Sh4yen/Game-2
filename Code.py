leben = 1
while leben == 1:
    
    name = input ("wie lautet dein Name?")
    getränk = input ("Ah ja " + name + " du stehst auf der Gästeliste. Kann ich die was zu trinken bringen? Wir haben:\n a Martini \n b Schnaps\n")
    if getränk == "a":
        martini = input ("geschüttelt oder gerührt")
        if martini == "gerührt":
            print ("Sorry aber so kommst hier nicht rein.\nDu hast verloren!")
            
        elif martini == "geschüttelt":
            print ("a man of culture i see.\nDer Türsteher winkt dich rein. ")
            leben = 0
    elif getränk == "b":
        print ("Sorry aber so kommst hier nicht rein.\nDu hast verloren!")
        
print ("Es hat geklappt")