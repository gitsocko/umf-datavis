filename = './lego_setsHB.csv'
counter=0
price = {}
difficulty = {}
with open(filename, 'r') as fl:
    next(fl)
    for line in fl:
        #print(line)
        tokens = line.split(',')
        #for el in tokens:
        #    print(el, end='--')
        #print()
        price[tokens[4]] = tokens[0]
        difficulty[tokens[4]] = tokens[5]
        counter+=1
        if counter==10:
          break
for key, value in price.items():
    print(key, value, difficulty[key])