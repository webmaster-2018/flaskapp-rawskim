import sqlite3
from modele import Klasa, Uczen, Plec, Ocena


def student(cur):
    cur.execute("""
            SELECT * FROM Uczen;
        """)
    wyniki = cur.fetchall()
    for row in wyniki:
            print(row)

def main(args):
    # KONFIGURACJA ####
    baza_nazwa = 'uczniowie'
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()
    ###################
    student(cur)
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

