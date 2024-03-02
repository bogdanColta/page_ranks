# Destabilize the Page Ranks

 The objective of this project was to study whether these three ranking algorithms are stable or not:
 - In-Degree
 - PageRank
 - HITS

 An algorithm is called stable if and only if small changes in the underlying graph of links will cause only small changes in the page ranks.

 As part of our research, we had to answer the following questions:
 - What is the largest change in the rank vector, for each algorithm, that you can
 cause by making a change of size k in any graph of n nodes?
 - What are the most vulnerable graphs you found, for each ranking algorithm, and
 what type of link change mattered most?
 - Which ranking algorithm for web pages is most stable? How about least stable?

### Conclusions

 - The In-Degree algorithm seems to be the most stable
 - The HITS algorithm seems to be the least stable
 - The PageRank algorithm produces results in-between HITS and In-Degree
 - Hierarchical and grid graphs appear to be the most vulnerable

 You can generate the graphs that support these conclusions in the provided Python notebooks.