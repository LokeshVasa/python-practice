from collections import Counter
available_parking_space=100

vehicles_occu={
    "car":7,
    "bike":4,
    "bus":14
    
}

incoming_veh=["bus", "car", "bike", "car", "bike", "bus", "car", "car", "car", "bike","car", "car", "car","bus","bus"]
register={}
for vehicle in incoming_veh:    
    occu= vehicles_occu[vehicle]
    if available_parking_space >= occu:
        if not vehicle in register.keys():
            register[vehicle]=1
        elif vehicle in register.keys():
            register[vehicle]+=1
        
        available_parking_space= available_parking_space - occu
         
    else:
        print("not space")
        break
# for vechicle_type in set(register):
#     print(vechicle_type, " - ", register.count(vechicle_type))
    
print(register)
print(available_parking_space)

# register = {
#     "bikes": ,
#     "car": ,
#     "bus": 
# }       

# total_occupied_space 
         
                                    

