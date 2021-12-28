---
title: "A Geometric Encoding for Neural Network Evolution"
collection: publications
permalink: /publication/2021-06-01-a-geometric-encoding-for-neural-network-evolution
excerpt: 'A major limitation to the optimization of artificial neural networks (ANN) with evolutionary methods lies in the high dimensionality of the search space, the number of weights growing quadratically with the size of the network. This leads to expensive training costs, especially in evolution strategies which rely on matrices whose sizes grow with the number of genes. We introduce a geometric encoding for neural network evolution (GENE) as a representation of ANN parameters in a smaller space that scales linearly with the number of neurons, allowing for efficient parameter search. Each neuron of the network is encoded as a point in a latent space and the weight of a connection between two neurons is computed as the distance between them. The coordinates of all neurons are then optimized with evolution strategies in a reduced search space while not limiting network fitness and possibly improving search.'
date: 2021-06-01
venue: 'GECCO 2021 (Genetic and Evolutionary Computation Conference)'
authors: 'Paul Templier, Emmanuel Rachelson, Dennis G. Wilson'
paperurl: 'https://dl.acm.org/doi/10.1145/3449639.3459361'
codeurl: 'https://github.com/TemplierPaul/GENE.jl'
---
A major limitation to the optimization of artificial neural networks (ANN) with evolutionary methods lies in the high dimensionality of the search space, the number of weights growing quadratically with the size of the network. This leads to expensive training costs, especially in evolution strategies which rely on matrices whose sizes grow with the number of genes. We introduce a geometric encoding for neural network evolution (GENE) as a representation of ANN parameters in a smaller space that scales linearly with the number of neurons, allowing for efficient parameter search. Each neuron of the network is encoded as a point in a latent space and the weight of a connection between two neurons is computed as the distance between them. The coordinates of all neurons are then optimized with evolution strategies in a reduced search space while not limiting network fitness and possibly improving search.

[Download paper here](https://dl.acm.org/doi/10.1145/3449639.3459361)
