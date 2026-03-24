import tkinter as tk
import random, webbrowser, base64, urllib.request

# ---------- ลิงก์รูป ----------
OUTSIDE_URL = "https://cdn.discordapp.com/attachments/1445058089777889392/1486048814686011402/IMG_20260311_230238_646.webp"
INSIDE_URL  = "https://cdn.discordapp.com/attachments/1445058089777889392/1486049430238138428/IMG_20260207_174601_375.webp"

# ---------- โหลดรูป ----------
def load_img(url):
    try:
        raw = urllib.request.urlopen(url).read()
        return tk.PhotoImage(data=base64.b64encode(raw))
    except:
        return None

outside_img = load_img(OUTSIDE_URL)
inside_img  = load_img(INSIDE_URL)

# ---------- root ----------
root = tk.Tk()
root.title("จดหมาย 💌")
root.geometry("500x600")
root.configure(bg="#ffe6f0")

# ---------- AI ----------
def ai_reply():
    return random.choice([
        "ก็...ให้อภัยก็ได้ 😳",
        "โอเค ๆ ใจอ่อนก็ได้ 💕",
        "งั้นยกโทษให้ครั้งนี้ 😆",
        "ก็รักแหละ เลยยอม 💖"
    ])

# ---------- พิมพ์ทีละตัว ----------
def type_text(label, text, i=0):
    if i <= len(text):
        label.config(text=text[:i])
        root.after(40, type_text, label, text, i+1)

# ---------- เพลง ----------
def play_music():
    webbrowser.open("https://youtu.be/a_idHhd77es")

# ---------- หัวใจระเบิด ----------
def hearts():
    for _ in range(40):
        x = random.randint(0,480)
        y = random.randint(0,580)
        h = tk.Label(root, text="💖", bg="#ffe6f0",
                     font=("Arial", random.randint(10,20)))
        h.place(x=x,y=y)

        def anim(lbl,y0):
            if y0>-50:
                lbl.place(y=y0)
                root.after(20,anim,lbl,y0-random.randint(5,15))
            else:
                lbl.destroy()
        anim(h,y)
    root.after(400, hearts)

# ---------- เคลียร์ ----------
def clear():
    for w in root.winfo_children():
        w.destroy()

# ---------- หน้าแรก ----------
def show_envelope():
    clear()

    tk.Label(root, text="📩 มีจดหมายถึงคุณ",
             font=("Arial",18), bg="#ffe6f0").pack(pady=10)

    if outside_img:
        lbl = tk.Label(root, image=outside_img, bg="#ffe6f0")
        lbl.image = outside_img
        lbl.pack(pady=10)
        zoom_effect(lbl)

    tk.Button(root, text="เปิดจดหมาย",
              font=("Arial",14),
              bg="#ff99cc",
              command=show_letter).pack(pady=20)

# ---------- zoom + กระพริบ ----------
def zoom_effect(widget):
    def blink():
        widget.config(bg=random.choice(["#ffe6f0","#ffd6ec","#fff0f5"]))
        root.after(300, blink)
    blink()

# ---------- หน้าจดหมาย ----------
def show_letter():
    clear()

    tk.Label(root, text="ขอโทษนะ 💗",
             font=("Arial",22), bg="#ffe6f0").pack(pady=10)

    if inside_img:
        lbl = tk.Label(root, image=inside_img, bg="#ffe6f0")
        lbl.image = inside_img
        lbl.pack(pady=10)
        zoom_effect(lbl)

    tk.Label(root,
             text="ให้อภัยเราได้ไหม 🥺",
             font=("Arial",14),
             bg="#ffe6f0").pack(pady=10)

    # Yes
    tk.Button(root,
              text="Yes 💖",
              font=("Arial",14),
              bg="#66ff99",
              command=answer).place(x=120,y=450)

    # ---------- No หลายตัว ----------
    no_buttons = []
    for i in range(5):
        b = tk.Button(root, text="No 😢", bg="#ff6666")
        b.place(x=random.randint(50,400), y=random.randint(300,550))
        no_buttons.append(b)

    # ---------- หนี + ตามเมาส์ ----------
    def chase_mouse(event):
        for b in no_buttons:
            bx = random.randint(0,420)
            by = random.randint(200,550)
            b.place(x=bx,y=by)

    root.bind("<Motion>", chase_mouse)

# ---------- กด Yes ----------
def answer():
    clear()
    play_music()

    lbl = tk.Label(root, font=("Arial",20), bg="#ffe6f0")
    lbl.pack(expand=True)

    type_text(lbl, ai_reply())
    hearts()

# ---------- start ----------
show_envelope()
root.mainloop()