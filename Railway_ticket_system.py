import random # FOR pnr
rr = random.randrange(2344634238947,9909345287389233380)
import datetime# for date and time
t = datetime.datetime.now()
coach1A=[[],[]]
coach2A=[[],[]]
coach3A=[[],[]]
coach4A=[[],[]]
def booking():
    print("*) Do You Want to book your seat press \"book\":-")
    press = input("Enter your decison:")
    print("\n")
    x = press.lower()
    if x=="book":
        print("*) How Many ticket you want ?")
        dice = int(input("enter here:"))
        for i in range(dice):
            #Detail
            print("*) Enter Your Name",i+1,":")
            d1 = input()
            d2 = input("*) Enter your Phone number:-")
            d3 = d1 +" "+ d2
            if len(a[0])<4:
               a[0].append(d3)
               for i in range(len(a)):
                   for j in range(len(a[i])):
                       if a[i][j]==d3:
                          print("")
                          print("\nTicket confirmed,Your seat No. is ",i,j,", in ",tr,"at ",b," pm .Your PNR is",rr,t,"\n")
            elif len(a[0])==4:
               a[1].append(d3)
               for i in range(len(a)):
                   for j in range(len(a[i])):
                       if a[i][j]==d3:
                          print("")
                          print("\nTicket confrimed,Your seat No. is ",i,j,", in ",tr,"at ",b," pm .Your PNR is",rr,t,"\n")
    else:
        print('INVALID INPUT !')
        
#
print("       <<<.....SUBH YATRA.....>>>")
while True:
    print(''' from       To          Train. 
himachal    chandigarh  JAN SHATBDI EXPRESS
shimla      delhi       KALKA SHATBDI EXPRESS
punjab      delhi       KALKA MAIL
devghar     nasik       DOON EXPRESS''')
    place1 = input("*) From :")
    x1 = place1.lower()
    place2 = input("*) To :")
    x2 = place2.lower()
    if x1 =='himachal' and x2=="chandigarh":
        print('''*) Dear Yatri ,Train depart form himachal at 4 pm
              Ticket price is :-Rs. 500''')
        tr = "JAN SHATBDI EXPRESS"
        a = coach1A
        b = 4
        booking()
        break
    elif x1 =='shimla' and x2=="delhi":
        print('''*) Dear Yatri ,Train depart form shimla at 2 pm
              Ticket price is :-Rs. 1500''')
        tr = "KALKA SHATBDI EXPRESS"
        a = coach2A
        b = 2
        booking()
        break
    elif x1 =='punjab' and x2=="delhi":
        print('''*) Dear Yatri ,Train depart form punjab at 12 pm
              Ticket price is :-Rs. 1000''')
        tr = "KALKA MAIL"
        a = coach3A
        b = 12
        booking()
        break
    elif x1 =='devghar' and x2=="nasik":
        print('''*) Dear Yatri ,Train depart form devghar at 9 pm
              Ticket price is :-Rs. 150''')
        tr = "DOON EXPRESS"
        a = coach4A
        b = 9
        booking()
        break
    else:
        print("*)Sorry, Train is unavailable...!")
