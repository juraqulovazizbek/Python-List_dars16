from rich.console import Console

console = Console()

ism_list = []

while True:
    ism = input("Ism kiriting (chiqish uchun 'stop' yozing): ")
    if ism.lower().strip() == "stop":
        break
    ism_list.append(ism)

print()
console.print("Siz kiritgan ismlar:", style="bold cyan")
console.print(ism_list, style="green")

print()
console.print(f"Umumiy kiritilgan ismlar soni: {len(ism_list)}", style="bold yellow")
