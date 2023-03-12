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


def check_p1_e2():
    print("\x1b[32mVšechny testy proběhly úspěšně!\x1b[0m")
