# dna_gui.py
# Version 3: Graphical interface using tkinter.
#
# Usage:
#   python dna_gui.py

import tkinter as tk
from tkinter import messagebox
from dna_library import analyze, format_results


def run_analysis():
    sequence = entry.get().strip()
    try:
        results = analyze(sequence)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, format_results(results))
        output_text.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


def clear_all():
    entry.delete(0, tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)


# --- Main window ---
root = tk.Tk()
root.title("DNA Sequence Analyzer")
root.resizable(False, False)

padding = {"padx": 12, "pady": 6}

# Title label
tk.Label(root, text="DNA Sequence Analyzer", font=("Helvetica", 16, "bold")).pack(**padding)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, **padding)

tk.Label(input_frame, text="Enter DNA sequence (5' → 3'):").pack(side=tk.LEFT)
entry = tk.Entry(input_frame, width=40, font=("Courier", 12))
entry.pack(side=tk.LEFT, padx=6)
entry.bind("<Return>", lambda event: run_analysis())  # Enter key triggers analysis

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(**padding)
tk.Button(btn_frame, text="Analyze", command=run_analysis, width=12, bg="#4a7c59", fg="white").pack(side=tk.LEFT, padx=4)
tk.Button(btn_frame, text="Clear", command=clear_all, width=12).pack(side=tk.LEFT, padx=4)

# Output text box
output_text = tk.Text(root, width=70, height=12, font=("Courier", 11), state=tk.DISABLED, bg="#f5f5f5")
output_text.pack(**padding)

root.mainloop()
