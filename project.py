import tkinter as tk


def calculate_final_grade():
    grade_10 = float(entry_grade_10.get())
    grade_11 = float(entry_grade_11.get())
    grade_12 = float(entry_grade_12.get())

    total_1 = grade_10 * 0.1
    total_2 = grade_11 * 0.2
    total_3 = grade_12 * 0.7
    final = total_1 + total_2 + total_3

    if final >= 90:
        result_label.config(text=f"Your grade is {final:.2f} and you get the excellence degree")
    elif 80 < final < 90:
        result_label.config(text=f"Your grade is {final:.2f} and study hard to get the excellence degree")
    else:
        result_label.config(text=f"Your grade is {final:.2f} and study hard to get the excellence degree")


root = tk.Tk()
root.title("حساب المعدل التراكمي")       


label_grade_10 = tk.Label(root, text="العاشر")
label_grade_11 = tk.Label(root, text="الحادي عشر")
label_grade_12 = tk.Label(root, text="الثاني عشر")
entry_grade_10 = tk.Entry(root)
entry_grade_11 = tk.Entry(root)
entry_grade_12 = tk.Entry(root)

calculate_button = tk.Button(root, text="احسب المعدل التراكمي", command=calculate_final_grade)


result_label = tk.Label(root, text="")


label_grade_10.grid(row=0, column=0)
entry_grade_10.grid(row=0, column=1)
label_grade_11.grid(row=1, column=0)
entry_grade_11.grid(row=1, column=1)
label_grade_12.grid(row=2, column=0)
entry_grade_12.grid(row=2, column=1)
calculate_button.grid(row=3, columnspan=2)
result_label.grid(row=4, columnspan=2)


root.mainloop()