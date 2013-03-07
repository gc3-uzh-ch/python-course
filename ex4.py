def load_data(filename):
    file = open(filename, 'r')
    L = []
    for line in file:
        value = int(line)
        L.append(value)
    return L

def load_csv(filename):
    stream = open(filename, 'r')
    D = { }
    for line in stream:
        currency, rate = line.split(',')
        D[currency] = float(rate)
    return D
