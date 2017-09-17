import random
from constants import(
    CIVILIZATIONS,
    EXCLUSIONS,
)


def print_available_civs():
    print("{:<8} {:<24} {:<15}".format('Number','Leader','Country'))
    for i in range(len(CIVILIZATIONS.keys())):
        civ = CIVILIZATIONS[i];
        if civ.available:
            print("{:<8} {:<24} {:<15}".format(civ.civid, civ.leader, civ.country))
    return


def create_users(num_players):
    users = list()
    print("Enter player names, press enter after each player")
    for i in range(num_players):
        player = input()
        users.append(player)
    return users


def _remove_exlusions(civ_id):
    CIVILIZATIONS[civ_id].available = False
    for exclusion in EXCLUSIONS[civ_id]:
        CIVILIZATIONS[exclusion].available = False
    return

def _get_pick():
    correct = None
    while correct != 'y':
        pick = None
        while type(pick) is not int:
            try:
                pick = int(input("Chose a civ (enter number): "))
            except ValueError:
                print("Please enter the number for the the civilization")

        civ = CIVILIZATIONS[pick]
        if civ.available:
            print("You have chosen " + civ.country + ", led by " + civ.leader + ". Is this correct?(Y/N)")
            correct = input().lower()
            if correct != 'y':
                print('Chose again')
        else:
            print("Not available, try again")
            correct = None
    return pick

def draft_civ(users):
    for user in users:
        print(user + ", it is your turn to pick")
        print("Available civilizations below")
        print_available_civs()
        pick = _get_pick()
        _remove_exlusions(pick)
        CIVILIZATIONS[pick].player = user


def print_results():
    print("{:<15} {:<24} {:<15}".format('Player','Leader','Country'))
    for i in range(len(CIVILIZATIONS.keys())):
        civ = CIVILIZATIONS[i];
        if civ.player is not None:
            print("{:<15} {:<24} {:<15}".format(civ.player, civ.leader, civ.country))
    return

if __name__ == "__main__":
    num_players = 8
    users = create_users(num_players)
    random.shuffle(users)
    print(users)
    draft_civ(users)
    print_results()
