import random
from enum import IntEnum

class Action(IntEnum):
    Pedra = 0
    Papel = 1
    Tesoura = 2
def get_user_selection():
            choices = [f"{action.name}[{action.value}]" for action in Action]
            choices_str = ", ".join(choices)
            selection = int(input(f"Faça uma escolha ({choices_str}): "))
            action = Action(selection)
            return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    victories = {
        Action.Pedra: [Action.Tesoura],  # Pedra beats Tesoura
        Action.Papel: [Action.Pedra],  # Papel beats Pedra
        Action.Tesoura: [Action.Papel]  # Tesoura beats Papel
    }

    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Ambos os players escolheram {user_action.name}. Isso é uma Empate!")
    elif computer_action in defeats:
        print(f"{user_action.name} vence {computer_action.name}! Você venceu!")
    else:
        print(f"{computer_action.name} vence {user_action.name}! Você perdeu.")

while True:
        try:
             user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action)-1}]"
            print(f"Seleção invalida. Escolhe um valor no range {range_str}")
            continue
        
        computer_action = get_computer_selection()
        print(f"\nVocê escolheu {user_action.name}, o computador escolheu {computer_action.name}.")
        determine_winner(user_action, computer_action)
        play_again = input("Quer jogar novamente? (y/n): ")
        if play_again.lower() != "y":
            break
        
        