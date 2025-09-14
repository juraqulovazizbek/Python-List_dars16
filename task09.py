from rich.console import Console
console = Console()



students = [
    ["Ali", 18],
    ["Vali", 20],
    ["G'ani", 25],
    ["Azizbek", 17]
]
print(students)
new_age = int(input("Yangi yosh: "))

students[2][1] = new_age   # faqat shu qator o‘zgartiriladi
console.print(students , style="bold bright_green")
