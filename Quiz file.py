# Imports
from tkinter import *
from tkinter import messagebox as mb
import json

# Define the componets of the GUI
class Quiz:

    def __init__(self):

        self.q_no = 0

        self.display_title()
        self.display_question()


        self.opt_selected = IntVar()


        self.opts = self.radio_buttons()

        self.display_options()

        self.buttons()

        self.data_size = len(question)

        self.correct = 0


    def display_result(self):

        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):

        if self.opt_selected.get() == answer[q_no]:
            return True


    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:

            self.display_result()

            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):


        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        next_button.place(x=623, y=600)


    def display_options(self):
        val = 0

        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1


    def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 30, 'bold'), anchor='w')

        q_no.place(x=100, y=100)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        quit_button.place(x=1200, y=80)

    def display_title(self):

        title = Label(gui, text="Cool Bots Quiz",
                      width=80, bg="green", fg="white", font=("ariel", 20, "bold"))

        title.place(x=0, y=8)

# Puting in the buttons
    def radio_buttons(self):

        q_list = []

        y_pos = 200

        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 30))

            q_list.append(radio_btn)

            radio_btn.place(x=350, y=y_pos)

            y_pos += 90

        return q_list


gui = Tk()

gui.geometry("1366x768")

gui.title("GeeksforGeeks Quiz")
# Extracitng data from Text file
setting_data = open('letter.txt', 'r')
lines = setting_data.readlines()
limited_n_ints = ''
for i in lines:
  limited_n_ints = limited_n_ints + i
print(limited_n_ints)
# Selecting the proper JSON FILE
if limited_n_ints == "1":
    with open('1.json') as f:
        data = json.load(f)
if limited_n_ints == "2":
    with open('2.json') as f:
        data = json.load(f)
if limited_n_ints == "3":
    with open('3.json') as f:
        data = json.load(f)
if limited_n_ints == "4":
    with open('4.json') as f:
        data = json.load(f)
if limited_n_ints == "5":
    with open('5.json') as f:
        data = json.load(f)
if limited_n_ints == "6":
    with open('6.json') as f:
        data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()

gui.mainloop()
