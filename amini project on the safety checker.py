from operator import mul
def check_safety(temp,pressure,equipment):
    if temp<100:
        temp_points = 1
    elif temp<=120:
        temp_points = 0.5
    else: 
        temp = 120
        temp_points = 0
    if pressure<200:
        pressure_points = 1
    elif pressure<=250:
        pressure_points = 0.5
    else:
        presssure = 250
        pressure_points = 0
    if equipment.lower() == "yes":
        equip_points = 1
    else :
        equip_points = 0
    score = mul(temp_points,0.4)+mul(pressure_points,0.4)+mul(equip_points,0.2)
    if score>=0.8:
        status = "safe"
    elif score>=0.5:
        status = "warning"
    else:
        status = "unsafe"
    return status , score*100
def safety_checker():
    while True:
        print("safety checker")
        print("1.check safety")
        print("2.exit")
        try:
            choice = int(input("enter your choice:"))
            if choice == 2:
                print("exiting from the safety checker")
                break
            elif choice !=1:
                print("invalid choice!try the choices 1 or 2")
                continue
            if choice ==1:
                temp = float(input("enter the temperature:"))
                if temp<-273.15:
                    print("temperature cannot be less than -273.15, try again!!!")
                pressure = float(input("enter the pressure:"))    
                if pressure<0:
                    print("pressure cannot be less than 0,try other than 0!!!!!")
                equipment = input("Is equipment working").strip().lower()
                if equipment not in ["yes","no"]:
                    print("error!!! please enter yes or no")
                    continue
                status , score = check_safety(temp,pressure,equipment)
                print(f"safety status:{status} (score:{score:.2f})")
        except ValueError:
            print("error,please enter valid numbers!!")
        except Exception as e:
            print(f"an unexpected error occurred: {e}")
            if __name__ == "__main__":
                safety_checker()


     

