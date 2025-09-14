from rich.console import Console
console = Console()

from random import randint as rr

raqam = []


for az in range(10):
 number = rr(1, 100)
 raqam.append([number])
console.print(f"raqamlar ruyxati: {raqam}", style="bold white")

console.print(f"juft raqamlar ro'yxati", raqam[::2] , style="bold yellow")
console.print(f"toq raqamlar ro'yxati", raqam[1::2], style="bold green")

