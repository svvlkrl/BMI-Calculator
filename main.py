from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("250x200")


label1 = Label(text="BMI Calculator",font=("Times New Roman",15,"normal"))
label1.pack()

label2 = Label(text="Enter Age",font=("Times New Roman",10,"normal"))
label2.pack()

entry_age = Entry()
entry_age.pack()

label3 = Label(text="Enter Height (cm)",font=("Times New Roman",10,"normal"))
label3.pack()

entry_height = Entry()
entry_height.pack()

label4 = Label(text="Enter Weight (kg)",font=("Times New Roman",10,"normal"))
label4.pack()

entry_weight = Entry()
entry_weight.pack()

label5 = Label(text="",font=("Times New Roman",12,"normal"))
label5.pack()



def calculate_bmi():
    try:
        age = float(entry_age.get())
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())
        bmi = weight / height ** 2

        if bmi < 18.5:
            category = "You are underweight."
        elif 18.5 <= bmi < 25:
            category = "You are normal weight."
        elif 25 <= bmi <30 :
            category = "You are overweight."
        elif 30 <= bmi <35 :
            category = "You are obese class 1."
        elif 35 <= bmi <40:
            category = "You are obese class 2."
        elif bmi > 40:
            category = "You are obese class 3."

        label5.config(text=f"BMI: {bmi:.2f}. {category}")
    except ValueError:
        label5.config(text="Enter valid numbers!")


def click_button():
    user_entry = enter_button.get(calculate_bmi())

enter_button = Button(text="Calculate",command=calculate_bmi)
enter_button.pack()


window.mainloop()