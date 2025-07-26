import tkinter as tk
from tkinter import messagebox

# クリック時の枠トグル
def on_click(event):
     # クリックされたのがフレームかラベルか判定して、Frameオブジェクトを取得
     widget = event.widget
     frame = widget if isinstance(widget, tk.LabelFrame) else widget.master

     # トグル用に現在の bd をチェック
     current_bd = int(frame.cget('bd'))
     # 元の bd と relief
     orig_bd = frame.original_bd
     orig_relief = frame.original_relief

     if current_bd == orig_bd:
         # 枠を太くして relief を変える
         frame.config(bd=6, relief='sunken')
     else:
         # 元に戻す
         frame.config(bd=orig_bd, relief=orig_relief)

# メインウィンドウ
root = tk.Tk()
root.title("Rifted Crown Ph2")

# 全フレームを保存するリスト
frames = []

colors = ['tan', 'deep pink', 'tomato', 'yellow', 'chartreuse2', 'deep sky blue', 'MediumPurple1', 'gray60', 'white']
labels = [
    'Baroness\nVorlithia', 
    'General\nMalvash', 
    'Warden\nKhorvath', 
    'Morrigan\nVeilshroud', 
    'Kalyndra\nNighthollow', 
    'Seraphine\nGloomveil', 
    'Harbinger\nDraal', 
    'Lord\nVhaelor', 
    'Inquisitor\nZynthar'
]

# フレーム作成
for i, (c, text) in enumerate(zip(colors, labels)):
    lf = tk.LabelFrame(root, width=80, height=50, bg=c, bd=2, relief="groove")
    # 元の枠設定を属性に保存
    lf.original_bd = 2
    lf.original_relief = "groove"
    lf.grid(column=i%3, row=i//3, padx=5, pady=5)

    lbl = tk.Label(lf, text=text, bg=c)
    lbl.place(relx=0.5, rely=0.5, anchor="center")

    # フレームとラベルにクリックイベントをバインド
    lf.bind("<Button-1>", on_click)
    lbl.bind("<Button-1>", on_click)

    # リストに追加
    frames.append(lf)

# リセットボタンのコールバック
def reset_all():
     if messagebox.askyesno("リセット確認", "リセットしますか？"):
         for frame in frames:
             frame.config(bd=frame.original_bd, relief=frame.original_relief)

# リセットボタン作成
reset_button = tk.Button(root, text="リセット", command=reset_all)
reset_button.grid(column=0, row=3, columnspan=3, pady=10)

root.mainloop()

