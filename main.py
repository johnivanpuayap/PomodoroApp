from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

label_timer = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

button_start = Button(text='Start', highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightthickness=0)
button_reset.grid(column=2, row=2)

pomodoro_counter = Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN)
pomodoro_counter.config(pady=20)
pomodoro_counter.grid(column=1, row=2)

window.mainloop()
