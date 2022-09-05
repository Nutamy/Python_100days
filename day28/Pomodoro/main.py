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
reps = 0
checks = ""
check = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checks
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)
    check_label.config(bg=YELLOW, fg=RED)
    checks = ""
    check_label.config(text=checks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=RED, bg=GREEN)
        canvas.config(bg=GREEN)
        window.config(bg=GREEN)
        check_label.config(bg=GREEN, fg=RED)
        reps += 1
    elif reps % 2 == 1 and reps % 7 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=GREEN, bg=YELLOW)
        canvas.config(bg=YELLOW)
        window.config(bg=YELLOW)
        check_label.config(bg=YELLOW, fg=GREEN)
        reps += 1
    elif reps % 7 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Relax", bg=PINK, fg=GREEN)
        canvas.config(bg=PINK)
        window.config(bg=PINK)
        check_label.config(bg=PINK, fg=GREEN)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checks
    minutes = count//60
    seconds = count%60
    if seconds >= 10:
        if minutes >= 10:
            canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        else:
            canvas.itemconfig(timer_text, text=f"0{minutes}:{seconds}")
    else:
        if minutes >= 10:
            canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
        else:
            canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps > 0:
            checks += check
            check_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)


window.mainloop()