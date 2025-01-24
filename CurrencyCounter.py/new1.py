def Currencycounter(note,howmanyuhave):
        if(note==1):
            print("Total amount you have:",howmanyuhave*10)
        if(note==2):
            print("Total amount you have:",howmanyuhave*20)
        elif(note==3):
            print("Total amount you have:",howmanyuhave*50)
        elif(note==4):
            print("Total amount you have:",howmanyuhave*100)
        elif(note==5):
            print("Total amount you have:",howmanyuhave*200)
        elif(note==6):
            print("Total amount you have:",howmanyuhave*500)
        elif(note==7):
            print("Total amount you have:",howmanyuhave*2000)
print("1.10RS \n 2.20RS \n 3.50RS \n 4.100RS \n 5.200RS \n 6.500RS \n 7.2000RS \n")
note=int(input(" Enter ur Input:"))
howmanyuhave=int(input(" Enter How many notes u have:"))
s=(Currencycounter(note,howmanyuhave))
