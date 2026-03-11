from typing import List


def getCountTeam(team: List[str]) -> int:
    return len(team)

def printFormatedReception(nameTeam: str, team: List[str], projectName: str):
    print(f"Witamy w projekcie {projectName}")
    print(f"Stworzonym przez zespół {nameTeam}")
    printTeamMembers(team)


def printTeamMembers(team: List[str]) -> str:
    for i in range(len(team)):
        print(f"{i+1}. {team[i]}")


projectName = "XYZ"
nameTeam = "DreamTeam"
list = ["Kamil Kajta","Bartosz Jaros"]

# print(len(list))
# print(list)

print(getCountTeam(list))
printFormatedReception(nameTeam, list, projectName)
print("Poprawnie uruchomiono projekt.")

