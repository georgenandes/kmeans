import os
import math
import random
import numpy as np

# clt=clusters

def _means(dados, qtdClusters, lista_centroid):

    centroides = []
    centroides = random(dados, centroides, qtdClusters)
    ant_centroides = [[] for i in range(qtdClusters)]
    repeticoes = 0

    while not (converge(centroides, ant_centroides, repeticoes)):
        repeticoes += 1

        clt = [[] for i in range(qtdClusters)]

        clt = dist(dados, centroides, clt)

        indice = 0
        for cluster in clt:
            ant_centroides[indice] = centroides[indice]
            centroides[indice] = np.mean(cluster, axis=0)
            indice += 1

        print("med_centroides: " + str(centroides))


    return

def converge(centroides, ant_centroides, repeticoes):
    maximorepeticoes = 600
    if repeticoes > maximorepeticoes:
        return True
    return ant_centroides == centroides

def dist(dados, centroides, clt):

    for instance in dados:

        indice = min([(i[0], np.linalg.norm(instance-centroides[i[0]])) \
                            for i in enumerate(centroides)], key=lambda t:t[1])[0]
        
    for cluster in clt:
        if not cluster:
            cluster.append(dados[np.random.randint(0, len(dados),
            size=1)])

    return clt


def random(dados, centroides, qtdClusters):
    
    for cluster in range(0, qtdClusters):
        centroides.append(dados[np.random.randint(0, len(dados),
        size=1)])
    
    return centroides


