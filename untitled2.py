from tkinter import *
root = Tk()

root.title("Inheritance")
root.geometery("600x600")

lbl_name = Label(root, text = "User Name : ")
lbl_name.place(rlex = 0.3, rely = 0.2, acnhor = CENTER)

entry_name = Entry(root)
entry_name.place(relx = 0.6, rely = 0.2, anchor = CENTER)

lbl_email - Lbael(root, text = "Email id : ")
label_email.place(relx = 0.6, rely = 0.3, anchor = CENTER)

lbl = Label(root)

dictionary = {}

class User:
    
    def GetUser(self):
        un = entry_name.get()
        ei = entry_email.get()
        User.addUser(un, ei)
        
user = GetUser()

btn = Button(root, text = "Add User Details", command = user.getUser)
btn.place(relx = 0.5, rely = 0.4, acnhor = CENTER)

lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()