import Menu
global current_resources,coinList
want = ""
current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
menu = Menu.MENU
coinList = []
coin_value_list = {
"penny":.01,
"nickle":.05,
"dime":.10,
"quarter":.25
}



def User_Prompt():
    global want
    valid_choices = ["espresso", "latte", "cappuccino","off","report"]
    want = input("What would you like? [espresso [e] / latte [l] / cappuccino [c]]: ")
    if want == "c":
        want = "cappuccino"
    if want == "l":
        want = "latte"
    if want == "e":
        want = "espresso"
    if want not in valid_choices:
        print ("That is not a valid choice, please try again")
        User_Prompt()
    elif want == "off":
        Off()
    elif want == "report":
        Report()
    else:
        Make_Coffee()

def Check_Resources():
    #print (current_resources)
    #print (f"Cost{ingredients}")
    for key,value in ingredients.items():
        for key2,value2 in current_resources.items():
            if key == key2:
                if value2 - value < 0:
                    print ("We don't have enough resources for this. ")
                    return
                else:
                    current_resources[key2] = value2-value
    Process_Coins()


def Make_Coffee():
    global cost,ingredients
    cost = 0
    if want in menu:
        description = (menu[want])
    for key,value in description.items():
        if key == "ingredients":
            ingredients = value
        if key == "cost":
            cost = round(value,2)
    Check_Resources()


def Process_Coins():
    done = False
    while done == False:
        print ("*****************************")
        print (f"You have deposited ${round(sum(coinList),2)}")
        print (f"The item costs ${cost}")
        proceed = input("Would you like to input coins? (y/n):  ")
        if proceed == "y":
            coin = input("Please enter a coin (penny/nickle/dime/quarter:  ")
            if coin in coin_value_list:
                numCoins = int(input(f"Please enter the number of {coin}s: "))
                for it in range(numCoins):
                    coinList.append(coin_value_list[coin])
            else:
                print ("Not a valid entry, please try again")
        elif proceed == "n":
            if sum(coinList) >= cost:
                done = True
            else:
                print (f"You have not submitted enough money, the item costs: ${cost}")
                print (f"You have submitted ${round(sum(coinList),2)}")
                resume = input("Press return to continue, type 'done' to cancel")
                if resume == "done":
                    return
        if sum(coinList) >= cost:
            done = True
            change = sum(coinList) - cost
            print (f"****\nYou have put in more than enough money ${round(sum(coinList),2)} for your item ({want})")
            print(f"Your change will be: ${change}")
    current_resources["money"] = cost
    #print (current_resources)
    Report()




def Report():
    print(f"\nThe following resources are in the machine after making {want}:\n*********\n")
    for key,value in current_resources.items():
        pre = ""
        unit = ""
        if key == "water" or key == "milk":
            unit = "ml"
        if key == "coffee":
            unit == "g"
        if key == "money":
            pre = "$"
        print (f"{key}:     {pre}{value}{unit}")

def Off():
    print ("Thank you. \n Shutting off now.")
    return

User_Prompt()

































































































#TODO: 1.  Define currency values  -DONE
#TODO: 2.  Create function to turn machine off -DONE
#TODO: 3.  Create dictionary that keeps track of resource values
#TODO: 4.  Ask user what they want-DONE
#TODO: 5.  Check for current resources
#TODO: 6.  Process coins
#TODO: 7.  Check if transaction successful
#TODO: 8.  Check if there are enough resources to make product
#TODO: 9.  Update resources
#TODO: 10. Final message






