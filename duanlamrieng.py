import tkinter as tk
from tkinter import messagebox
import random,time,secrets

def roll_dice():
    """
    Sinh ra 3 xúc xắc với độ ngẫu nhiên cao, khó đoán trước.
    Pha trộn entropy từ time, secrets và random.
    """
    dices = []
    for i in range(3):
        # Trộn ngẫu nhiên thời gian, random và secrets
        seed = int(time.time_ns() * random.random() * secrets.randbits(16))
        random.seed(seed)
        dices.append(random.randint(1, 6))
        time.sleep(random.random() * 0.02)  # trễ ngẫu nhiên vài mili-giây
    return dices

def is_triple(dices):
    return dices[0] == dices[1] == dices[2]

def get_result(dices):
    s = sum(dices)
    if is_triple(dices):
        return "TRIPLE", s
    elif 4 <= s <= 10:
        return "XIU", s
    elif 11 <= s <= 17:
        return "TAI", s
    return "UNKNOWN", s


class TaiXiuApp:
    def __init__(self, root):
        self.root = root
        root.title("🎲 Tài Xỉu Siêu Mượt 🎲")
        root.geometry("1400x900")
        root.configure(bg="#8B0000")
        root.resizable(False, False)

        self.balance = 1_000_000
        self.shaking = False
        self.bowl_dragging = False
        self.bowl_opened = False

        tk.Label(root, text="🎲 TÀI XỈU 🎲", font=("Arial", 24, "bold"),
                 bg="#8B0000", fg="white").pack(pady=10)
        self.balance_label = tk.Label(root, text=f"Số dư: {self.balance:,}",
                                      font=("Arial", 14), bg="#8B0000", fg="white")
        self.balance_label.pack()

        frm = tk.Frame(root, bg="#8B0000")
        frm.pack(pady=10)
        tk.Label(frm, text="Tiền cược:", bg="#8B0000", fg="white").grid(row=0, column=0, sticky="e")
        self.bet_entry = tk.Entry(frm, width=10)
        self.bet_entry.insert(0, "100000")
        self.bet_entry.grid(row=0, column=1, padx=6)

        self.choice_var = tk.StringVar(value="TAI")
        tk.Radiobutton(frm, text="Tài", variable=self.choice_var, value="TAI",
                       bg="#8B0000", fg="white", selectcolor="#a00000").grid(row=1, column=0)
        tk.Radiobutton(frm, text="Xỉu", variable=self.choice_var, value="XIU",
                       bg="#8B0000", fg="white", selectcolor="#a00000").grid(row=1, column=1)

        self.play_button = tk.Button(root, text="🎲 Lắc xúc xắc",
                                     font=("Arial", 14, "bold"),
                                     command=self.play,
                                     bg="gold", fg="black", width=15)
        self.play_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=500, height=300, bg="#B22222", highlightthickness=0)
        self.canvas.pack(pady=10)

        # 🎲 Xúc xắc màu trắng, xếp tam giác
        self.dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        positions = [(230, 180), (270, 180), (250, 150)]
        self.dice_labels = []
        for (x, y) in positions:
            lbl = self.canvas.create_text(
                x, y, text="⚀", font=("Arial", 36, "bold"),
                fill="white", tags="dice"
            )
            self.dice_labels.append(lbl)

        # 🥣 Bát úp (ở giữa)
        self.bowl = self.canvas.create_oval(100, -150, 400, 100,
                                            fill="#d4af37", outline="#b8860b", width=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 14),
                                     bg="#8B0000", fg="white")
        self.result_label.pack(pady=8)

        self.history_text = tk.Text(root, height=6, width=58,
                                    state="disabled", bg="#300000", fg="white")
        self.history_text.pack(pady=6)

        tk.Button(root, text="Reset số dư", command=self.reset,
                  bg="gray", fg="white").pack(pady=4)

        # Sự kiện kéo bát
        self.canvas.tag_bind(self.bowl, "<Button-1>", self.start_drag)
        self.canvas.tag_bind(self.bowl, "<B1-Motion>", self.drag_bowl)
        self.canvas.tag_bind(self.bowl, "<ButtonRelease-1>", self.stop_drag)

    # ===== Lô-gic chính =====
    def append_history(self, text):
        self.history_text.config(state="normal")
        self.history_text.insert("end", text + "\n")
        self.history_text.see("end")
        self.history_text.config(state="disabled")

    def play(self):
        if self.shaking:
            return
        try:
            bet = int(self.bet_entry.get())
        except:
            messagebox.showerror("Lỗi", "Tiền cược phải là số nguyên.")
            return
        if bet <= 0 or bet > self.balance:
            messagebox.showerror("Lỗi", "Tiền cược không hợp lệ.")
            return

        self.current_bet = bet
        self.current_choice = self.choice_var.get()
        self.result_label.config(text="🎲 Đang lắc xúc xắc...")
        self.shaking = True
        self.play_button.config(state="disabled")

        # ✅ Reset vị trí bát
        self.canvas.coords(self.bowl, 100, -150, 400, 100)
        self.canvas.itemconfig(self.bowl, state="normal")
        self.canvas.lift(self.bowl)
        self.bowl_opened = False

        # 🎲 Lắc xúc xắc rồi úp bát
        self.animate_dice(15)
        self.root.after(1000, self.drop_bowl)

    def animate_dice(self, count):
        if count <= 0:
            self.true_dices = roll_dice()
            for i, d in enumerate(self.true_dices):
                self.canvas.itemconfig(self.dice_labels[i], text=self.dice_faces[d - 1])
            return

        for i in range(3):
            self.canvas.itemconfig(self.dice_labels[i], text=random.choice(self.dice_faces))
        self.root.after(50, lambda: self.animate_dice(count - 1))

    def drop_bowl(self):
        self.bowl_y = -150
        self.animate_bowl_drop()

    def animate_bowl_drop(self):
        if self.bowl_y < 80:
            self.bowl_y += 30
            self.canvas.coords(self.bowl, 100, self.bowl_y, 400, self.bowl_y + 250)
            self.root.after(20, self.animate_bowl_drop)
        else:
            self.finish_round()

    def finish_round(self):
        self.true_result, self.true_sum = get_result(self.true_dices)
        self.result_label.config(text="🫕 Bát đã úp. Dùng chuột kéo bát ra để xem kết quả!")
        self.shaking = False

    # ===== Kéo bát =====
    def start_drag(self, event):
        if self.shaking or self.bowl_opened:
            return
        self.bowl_dragging = True
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def drag_bowl(self, event):
        if not self.bowl_dragging:
            return
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        self.canvas.move(self.bowl, dx, dy)
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        coords = self.canvas.coords(self.bowl)
        if coords[1] < -40:
            self.bowl_dragging = False
            self.open_result()

    def stop_drag(self, event):
        self.bowl_dragging = False

    def open_result(self):
        self.bowl_opened = True
        self.canvas.itemconfig(self.bowl, state="hidden")

        if self.true_result == "TRIPLE":
            self.balance -= self.current_bet
            msg = f"🎲 TRIPLE! {self.true_dices} — Bạn thua {self.current_bet:,}"
        else:
            if self.current_choice == self.true_result:
                self.balance += self.current_bet
                msg = f"✅ Bạn thắng! {self.true_dices} — Nhận {self.current_bet:,}"
            else:
                self.balance -= self.current_bet
                msg = f"❌ Bạn thua. {self.true_dices} — Mất {self.current_bet:,}"

        self.result_label.config(text=msg)
        self.append_history(msg)
        self.balance_label.config(text=f"Số dư: {self.balance:,}")
        self.play_button.config(state="normal")

    def reset(self):
        self.balance = 1_000_000
        self.balance_label.config(text=f"Số dư: {self.balance:,}")
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", "end")
        self.history_text.config(state="disabled")
        self.result_label.config(text="")
        for i in self.dice_labels:
            self.canvas.itemconfig(i, text="⚀")
        self.canvas.coords(self.bowl, 100, -150, 400, 100)
        self.canvas.itemconfig(self.bowl, state="normal")
        self.shaking = False
        self.bowl_opened = False
        self.play_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaiXiuApp(root)
    root.mainloop()
