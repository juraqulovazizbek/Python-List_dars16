from rich.console import Console
console = Console()

from random import randint as rr

raqam = []


for az in range(10):
 number = rr(1, 100)
 raqam.append([number])
console.print(f"raqamlar ruyxati: {raqam}", style="bold black")

console.print(f"teskari  raqamlar ro'yxati", raqam[::-1], style="bold bright_green")

