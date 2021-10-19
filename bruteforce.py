import operator


actions = {'action1': {'cout': 20, 'profit': 5}, 'action2': {'cout': 30, 'profit': 10}, 'action3': {'cout': 50, 'profit': 15}, 'action4': {'cout': 70, 'profit': 20},
           'action5': {'cout': 60, 'profit': 17}, 'action6': {'cout': 80, 'profit': 25}, 'action7': {'cout': 22, 'profit': 7}, 'action8': {'cout': 26, 'profit': 11},
           'action9': {'cout': 48, 'profit': 13}, 'action10': {'cout': 34, 'profit': 27}, 'action11': {'cout': 42, 'profit': 17}, 'action12': {'cout': 110, 'profit': 9},
           'action13': {'cout': 38, 'profit': 23}, 'action14': {'cout': 14, 'profit': 1}, 'action15': {'cout': 18, 'profit': 3}, 'action16': {'cout': 8, 'profit': 8},
           'action17': {'cout': 4, 'profit': 12}, 'action18': {'cout': 10, 'profit': 14}, 'action19': {'cout': 24, 'profit': 21}, 'action20': {'cout': 114, 'profit': 18}
           }


def check_best_combo(liste):
    binaries = [format(i, '020b') for i in range(2**len(liste))]
    combos = {}
    # iterate through every combination
    k = 1
    for binary in binaries:
        combo = {'actions': '', 'cout': 0, 'profit': 0}
        # iterate through each cell and if equals to one, take in account the corresponding action
        for index, cell in enumerate(binary):
            if cell == '1':
                action = f'action{index+1}'
                cout = actions[f'action{index+1}']['cout']
                profit = actions[f'action{index+1}']['cout'] * \
                    actions[f'action{index+1}']['profit'] // 100
                # increment combo
                combo['actions'] += f'{action} '
                combo['cout'] += cout
                combo['profit'] += profit
        # append the combo to the list of combos
        if combo:
            combos[f'combo{k}'] = combo
            k += 1

    # trie final des combos
    i = 0
    result = ''
    for key, value in combos.items():
        if value['cout'] < 500:
            if i < int(value['profit']):
                result = key, value
                i = value['profit']

    return result


print(check_best_combo(actions))
