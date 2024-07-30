filename = './data/lego_setsHB.csv'
counter=0
price = {}
difficulty = {}
with open(filename, 'r') as fl:
    next(fl)
    for line in fl:
        tokens = line.split(',')
        price[tokens[4]] = tokens[0]
        difficulty[tokens[4]] = tokens[5]
        counter+=1
        if counter==1000:
          break
for key, value in price.items():
    print(key, value, difficulty[key])