from rich.console import Console
console = Console()

ism_list = []

while True:
    ism = input("Ism kiriting (chiqish uchun 'stop' yozing): ")
    if ism.lower().strip() == "stop":
        break
    ism_list.append(ism)

# Ismlar sonini rangli chiqarish
console.print(f"{len(ism_list)} ta ism bor", style="yellow")

# Ro'yxat uzunligi toq yoki juftligini rangli chiqarish
if len(ism_list) % 2 == 1:
    console.print("Ro'yxat uzunligi toq: True", style="bold green")
else:
    console.print("Ro'yxat uzunligi juft: False", style="bold red")
