#from array import array


best_playlist = []

max_sum = 0


def my_permutation(vector,playlist,N,k,soma):

    global max_sum
    global best_playlist

    if k >= len(playlist) or soma >= N:
        #print(vector)
        #vector.clear()
        #print(soma)
        if(soma > max_sum):
            max_sum = soma
            #print(max_sum)
            if max_sum <= N :
                new_vec = vector.copy()
                best_playlist = [new_vec,max_sum]

        vector.clear()
    else:

        soma += playlist[k]
        if soma <= N:
            if len(vector) <= 20:
                vector.append(playlist[k])
                my_permutation(vector,playlist,N,k+1,soma)
        else:
            soma -= playlist[k]
            my_permutation(vector,playlist,N,k+1,soma)

def itPermutation(vector, playlist, N, index):

    k = index + 1
    while k <= len(playlist):

        vector.append(playlist[index])
        my_permutation(vector,playlist,N,k,playlist[index])
        k += 1


def permutation(vector,playlist,N):

    #print("Permutando")

    i = 0
    for item in playlist:
        itPermutation(vector,playlist,N,i)
        vector.clear()
        i += 1

    vector.clear()

def main():

    global best_playlist
    global max_sum
    #bool_vec = [False]*max(playlist)

    while True:

        N,num_faix = list(map(int,input().split()))
        if N == 0:
            break
        playlist = list(map(int,input().split()))

        vec =[]
        permutation(vec,playlist,N)

        for i in range(0,len(best_playlist[0])):
            print("{0} ".format(best_playlist[0][i]),end = "")
        print("sum:{0}".format(str(best_playlist[1])))
        #print(playlist)

        #print(best_playlist)
        max_sum = -1
        best_playlist.clear()

main()

