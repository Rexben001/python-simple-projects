combinations = []
amount = 12

def count_denoms(denoms, comb):
    global combinations
    for i in range(len(denoms)):
        comb_new = comb + [denoms[i]]
        if sum(comb_new) < amount:
            count_denoms(denoms[i:], comb_new)
        elif sum(comb_new) == amount:
            print(comb_new)
            combinations.append(comb_new)
    
if __name__ == "__main__":
    count_denoms([2, 5, 1], [])
    print("Number of combinations: " + str(len(combinations)))
