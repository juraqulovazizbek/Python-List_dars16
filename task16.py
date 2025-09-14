from rich.console import Console

console = Console()

def ruyxat(matn: str):
    result = matn.split()
    return result

ss = input("Matn kiriting: ")
result = ruyxat(ss)

console.print(f"Matnda {len(result)} ta so'z bor", style="bold green")

if len(result) <= 5:
    console.print("Kichkina matn", style="bold yellow")
elif len(result) < 100:
    console.print("O'rtacha matn", style="bold cyan")
else:
    console.print("Juda katta matn", style="bold red")
