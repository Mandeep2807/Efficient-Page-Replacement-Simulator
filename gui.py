import tkinter as tk
from tkinter import messagebox, scrolledtext

from page_replacement import simulate_fifo, simulate_lru, simulate_optimal


def run_simulation():
    try:
        frame_count = int(entry_frames.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for frames.")
        return

    ref_string = entry_ref.get().strip()
    if not ref_string:
        messagebox.showerror("Error", "Please enter a reference string.")
        return

    try:
        pages = list(map(int, ref_string.split()))
    except ValueError:
        messagebox.showerror("Error", "Reference string must contain only integers separated by spaces.")
        return

    fifo_result = simulate_fifo(pages, frame_count)
    lru_result = simulate_lru(pages, frame_count)
    optimal_result = simulate_optimal(pages, frame_count)

    # clear previous output
    text_output.delete(1.0, tk.END)

    for result in [fifo_result, lru_result, optimal_result]:
        text_output.insert(tk.END, f"\nAlgorithm: {result['name']}\n")
        text_output.insert(tk.END, "Step\tPage\tFrames\t\tResult\n")
        for idx, step in enumerate(result["steps"], start=1):
            frames_str = " ".join(str(x) for x in step["frames"])
            text_output.insert(
                tk.END,
                f"{idx}\t{step['page']}\t{frames_str:<10}\t{step['result']}\n"
            )
        text_output.insert(tk.END, f"Total Page Faults: {result['page_faults']}\n")
        text_output.insert(tk.END, f"Total Hits: {result['hits']}\n")
        text_output.insert(tk.END, f"Hit Ratio: {result['hit_ratio']*100:.2f}%\n")

    all_results = [fifo_result, lru_result, optimal_result]
    best = min(all_results, key=lambda r: r["page_faults"])
    text_output.insert(tk.END, f"\nBest algorithm for this input (least page faults): {best['name']}\n")


# GUI setup
root = tk.Tk()
root.title("Page Replacement Simulator - OS PROJECT")

label_title = tk.Label(root, text="Efficient Page Replacement Algorithm Simulator (FIFO, LRU, Optimal)", font=("Arial", 14, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_frames = tk.Label(root, text="Number of Frames:")
label_frames.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_frames = tk.Entry(root)
entry_frames.grid(row=1, column=1, padx=5, pady=5)

label_ref = tk.Label(root, text="Reference String:")
label_ref.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_ref = tk.Entry(root, width=40)
entry_ref.grid(row=2, column=1, padx=5, pady=5)

button_run = tk.Button(root, text="Run Simulation", command=run_simulation)
button_run.grid(row=3, column=0, columnspan=2, pady=10)

text_output = scrolledtext.ScrolledText(root, width=70, height=20)
text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()




