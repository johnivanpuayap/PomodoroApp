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
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        label_timer.config(text="Break", fg=PINK)
    else:
        count = WORK_MIN * 60
        label_timer.config(text="Work", fg=GREEN)

    count_down(count)
    reps += 1


def stop_timer():
    pass


def count_down(count):
    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count >= 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

label_timer = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

button_start = Button(text='Start', highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightthickness=0)
button_reset.grid(column=2, row=2)

pomodoro_counter = Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN)
pomodoro_counter.config(pady=20)
pomodoro_counter.grid(column=1, row=2)

window.mainloop()
