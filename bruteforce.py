
actions = {'action1': {'cout': 20, 'profit': 5}, 'action2': {'cout': 30, 'profit': 10}, 'action3': {'cout': 50, 'profit': 15}, 'action4': {'cout': 70, 'profit': 20},
           'action5': {'cout': 60, 'profit': 17}, 'action6': {'cout': 80, 'profit': 25}, 'action7': {'cout': 22, 'profit': 7}, 'action8': {'cout': 26, 'profit': 11},
           'action9': {'cout': 48, 'profit': 13}, 'action10': {'cout': 34, 'profit': 27}, 'action11': {'cout': 42, 'profit': 17}, 'action12': {'cout': 110, 'profit': 9},
           'action13': {'cout': 38, 'profit': 23}, 'action14': {'cout': 14, 'profit': 1}, 'action15': {'cout': 18, 'profit': 3}, 'action16': {'cout': 8, 'profit': 8},
           'action17': {'cout': 4, 'profit': 12}, 'action18': {'cout': 10, 'profit': 14}, 'action19': {'cout': 24, 'profit': 21}, 'action20': {'cout': 114, 'profit': 18}
           }


def check_best_combo(liste):
    binaries = [format(i, '020b') for i in range(2**len(liste))]
    for binary in binaries:
        actions_combo = []
        for cell in binary:
            if cell == '1':
                index = binary.index(cell)
                actions_combo.append(actions[f'action{index+1}'])


binaries = [format(i, '020b') for i in range(4)]

liste_of_combos = []
for binary in binaries:
    actions_combos = []
    for cell in binary:
        if cell == '1':
            index = binary.index(cell)
            action = f'action n° {index+1}'
            cout = f"cout: {actions[f'action{index+1}']['cout']}"
            profit = f"profit: {actions[f'action{index+1}']['cout'] * actions[f'action{index+1}']['profit'] //100}"
            actions_combos.append((action, cout, profit))
    liste_of_combos.append(actions_combos)

print(liste_of_combos)
