import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))


def check_p1_e1(dochazka, pocet_ucastniku):
    assert dochazka is not None, "Seznam není definován!"
    assert pocet_ucastniku is not None, "Počet účastníků není definován!"
    assert len(dochazka) == 4, "Seznam neobsahuje správný počet jmen!"
    for i in range(4):
        assert isinstance(
            dochazka[i], str), "Seznam není správného datového typu!"
    assert "Jitka" in dochazka, 'Seznam neobsahuje jméno "Jitka"!'
    assert "Michal" in dochazka, 'Seznam neobsahuje jméno "Michal"!'
    assert "Lucie" in dochazka, 'Seznam neobsahuje jméno "Lucie"!'
    assert "Josef" in dochazka, 'Seznam neobsahuje jméno "Josef"!'
    assert dochazka == ["Jitka", "Michal", "Lucie",
                        "Josef"], 'Seznam neobsahuje jména ve správném pořadí!'
    assert pocet_ucastniku == 4, "Počet účastníků není správný!"
    print("\x1b[32mVšechny testy proběhly úspěšně!\x1b[0m")


def check_p1_e2(func):
    zavodnice = []
    for i in range(random.randrange(8, 15)):
        zavodnice.append(get_random_string(8))
    jmeno_vitezky, jmeno_druhe, jmeno_treti, pocet_zavodnic = func(zavodnice)
    assert jmeno_vitezky == zavodnice[0], "Jméno vítězky neodpovídá skutečné vítězce!"
    assert jmeno_druhe == zavodnice[1], "Jméno druhé neodpovídá skutečné druhé závodnici!"
    assert jmeno_treti == zavodnice[2], "Jméno třetí neodpovídá skutečné třetí závodnici!"
    assert pocet_zavodnic == len(
        zavodnice), "Počet závodnic neodpovídá skutečnému počtu závodnic!"
    print("\x1b[32mVšechny testy proběhly úspěšně!\x1b[0m")
