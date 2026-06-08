# Sales Dashboard Project
# Built with Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("900x600")
root.configure(bg="white")

# --- Title Label ---
tk.Label(root,
         text="SALES DASHBOARD",
         font=("Arial", 20, "bold"),
         bg="navy",
         fg="white",
         pady=10).pack(fill="x")

root.mainloop()