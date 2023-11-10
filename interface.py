import tkinter as tk

window = tk.Tk()

window.geometry('500x500')

window.title("My First GUI")

label = tk.Label(window, text="Hello World!", font=("Arial", 18))

label.pack(padx=10, pady=10)

textbox = tk.Text(window, font=("Arial", 18), height=3)
textbox.pack(padx=10, pady=10)

# myentry = tk.Entry(window)
# myentry.pack()

button = tk.Button(window, text="CLick Me", font=('Arial', 14))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('Arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('Arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text='9', font=('Arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

# btn = tk.Button(window, text="PLACE", font=('Arial', 18))
# btn.place(x=200, y=300, height=100, width=100)
window.mainloop()


