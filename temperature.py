import customtkinter as ctk # import the customtkinter module; used to create custom widgets and windows for standalone apps

window = ctk.CTk()  # create the main window
window.title("Temperature Converter")  # set the title of the main window
window.geometry("500x300")  # set the size of the main window

label = ctk.CTkLabel(window, text="Enter temperature:", font=("Arial", 20))  # create a label widget; child of root
label.pack(pady=10)  # make the label visible; pack it into the main window (root)


def FahrenheitToCelcius(): # function to convert Fahrenheit to Celsius
    temperature = float(entry.get()) # gets value from entry
    result = (temperature - 32) * 5/9
    result_label.configure(text=f"{temperature}°F = {result}°C") # sends value to result_label

def CelciusToFahrenheit(): # function to convert Celsius to Fahrenheit
    temperature = float(entry.get()) # gets value from entry
    result = temperature * 9/5 + 32
    result_label.configure(text=f"{temperature}°C = {result}°F") # sends value to result_label

entry = ctk.CTkEntry(window) # create an entry widget; child of root; this is the input box
entry.pack(pady=10)

var = ctk.IntVar()
ctof_btn = ctk.CTkButton(window, text="Celsius to Fahrenheit", command=CelciusToFahrenheit)
ctof_btn.pack(pady=10)

ftoc_btn = ctk.CTkButton(window, text="Fahrenheit to Celsius", command=FahrenheitToCelcius)
ftoc_btn.pack(pady=10)

result_label = ctk.CTkLabel(window, text="", font=("Arial", 24))
result_label.pack(pady=10)

window.mainloop()