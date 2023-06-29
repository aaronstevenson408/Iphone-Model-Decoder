#TODO: Double check this is accurate

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
        return "iPhone 11 Pro or Pro Max"

phone_model = determine_phone_model()
print("The phone model is:", phone_model)
