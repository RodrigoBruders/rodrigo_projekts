import math

def iegut_darbibu():
    """
    Izvada uz ekrāna uzvedni lietotājam ievadīt darbību un atgriež to.
    """
    while True:
        darbiba = input("Ievadiet darbību (+, -, *, /, sin, cos, tan, log, faktoriāls, sakne, vai 'beigt'): ").lower()
        if darbiba in ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'log', 'faktoriāls', 'sakne', 'beigt']:
            return darbiba

def iegut_skaitlus(darbiba):
    """
    Izvada uz ekrāna uzvedni lietotājam ievadīt vienu vai divus skaitļus atkarībā no darbības.
    """
    if darbiba in ['sin', 'cos', 'tan', 'log', 'faktoriāls', 'sakne']:
        return [float(input("Ievadiet skaitli: "))]
    else:
        return [float(input("Ievadiet pirmo skaitli: ")), float(input("Ievadiet otro skaitli: "))]

def aprekinat(darbiba, skaitli):
    """
    Veic aprēķinu, pamatojoties uz darbību un skaitļiem.
    """
    darbibas = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Kļūda: Dalīšana ar nulli",
        'sin': lambda x: math.sin(math.radians(x)),
        'cos': lambda x: math.cos(math.radians(x)),
        'tan': lambda x: math.tan(math.radians(x)),
        'log': lambda x: math.log(x),
        'faktoriāls': lambda x: math.factorial(int(x)) if x >= 0 else "Kļūda: Faktoriāls nav definēts negatīviem skaitļiem",
        'sakne': lambda x: math.sqrt(x)
    }

    if darbiba in darbibas:
        if len(skaitli) == 1:
            return darbibas[darbiba](skaitli[0])
        else:
            return darbibas[darbiba](skaitli[0], skaitli[1])
    else:
        return "Kļūda: Nepareiza darbība"

def zinatniskais_kalkulators():
    """
    Izpilda zinātnisko kalkulatoru.
    """
    while True:
        darbiba = iegut_darbibu()
        if darbiba == 'beigt':
            break
        skaitli = iegut_skaitlus(darbiba)
        rezultats = aprekinat(darbiba, skaitli)
        print(f"Rezultāts: {rezultats}")

zinatniskais_kalkulators()