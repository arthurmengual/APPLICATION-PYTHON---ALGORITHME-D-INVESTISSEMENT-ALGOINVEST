import csv
import json
import operator

data = {}
file_path = 'data/dataset1_Python+P7.csv'

with open(file_path, 'r') as file:
    csvreader = csv.DictReader(file)
    for rows in csvreader:
        data[rows['name']] = {'price': rows['price'], 'profit': rows['profit']}


for elt in data:
    res = f"{elt} : prix: {data[elt]['price']} // profit: {data[elt]['profit']}"

##PSEUDO CODE##

# pour chaque combinaison possible d'action:

# si le cout inferieur à 200euros:
    # pour chaque action de la combinaison
    # incrémenter la liste des actions et la somme des profits
    # appender la liste des actions et somme des profits au resultat
# sinon
    # break
# trier la liste résultat
# retourner la combinaison avec le meilleu profi()


#####ALGORITHME GLOUTON#######
result = []
for elt in data:
    if data[elt]['price'] != '0':
        ratio = float(data[elt]['profit'])//float(data[elt]['price'])

    result.append({'name': elt, 'ratio': ratio, 'price': data[elt]['price']})

result = sorted(result, key=operator.itemgetter('ratio'), reverse=True)

total = 0
solution = []
for action in result:
    if total <= 200:
        total += float(action['price'])
        solution.append(action)
    else:
        break

del solution[-1]


###ALGORITHME####


# n => nombre d'objets = 1
# cout
# gain
# pour chaque action des actions
# incrementer cout et gain


# combinaisons possible avec un element
# combinaisons possibles avec 2 elt
# ....avec n element => derniere combinaison = toute la liste

# for i in range(20) => i nombre d'actions dans une combinaison
# for j in range(i, len(actions)


# def test_2_actions():
# init res
# for i in range(0, 20):
# for j in range(i+1, 20):
# val1 = actions[i]
# val2 = actions[j]
# res = val1 + val2
# si res < total_portefeuille
# si res > res davant => on remplace res davant
# return res


# def 3_actions():
# init res
# for i in range(0, 20):
# for j in range(i+1, 20):
# for k in range(j+1, 20):
# val1 = actions[i]
# val2 = actions[j]
# val3 = actions[k]
# res = val1 + val2 + val3
# si res < total_portefeuille
# si res > res d'avant => on remplace res davant
# return res
