import csv
from operator import itemgetter
import time
from matplotlib import pyplot as plt


###get data###
user_input = ''
while user_input not in ('1', '2'):
    user_input = input(
        'Enter the path of the file you want to analyse (press 1 for data1 / 2 for data2): \n')

if user_input == '1':
    file_path = 'data/dataset1_Python+P7.csv'
elif user_input == '2':
    file_path = 'data/dataset2_Python+P7.csv'

lst_actions = []
with open(file_path, 'r') as file:
    csvreader = csv.DictReader(file)
    for rows in csvreader:
        lst_actions.append({'name': rows['name'],
                            'price': float(rows['price']), 'profit': float(rows['profit'])})


###Dynamic programation###
###optimized algorithm to check the best combination of actions###


def dynamic(liste, budget):
    budget *= 100
    # create a matrice with zeros corresponding to an objetct and a maximum budget
    matrice = [[0 for i in range(budget + 1)] for x in range(len(liste) + 1)]
    # go through each cell
    for i in range(1, len(liste)+1):
        for c in range(1, budget+1):
            # if acutal element cost is inferior to the maximum budget
            if liste[i-1]['price'] <= c:
                # compare the profit of this object plus the maximum profit for the remaining budget and the last maximum profit
                # keep the best profit
                matrice[i][c] = max(
                    liste[i-1]['profit'] + matrice[i-1][c-liste[i-1]['price']], matrice[i-1][c])
            # if actual element cost superior to budget, then keep the las best profit for this object
            else:
                matrice[i][c] = matrice[i-1][c]

    # find the list of elements with the sum

    b = budget
    n = len(liste)
    result = []

    while b >= 0 and n >= 0:
        e = liste[n-1]
        if matrice[n][b] == matrice[n-1][b-e['price']] + e['profit']:
            result.append(e)
            b -= 1

        n -= 1

    return matrice[-1][-1], result


# print(dynamic(lst_actions, 500))

actions = [{'name': 'action1', 'price': 20, 'profit': 5*20/100}, {'name': 'action2', 'price': 30, 'profit': 30*10/100}, {'name': 'action3', 'price': 50, 'profit': 50*15/100},
           {'name': 'action4', 'price': 70, 'profit': 70*20/100}, {'name': 'action5', 'price': 60,
                                                                   'profit': 60*17/100}, {'name': 'action6', 'price': 80, 'profit': 80*25 / 100},
           {'name': 'action7', 'price': 22, 'profit': 22*7/100}, {'name': 'action8', 'price': 26,
                                                                  'profit': 26*11/100}, {'name': 'action9', 'price': 48, 'profit': 48*13/100},
           {'name': 'action10', 'price': 34, 'profit': 34*27/100}, {'name': 'action11', 'price': 42,
                                                                    'profit': 42*17/100}, {'name': 'action12', 'price': 110, 'profit': 110*9/100},
           {'name': 'action13', 'price': 38, 'profit': 38*23/100}, {'name': 'action14', 'price': 14,
                                                                    'profit': 14*1 / 100}, {'name': 'action15', 'price': 18, 'profit': 18*3/100},
           {'name': 'action16', 'price': 8, 'profit': 8*8/100}, {'name': 'action17', 'price': 4,
                                                                 'profit': 4*12/100}, {'name': 'action18', 'price': 10, 'profit': 10*14 / 100},
           {'name': 'action19', 'price': 24, 'profit': 24*21 /
            100}, {'name': 'action20', 'price': 114, 'profit': 114*18/100}
           ]


###ALGORITHME OPTIMISE NAIF###


def optimized(liste, budget):
    # clean data
    liste = [x for x in liste if x['price'] != 0 and x['profit'] != 0]
    # calcultate for each action the ratio between the cost and the profit
    for action in liste:
        action['ratio'] = action['profit']/action['price']
    # sort by ratio's decreasing order
    sorted_lst = sorted(liste, key=itemgetter('ratio'), reverse=True)
    # make the combination with the highest ratios
    combo_list = []
    combo_profit = 0
    for action in sorted_lst:
        # if still money in the budget
        if budget - action['price'] >= 0:
            # add the profit and the name of the action to the combo
            combo_list.append(action['name'])
            combo_profit += action['profit']
            # decrement budget
            budget -= action['price']

    return (f'Purchase of {len(combo_list)} actions: \n {combo_list}, \n Total returns: {combo_profit}, \n Total cost: {500-budget}')


print(optimized(lst_actions, 500))

##ANALYSING BRUTEFORCE ALGORITHM COMPLEXITY##

#1 action execution delay#
# check time before execution
time1 = time.time()
optimized(actions[5: 10], 500)
# check time after execution
time2 = time.time()
delay1 = time2 - time1


#5 action execution delay#

time1 = time.time()
optimized(actions[10: 15], 500)
time2 = time.time()
delay2 = time2 - time1


#10 action execution delay#

time1 = time.time()
optimized(actions[15: 20], 500)
time2 = time.time()
delay3 = time2 - time1


###graph###
abscisse = [10, 15, 20]
ordonnées = [delay1, delay2, delay3]

plt.figure(figsize=(12, 8))
plt.title('Optimized \n Complexité: x')
plt.xlabel('nb of actions')
plt.ylabel('time of execution')
plt.plot(abscisse, ordonnées,
         lw='2', ls='--', c='red', label='complexity')
plt.legend()
# plt.show()
# plt.savefig('bruteforce_graphe.png')


# cours sur la complexité
# noter à côté des courbes la complexité pour chaque alog (expo, loga, ...)
# checker ce que veux oc pour continuer les tâches
# comparer result avec les diffts algo
###
