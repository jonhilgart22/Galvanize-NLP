----
t-Distributed Stochastic Neighbor Embedding (t-SNE) 
----

http://distill.pub/2016/misread-tsne/?imm_mid=0e9d77&cmp=em-data-na-na-newsltr_20161026

<img src="http://www.trivial.io/content/images/2015/12/tsne-8.png" style="width: 400px;"/>

A tool to visualize high-dimensional data. 

Embedding high-dimensional data into a space of two or three dimensions, which can then be visualized in a scatter plot. Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that similar objects are modeled by nearby points and dissimilar objects are modeled by distant points.

It converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.

[demo 1](https://github.com/oreillymedia/t-SNE-tutorial)  
[demo 2](http://cs.stanford.edu/people/karpathy/tsnejs/)

The t-SNE algorithms comprises two main stages. 

1. t-SNE constructs a probability distribution over pairs of high-dimensional objects in such a way that similar objects have a high probability of being picked, whilst dissimilar points have an infinitesimal probability of being picked.

2. t-SNE defines a similar probability distribution over the points in the low-dimensional map, and it minimizes the Kullback–Leibler divergence between the two distributions with respect to the locations of the points in the map. Note that whilst the original algorithm uses the Euclidean distance between objects as the base of its similarity metric, this should be changed as appropriate.

[Source](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding)

[t-sne code](https://lvdmaaten.github.io/tsne/) 

[Implementation in python](http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

http://jkunst.com/flexdashboard-highcharter-examples/pokemon/

https://www.oreilly.com/learning/an-illustrated-introduction-to-the-t-sne-algorithm