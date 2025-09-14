from rich.console import Console
console = Console()

from random import randint as rr

raqam = []


for az in range(10):
 number = rr(1, 100)
 raqam.append([number])
console.print(f"raqamlar ruyxati: {raqam}" , style="bold green")

slicing = int(input("oxirdan nechta raqam olasiz: ") , style="bold cyan")
oxirgi_slicing = raqam[-slicing:]

console.print(f"{oxirgi_slicing} oxirgi {slicing}ta raqam", style="bold white")
