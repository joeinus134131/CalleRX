import tkinter as tk
from tkinter import messagebox, ttk
import time

# Fungsi untuk simulasi pengiriman pesan
def send_spam():
    phone_number = entry_number.get()
    message = entry_message.get()
    try:
        count = int(entry_count.get())
        delay = float(entry_delay.get())
    except ValueError:
        messagebox.showerror("Error", "Jumlah dan delay harus berupa angka!", icon="warning")
        return

    if not phone_number or not message:
        messagebox.showerror("Error", "Nomor telepon dan pesan tidak boleh kosong!", icon="warning")
        return

    status_label.config(text="Blasting...", fg="#00ffcc")
    progress_bar.start(10)
    root.update()

    for i in range(count):
        print(f"Pesan ke-{i+1} ke {phone_number}: {message}")
        time.sleep(delay)
        progress_bar.step(100 / count)

    progress_bar.stop()
    status_label.config(text="Blast Complete!", fg="#00ffcc")
    messagebox.showinfo("Sukses", f"{count} pesan telah 'dikirim' ke {phone_number}")

# Efek hover untuk tombol
def on_enter(e):
    send_button.config(bg="#ff6666", fg="white")

def on_leave(e):
    send_button.config(bg="#ff4444", fg="white")

# Membuat UI
root = tk.Tk()
root.title("Message Blaster X")
root.geometry("500x650")
root.configure(bg="#0f0f1a")

# Canvas untuk efek gradasi
canvas = tk.Canvas(root, width=500, height=650, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.configure(bg="#0f0f1a")

# Membuat gradasi
for i in range(650):
    r = int(15 + (i / 650) * 40)
    g = int(15 + (i / 650) * 40)
    b = int(26 + (i / 650) * 60)
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_line(0, i, 500, i, fill=color)

# Frame utama
main_frame = tk.Frame(canvas, bg="#1a1a2e", bd=0)
main_frame.place(relwidth=0.85, relheight=0.9, relx=0.075, rely=0.05)

# Judul
title_label = tk.Label(main_frame, text="Message Blaster X", font=("Arial", 26, "bold"), fg="#ff4444", bg="#1a1a2e")
title_label.pack(pady=25)

# Style untuk widget
style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", fieldbackground="#2e2e4d", foreground="#ffffff", borderwidth=0, padding=5)
style.configure("TLabel", background="#1a1a2e", foreground="#ffffff")
style.configure("Horizontal.TProgressbar", troughcolor="#1a1a2e", background="#ff4444")  # Gaya bawaan

# Nomor Telepon
label_number = ttk.Label(main_frame, text="📞 Nomor Telepon", font=("Arial", 12))
label_number.pack(pady=5)
entry_number = ttk.Entry(main_frame, width=35, font=("Arial", 12))
entry_number.pack()

# Pesan
label_message = ttk.Label(main_frame, text="💬 Pesan", font=("Arial", 12))
label_message.pack(pady=5)
entry_message = ttk.Entry(main_frame, width=35, font=("Arial", 12))
entry_message.pack()

# Jumlah Pengiriman
label_count = ttk.Label(main_frame, text="🔢 Jumlah", font=("Arial", 12))
label_count.pack(pady=5)
entry_count = ttk.Entry(main_frame, width=15, font=("Arial", 12))
entry_count.pack()

# Delay
label_delay = ttk.Label(main_frame, text="⏱ Delay (detik)", font=("Arial", 12))
label_delay.pack(pady=5)
entry_delay = ttk.Entry(main_frame, width=15, font=("Arial", 12))
entry_delay.pack()

# Tombol dengan efek hover
send_button = tk.Button(main_frame, text="Blast Off!", font=("Arial", 16, "bold"), bg="#ff4444", fg="white", 
                        bd=0, relief="flat", command=send_spam, padx=20, pady=10)
send_button.pack(pady=30)
send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# Progress Bar menggunakan gaya bawaan yang disesuaikan
progress_bar = ttk.Progressbar(main_frame, style="Horizontal.TProgressbar", length=350, mode="determinate")
progress_bar.pack(pady=15)

# Status
status_label = tk.Label(main_frame, text="", font=("Arial", 12, "italic"), bg="#1a1a2e", fg="#00ffcc")
status_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()