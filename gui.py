import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# 设置ttkbootstrap的主题
style = Style(theme='minty')


# 计算x, y, z的函数
def calculate_values(A0, B0, C0, A_step, B_step, C_step):
    results = []

    # 动态计算max_state，根据步长值限制最大状态
    max_A = A_step * 5  # 你可以根据需要调整这个倍数
    max_B = B_step * 5
    max_C = C_step * 5

    # 限制最大循环次数，防止长时间卡顿
    max_iterations = 20  # 最大迭代次数限制

    # 根据输入的步长和最大状态范围进行循环计算
    for i in range(0, min(lcm(max_A, max_C), max_iterations)):
        for j in range(0, min(lcm(max_B, max_C), max_iterations)):
            for k in range(0, min(lcm(max_B, max_A), max_iterations)):
                At = (i + k) * A_step + A0
                Bt = (j + k) * B_step + B0
                Ct = (i + j) * C_step + C0
                if not (At % 6 or Bt % 6 or Ct % 6):
                    results.append(f'x={i}; y={j}; z={k}')
    return results


# 当用户点击Calculate按钮时执行
def on_calculate():
    try:
        # 获取用户输入的值
        A0 = int(entry_A0.get())
        B0 = int(entry_B0.get())
        C0 = int(entry_C0.get())
        A_step = int(entry_A_step.get())
        B_step = int(entry_B_step.get())
        C_step = int(entry_C_step.get())

        # 调用计算函数
        results = calculate_values(A0, B0, C0, A_step, B_step, C_step)

        # 输出结果通过弹窗显示
        if results:
            messagebox.showinfo("Calculation Result", "\n".join(results))
        else:
            messagebox.showinfo("Calculation Result", "没有找到结果。")
    except ValueError:
        # 当输入的不是整数时，显示错误提示
        messagebox.showerror("Input Error", "请输入有效的整数。")


# 创建GUI窗口
root = tk.Tk()
root.title("Calculate x, y, z")

# 窗口自适应调整
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(7, weight=1)

# 输入A0, B0, C0, A_step, B_step, C_step
tk.Label(root, text="A0:").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
entry_A0 = tk.Entry(root)
entry_A0.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="B0:").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
entry_B0 = tk.Entry(root)
entry_B0.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="C0:").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
entry_C0 = tk.Entry(root)
entry_C0.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="A_step:").grid(row=3, column=0, padx=5, pady=5, sticky="ew")
entry_A_step = tk.Entry(root)
entry_A_step.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="B_step:").grid(row=4, column=0, padx=5, pady=5, sticky="ew")
entry_B_step = tk.Entry(root)
entry_B_step.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="C_step:").grid(row=5, column=0, padx=5, pady=5, sticky="ew")
entry_C_step = tk.Entry(root)
entry_C_step.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# 计算按钮
calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# 显示结果，初始化避免空白弹窗
result_text = tk.StringVar(value="点击 Calculate 查看结果")
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# 运行主循环
root.mainloop()
