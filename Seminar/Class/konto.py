class Konto:
    def __init__(self, nr: str, adm: str, betrag: int = 0):
        self.nr = nr
        self.betrag = betrag
        self.adm = adm

    def plus(self, k):
        self.betrag += k

    def minus(self, k):
        self.betrag -= k
