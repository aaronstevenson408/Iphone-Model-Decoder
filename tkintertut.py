from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
gui_height = 500
gui_width = 500
root.geometry(f"{gui_height}x{gui_width}")
root.title("GUI")

question_image = Image.open("wires.PNG")
question_image_tk = ImageTk.PhotoImage(question_image)

lbl_title = tk.Label(root, text="Hello World", font=("Arial", 18))
lbl_title.pack()

lbl_question_image = tk.Label(root, image=question_image_tk)
lbl_question_image.pack()

root.mainloop()