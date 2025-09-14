from random import randint as rr
from rich.console import Console
console = Console()

raqam = []


for az in range(10):
 number = rr(1, 100)
 raqam.append([number])


console.print(f"raqamlar ro'yxati {raqam}" , style="bold blue")


start = int(input("start: "))
  # 1 dan boshlangan deb olaymiz
end = int(input("end: "))


console.print(f"{start+1}-dan {end}-gacha bo'lgan qismi:", raqam[start:end], style="bold red")