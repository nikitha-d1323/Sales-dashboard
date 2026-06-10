# Sales Dashboard Project
# Built with Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("900x600")
root.configure(bg="white")

# --- Data ---
months  = ["Jan","Feb","Mar","Apr","May","Jun",
           "Jul","Aug","Sep","Oct","Nov","Dec"]
sales   = [150,180,210,170,230,260,245,290,310,280,320,350]
revenue = [45000,54000,63000,51000,69000,78000,
           73500,87000,93000,84000,96000,105000]
target  = [40000,50000,60000,65000,70000,75000,
           80000,85000,90000,95000,100000,110000]

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

# --- Chart Frame ---
chart_frame = tk.Frame(root, bg="white")
chart_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ── LEFT SIDE : Bar Chart ──────────────────────
left_frame = tk.Frame(chart_frame, bg="white")
left_frame.pack(side="left", fill="both",
                expand=True, padx=(0, 10))

tk.Label(left_frame,
         text="Monthly Sales Chart",
         font=("Arial", 12, "bold"),
         bg="white").pack()

canvas = tk.Canvas(left_frame,
                   bg="lightyellow",
                   highlightthickness=1,
                   highlightbackground="grey",
                   height=250)
canvas.pack(fill="both", expand=True)

# --- Draw Bar Chart ---
def draw_chart(event=None):
    canvas.delete("all")

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    left   = 40
    top    = 10
    bottom = h - 40

    # Draw bottom line (x axis)
    canvas.create_line(left, bottom, w - 10, bottom,
                       fill="black", width=2)

    # Draw left line (y axis)
    canvas.create_line(left, top, left, bottom,
                       fill="black", width=2)

    # Calculate bar size
    max_val = max(sales)
    gap     = (w - left) / len(sales)
    bw      = int(gap * 0.5)

    # Draw all bars with value and month labels
    for i, val in enumerate(sales):
        x  = left + int(i * gap + gap/2 - bw/2)
        bh = int((bottom - top) * val / max_val)
        y0 = bottom - bh

        # Draw bar
        canvas.create_rectangle(x, y0, x + bw, bottom,
                                 fill="steelblue",
                                 outline="")

        # Draw value on top of bar
        canvas.create_text(x + bw // 2, y0 - 8,
                           text=str(val),
                           font=("Arial", 8),
                           fill="black")

        # Draw month label below bar
        canvas.create_text(x + bw // 2, bottom + 15,
                           text=months[i],
                           font=("Arial", 8),
                           fill="black")

canvas.bind("<Configure>", draw_chart)

# ── RIGHT SIDE : Line Chart ────────────────────
right_frame = tk.Frame(chart_frame, bg="white")
right_frame.pack(side="left", fill="both", expand=True)

tk.Label(right_frame,
         text="Revenue vs Target",
         font=("Arial", 12, "bold"),
         bg="white").pack()

canvas2 = tk.Canvas(right_frame,
                    bg="lightyellow",
                    highlightthickness=1,
                    highlightbackground="grey",
                    height=250)
canvas2.pack(fill="both", expand=True)

# --- Draw Line Chart ---
def draw_line(event=None):
    canvas2.delete("all")

    w = canvas2.winfo_width()
    h = canvas2.winfo_height()
    if w < 10: return

    left   = 50
    top    = 10
    bottom = h - 40

    # Draw bottom line (x axis)
    canvas2.create_line(left, bottom, w - 10, bottom,
                        fill="black", width=2)

    # Draw left line (y axis)
    canvas2.create_line(left, top, left, bottom,
                        fill="black", width=2)

    # Find highest value to scale the chart
    max_val = max(max(revenue), max(target))

    # Gap between each data point
    gap = (w - left) / (len(revenue) - 1)

    # Draw revenue line (green)
    for i in range(len(revenue) - 1):
        x1 = left + int(i * gap)
        y1 = top + int((bottom - top) * (1 - revenue[i] / max_val))
        x2 = left + int((i + 1) * gap)
        y2 = top + int((bottom - top) * (1 - revenue[i + 1] / max_val))
        canvas2.create_line(x1, y1, x2, y2,
                            fill="green", width=2)

    # Draw target line (orange dashed)
    for i in range(len(target) - 1):
        x1 = left + int(i * gap)
        y1 = top + int((bottom - top) * (1 - target[i] / max_val))
        x2 = left + int((i + 1) * gap)
        y2 = top + int((bottom - top) * (1 - target[i + 1] / max_val))
        canvas2.create_line(x1, y1, x2, y2,
                            fill="orange", width=2,
                            dash=(6, 4))

    # Draw dots on revenue line
    for i in range(len(revenue)):
        x = left + int(i * gap)
        y = top + int((bottom - top) * (1 - revenue[i] / max_val))
        canvas2.create_oval(x - 4, y - 4, x + 4, y + 4,
                            fill="green", outline="white")

    # Draw dots on target line
    for i in range(len(target)):
        x = left + int(i * gap)
        y = top + int((bottom - top) * (1 - target[i] / max_val))
        canvas2.create_rectangle(x - 4, y - 4, x + 4, y + 4,
                                 fill="orange", outline="")

    # Draw month labels on x axis
    for i in range(len(months)):
        x = left + int(i * gap)
        canvas2.create_text(x, bottom + 15,
                            text=months[i],
                            font=("Arial", 7),
                            fill="black")

    # Draw legend
    canvas2.create_line(left, h - 15,
                        left + 20, h - 15,
                        fill="green", width=2)
    canvas2.create_text(left + 25, h - 15,
                        text="Revenue",
                        font=("Arial", 8),
                        fill="green", anchor="w")

    canvas2.create_line(left + 90, h - 15,
                        left + 110, h - 15,
                        fill="orange", width=2,
                        dash=(6, 4))
    canvas2.create_text(left + 115, h - 15,
                        text="Target",
                        font=("Arial", 8),
                        fill="orange", anchor="w")

canvas2.bind("<Configure>", draw_line)

# --- Footer ---
tk.Label(root,
         text="Sales Dashboard | Built with Python and Tkinter",
         font=("Arial", 8),
         bg="navy",
         fg="white",
         pady=5).pack(fill="x", side="bottom")

# --- Keep window open ---
root.mainloop()