from tkinter import *   # import tkinter widgets
import datetime         # import datetime module

root = Tk()
root.title("Age Calculator")
root.geometry("350x220")

# Variables (must be created AFTER root)
NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()

def apple():
    try:
        # 1) build birthdate from the entries
        birthdate = datetime.date(
            int(YearVariable.get()),
            int(MonthVariable.get()),
            int(DayVariable.get())
        )

        # 2) calculate age
        today = datetime.date.today()
        age_days = (today - birthdate).days
        age_years = round(age_days / 365.25, 2)  # 365.25 is more accurate

        result_label.config(
            text=f"{NameVariable.get()}, your age is about {age_years} years old."
        )

    except ValueError:
        result_label.config(text="Please enter a valid date (numbers only).")

# Labels
Label(root, text="Your Name").grid(row=1, column=1, padx=8, pady=4, sticky="w")
Label(root, text="Your Birth Year").grid(row=2, column=1, padx=8, pady=4, sticky="w")
Label(root, text="Your Birth Month").grid(row=3, column=1, padx=8, pady=4, sticky="w")
Label(root, text="Your Birth Day").grid(row=4, column=1, padx=8, pady=4, sticky="w")

# Entries
Entry(root, textvariable=NameVariable).grid(row=1, column=2, padx=8, pady=4)
Entry(root, textvariable=YearVariable).grid(row=2, column=2, padx=8, pady=4)
Entry(root, textvariable=MonthVariable).grid(row=3, column=2, padx=8, pady=4)
Entry(root, textvariable=DayVariable).grid(row=4, column=2, padx=8, pady=4)

# Button
Button(root, text="Calculate Age", command=apple).grid(row=5, column=2, pady=10)

# Result label (so it updates instead of creating a new label every click)
result_label = Label(root, text="")
result_label.grid(row=6, column=1, columnspan=2, pady=8)

root.mainloop()