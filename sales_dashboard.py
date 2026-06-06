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

# --- KPI Cards ---
kpi_frame = tk.Frame(root, bg="#1e1e2e", pady=10)
kpi_frame.pack(fill="x", padx=20)

cards = [
    ("🛒  Total Sales",   "1800 units",  "#0077b6"),
    ("💰  Total Revenue", "₹ 8,98,500",  "#00b4a0"),
    ("🎯  Target",        "₹ 9,60,000",  "#f4a261"),
    ("✅  Achievement",   "93.5 %",       "#2dc653"),
    ("🏆  Best Month",    "December",     "#9b59b6"),
]

for title, value, color in cards:
    card = tk.Frame(kpi_frame, bg=color, padx=15, pady=10)
    card.pack(side="left", expand=True, fill="both", padx=6)

    tk.Label(card, text=title,
             font=("Courier", 9, "bold"),
             fg="white", bg=color).pack(anchor="w")

    tk.Label(card, text=value,
             font=("Courier", 15, "bold"),
             fg="white", bg=color).pack(anchor="w")

root.mainloop()