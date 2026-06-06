# Sales Dashboard Project
# CADD Centre Internship

import tkinter as tk

root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("1100x700")
root.configure(bg="#1e1e2e")

# --- Header ---
header = tk.Frame(root, bg="#12122a", pady=10)
header.pack(fill="x")

tk.Label(header, text="📊  SALES DASHBOARD",
         font=("Courier", 20, "bold"),
         fg="#00d4ff", bg="#12122a").pack(side="left", padx=20)

tk.Label(header, text="CADD Centre Internship Project",
         font=("Courier", 10),
         fg="#aaaaaa", bg="#12122a").pack(side="right", padx=20)

root.mainloop()