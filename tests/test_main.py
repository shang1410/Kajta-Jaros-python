from src.main import *


def testGetCountTeam():
    assert getCountTeam(["sgr", "ert"]) == 2
    assert getCountTeam([]) == 0


def testPrintTeamMembers(capsys):
    team = ["a", "b", "c"]
    printTeamMembers(team)
    captured = capsys.readouterr()
    assert "1. a" in captured.out
    assert "2. b" in captured.out
    assert "3. c" in captured.out


def testPrintFormattedReception(capsys):
    team = ["a", "b"]
    printFormatedReception("t", team, "p")
    captured = capsys.readouterr()
    assert "Witamy w projekcie p" in captured.out
    assert "Stworzonym przez zespół t" in captured.out
    assert "1. a" in captured.out
    assert "2. b" in captured.out
