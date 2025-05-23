import tkinter as tk
from tkinter import ttk
import json

# Load JSON from file
def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Hover effects
def on_enter(event):
    event.widget.config(bg="#e0e7ff", highlightbackground="#888", highlightthickness=3)

def on_leave(event):
    event.widget.config(bg="#f0f4ff", highlightthickness=0)

# Display each student as a colorful card
def display_students(frame, data):
    for widget in frame.winfo_children():
        widget.destroy()

    for i, student in enumerate(data):
        # Card frame
        card = tk.Frame(
            frame,
            bg="#f0f4ff",
            bd=2,
            relief="flat",
            padx=15,
            pady=15,
            highlightbackground="#ccc",
            highlightthickness=0,
        )
        card.grid(row=i, column=0, pady=10, padx=10)
        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)

        # Centering card contents
        inner = tk.Frame(card, bg="#f0f4ff")
        inner.pack()

        # Get student data
        name = student.get("name", "No Name")
        school = student.get("school", "Unknown School")
        course = student.get("course-of-study", "Mystery Course")
        quote = student.get("favourite-Quote", "No quote here!")

        # Labels
        tk.Label(inner, text=f"🎓 {name}", font=('Comic Sans MS', 14, 'bold'), bg="#f0f4ff", fg="#4a148c").pack(anchor='center')
        tk.Label(inner, text=f"🏫 School: {school}", font=('Comic Sans MS', 10), bg="#f0f4ff").pack(anchor='center')
        tk.Label(inner, text=f"📘 Course: {course}", font=('Comic Sans MS', 10), bg="#f0f4ff").pack(anchor='center')
        tk.Label(inner, text=f"✨ Quote: “{quote}”", font=('Comic Sans MS', 10, 'italic'), bg="#f0f4ff", fg="#1b5e20").pack(anchor='center')

# Main app
def main():
    data = load_json('data.json')

    root = tk.Tk()
    root.title("🎉 ICT Students Hall of Fame 🎉")
    # root.geometry("300x300")
    root.configure(bg="#e3f2fd")

    title = tk.Label(root, text="Welcome to the IT Club 😎", font=('Comic Sans MS', 16, 'bold'), bg="#e3f2fd", fg="#0d47a1")
    title.pack(pady=10)

    # Scrollable frame setup
    container = tk.Frame(root, bg="#e3f2fd")
    canvas = tk.Canvas(container, bg="#e3f2fd", highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#e3f2fd")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Center column in scrollable_frame
    scrollable_frame.grid_columnconfigure(0, weight=1)

    # Display students
    display_students(scrollable_frame, data)

    root.mainloop()

if __name__ == "__main__":
    main()
