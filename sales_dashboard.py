import tkinter as tk

# --- Data ---
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = [150, 180, 210, 170, 230, 260, 245, 290, 310, 280, 320, 350]

# --- Window ---
root = tk.Tk()
root.title("Sales Dashboard")
root.geometry("900x600")
root.configure(bg="white")

# --- Header ---
tk.Label(root,
         text="SALES DASHBOARD",
         font=("Arial", 20, "bold"),
         bg="navy", fg="white",
         pady=10).pack(fill="x")

# --- KPI Cards ---
card_frame = tk.Frame(root, bg="white", pady=10)
card_frame.pack(fill="x", padx=20)

cards = [
    ("Total Sales",   str(sum(sales)) + " units", "blue"),
    ("Best Month",    months[sales.index(max(sales))], "green"),
    ("Lowest Month",  months[sales.index(min(sales))], "red"),
]

for title, value, color in cards:
    f = tk.Frame(card_frame, bg=color, padx=20, pady=10)
    f.pack(side="left", expand=True, fill="both", padx=10)
    tk.Label(f, text=title, font=("Arial", 10, "bold"), fg="white", bg=color).pack()
    tk.Label(f, text=value, font=("Arial", 14, "bold"), fg="white", bg=color).pack()

# --- Bar Chart ---
tk.Label(root,
         text="Monthly Sales",
         font=("Arial", 12, "bold"),
         bg="white").pack(pady=(10,0))

canvas = tk.Canvas(root, bg="white", height=250)
canvas.pack(fill="both", expand=True, padx=20, pady=10)

def draw_chart(e=None):
    canvas.delete("all")

    # Canvas size
    w = canvas.winfo_width()
    h = canvas.winfo_height()

    # Chart area
    left   = 40
    top    = 10
    bottom = h - 40

    max_val = max(sales)
    gap     = (w - left) / len(sales)
    bw      = int(gap * 0.5)

    for i, (month, val) in enumerate(zip(months, sales)):

        # Bar position
        x  = left + int(i * gap + gap/2 - bw/2)
        bh = int((bottom - top) * val / max_val)
        y0 = bottom - bh

        # Draw bar
        canvas.create_rectangle(x, y0, x+bw, bottom, fill="steelblue", outline="")

        # Value on top of bar
        canvas.create_text(x + bw//2, y0 - 8,
                           text=str(val),
                           font=("Arial", 8),
                           fill="black")

        # Month label below bar
        canvas.create_text(x + bw//2, bottom + 15,
                           text=month,
                           font=("Arial", 8),
                           fill="black")

canvas.bind("<Configure>", draw_chart)

root.mainloop()