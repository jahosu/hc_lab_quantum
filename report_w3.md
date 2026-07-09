# Week 3: Mini Project
This week we build on the Week 2 idea (overlap estimation via the swap test) to implement a tiny similarity
search: given a query vector and a small database of vectors, we compute similarity scores and rank
the database. Furthermore we implement our own hybrid quantum k-means and explore design choices regarding centroid initialization, 
the metric used for cluster assignment and handling the non-determinism that comes with quantum-based metrics.

## Similarity Search on a Tiny Database
How reliably (as a function of shots) can a swap-test similarity score identify the nearest vector in
a tiny 2D database? To answer this question, we conducted a similarity search over a set of vectors and recorded the results for different shots,
as shown by the table below. 

| shots | label |  v0 |   v1 | overlap_sq |
| ----: | :---- | --: | ---: | ---------: |
|   200 | A     | 1.0 |  0.0 |     1.0000 |
|   200 | B     | 0.0 |  1.0 |     0.0100 |
|   200 | C     | 1.0 |  1.0 |     0.4400 |
|   200 | D     | 1.0 | -1.0 |     0.5100 |
|   500 | A     | 1.0 |  0.0 |     1.0000 |
|   500 | B     | 0.0 |  1.0 |     0.0000 |
|   500 | C     | 1.0 |  1.0 |     0.4720 |
|   500 | D     | 1.0 | -1.0 |     0.4960 |
|  1000 | A     | 1.0 |  0.0 |     1.0000 |
|  1000 | B     | 0.0 |  1.0 |     0.0160 |
|  1000 | C     | 1.0 |  1.0 |     0.4880 |
|  1000 | D     | 1.0 | -1.0 |     0.4600 |
|  2000 | A     | 1.0 |  0.0 |     1.0000 |
|  2000 | B     | 0.0 |  1.0 |     0.0000 |
|  2000 | C     | 1.0 |  1.0 |     0.4890 |
|  2000 | D     | 1.0 | -1.0 |     0.5080 |
|  4000 | A     | 1.0 |  0.0 |     1.0000 |
|  4000 | B     | 0.0 |  1.0 |     0.0260 |
|  4000 | C     | 1.0 |  1.0 |     0.4895 |
|  4000 | D     | 1.0 | -1.0 |     0.5005 |

The following plot shows the final similarities:

<img src="results/week3/similarity_ranking.png" alt="noise overlap depth" width="400">
It was observed that the same labels are assigns for all shot counts, but the scores slightly diverge
for the non-identical vectors. 

## Hybrid Quantum K-means
### Design Proposal
Centroids are initialized randomly to avoid additional overhead. We chose  1 - squared overlap as a distance metric. It is zero for identical states and approaches one for orthogonal states, making it an appropriate measure of dissimilarity for clustering.
Centroids are updated by computing the average of the points in their respective cluster. For empty clusters, we just keep the previous centroid.
Convergence is decided by checking if any of the cluster assignments has changed after each iteration. If no assignment changes, centroids stay the same as well and k-means has converged.

### Results and Discussion
For our experiment we chose 1000 shots, as it is sufficiently stable based on our similarity search results from above. Here, the search converged after two iteration, varying with the initial centroid assignments. Using a quantum-based distance introduces shot-noise, leading to non-deterministic results in contrast to classical k-means. We have shown, however, that the assignments sufficiently stabilize when more (In our setting ~1000) shots are used. 
<img src="results/week3/quantum_kmeans_clusters.png" alt="noise overlap depth" width="400">
<img src="results/week3/quantum_kmeans_convergence.png" alt="noise overlap depth" width="400">
