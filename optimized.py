import csv


###get data###

file_path_ = input('Enter the path of the file you want to analyse: ')

data = {}
file_path = 'data/dataset1_Python+P7.csv'

with open(file_path, 'r') as file:
    csvreader = csv.DictReader(file)
    for rows in csvreader:
        data[rows['name']] = {'price': rows['price'], 'profit': rows['profit']}

lst_actions = [(elt, float(data[elt]['price']), float(
    data[elt]['profit'])) for elt in data]


###optimized algorithm to check the best combination of actions###


def main(liste, budget):
    # create a matrice with zeros corresponding to an objetct and a maximum budget
    matrice = [[0 for i in range(budget + 1)] for x in range(len(liste) + 1)]
    # go through each cell
    for i in range(1, len(liste)+1):
        for c in range(1, budget+1):
            # if acutal element cost is inferior to the maximum budget
            if liste[i-1][1] <= c:
                # compare the profit of this object plus the maximum profit for the remaining budget and the last maximum profit
                # keep the best profit
                matrice[i][c] = max(
                    liste[i-1][2] + matrice[i-1][c-liste[i-1][1]], matrice[i-1][c])
            # if actual element cost superior to budget, then keep the las best profit for this object
            else:
                matrice[i][c] = matrice[i-1][c]

    # find the list of elements with the sum

    b = budget
    n = len(liste)
    result = []

    while b >= 0 and n >= 0:
        e = liste[n-1]
        if matrice[n][b] == matrice[n-1][b-e[1]] + e[2]:
            result.append(e)
            b -= 1

        n -= 1

    return matrice[-1][-1], result


print(main(lst_actions, 500))


# test optimized with 20 actions
liste_actions = [('action1', 20, 1), ('action2', 30, 3), ('action3',  50, 7), ('action4', 70, 14), ('action5', 60, 10),
                 ('action6', 80, 20), ('action7', 22,  1), ('action8',
                                                            26, 2), ('action9', 48, 6), ('action10', 34, 9),
                 ('action11', 42, 7), ('action12', 110, 9), ('action13',
                                                             38, 8), ('action14', 14, 0), ('action15', 18, 0),
                 ('action16', 8, 0), ('action17', 4, 0), ('action18', 10, 1), ('action19', 24, 5), ('action20', 114, 20)]


if __name__ == "__main__":
    main()
