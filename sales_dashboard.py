# Sales Dashboard Project
# Built with Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("900x600")
root.configure(bg="white")

# --- Header Frame ---
header_frame = tk.Frame(root, bg="navy", pady=10)
header_frame.pack(fill="x")

# --- Header Label ---
tk.Label(header_frame,
         text="SALES DASHBOARD",
         font=("Arial", 20, "bold"),
         bg="navy",
         fg="white").pack()

root.mainloop()