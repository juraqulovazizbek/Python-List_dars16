from rich.console import Console
console = Console()



students = [
    ["Ali"],
    ["Vali",],
    ["G'ani"],
    ["Azizbek"],
    ["laziz"],
    ["uktam"]
]

console.print(f"hozirgi ro'yxat{students}", style="bold white")

while True:
# Foydalanuvchidan indeks va yangi ism so'rash
 index = int(input("Qaysi indeksni yangilamoqchisiz (0-5): "))
 new_name = input("Yangi ism kiriting: ")

 # Indeks bo‘yicha qiymatni yangilash
 if 0 <= index < len(students):
    students[index] = [new_name]   # ro'yxat ichida yangilanadi
    console.print("Yangilangan ro'yxat:", students, style="bold magenta")
    break
 else:
    console.print(" Bunday indeks mavjud emas!" , style="bold black")
    continue


