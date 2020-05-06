def je_prastevilo(n):
    """Funkcija, ki pove ali je podano stevilo prastevilo."""
    a = 0
    for i in range(1, n + 1):
        if n % i == 0:
            a += 1
    if a == 2:
        return True
    else:
        return False

for i in range(200):
    if je_prastevilo(i):
        print(i)