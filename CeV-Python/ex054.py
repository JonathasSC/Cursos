import datetime 
anoat = datetime.date.today().year
adultos = 0
teens = 0
idosos = 0
for s in range(1,8):
    dateyear = int(input(f"Em que ano nasceu a {s} pessoa?: "))
    yearsold = anoat - dateyear 
    if yearsold >= 18 and yearsold < 56:
        adultos = adultos + 1
    if yearsold < 18:
        teens = teens + 1
    if yearsold >= 60:
        idosos = idosos + 1
print(f"Entre os perguntados existe {idosos} idoso(s), {adultos} adulto(s) e {teens} joven(s)")