import customtkinter as ctk
import time as tm
import os

confirm = 0

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
ctk.set_widget_scaling(1.3)  # widget dimensions and text size
ctk.set_window_scaling(1.36888)  # window geometry dimensions

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("580x390")
app.title("Idk just some stuff")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("Terminal was successfully cleared")



def button_function():
    print("Succesfully run")



def button2_function(): # Works
    global confirm
    print("Exit button succesfully pressed. Do you wish to exit?")
    confirm += 1
    if confirm == 2:
        print("Closing window")
        tm.sleep(1.5)
        app.destroy()



var_checkbox = ctk.StringVar(value="False")
def checkbox_toggle():
    chechbox_value = var_checkbox.get()
    
    if chechbox_value == "True":
        print("Checkbox is toggled")
    else: 
        print("Checkbox is untoggled")



def pop_up_input():
    input1 = ctk.CTkInputDialog(text="Enter your input", title="Input")
    print("Input is", input1.get_input())


def add_progress():
    global bar_progerss
    value_bar = bar_progerss.get()
    if value_bar >= 0.999:
        print("Max progress reached")
        bar_progerss.set(1)
    else:
        bar_progerss.step()
    
    formatted_bar = "{:.2f}".format(value_bar)
    progress_label.configure(text = formatted_bar)
    




# Use CTkButton instead of tkinter Button
    
title_label = ctk.CTkLabel(master=app, text="Some random boring tkinter project", width=10, height=10, font=("Arial Bold", 25))
title_label.place(relx = 0.5, rely = 0.1, anchor=ctk.CENTER)



button = ctk.CTkButton(master=app, text="Test Run", command=button_function)
button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

button2 = ctk.CTkButton(master=app, text="Exit", command = button2_function, hover_color="red")
button2.place(relx = 0.5, rely= 0.45, anchor = ctk.CENTER)

button3_popup = ctk.CTkButton(master=app, text="Click me to pop up some text", hover_color="purple", command=pop_up_input)
button3_popup.place(relx = 0.5, rely = 0.60, anchor = ctk.CENTER)

button4 = ctk.CTkButton(app, text="Clear terminal", command=clear_terminal, corner_radius=16, width=34)
button4.place(relx = 0.909, rely = 0.95, anchor = ctk.CENTER)

button5_progress = ctk.CTkButton(app, text="Click me to add progress", command=add_progress)
button5_progress.place(relx = 0.5, rely = 0.90984, anchor = ctk.CENTER)



checkbox1 = ctk.CTkCheckBox(master=app, text="Checkbox", variable=var_checkbox, onvalue="True", offvalue="False", command = checkbox_toggle)
checkbox1.place(relx = 0.5, rely = 0.81, anchor = ctk.CENTER)

bar_progerss = ctk.CTkProgressBar(app, orientation="horizontal", determinate_speed=2)
bar_progerss.place(relx = 0.5, rely = 0.95666, anchor = ctk.CENTER)
bar_progerss.configure(mode="determinate")
bar_progerss.set(0)
# def - 0.5

progress_label = ctk.CTkLabel(app, text=bar_progerss.get())
progress_label.place(relx = 0.7, rely = 0.95667, anchor = ctk.CENTER)



app.mainloop()