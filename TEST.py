# import random
# from tkinter import *
# 
# 
# 
# class GUI:
#     def __init__(self, MASTER):
#         # MASTER = Tk()
#         self.MASTER = MASTER
#         self.FRAME_LIST = []
#         MASTER.title("xptmxm")
#         MASTER.geometry("640x400")
# 
#     def CreateFrame(self):
#         for _ in range(3):
#             FRAME = Frame(self.MASTER)
#             FRAME.pack()
#             self.FRAME_LIST.append(FRAME)
# 
#     def CreateButton(self):
#         for NUM in range(10):
#             BUTTON = Button(self.FRAME_LIST[0], text = f" {random.randint(0,4)} ")
#             BUTTON.grid(row = 0, column = NUM)
# 
# 
# if __name__ == "__main__":
#     TKINTER_OBJECT = Tk()
#     FindMine_GUI = GUI(TKINTER_OBJECT)
#     FindMine_GUI.CreateFrame()
#     FindMine_GUI.CreateButton()
#     TKINTER_OBJECT.mainloop()


b = 1000
a = 1000

print(a is b)











