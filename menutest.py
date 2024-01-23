import time as tm
import random
import os

# Profile variables
profile_name = "None" # Default if profile_stats is 0
profile_username = "None" # Default if profile_stats is 0
profile_bio = "None" # Default if profile_stats is 0
profile_gender = "Unset" # Default if profile_stats is 0
profile_age = 0 
profile_is_created = 0   # 0 = False while 1 = True


# Money and currency related
currency_related = {
    "money_balance" : 500,
    "credits_balance" : 0,
    "rebirth_level" : 0, # Max is 10 (for now)
    "money_boost" : 0, # 0 = 0% up to 100 which is 100%
}


# Jobs and stuff
job_payout_multipliers = {
    "rookie": 1.2,
    "leader": 2.4,
    "chief": 3.0,
}



job_related = {
    "job_list" : ["Daydreamer", "Guard", "Accountant", 
                  "Content creator", "Police", "Firefighter", 
                  "Banker", "Pilot", "Doctor", 
                  "Famed Chef", "Ground Forces", "Air Forces", 
                  "Marines", "Astronauts", "Housewife"],
    "job_id" : 0, # 0 is unemployed / jobless, starts from id 1 which is daydreamer. Index sync to job_list
    "job_name" : "None",
    "job_rank" : "employed", # 3 ranks for now: rookie, leader, chief
    "job_payout" : 500, # Will increase depends on the job rank and id
    "working_count" : 0 # certain count will promote user in "job rank" 
}

trading_account = 0 # 0 if no trading account is created / 1 if trading account is already created
trading_level = 1 # lower level has higher chance to lose profit when trading
trading_return_worth = 0.50
trading_return_risk = 0.85


mining_account = 0 # 0 is there is no mining account
mining_level = 1 # Will increase each specified blocks mined
minimum_mining_income = 200
maximum_mining_income = 9000
mining_income = random.randint(minimum_mining_income, maximum_mining_income)




def clear():
    os.system('cls')



dash_options = ["Profile",
                "Wallet",
                "Fun Tools",
                "Return"]


menu_options = ["Dashboard",
        "Shop",
        "Quit",
        "Save Game (soon)"]


# --------------------------------------------------------------------------------------------------------------- #
# Functions

def get_job_name_by_id(job_id):
    if 1 <= job_id <= len(job_related["job_list"]):
        return job_related["job_list"][job_id - 1]
    else:
        return "Invalid job_id"


def profile():


    view_profile_state = 0
    view_profile = False

    global in_dash

    global profile_is_created
    global profile_name
    global profile_username
    global profile_bio
    global profile_gender
    global profile_age
    


    if profile_is_created == 0:  # Check if there is a profile created already
        print("You havent set a profile, would like to set a profile now?")
        profile_input_create = input("Yes / No\n> ")
        if profile_input_create == "Yes" or profile_input_create == "yes":
            print("Please set up your name")
            profile_name = input("Your name : ")
            print("Please set up your username")
            profile_username = input("Your username : ")
            print("Please set up your bio")
            profile_bio = input("> ")
            print("Please select your gender :\nGirl\nBoy")
            profile_gender = input("Select your gender (caps sensitive) : ")
            print("Please enter your age")
            profile_age = input("Your age : ")
            print("Congartulation, you have finished setting up your profile")
            tm.sleep(1.2)
            print("To check your profile, go to Dashboard - Profile")
            tm.sleep(2)
            profile_is_created = 1
            in_dash = True

        elif profile_input_create == "No" or profile_input_create == "no":
            print("Alright, exiting profile menu...")
    
    elif profile_is_created == 1:
        view_profile = True
        while view_profile == True: 
            tm.sleep(0.4)
            print("\n#------------------- # Profile # -------------------#")
            print("Name :", profile_name,"\nUsername: ",profile_username,"\nGender : ",profile_gender,"\nAge : ",profile_age,"\nBio : ",profile_bio)
            print("#---------------------------------------------------#\n")
            tm.sleep(1)
            print("If you wish to exit, please type 'Exit'")
            view_profile_state = input(">> ")
            if view_profile_state == "Exit" or view_profile_state == "exit":
                print("Exiting profile...")
                tm.sleep(1.3)
                view_profile = False
                in_dash = True
            
def wallet():
    
    wallet_view = True
    wallet_view_state = 0
    global in_dash


    if currency_related["money_balance"] <= 100:
        print("\nWelcome to your waller, where emptiness fills your space! ")

    elif currency_related["money_balance"] >= 100:
        print("\nWelcome to your wallet, sire, your treasure chest")

    while wallet_view == True:
        tm.sleep(1.733)
        print("\n💲------------------ + Wallet + ------------------💲\n")
        print("💵 Your current balance : ", currency_related["money_balance"])
        tm.sleep(0.3)
        print("🎲 Your credits balance : ", currency_related["credits_balance"])
        tm.sleep(0.3)
        print("🥇 Rebirth Level : ", currency_related["rebirth_level"])
        tm.sleep(0.3)
        print("⭐ Boost : ", currency_related["money_boost"])
        tm.sleep(0.3)
        print("\n#---------------------------------------------------#")
        tm.sleep(1)
        print("If you would like to exit, type 'Exit'") # Planning to add more option in the future
        wallet_view_state = input(">> ").lower()

        if wallet_view_state == "exit": # or exit or ExIt or EXIT
            print("Exiting...")
            tm.sleep(0.4)
            print("Also dont forget to fill your wallet as always!")
            tm.sleep(0.7)
            clear
            wallet_view = False
            in_dash = True

def funtools():
    
    fun_active_menu = True
    fun_active_state = 0
    fun_choosing = 0
    global in_dash
    
    fun_tools_list = ["Work",
                      "Trading",
                      "Mines",
                      "Math quiz",
                      "FrrEe MONey CHHeCk",
                      "The Command Printer",
                      "Exit Fun Section"]

    job_option_id = 0


    random_delay = random.uniform(5, 15)


    
    while fun_active_menu == True:
        tm.sleep(0.3)
        print("Heya, welcome to the fun section where everything is randomized out of my funny brain")
        tm.sleep(0.6)
        print("You can also type 'Exit' if you wish to exit this section")
        tm.sleep(2)
        print("Anyway, whats good?")
        tm.sleep(2.1)
        print("\n---------- * Fun Tools * ----------")
        for i, option in enumerate(fun_tools_list, start=1):
            print(f"[{i}] {option}"), tm.sleep(0.02699)
        print("-----------------------------------")

        fun_choosing = input("Choose your option : ")

        if fun_choosing == "1":
            fun_active_menu == False
            print("You finna work eh?")
            tm.sleep(0.5)
            if job_related["job_id"] == 0:
                print("Buddy you're jobless, get a job")
                tm.sleep(1)
                print("Here is currently the available job for the moment")
                tm.sleep(0.6)
                for i, option in enumerate(job_related["job_list"], start=1):
                    print(f"[{i}] {option}"), tm.sleep(0.08699)
                
                try:
                    job_option_id = int(input("\nJust type the job id (1 ~ 15) : "))
                    job_related["job_name"] = get_job_name_by_id(job_option_id)
                    tm.sleep(1)
                    print("Congrats, you are now working as", job_related["job_name"])
                    job_related["job_id"] = job_option_id
                    job_related["job_rank"] = "Rookie"

                except ValueError:
                    print("Such job doesn't exists bro")
            
            elif job_related["job_id"] != 0:
                print("Lets get to work")
                tm.sleep(0.3)
                print("You are currently working...\nPlease wait up to 20 seconds until you finish your shift")
                
                if job_related["working_count"] == 3:
                    if job_related["job_rank"] == "Rookie":
                        job_related["job_rank"] == "Leader"
                    elif job_related["job_rank"] == "Leader":
                        job_related["job_rank"] == "Chief"
                
                tm.sleep(random_delay)
                print("You have finished your shift, you have earned some money")
                job_related["working_count"] += 1
                if job_related["job_rank"] == "Rookie":
                    job_related["job_payout"] *= job_payout_multipliers["rookie"]
                    currency_related["money_balance"] += job_related["job_payout"]
                    print("Current money balance is", currency_related["money_balance"])
                if job_related["job_rank"] == "Leader":
                    job_related["job_payout"] *= job_payout_multipliers["leader"]
                    currency_related["money_balance"] += job_related["job_payout"]
                    print("Current money balance is", currency_related["money_balance"])
                if job_related["job_rank"] == "Chief":
                    job_related["job_payout"] *= job_payout_multipliers["chief"]
                    currency_related["money_balance"] += job_related["job_payout"]
                    print("Current money balance is", currency_related["money_balance"])

        elif fun_choosing == "7":
           fun_active_menu = False
           in_dash = True
                

            








in_menu = True
in_dash = True


while in_menu == True or in_dash == True :
    print("\n---------- + Main Menu + ----------")
    for i, option in enumerate(menu_options, start=1):
        print(f"[{i}] {option}"), tm.sleep(0.02699)

    menu_input = input("Choose your option : ")
    
    
    if menu_input == "1" :
        in_dash = True
        print("\nWorking on it...")
        tm.sleep(0.7)
        while in_dash == True:
            print("\n\n---------- + Dashboard + ----------")
            for i, option in enumerate(dash_options, start=1):
                print(f"[{i}] {option}"), tm.sleep(0.03)

            dash_input = input("Choose your option : ")

            if dash_input == "1" :
                profile()

            elif dash_input == "2":
                wallet()
            
            elif dash_input == "3":
                funtools()

