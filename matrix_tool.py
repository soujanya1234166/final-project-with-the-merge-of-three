import tkinter as tk
from tkinter import messagebox
import numpy as np

# -------- FUNCTIONS -------- #

def get_matrix(entries, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = entries[i][j].get()
            if value == "":
                return None
            row.append(float(value))
        matrix.append(row)
    return np.array(matrix)


def display_result(result):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(result))


def add_matrices():
    A = get_matrix(entries_A, rows, cols)
    B = get_matrix(entries_B, rows, cols)
    if A is not None and B is not None:
        display_result(A + B)
    else:
        messagebox.showerror("Error", "Fill all matrix fields")


def subtract_matrices():
    A = get_matrix(entries_A, rows, cols)
    B = get_matrix(entries_B, rows, cols)
    if A is not None and B is not None:
        display_result(A - B)
    else:
        messagebox.showerror("Error", "Fill all matrix fields")


def multiply_matrices():
    A = get_matrix(entries_A, rows, cols)
    B = get_matrix(entries_B, rows, cols)
    if A is not None and B is not None:
        display_result(np.dot(A, B))
    else:
        messagebox.showerror("Error", "Fill all matrix fields")


def transpose_A():
    A = get_matrix(entries_A, rows, cols)
    if A is not None:
        display_result(A.T)


def determinant_A():
    A = get_matrix(entries_A, rows, cols)
    if A is not None:
        display_result(np.linalg.det(A))


# -------- GUI SETUP -------- #

rows, cols = 2, 2  # Fixed 2x2 matrix for simplicity

root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("600x500")
root.configure(bg="#f0f4f8")

title = tk.Label(root, text="Matrix Operations Tool",
                 font=("Arial", 18, "bold"),
                 bg="#f0f4f8", fg="#2c3e50")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

entries_A = []
entries_B = []

tk.Label(frame, text="Matrix A", font=("Arial", 12, "bold"),
         bg="#f0f4f8").grid(row=0, column=0, columnspan=2)

tk.Label(frame, text="Matrix B", font=("Arial", 12, "bold"),
         bg="#f0f4f8").grid(row=0, column=3, columnspan=2)

for i in range(rows):
    row_A = []
    row_B = []
    for j in range(cols):
        eA = tk.Entry(frame, width=5, font=("Arial", 14))
        eA.grid(row=i+1, column=j, padx=5, pady=5)
        row_A.append(eA)

        eB = tk.Entry(frame, width=5, font=("Arial", 14))
        eB.grid(row=i+1, column=j+3, padx=5, pady=5)
        row_B.append(eB)

    entries_A.append(row_A)
    entries_B.append(row_B)

# -------- BUTTONS -------- #

button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add", width=12, bg="#27ae60",
          fg="white", command=add_matrices).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Subtract", width=12, bg="#e67e22",
          fg="white", command=subtract_matrices).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Multiply", width=12, bg="#2980b9",
          fg="white", command=multiply_matrices).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="Transpose A", width=12, bg="#8e44ad",
          fg="white", command=transpose_A).grid(row=1, column=0, pady=5)

tk.Button(button_frame, text="Determinant A", width=12, bg="#c0392b",
          fg="white", command=determinant_A).grid(row=1, column=1, pady=5)

# -------- RESULT AREA -------- #

result_label = tk.Label(root, text="Result:",
                        font=("Arial", 12, "bold"),
                        bg="#f0f4f8")
result_label.pack()

result_text = tk.Text(root, height=5, width=40,
                      font=("Arial", 14))
result_text.pack(pady=10)

root.mainloop()
