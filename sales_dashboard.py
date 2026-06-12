# Sales Dashboard Project
# Built with Python and Tkinter

import tkinter as tk

# --- Data ---
months  = ["Jan","Feb","Mar","Apr","May","Jun",
           "Jul","Aug","Sep","Oct","Nov","Dec"]
sales   = [150,180,210,170,230,260,245,290,310,280,320,350]
revenue = [45000,54000,63000,51000,69000,78000,
           73500,87000,93000,84000,96000,105000]
target  = [40000,50000,60000,65000,70000,75000,
           80000,85000,90000,95000,100000,110000]

# --- Window ---
root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("1100x650")
root.configure(bg="white")

# --- Header ---
header = tk.Frame(root, bg="navy", pady=12)
header.pack(fill="x")
tk.Label(header,
         text="SALES DASHBOARD",
         font=("Arial", 22, "bold"),
         bg="navy",
         fg="white").pack()

# --- KPI Frame ---
kpi = tk.Frame(root, bg="white", pady=10)
kpi.pack(fill="x", padx=20)

# --- Card 1 Total Sales ---
c1 = tk.Frame(kpi, bg="blue", padx=15, pady=10)
c1.pack(side="left", expand=True, fill="both", padx=8)
tk.Label(c1,
         text="Total Sales",
         font=("Arial", 10, "bold"),
         bg="blue",
         fg="white").pack()
tk.Label(c1,
         text=str(sum(sales)) + " units",
         font=("Arial", 15, "bold"),
         bg="blue",
         fg="white").pack()

# --- Card 2 Best Month ---
c2 = tk.Frame(kpi, bg="green", padx=15, pady=10)
c2.pack(side="left", expand=True, fill="both", padx=8)
tk.Label(c2,
         text="Best Month",
         font=("Arial", 10, "bold"),
         bg="green",
         fg="white").pack()
tk.Label(c2,
         text=months[sales.index(max(sales))],
         font=("Arial", 15, "bold"),
         bg="green",
         fg="white").pack()

# --- Card 3 Lowest Month ---
c3 = tk.Frame(kpi, bg="red", padx=15, pady=10)
c3.pack(side="left", expand=True, fill="both", padx=8)
tk.Label(c3,
         text="Lowest Month",
         font=("Arial", 10, "bold"),
         bg="red",
         fg="white").pack()
tk.Label(c3,
         text=months[sales.index(min(sales))],
         font=("Arial", 15, "bold"),
         bg="red",
         fg="white").pack()

# --- Card 4 Total Revenue ---
c4 = tk.Frame(kpi, bg="orange", padx=15, pady=10)
c4.pack(side="left", expand=True, fill="both", padx=8)
tk.Label(c4,
         text="Total Revenue",
         font=("Arial", 10, "bold"),
         bg="orange",
         fg="white").pack()
tk.Label(c4,
         text="Rs " + str(sum(revenue)),
         font=("Arial", 15, "bold"),
         bg="orange",
         fg="white").pack()

# --- Card 5 Achievement ---
c5 = tk.Frame(kpi, bg="purple", padx=15, pady=10)
c5.pack(side="left", expand=True, fill="both", padx=8)
tk.Label(c5,
         text="Achievement",
         font=("Arial", 10, "bold"),
         bg="purple",
         fg="white").pack()
tk.Label(c5,
         text=str(round(sum(revenue)/sum(target)*100, 1)) + " %",
         font=("Arial", 15, "bold"),
         bg="purple",
         fg="white").pack()

# --- Charts Frame ---
charts = tk.Frame(root, bg="white")
charts.pack(fill="both", expand=True, padx=20, pady=10)

# --- Left Bar Chart ---
left = tk.Frame(charts, bg="white")
left.pack(side="left", fill="both", expand=True, padx=(0,10))
tk.Label(left,
         text="Monthly Sales (Units)",
         font=("Arial", 12, "bold"),
         bg="white").pack()
canvas = tk.Canvas(left,
                   bg="white",
                   highlightthickness=1,
                   highlightbackground="grey",
                   height=260)
canvas.pack(fill="both", expand=True)

# --- Draw Bar Chart Function ---
def draw_chart(event=None):
    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    if w < 10:
        return
    pl  = 40
    pt  = 15
    pb  = h - 40
    canvas.create_line(pl, pb, w-10, pb,
                       fill="black", width=2)
    canvas.create_line(pl, pt, pl, pb,
                       fill="black", width=2)
    mx  = max(sales)
    gap = (w - pl) / len(sales)
    bw  = int(gap * 0.55)
    for i, val in enumerate(sales):
        x  = pl + int(i * gap + gap/2 - bw/2)
        bh = int((pb - pt) * val / mx)
        y0 = pb - bh
        canvas.create_rectangle(x, y0, x+bw, pb,
                                 fill="steelblue",
                                 outline="")
        canvas.create_text(x+bw//2, y0-8,
                           text=str(val),
                           font=("Arial", 8),
                           fill="black")
        canvas.create_text(x+bw//2, pb+15,
                           text=months[i],
                           font=("Arial", 8),
                           fill="black")

canvas.bind("<Configure>", draw_chart)

# --- Right Line Chart ---
right = tk.Frame(charts, bg="white")
right.pack(side="left", fill="both", expand=True)
tk.Label(right,
         text="Revenue vs Target (Rs)",
         font=("Arial", 12, "bold"),
         bg="white").pack()
canvas2 = tk.Canvas(right,
                    bg="white",
                    highlightthickness=1,
                    highlightbackground="grey",
                    height=260)
canvas2.pack(fill="both", expand=True)

# --- Draw Line Chart Function ---
def draw_line(event=None):
    canvas2.delete("all")
    w = canvas2.winfo_width()
    h = canvas2.winfo_height()
    if w < 10:
        return
    pl  = 50
    pt  = 15
    pb  = h - 40
    canvas2.create_line(pl, pb, w-10, pb,
                        fill="black", width=2)
    canvas2.create_line(pl, pt, pl, pb,
                        fill="black", width=2)
    mx  = max(max(revenue), max(target))
    gap = (w - pl) / (len(revenue) - 1)
    for i in range(len(revenue) - 1):
        x1 = pl + int(i * gap)
        y1 = pt + int((pb-pt) * (1 - revenue[i] / mx))
        x2 = pl + int((i+1) * gap)
        y2 = pt + int((pb-pt) * (1 - revenue[i+1] / mx))
        canvas2.create_line(x1, y1, x2, y2,
                            fill="green", width=2)
    for i in range(len(target) - 1):
        x1 = pl + int(i * gap)
        y1 = pt + int((pb-pt) * (1 - target[i] / mx))
        x2 = pl + int((i+1) * gap)
        y2 = pt + int((pb-pt) * (1 - target[i+1] / mx))
        canvas2.create_line(x1, y1, x2, y2,
                            fill="orange", width=2,
                            dash=(6,4))
    for i in range(len(revenue)):
        x = pl + int(i * gap)
        y = pt + int((pb-pt) * (1 - revenue[i] / mx))
        canvas2.create_oval(x-4, y-4, x+4, y+4,
                            fill="green",
                            outline="white")
    for i in range(len(target)):
        x = pl + int(i * gap)
        y = pt + int((pb-pt) * (1 - target[i] / mx))
        canvas2.create_rectangle(x-4, y-4, x+4, y+4,
                                 fill="orange",
                                 outline="")
    for i in range(len(months)):
        x = pl + int(i * gap)
        canvas2.create_text(x, pb+15,
                            text=months[i],
                            font=("Arial", 7),
                            fill="black")
    canvas2.create_line(pl, h-15, pl+20, h-15,
                        fill="green", width=2)
    canvas2.create_text(pl+25, h-15,
                        text="Revenue",
                        font=("Arial", 8),
                        fill="green", anchor="w")
    canvas2.create_line(pl+90, h-15, pl+110, h-15,
                        fill="orange", width=2,
                        dash=(6,4))
    canvas2.create_text(pl+115, h-15,
                        text="Target",
                        font=("Arial", 8),
                        fill="orange", anchor="w")

canvas2.bind("<Configure>", draw_line)

# --- Footer ---
tk.Label(root,
         text="Sales Dashboard | Built with Python and Tkinter | 2024",
         font=("Arial", 8),
         bg="navy",
         fg="white",
         pady=5).pack(fill="x", side="bottom")

# --- Run Window ---
root.mainloop()