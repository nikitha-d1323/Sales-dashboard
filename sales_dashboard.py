# Sales Dashboard Project
# Built with Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("900x600")
root.configure(bg="white")

# --- Data ---
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = [150,180,210,170,230,260,245,290,310,280,320,350]

# --- Header Frame ---
header_frame = tk.Frame(root, bg="navy", pady=10)
header_frame.pack(fill="x")

# --- Header Label ---
tk.Label(header_frame,
         text="SALES DASHBOARD",
         font=("Arial", 20, "bold"),
         bg="navy",
         fg="white").pack()

# --- KPI Frame ---
kpi_frame = tk.Frame(root, bg="white", pady=10)
kpi_frame.pack(fill="x", padx=20)

# --- Card 1 : Total Sales ---
card1 = tk.Frame(kpi_frame, bg="blue", padx=15, pady=10)
card1.pack(side="left", expand=True, fill="both", padx=10)

tk.Label(card1, text="Total Sales",
         font=("Arial", 10, "bold"),
         bg="blue", fg="white").pack()
tk.Label(card1, text=str(sum(sales)) + " units",
         font=("Arial", 14, "bold"),
         bg="blue", fg="white").pack()

# --- Card 2 : Best Month ---
card2 = tk.Frame(kpi_frame, bg="green", padx=15, pady=10)
card2.pack(side="left", expand=True, fill="both", padx=10)

tk.Label(card2, text="Best Month",
         font=("Arial", 10, "bold"),
         bg="green", fg="white").pack()
tk.Label(card2, text=months[sales.index(max(sales))],
         font=("Arial", 14, "bold"),
         bg="green", fg="white").pack()

# --- Card 3 : Lowest Month ---
card3 = tk.Frame(kpi_frame, bg="red", padx=15, pady=10)
card3.pack(side="left", expand=True, fill="both", padx=10)

tk.Label(card3, text="Lowest Month",
         font=("Arial", 10, "bold"),
         bg="red", fg="white").pack()
tk.Label(card3, text=months[sales.index(min(sales))],
         font=("Arial", 14, "bold"),
         bg="red", fg="white").pack()

root.mainloop()