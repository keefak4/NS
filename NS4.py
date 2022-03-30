def w_sum(a,b):
    assert (len(a)==len(b))
    output = 0
    return output
def vect_mat_mul(vect,matrix):
    assert(len(vector)==len(matrix))
    output = [0,0,0]
    for i in range (len(vect)):
    output[i] = w_sum(vect,matrix[i])
    return output
    toes = [8.5,8.7,8.4,8.2]
    winandlos = [0.5,0.7,0.4,0.2]
    nfanc = [1.5,1.7,1.4,1.2]
    input = [toes[0],winandlos[0],nfanc[0]]
    pred = neural_network(input,weights)
    def neural_network(input,weights):
        pred = vect_mat_mul(input,weights)
        return pred


