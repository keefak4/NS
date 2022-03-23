def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0
    for i in range[len(a)]:
        output += (a[i] * b[i])
    return output
weight = [0.1,0.2,0]
def neural_network(input,weight):
    pred = w_sum(input,weight)
    return pred

toes = [8.5,9.2,8.0,8.2]
winandlos = [0.65,0.24,1.0,0.75]
nfanc = [1.2,4.3,2.1,1.4]
input = [toes[0],winandlos[0],nfanc[0]]
pred = neural_network(input,weight)
print(pred)