from app import window
from customtkinter import *
from random import randint


text = ("Elephant", 30)
emoji = ("Elephant", 40)
list1= ["✊","✋","✌️"]



def game(option1):
    n = randint(0,2)
    option2 = list1[n]
    if (option1 == "✊" and option2 == "✊") or (option1 == "✋" and option2 == "✋") or (option1 == "✌️" and option2 == "✌️"):
        result = "Draw"
    elif (option1 == "✋" and option2 == "✌️") or (option1 == "✌️" and option2 == "✊") or (option1 == "✊" and option2 == "✋"):
        result = "Lost"
    else:
        result = "Won"
    lbl1.configure(text=option2)
    lbl2.configure(text=result)





win = window("SPR", mode='dark', scrollbar=False)


btn1 = CTkButton(win, text="✊", text_color="white", fg_color='red', font=emoji)
btn1.configure(command=lambda: game("✊"))
btn1.grid(pady=100, padx=10, row=2, column=0)

btn2 = CTkButton(win, text="✋", text_color="white", fg_color='red', font=emoji)
btn2.configure(command=lambda: game("✋"))
btn2.grid(pady=100, padx=10, row=2, column=1)

btn3 = CTkButton(win, text="✌️", text_color="white", fg_color='red', font=emoji)
btn3.configure(command=lambda: game("✌️"))
btn3.grid(pady=100, padx=10, row=2, column=2)

lbl1 = CTkLabel(win, text="", fg_color="transparent", font=emoji)
lbl1.grid(pady=40, padx=10, row=1, column=1)

lbl2 = CTkLabel(win, text="", fg_color="transparent", font=text)
lbl2.grid(pady=40, padx=10, row=0, column=1)

win.mainloop()




"""

winning_combinations = {
    ("✊", "✊"): "Draw",
    ("✋", "✋"): "Draw",
    ("✌️", "✌️"): "Draw",
    ("✋", "✊"): "Lost",
    ("✌️", "✋"): "Lost",
    ("✊", "✋"): "Lost",
}

result = winning_combinations.get((option1, option2), "Won")

"""