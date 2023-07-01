#TODO: Double check this is accurate
import tkinter as tk
from tkinter import messagebox

class PhoneIdentifier:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Phone Identifier")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.build_gui()
        self.root.mainloop()

    def build_gui(self):
        self.question_label = tk.Label(self.frame, wraplength=300)
        self.question_label.pack(pady=10)
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.frame, state=tk.DISABLED, command=lambda index=i: self.on_option_click(index))
            button.pack(fill=tk.X, pady=2)
            self.option_buttons.append(button)
        self.ask_question()

    def ask_question(self):
        self.question, self.options = self.get_next_question()
        self.question_label.config(text=self.question)
        for i, option in enumerate(self.options):
            self.option_buttons[i].config(text=option, state=tk.NORMAL)
        for button in self.option_buttons[len(self.options):]:
            button.config(state=tk.DISABLED)

    def on_option_click(self, index):
        self.set_answer(index)
        if self.is_finished():
            self.show_result()
        else:
            self.ask_question()

    def get_next_question(self):
        # Modify this method to get the next question and options
        return "Example question?", ["Option 1", "Option 2", "Option 3"]

    def set_answer(self, index):
        # Modify this method to store the answer for the chosen option
        pass

    def is_finished(self):
        # Modify this method to check if the identification process is finished
        return False

    def show_result(self):
        # Modify this method to show the result (phone model)
        self.question_label.config(text="The phone model is: Example Model")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

def ask_yes_no_question(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Please answer with 'y' or 'n'.")

def ask_multiple_choice_question(question, options):
    while True:
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        answer = input("Enter your choice: ")
        try:
            index = int(answer) - 1
            if 0 <= index < len(options):
                return options[index]
        except ValueError:
            if answer.lower() in [option.lower() for option in options]:
                return answer
        print("Invalid choice. Please enter a valid option.")

def determine_phone_model():
    if ask_yes_no_question("Does it have a home button?"):
        return determine_home_button_model()
    else:
        edges = ask_multiple_choice_question("Does it have flat or rounded edges?", ["Flat", "Rounded"])
        if edges == "Flat":
            return determine_flat_sides_model()
        else:
            return determine_rounded_sides_model()

def determine_home_button_model():
    if ask_yes_no_question("Does it have a glass back?"):
        camera_shape = ask_multiple_choice_question("Does it have a circle or oval camera?", ["Circle", "Oval"])
        if camera_shape == "Circle":
            return "iPhone 8, SE 2020 or SE 2022"
        else:
            return "iPhone 8+"
    else:
        stripes = ask_multiple_choice_question("Does it have 1 or 2 stripes going across both the top and bottom?", ["1", "2"])
        if stripes == "1":
            camera_shape = ask_multiple_choice_question("Does it have a circle or oval camera?", ["Circle", "Oval"])
            if camera_shape == "Circle":
                return "iPhone 7"
            else:
                return "iPhone 7+"
        else:
            s_on_back = ask_yes_no_question("Does it have an S on the back?")
            if s_on_back:
                size = ask_multiple_choice_question("Is it large or small?", ["Large", "Small"])
                if size == "Large":
                    return "iPhone 6s+"
                else:
                    return "iPhone 6s"
            else:
                size = ask_multiple_choice_question("Is it large or small?", ["Large", "Small"])
                if size == "Large":
                    return "iPhone 6+"
                else:
                    return "iPhone 6"

def determine_flat_sides_model():
    size = ask_multiple_choice_question("What is the size of the phone?", ["Mini", "Normal", "Large/Pro Max"])
    if size == "Mini":
        camera_orientation = ask_multiple_choice_question("What is the orientation of the camera lenses?", ["Vertical", "Diagonal"])
        if camera_orientation == "Vertical":
            return "iPhone 12 mini"
        else:
            return "iPhone 13 mini"
    elif size == "Normal":
        rear_cameras = ask_multiple_choice_question("How many rear cameras does it have?", ["Two", "Three or Four"])
        if rear_cameras == "Two":
            sim_slot = ask_yes_no_question("Does it have a SIM card slot?")
            if sim_slot:
                camera_orientation = ask_multiple_choice_question("What is the orientation of the camera lenses?", ["Vertical", "Diagonal"])
                if camera_orientation == "Vertical":
                    return "iPhone 12"
                else:
                    return "iPhone 13"
            else:
                return "iPhone 14"
        else:
            island_or_notch = ask_multiple_choice_question("Does it have a dynamic island or a notch?", ["Dynamic Island or Missing Sim Slot", "Notch"])
            if island_or_notch == "Dynamic Island or Missing Sim Slot":
                return "iPhone 14 Pro"
            else:
                ear_speaker_position = ask_multiple_choice_question("Is the ear speaker mesh right against the frame or slightly lower?", ["Right against the frame", "Slightly lower"])
                if ear_speaker_position == "Right against the frame":
                    return "iPhone 13 Pro"
                else:
                    return "iPhone 12 Pro"
    else:  # Large/Pro Max
        rear_cameras = ask_multiple_choice_question("How many rear cameras does it have?", ["Two", "Three or Four"])
        if rear_cameras == "Two":
            island_or_notch = ask_multiple_choice_question("Does it have a dynamic island or a notch?", ["Dynamic Island or Missing Sim Slot", "Notch"])
            if island_or_notch == "Dynamic Island or Missing Sim Slot":
                return "iPhone 14 Pro Max"
            else:
                ear_speaker_position = ask_multiple_choice_question("Is the ear speaker mesh right against the frame or slightly lower?", ["Right against the frame", "Slightly lower"])
                if ear_speaker_position == "Right against the frame":
                    return "iPhone 13 Pro Max"
                else:
                    return "iPhone 12 Pro Max"
        else:
            return "iPhone 14 Plus"

def determine_rounded_sides_model():
    camera_shape = ask_multiple_choice_question("What is the shape and number of cameras on the back?", ["One circle camera in a square module", "One oval camera in a vertical module", "Two circle cameras in a square module", "Three circle cameras in a square module"])
    if camera_shape == "One circle camera in a square module":
        return "iPhone XR"
    elif camera_shape == "One oval camera in a vertical module":
        size = ask_multiple_choice_question("Is it large or small?", ["Large", "Small"])
        if size == "Large":
            holes = ask_multiple_choice_question("Does it have the same amount of holes or different on each side of the lightning port?", ["Same", "Different"])
            if holes == "Same":
                return "iPhone X"
            else:
                return "iPhone XS"
        else:
            return "iPhone XS Max"
    elif camera_shape == "Two circle cameras in a square module":
        return "iPhone 11"
    else:  # Three circle cameras in a square module
        size = ask_multiple_choice_question("Is it large or small?", ["Large", "Small"])
        if size == "Large":
            return "iPhone 11 Pro Max"
        else:
            return "iPhone 11 Pro"
        
        
# def main():

#     phone_model = determine_phone_model()
#     print("The phone model is:", phone_model)
    

if __name__ == "__main__":
    PhoneIdentifier()

# def create_window():
#     window = tk.Tk()
#     # Add widgets and configure the window here
#     window.mainloop()

# def ask_yes_no_question(question):
#     def handle_yes():
#         window.destroy()
#         return True

#     def handle_no():
#         window.destroy()
#         return False

#     window = tk.Tk()
#     window.title("Question")

#     label = tk.Label(window, text=question)
#     label.pack()

#     yes_button = tk.Button(window, text="Yes", command=handle_yes)
#     yes_button.pack()

#     no_button = tk.Button(window, text="No", command=handle_no)
#     no_button.pack()

#     window.mainloop()

# def ask_multiple_choice_question(question, options):
#     def handle_choice():
#         answer = variable.get()
#         window.destroy()
#         return answer

#     window = tk.Tk()
#     window.title("Question")

#     label = tk.Label(window, text=question)
#     label.pack()

#     variable = tk.StringVar(window)
#     variable.set(options[0])  # Set default option

#     option_menu = tk.OptionMenu(window, variable, *options)
#     option_menu.pack()

#     button = tk.Button(window, text="Submit", command=handle_choice)
#     button.pack()

#     window.mainloop()
#     return variable.get()