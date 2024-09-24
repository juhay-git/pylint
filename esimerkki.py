# esimerkki.py

"""Esimerkkimoduuli, joka demonstroi peruslaskutoimituksia ja yksinkertaisen luokan."""

from numbers import Number


def add(a: Number, b: Number) -> Number:
    """Laskee kahden luvun summan.

    Args:
        a (Number): Ensimmäinen yhteenlaskettava.
        b (Number): Toinen yhteenlaskettava.

    Returns:
        Number: Lukujen a ja b summa.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Vähentää toisen luvun ensimmäisestä.

    Args:
        a (Number): Vähennettävä.
        b (Number): Vähentäjä.

    Returns:
        Number: Lukujen a ja b erotus.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Kertoo kaksi lukua keskenään.

    Args:
        a (Number): Ensimmäinen kerrottava.
        b (Number): Toinen kerrottava.

    Returns:
        Number: Lukujen a ja b tulo.
    """
    return a * b


class OmaLuokka:
    """Luokka, joka säilyttää arvon ja voi suorittaa operaatioita sille."""

    def __init__(self, x: Number):
        """Alustaa luokan annetulla arvolla.

        Args:
            x (Number): Tallennettava arvo.
        """
        self.x = x

    def double_value(self) -> Number:
        """Laskee tallennetun arvon kaksinkertaisena.

        Returns:
            Number: Kaksinkertainen arvo.
        """
        return self.x * 2

    def print_x(self):
        """Tulostaa tallennetun arvon."""
        print(f"Tallennettu arvo on: {self.x}")

    def __str__(self) -> str:
        """Tarjoaa merkkijonoesityksen oliosta.

        Returns:
            str: Olion kuvaava merkkijono.
        """
        return f'OmaLuokka(x={self.x})'


def main():
    """Pääfunktio, joka demonstroi funktioiden ja OmaLuokka-luokan käyttöä."""
    # Demonstroi laskufunktioita
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}\n")

    # Demonstroi OmaLuokka
    x = 5
    olio = OmaLuokka(x)
    olio.print_x()
    print(f"Kaksinkertainen arvo: {olio.double_value()}")
    print(f"Olion esitys: {olio}")


if __name__ == '__main__':
    main()
