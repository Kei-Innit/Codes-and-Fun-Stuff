# Masalah kewangan / currency related of a Cafe
# Idk man just read the comment for the manual later
# Includes everything related on a store
# e.g : electricity cost, ingredient cost, water cost etc etc



# Packages / Modules imported

import os
import time as tm
from rich import print
from rich.console import Console
from rich.text import Text



# Clearing terminal for a new and clean look


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen


# Self defined functions



# Basic cost functions

def basic_cost():

    confirmation1 = 0 # 0 as true while 1 as false
    confirmation_input = 0 # 0 as blank
    calculating_status = 0 # 0 as true while 1 as false
    monthly = 0
    yearly = 0
    global start_status
    global status_menu

    while confirmation1 == 0:
        csltext.print("[blue]Would you like to calculate Cafe utility cost per month (and year)?\n[bold green]Yes[/bold green] or [bold red]No[/bold red]")
        confirmation_input = input(">>  ").lower()
        if confirmation_input == "yes" or confirmation_input == "y":
            print("Alright, please enter the correct information below")
            confirmation1 = 1
            calculating_status = 1
            start_status = 1
            while calculating_status == 1:
                basic_costs["electricity_usage_per_month"] = float(input("Electricity usage per month (kWH) : "))
                basic_costs["electricity_cost_per_kilowatt"] = float(input("Electricity costs per kilowatt : "))
                basic_costs["water_usage_per_month"] = float(input("Water usage per month (litre) : "))
                basic_costs["water_cost_per_litre"] = float(input("Water cost per litre : "))
                basic_costs["rent_of_building_per_month"] = float(input("Rent of lot per month : "))
                basic_costs["internet_cost_per_month"]  = float(input("Internet cost per month : "))
                print("Total utility cost has been calculated")
                basic_costs["electricity_total_cost"] = basic_costs["electricity_usage_per_month"] * basic_costs["electricity_cost_per_kilowatt"]
                basic_costs["water_total_cost"] = basic_costs["water_usage_per_month"] * basic_costs["water_cost_per_litre"]
                basic_costs["total_cost_everything"] = basic_costs["electricity_total_cost"] + basic_costs["water_total_cost"] + basic_costs["rent_of_building_per_month"] + basic_costs["internet_cost_per_month"]
                basic_costs["electricity_percentage_usage"] = (basic_costs["electricity_total_cost"] / basic_costs["total_cost_everything"]) * 100
                basic_costs["water_percentage_usage"] = (basic_costs["water_total_cost"] / basic_costs["total_cost_everything"]) * 100
                print()
                print("+-----------------------------------------+")
                csltext.print("[bold blue]Electricity cost per month :", round(basic_costs["electricity_total_cost"], 2), "[green]MYR")
                csltext.print("[bold cyan]Water cost per month : ", round(basic_costs["water_total_cost"], 2), "[green]MYR")
                csltext.print("[yellow]Total cost per month is : ", round(basic_costs["total_cost_everything"], 2), "[green]MYR")
                tm.sleep(0.5)
                yearly = basic_costs["total_cost_everything"] * 12
                print("+-----------------------------------------+")
                csltext.print("[gold1]Total cost per year is :", yearly, "[green]MYR")
                calculating_status = 0
                confirmation1 = 0
                # Determination of usage
                print("+-----------------------------------------------------------------------------+")
                print("Percentage of utility has been determined")
                print("[cyan]Electricity usage : ", round(basic_costs["electricity_percentage_usage"], 2), "%")
                print("[blue]Water usage : ", round(basic_costs["water_percentage_usage"], 2), "%")
                tm.sleep(2)
                if round(basic_costs["electricity_percentage_usage"], 2) >= 50: # If electric usage is more than 50%
                    print()
                    csltext.print("[bold]You should consider lowering the usage of electricity as it is beyond average usage that is currently up to", round(basic_costs["electricity_percentage_usage"], 2), "%")
                    print()
                elif round(basic_costs["water_percentage_usage"], 2) >= 50: # If water usage is more than 50%
                    print()
                    csltext.print("[bold]You should consider lowering the usage of water as it is beyond average usage that is currently up to", round(basic_costs["water_percentage_usage"], 2), "%")
                    print()

                elif round(basic_costs["water_percentage_usage"], 2) and round(basic_costs["electricity_percentage_usage"], 2) <= 39: # If electric usage and water usage is less than 39%
                    print()
                    csltext.print("[bold green1]Your cafe utility (water and electricity) usage is currently below average of usage, keep it up! ")
                    print()

                elif round(basic_costs["water_percentage_usage"], 2) and round(basic_costs["electricity_percentage_usage"], 2) >= 40: # If electric usage and water usage is more than 40%
                    print()
                    csltext.print("[bold red]Your cafe utility (water and electricity) usage is currently above average of usage, please consider minimising the usage as it can result in a loss of income")

                print("+-----------------------------------------------------------------------------+")
                tm.sleep(5)


# Exit option

        elif confirmation_input == "no" or confirmation_input == "n":
            print("Wilco, returning")
            tm.sleep(1)
            clear_terminal()
            confirmation1 = 1
            start_status = 0
            
        else:
            print("That is not a valid input.")
            tm.sleep(0.7)
            print("\n")




# Core cost function

def core_cost():
    
    confirmation1 = 0
    confirmation_input = 0
    calculating_status = 0
    option_calc = 0
    option_calc_choose = 0
    monthly = 0
    yearly = 0
    global start_status
    global status_menu
    while confirmation1 == 0:
        csltext.print("[blue_violet]Would you like to calculate the core cost of cafe? This also includes workers and ingredients used[/blue_violet]\n[green]Yes[/green] or [red]No[/red]")
        confirmation_input = input(">>  ").lower()
        if confirmation_input == "yes" or confirmation_input == "y":
            option_calc = 0
            while option_calc == 0:
                print("Please choose your calculator option: ")
                print("[blue]1. Ingredients Calculator")
                print("[#7353BA]2. Labor Cost Calculator")
                option_calc_choose = input(">> ")
                # Prices of ingredient
                if option_calc_choose == "1":
                    option_calc = 1
                    print("Okay")
                    print("Please enter the correct information below")
                    confirmation1 = 1
                    calculating_status = 1
                    start_status = 1
                    while calculating_status == 1: # User inputs
                        ingredients["ice"] = float(input("Bag of ice used per month : "))
                        ingredients["ice_price"] = float(input("Average cost of bag of ice (monthly) : "))
                        ingredients["coffee_beans"] = float(input("Coffee bean used per month (packet) : "))
                        ingredients["coffee_beans_price"] = float(input("Average cost of coffee bean (monthly) : "))
                        ingredients["creamers"] = float(input("Creamer used per month (cans) : "))
                        ingredients["creamers_price"] = float(input("Average cost of can of creamers (monthly) : "))
                        ingredients["sugars"] = float(input("Sugar used per month (packet) : "))
                        ingredients["sugar_price"] = float(input("Average cost of sugar per packet (monthly) : "))
                        ingredients["salts"] = float(input("Salt used per month (packet) : "))
                        ingredients["salts_price"] = float(input("Average cost of salt per packet (monthly) : "))
                        ingredients["chocolate_syrup"] = float(input("Chocolate syrup used per month (bottle) : "))
                        ingredients["chocolate_syrup_price"] = float(input("Average cost of chocolate syrup per bottle (monthly) : "))
                        ingredients["caramel_syrup"] = float(input("Caramel syrup used per month (bottle) : "))
                        ingredients["caramel_syrup_price"] = float(input("Average carammel of syrup used per bottle (monthly) : "))
                        ingredients["whipping_cream"] = float(input("Whipping cream used per month (cans) : "))
                        ingredients["whipping_cream_price"] = float(input("Average cost of whipping cream per bottle (monthly) : "))
                        ingredients["condensed_milk"] = float(input("Condensed milk used per month (cans) : "))
                        ingredients["condensed_milk_price"] = float(input("Average cost of condensed milk per can (monthly) : "))
                        ingredients["liquid_milk"] = float(input("Liquid milk used per month (cans) : "))
                        ingredients["liquid_milk_price"] = float(input("Average cost of liquid milk per can (monthly) : "))
                        ingredients["chocolate_topping"] = float(input("Chocolate topping used per month (cans) : "))
                        ingredients["chocolate_topping_price"] = float(input("Average cost of chocolate topping per can (monthly) : "))
                        ingredients["roll_biscuit_topping"] = float(input("Biscuit roll topping used per month (cans) : "))
                        ingredients["roll_biscuit_top_price"] = float(input("Average cost of biscuit topping per can (monthly) : "))
                        # Prints output from input
                        print("+--------------------------------------------------------------------------------------+")
                        ingredients["ice_price_total"] = float(ingredients["ice"] * ingredients["ice_price"])
                        ingredients["coffee_beans_price_total"] = float(ingredients["coffee_beans"] * ingredients["coffee_beans_price"])
                        ingredients["creamers_price_total"] = float(ingredients["creamers"] * ingredients["creamers_price"])
                        ingredients["sugar_price_total"] = float(ingredients["sugars"] * ingredients["sugar_price"])
                        ingredients["salts_price_total"] = float(ingredients["salts"] * ingredients["salts_price"])
                        ingredients["chocolate_syrup_price_total"] = float(ingredients["chocolate_syrup"] * ingredients["chocolate_syrup_price"])
                        ingredients["caramel_syrup_price_total"] = float(ingredients["caramel_syrup"] * ingredients["caramel_syrup_price"])
                        ingredients["whipping_cream_price_total"] = float(ingredients["whipping_cream"] * ingredients["whipping_cream_price"])
                        ingredients["condensed_milk_price_total"] = float(ingredients["condensed_milk"] * ingredients["condensed_milk_price"])
                        ingredients["liquid_milk_price_total"] = float(ingredients["liquid_milk"] * ingredients["liquid_milk_price"])
                        ingredients["chocolate_topping_price_total"] = float(ingredients["chocolate_topping"] * ingredients["chocolate_topping_price"])
                        ingredients["roll_biscuit_top_price_total"] = float(ingredients["roll_biscuit_topping"] * ingredients["roll_biscuit_top_price"])

                        ingredients["total_cost"] = (ingredients["ice_price_total"] + ingredients["coffee_beans_price_total"] + ingredients["creamers_price_total"] + ingredients["sugar_price_total"] + ingredients["salts_price_total"] + ingredients["chocolate_syrup_price_total"] + 
                                                     ingredients["caramel_syrup_price_total"] + ingredients["whipping_cream_price_total"] + ingredients["condensed_milk_price_total"] + ingredients["liquid_milk_price_total"] + ingredients["chocolate_topping_price_total"] + ingredients["roll_biscuit_top_price_total"])



                        csltext.print("Total cost of Ice per month [green](MYR)[/green] : ", round(ingredients["ice_price_total"], 2))
                        tm.sleep(0.3)
                        csltext.print("Total cost of Coffee Beans per month [green](MYR)[/green] : ", round(ingredients["coffee_beans_price_total"], 2))
                        tm.sleep(0.4)
                        csltext.print("Total cost of Creamers per month [green](MYR)[/green] : ", round(ingredients["creamers_price_total"], 2))
                        tm.sleep(0.2)
                        csltext.print("Total cost of Sugar per month [green](MYR)[/green] : ", round(ingredients["sugar_price_total"], 2))
                        tm.sleep(0.3)
                        csltext.print("Total cost of Salt per month [green](MYR)[/green] : ", round(ingredients["salts_price_total"], 2))
                        tm.sleep(0.4)
                        csltext.print("Total cost of Chocolate Syrup per month [green](MYR)[/green] : ", round(ingredients["chocolate_syrup_price_total"], 2))
                        tm.sleep(0.4)
                        csltext.print("Total cost of Caramel Syrup per month [green](MYR)[/green] : ", round(ingredients["caramel_syrup_price_total"], 2))
                        tm.sleep(0.3)
                        csltext.print("Total cost of Whipping Cream per month [green](MYR)[/green] : ", round(ingredients["whipping_cream_price_total"], 2))
                        tm.sleep(0.4)
                        csltext.print("Total cost of Condensed Milk per month [green](MYR)[/green] : ", round(ingredients["condensed_milk_price_total"], 2))
                        tm.sleep(0.3)
                        csltext.print("Total cost of Liquid Milk per month [green](MYR)[/green] : ", round(ingredients["liquid_milk_price_total"], 2))
                        tm.sleep(0.2)
                        csltext.print("Total cost of Chocolate Topping per month [green](MYR)[/green] : ", round(ingredients["chocolate_topping_price_total"], 2))
                        tm.sleep(0.2)
                        csltext.print("Total cost of Roll Biscuit Topping per month [green](MYR)[/green] : ", round(ingredients["roll_biscuit_top_price_total"], 2))
                        

                        
                        
                        print("+-----------------------------------------+")
                        csltext.print("[yellow]Total ingredients cost per month is : ", ingredients["total_cost"], "[green]MYR") # Prints out monthly output
                        tm.sleep(0.5)
                        yearly = ingredients["total_cost"] * 12 # Multiply for yearly
                        print()
                        print("+-----------------------------------------+")
                        csltext.print("[gold1]Total cost per year is :", round(yearly, 2), "[green]MYR") # Prints out yearly output
                        calculating_status = 0 # Break while
                        confirmation1 = 0 # Break while
                        print()
                        print("+-----------------------------------------------------------------------------+")
                        print()
                        tm.sleep(5)
                
                
                # Ranks and stuff related to rank
                elif option_calc_choose == "2":
                    option_calc = 1
                    print("Okay")
                    print("Please enter the correct information below")
                    confirmation1 = 1
                    calculating_status = 1
                    start_status = 1
                    while calculating_status == 1:
                        print("+------------------------------------------+")
                        print("1. Cashier")
                        workers_costs["worker_ranks"]["cashier"]["payout"] = int(input("Payout amount (monthly) for Cashier : "))
                        workers_costs["worker_ranks"]["cashier"]["count"] = int(input("Total Cashier available : "))
                        workers_costs["worker_ranks"]["cashier"]["total"] = (workers_costs["worker_ranks"]["cashier"]["payout"] * workers_costs["worker_ranks"]["cashier"]["count"])
                        print("+------------------------------------------+")
                        print("2. Barista")
                        workers_costs["worker_ranks"]["barista"]["payout"] = int(input("Payout amount (monthly) for Barista : "))
                        workers_costs["worker_ranks"]["barista"]["count"] = int(input("Total Barista available : "))
                        workers_costs["worker_ranks"]["barista"]["total"] = (workers_costs["worker_ranks"]["barista"]["payout"] * workers_costs["worker_ranks"]["barista"]["count"])
                        print("+------------------------------------------+")
                        print("3. Waiter")
                        workers_costs["worker_ranks"]["waiter"]["payout"] = int(input("Payout amount (monthly) for Waiter : "))
                        workers_costs["worker_ranks"]["waiter"]["count"] = int(input("Total Waiter available : "))
                        workers_costs["worker_ranks"]["waiter"]["total"] = (workers_costs["worker_ranks"]["waiter"]["payout"] * workers_costs["worker_ranks"]["waiter"]["count"])
                        print("+------------------------------------------+")
                        print("4. Cleaner")
                        workers_costs["worker_ranks"]["cleaner"]["payout"] = int(input("Payout amount (monthly) for Cleaner : "))
                        workers_costs["worker_ranks"]["cleaner"]["count"] = int(input("Total Cleaner available : "))
                        workers_costs["worker_ranks"]["cleaner"]["total"] = (workers_costs["worker_ranks"]["cleaner"]["payout"] * workers_costs["worker_ranks"]["cleaner"]["count"])
                        print("+------------------------------------------+")
                        print("5. Shift Supervisor / Supervisor")
                        workers_costs["worker_ranks"]["supervisor"]["payout"] = int(input("Payout amount (monthly) for Supervisor : "))
                        workers_costs["worker_ranks"]["supervisor"]["count"] = int(input("Total Supervisor available : "))
                        workers_costs["worker_ranks"]["supervisor"]["total"] = (workers_costs["worker_ranks"]["supervisor"]["payout"] * workers_costs["worker_ranks"]["supervisor"]["count"])
                        print("+------------------------------------------+")
                        print("6. Manager")
                        workers_costs["worker_ranks"]["manager"]["payout"] = int(input("Payout amount (monthly) for Manager : "))
                        workers_costs["worker_ranks"]["manager"]["count"] = int(input("Total Manager available : "))
                        workers_costs["worker_ranks"]["manager"]["total"] = (workers_costs["worker_ranks"]["manager"]["payout"] * workers_costs["worker_ranks"]["manager"]["count"])
                        print("+------------------------------------------------------------------------------------------------------------------------+")
                        csltext.print("[violet]Total : \n-------------------------------------------------------------------------------------------------")
                        print("Total payout monthly for Barista : MYR",workers_costs["worker_ranks"]["barista"]["total"])
                        print("Total payout monthly for Cashier : MYR",workers_costs["worker_ranks"]["cashier"]["total"])
                        print("Total payout monthly for Waiter : MYR",workers_costs["worker_ranks"]["waiter"]["total"])
                        print("Total payout monthly for Cleaner : MYR",workers_costs["worker_ranks"]["cleaner"]["total"])
                        print("Total payout monthly for Supervisor : MYR",workers_costs["worker_ranks"]["supervisor"]["total"])
                        print("Total payout monthly for Manager : MYR",workers_costs["worker_ranks"]["manager"]["total"])
                        workers_costs["total_of_workers"] = (workers_costs["worker_ranks"]["barista"]["count"] + workers_costs["worker_ranks"]["cashier"]["count"] + workers_costs["worker_ranks"]["waiter"]["count"] + workers_costs["worker_ranks"]["cleaner"]["count"] + workers_costs["worker_ranks"]["supervisor"]["count"] + workers_costs["worker_ranks"]["manager"]["count"])
                        workers_costs["worker_sallary_total_monthly"] = (workers_costs["worker_ranks"]["barista"]["total"] + workers_costs["worker_ranks"]["cashier"]["total"] + workers_costs["worker_ranks"]["cleaner"]["total"] + workers_costs["worker_ranks"]["supervisor"]["total"] + workers_costs["worker_ranks"]["manager"]["total"])
                        print("[bright_blue]Total workers : ",workers_costs["total_of_workers"])
                        print("[bright_green]Total payout monthly : MYR",workers_costs["worker_sallary_total_monthly"])
                        calculating_status = 0
                        confirmation1 = 0
                        print()
                        print("+-----------------------------------------------------------------------------+")
                        print()
                        tm.sleep(5)
                                          
            
            
        elif confirmation_input == "no" or confirmation_input == "n":
            print("Wilco, returning")
            tm.sleep(1)
            clear_terminal()
            confirmation1 = 1
            start_status = 0
            
        else:
            print("That is not a valid input.")
            tm.sleep(0.7)
            print("\n")





# Income related function  
    
def income_calculator():
    
    confirmation1 = 0 # 0 as true while 1 as false
    confirmation_input = 0 # 0 as blank
    calculating_status = 0 # 0 as true while 1 as false
    monthly = 0
    yearly = 0
    global start_status
    global status_menu

    while confirmation1 == 0:
        csltext.print("[blue]Would you like to calculate income per month (and year)?\n[bold green]Yes[/bold green] or [bold red]No[/bold red]")
        confirmation_input = input(">>  ").lower()
        if confirmation_input == "yes" or confirmation_input == "y":
            print("Alright, please enter the correct information below")
            confirmation1 = 1
            calculating_status = 1
            start_status = 1
            while calculating_status == 1:
                # User inputs
                incomes_related["beverage_sales_per_month"] = float(input("Beverage / Drinks sales per month (average) : "))
                incomes_related["food_sales_per_month"] = float(input("Food sales per month (average) : "))
                incomes_related["tips_bonus_monthly"] = float(input("Average of tip given by customer : "))
                incomes_related["sponsorship"] = float(input("Total income from sponsership : "))
                incomes_related["online_sales_monthly"] = float(input("Total online sales per month (average) : "))
                print("Total of income has been calculated")
                incomes_related["food_beverage_sales_per_month"] = (incomes_related["beverage_sales_per_month"] + incomes_related["food_sales_per_month"])
                incomes_related["total_sales_per_month"] = (incomes_related["food_beverage_sales_per_month"] + incomes_related["tips_bonus_monthly"] + incomes_related["sponsorship"] + incomes_related["online_sales_monthly"])
                incomes_related["food_beverage_sales_percentage"] = (incomes_related["food_beverage_sales_per_month"] / incomes_related["total_sales_per_month"]) * 100
                print("[pale_turquoise1 bold]\nLet say if average monthly sale is") # Prints out total result
                print("+------------------------------------------------------------------------------------------------------------------------+")
                tm.sleep(0.5)
                print("Food and Beverage sale : ", incomes_related["food_beverage_sales_per_month"], "MYR")
                print("Sponsorship : ", incomes_related["sponsorship"], "MYR")
                print("Tips from customer : ", incomes_related["tips_bonus_monthly"], "MYR")
                print("Online sale : ", incomes_related["online_sales_monthly"], "MYR")
                tm.sleep(1)
                print("+------------------------------------------------------------------------------------------------------------------------+")
                csltext.print("[#70D6FF]Total income per month is : ", incomes_related["total_sales_per_month"]) # Prints out monthly output
                csltext.print("[#00F0B5]Total income per year is : ", (incomes_related["total_sales_per_month"] * 12)) # Prints out yearly output
                print("+----------------------------------------------------------------------------------+")
                tm.sleep(5.5)
                csltext.print("[#1640D6]Analyzing data")
                tm.sleep(0.3)
                # Determine whether cafe is in average profit gain or below average
                if incomes_related["food_beverage_sales_percentage"] >= 60: # If food and beverage sale is 60% of the total monthly income
                    print("Your cafe profit is average as your sale of food and beverage is", round(incomes_related["food_beverage_sales_percentage"], 2), "% your income.","\nKeep it up!")
                else: # If food and beverage sale is less than 60% of the total monthly income
                    print("Your cafe main profit is below average, consider improving sales")
                    print("To optimize your cafe's performance, consider increasing the contribution of food and beverage sales, which currently make up", round(incomes_related["food_beverage_sales_percentage"], 2), "% the total profit.")

                
                tm.sleep(7)
                print("+----------------------------------------------------------------------------------+")
                calculating_status = 0
                confirmation1 = 0



        elif confirmation_input == "no" or confirmation_input == "n":
            print("Wilco, returning")
            tm.sleep(1)
            clear_terminal()
            confirmation1 = 1
            start_status = 0
            
        else:
            print("That is not a valid input.")
            tm.sleep(0.7)
            print("\n")
    
    


# Coloring text variable

csltext = Console() # Set rich color printing to csltext so it can be easier to type and call out e.g csltext.print([color_name] I love you [/color_name])
# Using this or some basic printing function allows the programmer to set color for their output printing
# Any [colorname format] in print or csltext.print will be counted as color/format name for the text while the [/colorname format] indicates the closure of the format / colored text





# This is a dictionary, containing variables. Can be use in function (def) without using the 'global'
basic_costs = {
    "electricity_usage_per_month" : 0,
    "electricity_cost_per_kilowatt" : 0,
    "electricity_percentage_usage" : 0,
    "water_usage_per_month" : 0,
    "water_cost_per_litre" : 0,
    "water_percentage_usage" : 0,
    "rent_of_building_per_month" : 0,
    "internet_cost_per_month" : 0,
    "electricity_total_cost" : 0,
    "water_total_cost" : 0, 
    "total_cost_everything" : 0

    
}




ingredients = {
    "ice" : 0,
    "ice_price" : 0,
    "ice_price_total" : 0,
    "coffee_beans" : 0,
    "coffee_beans_price" : 0,
    "coffee_beans_price_total" : 0,
    "creamers" : 0,
    "creamers_price" : 0,
    "creamers_price_total" : 0,
    "sugars" : 0,
    "sugar_price" : 0,
    "sugar_price_total" : 0,
    "salts" : 0,
    "salts_price" : 0,
    "salts_price_total" : 0,
    "chocolate_syrup" : 0,
    "chocolate_syrup_price" : 0,
    "chocolate_syrup_price_total" : 0,
    "caramel_syrup" : 0,
    "caramel_syrup_price" : 0,
    "caramel_syrup_price_total" : 0,
    "whipping_cream" : 0,
    "whipping_cream_price" : 0,
    "whipping_cream_price_total" : 0,
    "condensed_milk" : 0,
    "condensed_milk_price" : 0,
    "condensed_milk_price_total" : 0,
    "liquid_milk" : 0,
    "liquid_milk_price" : 0,
    "liquid_milk_price_total" : 0,
    "chocolate_topping" : 0,
    "chocolate_topping_price" : 0,
    "chocolate_topping_price_total" : 0,
    "roll_biscuit_topping" : 0,
    "roll_biscuit_top_price" : 0,
    "roll_biscuit_top_price_total" : 0,
    "total_cost" : 0

}



workers_costs = {
    "worker_ranks" : {
        "cashier" : {
            "payout" : 0,
            "count" : 0,
            "total" : 0
        },

        "barista" : {
            "payout" : 0,
            "count" : 0,
            "total" : 0
        },

        "waiter" : {
            "payout" : 0,
            "count" : 0,
            "total" : 0
        },
        "cleaner" : {
            "payout" : 0,
            "count" : 0,
            "total" : 0
        },

        "supervisor" : {
            "payout" : 0,
            "count" : 1,
            "total" : 0
        },

        "manager" : {
            "payout" : 0,
            "count" : 1,
            "total" : 0
        },
    },
        
    
    "total_of_workers" : 0,
    "worker_sallary_total_monthly" : 0
}



incomes_related = {
    "food_sales_per_month" : 0,
    "beverage_sales_per_month" : 0,
    "food_beverage_sales_per_month" : 0,
    "food_beverage_sales_percentage" : 0,
    "tips_bonus_monthly" : 0,
    "sponsorship" : 0,
    "online_sales_monthly" : 0,
    "total_sales_per_month" : 0
}



# This is a list

calculator_list = [
    "[bold blue]Utility Costs",
    "[bold red]Core Costs",
    "[bold green]Incomes Related",
    "[bold gold3]Exit"
]


# Variables


start_status = 0 # 0 as true, vice versa

status_menu = 0 # 0 as true, 1 as false
input_menu = 0 # Determines the value by receiving input





# Code starts here, where all things begin and starts printing to the console / terminal
# Starting menu

tm.sleep(0.6) # Wait for a second
clear_terminal() # Clear user terminal

print('''+-----------------------------+
 |        Welcome user       |
+-----------------------------+''')      # Print Welcome banner

tm.sleep(0.4) # Wait


# Includes option which then lead to it's function above



csltext.print("[bold green]Preparing, Cafe profit and cost calculator...") # Print this text
tm.sleep(0.5)
while start_status == 0: # Will loop while start_status is 0
    csltext.print("[bold green]Welcome") # Print in bold green
    tm.sleep(0.3) # Wait
    csltext.print("[bold]What would you like to calculate?") # Print in bold
    tm.sleep(0.8) # Wait
    csltext.print("[bold green]Options:\n") # Print in bold green
    status_menu = 0 # Set status_menu = 0

    # Prints the list of 3 calculator in a cleaner way
    for i, item in enumerate(calculator_list, start=1):
        print(f"[cyan]{i}.[/cyan] {item}"), tm.sleep(0.067488)
    print() # This for blank line


    while status_menu == 0: # Will loop while status_menu is 0
        input_menu = csltext.input("[green]>>  ")

        # Cost / Utility calculator
        if input_menu == "1" : 
            csltext.print("[bold blue]Diving into utility cost calculator, hold tight!") # Print in blue
            status_menu = 1 # Set to 1 which break the status_menu loop 
            start_status = 1 # Set to 1 which break the start_status loop
            tm.sleep(1.3) # Wait
            clear_terminal() # Clear user terminal
            tm.sleep(0.3) # Wait
            basic_cost() # Call the basic_cost function

        # Core cost calculator
        elif input_menu == "2" :
            csltext.print("[bold red]Diving into core cost calculator, hold tight!")
            status_menu = 1 # Set to 1 which break the status_menu loop
            start_status = 1 # Set to 1 which break the start_status loop
            tm.sleep(1) # Wait
            clear_terminal() # Clear user terminal
            tm.sleep(0.2) # Wait
            core_cost() # Call the core_cost funtion
            
            
        # Income related calculator    
        elif input_menu == "3" :
            csltext.print("[bold green]Diving into income calculator, hold tight!")
            status_menu = 1 # Set to 1 which break the status_menu loop
            start_status = 1 # Set to 1 which break the start_status loop
            tm.sleep(1) # Wait
            clear_terminal() # Clear user terminal
            tm.sleep(0.2) # Wait
            income_calculator() # Call the income_calculator function
            
            
            
        # Exit the program    
        elif input_menu == "4":
            print("[#5465FF bold underline]Quitting, thanks and see you again!")
            status_menu = 1 # Set to 1 which break the status_menu loop
            start_status = 1 # Set to 1 which break the start_status loop
            tm.sleep(2) # Wait
            clear_terminal() # Clear user terminal
            exit() # Exit loops and the whole application
            
            
            
        # If enter option that is not available / Unavailable option error    
        else:
            csltext.print("[#fc0303 underline bold]\nThis option does not exist ; invalid input") # Prints in red bold underline

# Code ends here

# "Ingatlah bahawa sepanjang-panjang nyawa saya di dunia ini, panjang lagi saya punya coding"