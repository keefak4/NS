def ele_mul(number,vector):
    output = [0,0,0]
    assert(len(output) == len(vector))
    for i in range (len(vector)):
        output[i] = number * vector[i]
        return output
    weights = [0.3,0.2,0.9]
    def nerual_network(input,weights):
        pred = ele_mul(input,weights)
        return pred
    winandlos = [0.65,0.8,0.8,0.9]
    input = winandlos[0]
    pred = nerual_network(input,weights)
    print(pred)
