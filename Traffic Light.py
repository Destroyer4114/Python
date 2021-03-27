def tl():
    signal = input("Enter color of traffic lights: ")
    if signal not in ("RED","GREEN","YELLOW"):
        print("Error")
    else:
        i = l(signal)
        if i == 0:
            print("Go")
        elif i == 1:
            print("Wait")
        else:
            print("Stop")
def l(signal):
    if signal == "GREEN":
        i = 0
    elif signal =="YELLOW":
        i = 1
    else:
        i=2
    return i


tl()
print("SPEED THRILLS BUT KILLS\nTHANK YOU")
