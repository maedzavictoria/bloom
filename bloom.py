import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import calendar


# =========================================================
# BLOOM - YOUR LITTLE PRODUCTIVITY SPACE 🌸
# =========================================================

root = tk.Tk()
root.title("🌸 BLOOM")
root.geometry("1100x700")
root.minsize(850, 600)


# =========================================================
# COLORS
# =========================================================

# LIGHT THEME
LIGHT_BACKGROUND = "#FFF7FB"
LIGHT_SIDEBAR = "#FFE4F0"
LIGHT_CARD = "#FFFFFF"
LIGHT_PINK = "#EFA3C7"
LIGHT_DARK_PINK = "#D96C9D"
LIGHT_TEXT = "#4A3441"
LIGHT_MUTED = "#9A7F8D"
LIGHT_SOFT_PINK = "#FCEAF3"
LIGHT_GREEN = "#8BC9A3"
LIGHT_LIGHT_GREEN = "#EAF7EF"

# DARK THEME
DARK_BACKGROUND = "#1E1B20"
DARK_SIDEBAR = "#2A252C"
DARK_CARD = "#302B32"
DARK_PINK = "#EFA3C7"
DARK_DARK_PINK = "#F28AB8"
DARK_TEXT = "#F8EEF4"
DARK_MUTED = "#B9A9B2"
DARK_SOFT_PINK = "#47333F"
DARK_GREEN = "#8BC9A3"
DARK_LIGHT_GREEN = "#304538"


# Current theme
current_theme = "light"

BACKGROUND = LIGHT_BACKGROUND
SIDEBAR = LIGHT_SIDEBAR
CARD = LIGHT_CARD
PINK = LIGHT_PINK
DARK_PINK = LIGHT_DARK_PINK
TEXT = LIGHT_TEXT
MUTED = LIGHT_MUTED
SOFT_PINK = LIGHT_SOFT_PINK
GREEN = LIGHT_GREEN
LIGHT_GREEN = LIGHT_LIGHT_GREEN


# =========================================================
# DATA
# =========================================================

plans = [
    {
        "name": "Study Python 🐍",
        "completed": False,
        "priority": "High",
        "due_date": "30/09/2026"
    },
    {
        "name": "Work on my website 💻",
        "completed": True,
        "priority": "Medium",
        "due_date": "02/10/2026"
    },
    {
        "name": "Practice Cisco 🌐",
        "completed": False,
        "priority": "Low",
        "due_date": "05/10/2026"
    }
]

goals = [
    {
        "name": "Learn Python 🐍",
        "target": 10,
        "progress": 4,
        "deadline": "31/10/2026"
    },
    {
        "name": "Build my portfolio 💻",
        "target": 10,
        "progress": 3,
        "deadline": "30/11/2026"
    }
]

notes = [
    {
        "title": "Python ideas 🐍",
        "content": "Build a portfolio project using Python.",
        "date": "28/09/2026",
        "pinned": True
    },
    {
        "title": "Things I want to learn 💻",
        "content": "Python, AI, Web Development and Machine Learning.",
        "date": "28/09/2026",
        "pinned": False
    }
]

habits = [
    {
        "name": "Study Python",
        "completed_today": False,
        "streak": 3
    },
    {
        "name": "Drink enough water",
        "completed_today": True,
        "streak": 5
    },
    {
        "name": "Practice coding",
        "completed_today": False,
        "streak": 2
    }
]


# =========================================================
# MAIN VARIABLES
# =========================================================

content_area = None
page_title = None
greeting_label = None

calendar_year = 2026
calendar_month = 9


# =========================================================
# THEME FUNCTIONS
# =========================================================

def set_theme(theme):
    global current_theme
    global BACKGROUND
    global SIDEBAR
    global CARD
    global PINK
    global DARK_PINK
    global TEXT
    global MUTED
    global SOFT_PINK
    global GREEN
    global LIGHT_GREEN

    current_theme = theme

    if theme == "dark":
        BACKGROUND = DARK_BACKGROUND
        SIDEBAR = DARK_SIDEBAR
        CARD = DARK_CARD
        PINK = DARK_PINK
        DARK_PINK = DARK_DARK_PINK
        TEXT = DARK_TEXT
        MUTED = DARK_MUTED
        SOFT_PINK = DARK_SOFT_PINK
        GREEN = DARK_GREEN
        LIGHT_GREEN = DARK_LIGHT_GREEN

    else:
        BACKGROUND = LIGHT_BACKGROUND
        SIDEBAR = LIGHT_SIDEBAR
        CARD = LIGHT_CARD
        PINK = LIGHT_PINK
        DARK_PINK = LIGHT_DARK_PINK
        TEXT = LIGHT_TEXT
        MUTED = LIGHT_MUTED
        SOFT_PINK = LIGHT_SOFT_PINK
        GREEN = LIGHT_GREEN
        LIGHT_GREEN = LIGHT_LIGHT_GREEN

    update_main_theme()

    # Refresh current page so every widget gets the new colors
    if page_title is not None:
        current_page = page_title.cget("text")

        if current_page == "Dashboard":
            show_home()

        elif current_page == "Plans":
            show_plans()

        elif current_page == "Goals":
            show_goals()

        elif current_page == "Calendar":
            show_calendar()

        elif current_page == "Habits":
            show_habits()

        elif current_page == "Progress":
            show_progress()

        elif current_page == "Notes":
            show_notes()

        elif current_page == "Settings":
            show_settings()


def update_main_theme():
    root.configure(bg=BACKGROUND)

    if sidebar is not None:
        sidebar.configure(bg=SIDEBAR)

        for widget in sidebar.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=SIDEBAR)

            elif isinstance(widget, tk.Button):
                widget.configure(
                    bg=SIDEBAR,
                    fg=TEXT,
                    activebackground=SOFT_PINK,
                    activeforeground=DARK_PINK
                )

    if main_area is not None:
        main_area.configure(bg=BACKGROUND)

    if topbar is not None:
        topbar.configure(bg=BACKGROUND)

    if page_title is not None:
        page_title.configure(
            bg=BACKGROUND,
            fg=TEXT
        )

    if content_area is not None:
        content_area.configure(bg=BACKGROUND)


# =========================================================
# GENERAL HELPERS
# =========================================================

def clear_content():
    for widget in content_area.winfo_children():
        widget.destroy()


def get_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def update_greeting():
    try:
        if greeting_label is not None and greeting_label.winfo_exists():
            greeting_label.config(
                text=f"{get_greeting()}, Victoria 💕"
            )
    except tk.TclError:
        pass

    root.after(30000, update_greeting)


def priority_display(priority):
    if priority == "High":
        return "🔴 High"
    elif priority == "Medium":
        return "🟡 Medium"
    return "🟢 Low"


def due_date_status(date_text):
    try:
        due_date = datetime.strptime(date_text, "%d/%m/%Y").date()
        today = datetime.now().date()

        if due_date < today:
            return "Overdue"
        elif due_date == today:
            return "Today"
        else:
            return date_text

    except ValueError:
        return date_text


def format_calendar_date(year, month, day):
    return f"{day:02d}/{month:02d}/{year}"


# =========================================================
# CUSTOM PENCIL ICON
# =========================================================

def create_pencil_icon(parent, command):
    canvas = tk.Canvas(
        parent,
        width=25,
        height=25,
        bg=CARD,
        highlightthickness=0,
        cursor="hand2"
    )

    # Pencil body
    canvas.create_polygon(
        6, 18,
        18, 6,
        21, 9,
        9, 21,
        fill=MUTED,
        outline=MUTED
    )

    # Pencil tip
    canvas.create_polygon(
        6, 18,
        4, 22,
        9, 21,
        fill=MUTED,
        outline=MUTED
    )

    # Pencil highlight
    canvas.create_line(
        10, 17,
        18, 9,
        fill=CARD,
        width=2
    )

    canvas.bind("<Button-1>", lambda event: command())

    return canvas


# =========================================================
# CUSTOM BIN ICON
# =========================================================

def create_bin_icon(parent, command):
    canvas = tk.Canvas(
        parent,
        width=25,
        height=25,
        bg=CARD,
        highlightthickness=0,
        cursor="hand2"
    )

    # Bin body
    canvas.create_rectangle(
        7, 8,
        18, 21,
        fill=MUTED,
        outline=MUTED
    )

    # Top
    canvas.create_rectangle(
        5, 5,
        20, 8,
        fill=MUTED,
        outline=MUTED
    )

    # Handle
    canvas.create_line(
        10, 4,
        15, 4,
        fill=MUTED,
        width=2
    )

    # Lines
    canvas.create_line(
        10, 11,
        10, 18,
        fill=CARD,
        width=1
    )

    canvas.create_line(
        14, 11,
        14, 18,
        fill=CARD,
        width=1
    )

    canvas.bind("<Button-1>", lambda event: command())

    return canvas


# =========================================================
# SUMMARY CARD
# =========================================================

def create_summary_card(parent, title, value, icon, column):
    card = tk.Frame(
        parent,
        bg=CARD,
        width=220,
        height=110
    )

    card.grid(row=0, column=column, padx=8, pady=8, sticky="nsew")
    card.grid_propagate(False)

    tk.Label(
        card,
        text=icon,
        bg=CARD,
        fg=DARK_PINK,
        font=("Arial", 20)
    ).pack(anchor="w", padx=18, pady=(14, 0))

    tk.Label(
        card,
        text=str(value),
        bg=CARD,
        fg=TEXT,
        font=("Arial", 20, "bold")
    ).pack(anchor="w", padx=18)

    tk.Label(
        card,
        text=title,
        bg=CARD,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(anchor="w", padx=18)


# =========================================================
# HOME
# =========================================================

def show_home():
    global page_title
    global greeting_label

    clear_content()

    page_title.config(text="Dashboard")

    greeting_label = tk.Label(
        content_area,
        text=f"{get_greeting()}, Victoria 💕",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 25, "bold")
    )

    greeting_label.pack(
        anchor="w",
        pady=(5, 3)
    )

    tk.Label(
        content_area,
        text="Welcome back to your little productivity space.",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 11)
    ).pack(anchor="w")

    summary_frame = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    summary_frame.pack(fill="x", pady=22)

    for i in range(3):
        summary_frame.grid_columnconfigure(i, weight=1)

    create_summary_card(
        summary_frame,
        "Plans",
        len(plans),
        "📝",
        0
    )

    create_summary_card(
        summary_frame,
        "Goals",
        len(goals),
        "🎯",
        1
    )

    create_summary_card(
        summary_frame,
        "Habits",
        len(habits),
        "💗",
        2
    )

    plans_card = tk.Frame(
        content_area,
        bg=CARD
    )

    plans_card.pack(
        fill="x",
        pady=(5, 15)
    )

    tk.Label(
        plans_card,
        text="Today's Plans",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=(18, 10))

    if not plans:
        tk.Label(
            plans_card,
            text="🌸 No plans yet.",
            bg=CARD,
            fg=MUTED,
            font=("Arial", 10)
        ).pack(anchor="w", padx=20, pady=(0, 18))

    else:
        for plan in plans:
            row = tk.Frame(
                plans_card,
                bg=CARD
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )

            status = "✓" if plan["completed"] else "○"

            tk.Label(
                row,
                text=status,
                bg=CARD,
                fg=GREEN if plan["completed"] else PINK,
                font=("Arial", 13, "bold")
            ).pack(side="left")

            tk.Label(
                row,
                text=plan["name"],
                bg=CARD,
                fg=MUTED if plan["completed"] else TEXT,
                font=("Arial", 10),
                anchor="w"
            ).pack(side="left", padx=10)

            tk.Label(
                row,
                text=plan["due_date"],
                bg=CARD,
                fg=MUTED,
                font=("Arial", 9)
            ).pack(side="right")

    motivation = tk.Frame(
        content_area,
        bg=SOFT_PINK
    )

    motivation.pack(
        fill="x",
        pady=5
    )

    tk.Label(
        motivation,
        text="🌷 Little reminder",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", padx=20, pady=(15, 5))

    tk.Label(
        motivation,
        text="You don't have to do everything today. Just keep blooming. 💕",
        bg=SOFT_PINK,
        fg=TEXT,
        font=("Arial", 10)
    ).pack(anchor="w", padx=20, pady=(0, 15))


# =========================================================
# PLANS
# =========================================================

def show_plans():
    clear_content()

    page_title.config(text="Plans")

    header = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    header.pack(fill="x")

    tk.Label(
        header,
        text="My Plans 📝",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(side="left")

    tk.Button(
        header,
        text="+ Add Plan",
        bg=DARK_PINK,
        fg="white",
        activebackground=PINK,
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=add_plan
    ).pack(side="right")

    tk.Label(
        content_area,
        text="Keep track of the things you want to accomplish.",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(anchor="w", pady=(5, 18))

    if not plans:
        tk.Label(
            content_area,
            text="🌸 You don't have any plans yet.",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Arial", 11)
        ).pack(pady=40)

        return

    for index, plan in enumerate(plans):
        create_plan_row(index, plan)


def create_plan_row(index, plan):
    row = tk.Frame(
        content_area,
        bg=CARD
    )

    row.pack(
        fill="x",
        pady=6
    )

    check_var = tk.BooleanVar(
        value=plan["completed"]
    )

    check = tk.Checkbutton(
        row,
        variable=check_var,
        bg=CARD,
        activebackground=CARD,
        selectcolor=CARD,
        command=lambda: toggle_plan(index, check_var.get())
    )

    check.pack(side="left", padx=(15, 5))

    tk.Label(
        row,
        text=plan["name"],
        bg=CARD,
        fg=MUTED if plan["completed"] else TEXT,
        font=("Arial", 11, "bold")
    ).pack(side="left", padx=5, pady=17)

    tk.Label(
        row,
        text=plan["due_date"],
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(side="right", padx=5)

    tk.Label(
        row,
        text=priority_display(plan["priority"]),
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(side="right", padx=10)

    create_bin_icon(
        row,
        lambda: delete_plan(index)
    ).pack(side="right", padx=(3, 8))

    create_pencil_icon(
        row,
        lambda: edit_plan(index)
    ).pack(side="right", padx=3)


def toggle_plan(index, completed):
    plans[index]["completed"] = completed
    show_plans()


def add_plan():
    popup = tk.Toplevel(root)
    popup.title("Add Plan")
    popup.geometry("420x430")
    popup.configure(bg=BACKGROUND)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="Add a New Plan 🌸",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Plan name",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    name_entry = tk.Entry(
        popup,
        width=40
    )
    name_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Priority",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    priority_var = tk.StringVar(
        value="Medium"
    )

    tk.OptionMenu(
        popup,
        priority_var,
        "High",
        "Medium",
        "Low"
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Due date (DD/MM/YYYY)",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    date_entry = tk.Entry(
        popup,
        width=40
    )
    date_entry.pack(
        padx=30,
        pady=(5, 20)
    )

    def save():
        name = name_entry.get().strip()
        priority = priority_var.get()
        date = date_entry.get().strip()

        if not name or not date:
            messagebox.showwarning(
                "Missing information",
                "Please fill in all fields."
            )
            return

        try:
            datetime.strptime(
                date,
                "%d/%m/%Y"
            )
        except ValueError:
            messagebox.showerror(
                "Invalid date",
                "Please use DD/MM/YYYY."
            )
            return

        plans.append({
            "name": name,
            "completed": False,
            "priority": priority,
            "due_date": date
        })

        popup.destroy()
        show_plans()

    tk.Button(
        popup,
        text="Save Plan",
        bg=DARK_PINK,
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=save
    ).pack()


def edit_plan(index):
    plan = plans[index]

    popup = tk.Toplevel(root)
    popup.title("Edit Plan")
    popup.geometry("420x430")
    popup.configure(bg=BACKGROUND)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="Edit Plan ✏️",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Plan name",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    name_entry = tk.Entry(
        popup,
        width=40
    )
    name_entry.insert(
        0,
        plan["name"]
    )
    name_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Priority",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    priority_var = tk.StringVar(
        value=plan["priority"]
    )

    tk.OptionMenu(
        popup,
        priority_var,
        "High",
        "Medium",
        "Low"
    ).pack(
        anchor="w",
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Due date (DD/MM/YYYY)",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    date_entry = tk.Entry(
        popup,
        width=40
    )
    date_entry.insert(
        0,
        plan["due_date"]
    )
    date_entry.pack(
        padx=30,
        pady=(5, 20)
    )

    def save():
        name = name_entry.get().strip()
        priority = priority_var.get()
        date = date_entry.get().strip()

        if not name or not date:
            messagebox.showwarning(
                "Missing information",
                "Please fill in all fields."
            )
            return

        try:
            datetime.strptime(
                date,
                "%d/%m/%Y"
            )
        except ValueError:
            messagebox.showerror(
                "Invalid date",
                "Please use DD/MM/YYYY."
            )
            return

        plans[index]["name"] = name
        plans[index]["priority"] = priority
        plans[index]["due_date"] = date

        popup.destroy()
        show_plans()

    tk.Button(
        popup,
        text="Save Changes",
        bg=DARK_PINK,
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=save
    ).pack()


def delete_plan(index):
    answer = messagebox.askyesno(
        "Delete Plan",
        "Are you sure you want to delete this plan?"
    )

    if answer:
        plans.pop(index)
        show_plans()


# =========================================================
# GOALS
# =========================================================

def show_goals():
    clear_content()

    page_title.config(text="Goals")

    header = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    header.pack(fill="x")

    tk.Label(
        header,
        text="My Goals 🎯",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(side="left")

    tk.Button(
        header,
        text="+ Add Goal",
        bg=DARK_PINK,
        fg="white",
        activebackground=PINK,
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=add_goal
    ).pack(side="right")

    tk.Label(
        content_area,
        text="Turn your big dreams into small steps.",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(anchor="w", pady=(5, 18))

    if not goals:
        tk.Label(
            content_area,
            text="🌸 No goals yet.",
            bg=BACKGROUND,
            fg=MUTED
        ).pack(pady=40)

        return

    for index, goal in enumerate(goals):
        create_goal_row(index, goal)


def create_goal_row(index, goal):
    card = tk.Frame(
        content_area,
        bg=CARD
    )

    card.pack(
        fill="x",
        pady=7
    )

    top = tk.Frame(
        card,
        bg=CARD
    )

    top.pack(
        fill="x",
        padx=18,
        pady=(15, 5)
    )

    tk.Label(
        top,
        text=goal["name"],
        bg=CARD,
        fg=TEXT,
        font=("Arial", 11, "bold")
    ).pack(side="left")

    create_bin_icon(
        top,
        lambda: delete_goal(index)
    ).pack(side="right", padx=(3, 0))

    create_pencil_icon(
        top,
        lambda: edit_goal(index)
    ).pack(side="right", padx=3)

    percentage = 0

    if goal["target"] > 0:
        percentage = int(
            (goal["progress"] / goal["target"]) * 100
        )

    percentage = min(
        percentage,
        100
    )

    tk.Label(
        card,
        text=f"{goal['progress']} / {goal['target']}     {percentage}%",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(anchor="w", padx=18)

    progress_background = tk.Frame(
        card,
        bg=SOFT_PINK,
        height=10
    )

    progress_background.pack(
        fill="x",
        padx=18,
        pady=8
    )

    progress_background.pack_propagate(False)

    progress_fill = tk.Frame(
        progress_background,
        bg=PINK,
        width=percentage * 3
    )

    progress_fill.pack(
        side="left",
        fill="y"
    )

    bottom = tk.Frame(
        card,
        bg=CARD
    )

    bottom.pack(
        fill="x",
        padx=18,
        pady=(2, 15)
    )

    tk.Label(
        bottom,
        text=f"Deadline: {goal['deadline']}",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(side="left")

    tk.Button(
        bottom,
        text="−",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        relief="flat",
        width=3,
        cursor="hand2",
        command=lambda: change_goal_progress(index, -1)
    ).pack(side="right", padx=3)

    tk.Button(
        bottom,
        text="+",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        relief="flat",
        width=3,
        cursor="hand2",
        command=lambda: change_goal_progress(index, 1)
    ).pack(side="right")


def change_goal_progress(index, amount):
    goal = goals[index]

    goal["progress"] += amount

    if goal["progress"] < 0:
        goal["progress"] = 0

    if goal["progress"] > goal["target"]:
        goal["progress"] = goal["target"]

    show_goals()


def add_goal():
    goal_popup(
        title="Add Goal",
        index=None
    )


def edit_goal(index):
    goal_popup(
        title="Edit Goal",
        index=index
    )


def goal_popup(title, index=None):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("430x500")
    popup.configure(bg=BACKGROUND)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text=f"{title} 🎯",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Goal name",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    name_entry = tk.Entry(
        popup,
        width=40
    )

    name_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Target",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    target_entry = tk.Entry(
        popup,
        width=40
    )

    target_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Current progress",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    progress_entry = tk.Entry(
        popup,
        width=40
    )

    progress_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Deadline (DD/MM/YYYY)",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    deadline_entry = tk.Entry(
        popup,
        width=40
    )

    deadline_entry.pack(
        padx=30,
        pady=(5, 20)
    )

    if index is not None:
        goal = goals[index]

        name_entry.insert(
            0,
            goal["name"]
        )

        target_entry.insert(
            0,
            goal["target"]
        )

        progress_entry.insert(
            0,
            goal["progress"]
        )

        deadline_entry.insert(
            0,
            goal["deadline"]
        )

    def save():
        name = name_entry.get().strip()
        target = target_entry.get().strip()
        progress = progress_entry.get().strip()
        deadline = deadline_entry.get().strip()

        if not name or not target or not progress or not deadline:
            messagebox.showwarning(
                "Missing information",
                "Please fill in all fields."
            )
            return

        try:
            target = int(target)
            progress = int(progress)

            if target <= 0 or progress < 0:
                raise ValueError

            if progress > target:
                messagebox.showerror(
                    "Invalid progress",
                    "Progress cannot be greater than the target."
                )
                return

            datetime.strptime(
                deadline,
                "%d/%m/%Y"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid information",
                "Check your numbers and make sure the date is DD/MM/YYYY."
            )
            return

        new_goal = {
            "name": name,
            "target": target,
            "progress": progress,
            "deadline": deadline
        }

        if index is None:
            goals.append(new_goal)
        else:
            goals[index] = new_goal

        popup.destroy()
        show_goals()

    tk.Button(
        popup,
        text="Save Goal",
        bg=DARK_PINK,
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=save
    ).pack()


def delete_goal(index):
    answer = messagebox.askyesno(
        "Delete Goal",
        "Are you sure you want to delete this goal?"
    )

    if answer:
        goals.pop(index)
        show_goals()


# =========================================================
# NOTES
# =========================================================

def show_notes():
    clear_content()

    page_title.config(text="Notes")

    header = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    header.pack(fill="x")

    tk.Label(
        header,
        text="My Notes 📝",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(side="left")

    tk.Button(
        header,
        text="+ Add Note",
        bg=DARK_PINK,
        fg="white",
        activebackground=PINK,
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=add_note
    ).pack(side="right")

    search_frame = tk.Frame(
        content_area,
        bg=CARD
    )

    search_frame.pack(
        fill="x",
        pady=(18, 15)
    )

    tk.Label(
        search_frame,
        text="🔍",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 11)
    ).pack(
        side="left",
        padx=(12, 4)
    )

    search_var = tk.StringVar()

    search_entry = tk.Entry(
        search_frame,
        textvariable=search_var,
        bg=CARD,
        fg=TEXT,
        relief="flat",
        font=("Arial", 10)
    )

    search_entry.pack(
        side="left",
        fill="x",
        expand=True,
        pady=10
    )

    tk.Label(
        search_frame,
        text="Search your notes",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(
        side="left",
        padx=15
    )

    notes_container = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    notes_container.pack(
        fill="both",
        expand=True
    )

    def render_notes(*args):
        for widget in notes_container.winfo_children():
            widget.destroy()

        query = search_var.get().lower().strip()

        sorted_notes = sorted(
            enumerate(notes),
            key=lambda item: item[1]["pinned"],
            reverse=True
        )

        found = False

        for index, note in sorted_notes:

            if (
                query
                and query not in note["title"].lower()
                and query not in note["content"].lower()
            ):
                continue

            found = True

            create_note_card(
                notes_container,
                index,
                note
            )

        if not found:
            tk.Label(
                notes_container,
                text="🌸 No notes found.",
                bg=BACKGROUND,
                fg=MUTED,
                font=("Arial", 11)
            ).pack(pady=30)

    search_var.trace_add(
        "write",
        render_notes
    )

    render_notes()


def create_note_card(parent, index, note):
    card = tk.Frame(
        parent,
        bg=CARD
    )

    card.pack(
        fill="x",
        pady=6
    )

    top = tk.Frame(
        card,
        bg=CARD
    )

    top.pack(
        fill="x",
        padx=18,
        pady=(15, 5)
    )

    tk.Label(
        top,
        text=note["title"],
        bg=CARD,
        fg=TEXT,
        font=("Arial", 11, "bold")
    ).pack(side="left")

    if note["pinned"]:
        tk.Label(
            top,
            text="📌 Pinned",
            bg=CARD,
            fg=DARK_PINK,
            font=("Arial", 9)
        ).pack(
            side="left",
            padx=10
        )

    create_bin_icon(
        top,
        lambda: delete_note(index)
    ).pack(side="right")

    create_pencil_icon(
        top,
        lambda: edit_note(index)
    ).pack(
        side="right",
        padx=8
    )

    tk.Button(
        top,
        text="📌",
        bg=CARD,
        fg=MUTED,
        activebackground=CARD,
        relief="flat",
        font=("Arial", 10),
        cursor="hand2",
        command=lambda: toggle_pin(index)
    ).pack(
        side="right",
        padx=3
    )

    tk.Label(
        card,
        text=note["content"],
        bg=CARD,
        fg=MUTED,
        font=("Arial", 10),
        justify="left",
        wraplength=700
    ).pack(
        anchor="w",
        padx=18,
        pady=(2, 5)
    )

    tk.Label(
        card,
        text=note["date"],
        bg=CARD,
        fg=MUTED,
        font=("Arial", 8)
    ).pack(
        anchor="w",
        padx=18,
        pady=(0, 15)
    )


def add_note():
    note_popup(
        title="Add Note",
        index=None
    )


def edit_note(index):
    note_popup(
        title="Edit Note",
        index=index
    )


def note_popup(title, index=None):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("500x500")
    popup.configure(bg=BACKGROUND)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text=f"{title} 📝",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Title",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    title_entry = tk.Entry(
        popup,
        width=50
    )

    title_entry.pack(
        padx=30,
        pady=(5, 15)
    )

    tk.Label(
        popup,
        text="Note",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    content_text = tk.Text(
        popup,
        width=50,
        height=10
    )

    content_text.pack(
        padx=30,
        pady=(5, 20)
    )

    if index is not None:
        note = notes[index]

        title_entry.insert(
            0,
            note["title"]
        )

        content_text.insert(
            "1.0",
            note["content"]
        )

    def save():
        title_text = title_entry.get().strip()
        content = content_text.get(
            "1.0",
            "end"
        ).strip()

        if not title_text or not content:
            messagebox.showwarning(
                "Missing information",
                "Please fill in the title and note."
            )
            return

        today = datetime.now().strftime(
            "%d/%m/%Y"
        )

        if index is None:
            notes.append({
                "title": title_text,
                "content": content,
                "date": today,
                "pinned": False
            })
        else:
            notes[index]["title"] = title_text
            notes[index]["content"] = content

        popup.destroy()
        show_notes()

    tk.Button(
        popup,
        text="Save Note",
        bg=DARK_PINK,
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=save
    ).pack()


def toggle_pin(index):
    notes[index]["pinned"] = not notes[index]["pinned"]
    show_notes()


def delete_note(index):
    answer = messagebox.askyesno(
        "Delete Note",
        "Are you sure you want to delete this note?"
    )

    if answer:
        notes.pop(index)
        show_notes()


# =========================================================
# CALENDAR
# =========================================================

def show_calendar():
    clear_content()

    page_title.config(text="Calendar")

    header = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    header.pack(
        fill="x",
        pady=(0, 15)
    )

    tk.Button(
        header,
        text="‹",
        bg=BACKGROUND,
        fg=DARK_PINK,
        relief="flat",
        font=("Arial", 20, "bold"),
        cursor="hand2",
        command=previous_month
    ).pack(side="left")

    month_name = calendar.month_name[
        calendar_month
    ]

    tk.Label(
        header,
        text=f"{month_name} {calendar_year}",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 20, "bold")
    ).pack(
        side="left",
        padx=20
    )

    tk.Button(
        header,
        text="›",
        bg=BACKGROUND,
        fg=DARK_PINK,
        relief="flat",
        font=("Arial", 20, "bold"),
        cursor="hand2",
        command=next_month
    ).pack(side="left")

    tk.Button(
        header,
        text="Today",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        relief="flat",
        font=("Arial", 9, "bold"),
        padx=12,
        pady=6,
        cursor="hand2",
        command=go_to_today
    ).pack(side="right")

    main_frame = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    main_frame.pack(
        fill="both",
        expand=True
    )

    calendar_frame = tk.Frame(
        main_frame,
        bg=CARD
    )

    calendar_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    details_frame = tk.Frame(
        main_frame,
        bg=CARD,
        width=270
    )

    details_frame.pack(
        side="right",
        fill="y"
    )

    details_frame.pack_propagate(False)

    weekdays = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    for col, day_name in enumerate(weekdays):
        calendar_frame.grid_columnconfigure(
            col,
            weight=1
        )

        tk.Label(
            calendar_frame,
            text=day_name,
            bg=CARD,
            fg=MUTED,
            font=("Arial", 9, "bold")
        ).grid(
            row=0,
            column=col,
            sticky="nsew",
            pady=12
        )

    month_calendar = calendar.monthcalendar(
        calendar_year,
        calendar_month
    )

    for row_index, week in enumerate(
        month_calendar,
        start=1
    ):

        calendar_frame.grid_rowconfigure(
            row_index,
            weight=1
        )

        for col_index, day in enumerate(week):

            if day == 0:
                continue

            date_string = format_calendar_date(
                calendar_year,
                calendar_month,
                day
            )

            has_plan = any(
                plan["due_date"] == date_string
                for plan in plans
            )

            has_goal = any(
                goal["deadline"] == date_string
                for goal in goals
            )

            has_note = any(
                note["date"] == date_string
                for note in notes
            )

            has_event = (
                has_plan
                or has_goal
                or has_note
            )

            day_frame = tk.Frame(
                calendar_frame,
                bg=CARD,
                cursor="hand2"
            )

            day_frame.grid(
                row=row_index,
                column=col_index,
                sticky="nsew",
                padx=2,
                pady=2
            )

            tk.Label(
                day_frame,
                text=str(day),
                bg=CARD,
                fg=TEXT,
                font=("Arial", 10, "bold")
            ).pack(pady=(10, 2))

            if has_event:
                tk.Label(
                    day_frame,
                    text="•",
                    bg=CARD,
                    fg=PINK,
                    font=("Arial", 14, "bold")
                ).pack()

            else:
                tk.Label(
                    day_frame,
                    text="",
                    bg=CARD,
                    height=1
                ).pack()

            day_frame.bind(
                "<Button-1>",
                lambda event,
                y=calendar_year,
                m=calendar_month,
                d=day: show_calendar_details(
                    details_frame,
                    y,
                    m,
                    d
                )
            )

            for child in day_frame.winfo_children():
                child.bind(
                    "<Button-1>",
                    lambda event,
                    y=calendar_year,
                    m=calendar_month,
                    d=day: show_calendar_details(
                        details_frame,
                        y,
                        m,
                        d
                    )
                )

    today = datetime.now()

    if (
        today.year == calendar_year
        and today.month == calendar_month
    ):
        show_calendar_details(
            details_frame,
            today.year,
            today.month,
            today.day
        )

    else:
        show_calendar_details(
            details_frame,
            calendar_year,
            calendar_month,
            1
        )


def show_calendar_details(details_frame, year, month, day):
    for widget in details_frame.winfo_children():
        widget.destroy()

    date_string = format_calendar_date(
        year,
        month,
        day
    )

    date_object = datetime.strptime(
        date_string,
        "%d/%m/%Y"
    )

    # ONLY DATE — NO WEDNESDAY / NO WEEKDAY
    nice_date = date_object.strftime(
        "%d %B %Y"
    )

    tk.Label(
        details_frame,
        text="Selected Date",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(
        anchor="w",
        padx=20,
        pady=(22, 5)
    )

    tk.Label(
        details_frame,
        text=f"📅 {nice_date}",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 14, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 25)
    )

    # -----------------------------------------------------
    # PLANS
    # -----------------------------------------------------

    tk.Label(
        details_frame,
        text="Plans",
        bg=CARD,
        fg=DARK_PINK,
        font=("Arial", 11, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(5, 10)
    )

    matching_plans = [
        plan for plan in plans
        if plan["due_date"] == date_string
    ]

    if matching_plans:
        for plan in matching_plans:

            frame = tk.Frame(
                details_frame,
                bg=SOFT_PINK
            )

            frame.pack(
                fill="x",
                padx=20,
                pady=4
            )

            status = "✓" if plan["completed"] else "○"

            tk.Label(
                frame,
                text=f"{status} {plan['name']}",
                bg=SOFT_PINK,
                fg=TEXT,
                font=("Arial", 9),
                wraplength=210,
                justify="left"
            ).pack(
                anchor="w",
                padx=10,
                pady=8
            )

    else:
        tk.Label(
            details_frame,
            text="No plans",
            bg=CARD,
            fg=MUTED,
            font=("Arial", 9)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    # -----------------------------------------------------
    # GOALS
    # -----------------------------------------------------

    tk.Label(
        details_frame,
        text="Goals",
        bg=CARD,
        fg=DARK_PINK,
        font=("Arial", 11, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    matching_goals = [
        goal for goal in goals
        if goal["deadline"] == date_string
    ]

    if matching_goals:
        for goal in matching_goals:

            frame = tk.Frame(
                details_frame,
                bg=SOFT_PINK
            )

            frame.pack(
                fill="x",
                padx=20,
                pady=4
            )

            tk.Label(
                frame,
                text=f"🎯 {goal['name']}",
                bg=SOFT_PINK,
                fg=TEXT,
                font=("Arial", 9),
                wraplength=210,
                justify="left"
            ).pack(
                anchor="w",
                padx=10,
                pady=(8, 2)
            )

            percentage = 0

            if goal["target"] > 0:
                percentage = int(
                    goal["progress"]
                    / goal["target"]
                    * 100
                )

            tk.Label(
                frame,
                text=f"{goal['progress']} / {goal['target']} ({percentage}%)",
                bg=SOFT_PINK,
                fg=MUTED,
                font=("Arial", 8)
            ).pack(
                anchor="w",
                padx=10,
                pady=(0, 8)
            )

    else:
        tk.Label(
            details_frame,
            text="No goals",
            bg=CARD,
            fg=MUTED,
            font=("Arial", 9)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    # -----------------------------------------------------
    # NOTES
    # -----------------------------------------------------

    tk.Label(
        details_frame,
        text="Notes",
        bg=CARD,
        fg=DARK_PINK,
        font=("Arial", 11, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    matching_notes = [
        note for note in notes
        if note["date"] == date_string
    ]

    if matching_notes:
        for note in matching_notes:

            frame = tk.Frame(
                details_frame,
                bg=SOFT_PINK
            )

            frame.pack(
                fill="x",
                padx=20,
                pady=4
            )

            pin_text = " 📌" if note["pinned"] else ""

            tk.Label(
                frame,
                text=f"{note['title']}{pin_text}",
                bg=SOFT_PINK,
                fg=TEXT,
                font=("Arial", 9, "bold"),
                wraplength=210,
                justify="left"
            ).pack(
                anchor="w",
                padx=10,
                pady=(8, 2)
            )

            tk.Label(
                frame,
                text=note["content"],
                bg=SOFT_PINK,
                fg=MUTED,
                font=("Arial", 8),
                wraplength=210,
                justify="left"
            ).pack(
                anchor="w",
                padx=10,
                pady=(0, 8)
            )

    else:
        tk.Label(
            details_frame,
            text="No notes",
            bg=CARD,
            fg=MUTED,
            font=("Arial", 9)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )


def previous_month():
    global calendar_month
    global calendar_year

    calendar_month -= 1

    if calendar_month == 0:
        calendar_month = 12
        calendar_year -= 1

    show_calendar()


def next_month():
    global calendar_month
    global calendar_year

    calendar_month += 1

    if calendar_month == 13:
        calendar_month = 1
        calendar_year += 1

    show_calendar()


def go_to_today():
    global calendar_month
    global calendar_year

    today = datetime.now()

    calendar_month = today.month
    calendar_year = today.year

    show_calendar()


# =========================================================
# HABITS
# =========================================================

def show_habits():
    clear_content()

    page_title.config(text="Habits")

    header = tk.Frame(
        content_area,
        bg=BACKGROUND
    )

    header.pack(fill="x")

    tk.Label(
        header,
        text="My Habits 💗",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(side="left")

    tk.Button(
        header,
        text="+ Add Habit",
        bg=DARK_PINK,
        fg="white",
        activebackground=PINK,
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=add_habit
    ).pack(side="right")

    tk.Label(
        content_area,
        text="Small habits can create big changes. 🌷",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(5, 18)
    )

    completed_count = sum(
        1 for habit in habits
        if habit["completed_today"]
    )

    summary = tk.Frame(
        content_area,
        bg=SOFT_PINK
    )

    summary.pack(
        fill="x",
        pady=(0, 15)
    )

    tk.Label(
        summary,
        text=f"Today's progress: {completed_count}/{len(habits)} habits completed 💕",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        font=("Arial", 10, "bold")
    ).pack(
        anchor="w",
        padx=18,
        pady=14
    )

    for index, habit in enumerate(habits):
        create_habit_row(
            index,
            habit
        )


def create_habit_row(index, habit):
    row = tk.Frame(
        content_area,
        bg=CARD
    )

    row.pack(
        fill="x",
        pady=6
    )

    check_var = tk.BooleanVar(
        value=habit["completed_today"]
    )

    tk.Checkbutton(
        row,
        variable=check_var,
        bg=CARD,
        activebackground=CARD,
        selectcolor=CARD,
        command=lambda: toggle_habit(
            index,
            check_var.get()
        )
    ).pack(
        side="left",
        padx=(15, 5)
    )

    tk.Label(
        row,
        text=habit["name"],
        bg=CARD,
        fg=TEXT,
        font=("Arial", 11, "bold")
    ).pack(
        side="left",
        padx=5,
        pady=16
    )

    tk.Label(
        row,
        text=f"🔥 {habit['streak']} day streak",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(
        side="right",
        padx=10
    )

    create_bin_icon(
        row,
        lambda: delete_habit(index)
    ).pack(
        side="right",
        padx=(3, 8)
    )

    create_pencil_icon(
        row,
        lambda: edit_habit(index)
    ).pack(
        side="right",
        padx=3
    )


def toggle_habit(index, completed):
    old_value = habits[index]["completed_today"]

    habits[index]["completed_today"] = completed

    if completed and not old_value:
        habits[index]["streak"] += 1

    elif not completed and old_value:
        habits[index]["streak"] = max(
            0,
            habits[index]["streak"] - 1
        )

    show_habits()


def add_habit():
    habit_popup(
        title="Add Habit",
        index=None
    )


def edit_habit(index):
    habit_popup(
        title="Edit Habit",
        index=index
    )


def habit_popup(title, index=None):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("400x280")
    popup.configure(bg=BACKGROUND)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text=f"{title} 💗",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Habit name",
        bg=BACKGROUND,
        fg=TEXT
    ).pack(anchor="w", padx=30)

    name_entry = tk.Entry(
        popup,
        width=40
    )

    name_entry.pack(
        padx=30,
        pady=(5, 20)
    )

    if index is not None:
        name_entry.insert(
            0,
            habits[index]["name"]
        )

    def save():
        name = name_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Missing information",
                "Please enter a habit name."
            )
            return

        if index is None:
            habits.append({
                "name": name,
                "completed_today": False,
                "streak": 0
            })
        else:
            habits[index]["name"] = name

        popup.destroy()
        show_habits()

    tk.Button(
        popup,
        text="Save Habit",
        bg=DARK_PINK,
        fg="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8,
        command=save
    ).pack()


def delete_habit(index):
    answer = messagebox.askyesno(
        "Delete Habit",
        "Are you sure you want to delete this habit?"
    )

    if answer:
        habits.pop(index)
        show_habits()


# =========================================================
# PROGRESS
# =========================================================

def show_progress():
    clear_content()

    page_title.config(text="Progress")

    tk.Label(
        content_area,
        text="My Progress 📊",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(anchor="w")

    tk.Label(
        content_area,
        text="Look how far you've come. 🌸",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(5, 20)
    )

    completed_plans = sum(
        1 for plan in plans
        if plan["completed"]
    )

    plan_percentage = 0

    if plans:
        plan_percentage = int(
            completed_plans
            / len(plans)
            * 100
        )

    create_progress_card(
        "Plans completed 📝",
        completed_plans,
        len(plans),
        plan_percentage
    )

    total_goal_target = sum(
        goal["target"]
        for goal in goals
    )

    total_goal_progress = sum(
        goal["progress"]
        for goal in goals
    )

    goal_percentage = 0

    if total_goal_target > 0:
        goal_percentage = int(
            total_goal_progress
            / total_goal_target
            * 100
        )

    create_progress_card(
        "Goal progress 🎯",
        total_goal_progress,
        total_goal_target,
        goal_percentage
    )

    completed_habits = sum(
        1 for habit in habits
        if habit["completed_today"]
    )

    habit_percentage = 0

    if habits:
        habit_percentage = int(
            completed_habits
            / len(habits)
            * 100
        )

    create_progress_card(
        "Today's habits 💗",
        completed_habits,
        len(habits),
        habit_percentage
    )

    message = tk.Frame(
        content_area,
        bg=SOFT_PINK
    )

    message.pack(
        fill="x",
        pady=15
    )

    tk.Label(
        message,
        text="🌷 Keep going!",
        bg=SOFT_PINK,
        fg=DARK_PINK,
        font=("Arial", 12, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    tk.Label(
        message,
        text="Every completed plan, goal step and habit is progress.",
        bg=SOFT_PINK,
        fg=TEXT,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )


def create_progress_card(title, current, total, percentage):
    card = tk.Frame(
        content_area,
        bg=CARD
    )

    card.pack(
        fill="x",
        pady=6
    )

    top = tk.Frame(
        card,
        bg=CARD
    )

    top.pack(
        fill="x",
        padx=20,
        pady=(15, 5)
    )

    tk.Label(
        top,
        text=title,
        bg=CARD,
        fg=TEXT,
        font=("Arial", 11, "bold")
    ).pack(side="left")

    tk.Label(
        top,
        text=f"{percentage}%",
        bg=CARD,
        fg=DARK_PINK,
        font=("Arial", 11, "bold")
    ).pack(side="right")

    background_bar = tk.Frame(
        card,
        bg=SOFT_PINK,
        height=12
    )

    background_bar.pack(
        fill="x",
        padx=20,
        pady=8
    )

    background_bar.pack_propagate(False)

    progress_fill = tk.Frame(
        background_bar,
        bg=PINK
    )

    progress_fill.place(
        relwidth=percentage / 100,
        relheight=1
    )

    tk.Label(
        card,
        text=f"{current} / {total}",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 9)
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )


# =========================================================
# SETTINGS
# =========================================================

def show_settings():
    clear_content()

    page_title.config(text="Settings")

    tk.Label(
        content_area,
        text="Settings ⚙️",
        bg=BACKGROUND,
        fg=TEXT,
        font=("Arial", 23, "bold")
    ).pack(anchor="w")

    tk.Label(
        content_area,
        text="Customize your little productivity space.",
        bg=BACKGROUND,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(5, 20)
    )

    # =====================================================
    # APPEARANCE CARD
    # =====================================================

    appearance_card = tk.Frame(
        content_area,
        bg=CARD
    )

    appearance_card.pack(
        fill="x",
        pady=6
    )

    tk.Label(
        appearance_card,
        text="Appearance 🌸",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 5)
    )

    tk.Label(
        appearance_card,
        text="Choose how BLOOM looks.",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 12)
    )

    theme_frame = tk.Frame(
        appearance_card,
        bg=CARD
    )

    theme_frame.pack(
        anchor="w",
        padx=20,
        pady=(0, 20)
    )

    # Light theme button
    light_button = tk.Button(
        theme_frame,
        text="☀️  Light Theme",
        bg=LIGHT_SOFT_PINK,
        fg=LIGHT_DARK_PINK,
        activebackground=LIGHT_PINK,
        activeforeground="white",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: set_theme("light")
    )

    light_button.pack(
        side="left",
        padx=(0, 8)
    )

    # Dark theme button
    dark_button = tk.Button(
        theme_frame,
        text="🌙  Dark Theme",
        bg="#3A333B",
        fg="#FFFFFF",
        activebackground="#4A3C46",
        activeforeground="#FFFFFF",
        relief="flat",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8,
        cursor="hand2",
        command=lambda: set_theme("dark")
    )

    dark_button.pack(
        side="left"
    )

    # =====================================================
    # ABOUT CARD
    # =====================================================

    about_card = tk.Frame(
        content_area,
        bg=CARD
    )

    about_card.pack(
        fill="x",
        pady=6
    )

    tk.Label(
        about_card,
        text="About BLOOM 🌷",
        bg=CARD,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 5)
    )

    tk.Label(
        about_card,
        text="Your little productivity space for plans, goals, habits, notes and progress.",
        bg=CARD,
        fg=MUTED,
        font=("Arial", 10),
        wraplength=700,
        justify="left"
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 18)
    )


# =========================================================
# SIDEBAR
# =========================================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# Logo
tk.Label(
    sidebar,
    text="🌸",
    bg=SIDEBAR,
    fg=DARK_PINK,
    font=("Arial", 30)
).pack(
    pady=(25, 0)
)

tk.Label(
    sidebar,
    text="BLOOM",
    bg=SIDEBAR,
    fg=TEXT,
    font=("Arial", 20, "bold")
).pack()

tk.Label(
    sidebar,
    text="Your little productivity space",
    bg=SIDEBAR,
    fg=MUTED,
    font=("Arial", 8)
).pack(
    pady=(0, 25)
)


def create_menu_button(text, command):
    button = tk.Button(
        sidebar,
        text=text,
        bg=SIDEBAR,
        fg=TEXT,
        activebackground=SOFT_PINK,
        activeforeground=DARK_PINK,
        relief="flat",
        anchor="w",
        font=("Arial", 10),
        padx=22,
        pady=10,
        cursor="hand2",
        command=command
    )

    button.pack(
        fill="x",
        padx=10,
        pady=2
    )

    return button


create_menu_button(
    "🏠   Dashboard",
    show_home
)

create_menu_button(
    "📝   Plans",
    show_plans
)

create_menu_button(
    "🎯   Goals",
    show_goals
)

create_menu_button(
    "📅   Calendar",
    show_calendar
)

create_menu_button(
    "💗   Habits",
    show_habits
)

create_menu_button(
    "📊   Progress",
    show_progress
)

create_menu_button(
    "📔   Notes",
    show_notes
)

create_menu_button(
    "⚙️   Settings",
    show_settings
)


# =========================================================
# MAIN CONTENT
# =========================================================

main_area = tk.Frame(
    root,
    bg=BACKGROUND
)

main_area.pack(
    side="right",
    fill="both",
    expand=True
)


# Top bar
topbar = tk.Frame(
    main_area,
    bg=BACKGROUND,
    height=65
)

topbar.pack(
    fill="x",
    padx=30,
    pady=(15, 0)
)

topbar.pack_propagate(False)

page_title = tk.Label(
    topbar,
    text="Dashboard",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Arial", 18, "bold")
)

page_title.pack(
    side="left",
    pady=15
)


# Content area
content_area = tk.Frame(
    main_area,
    bg=BACKGROUND
)

content_area.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


# =========================================================
# START APP
# =========================================================

show_home()
update_greeting()

root.mainloop()
