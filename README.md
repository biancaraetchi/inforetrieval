## Report

### Precision and Recall
This metric describes the percentage of relevant results out of the entire returned list (precision) and the percentage of results returned out of the entire list of relevant documents (recall). The list of relevant documents is Google's top 7 results. For Google, since their results are the baseline, the precision and recall are both 1. For Bing, query 1, the precision is 0.15 with the highest recall out of all of them, 0.43. For Duckduckgo, the precision was the lowest out of all for query 1, with only a 1, while the recall was 0.29. For query 2, both Bing and Duckduckgo had a precision of 0.2 and a recall of 0.57. And for Yahoo, the precision was 0.2, while the recall was only 0.14 for both queries.

(Observation to mention in comparative evaluation: it is weird how the precision is so low, while the recall is relatively high; this is because we selected such a short set of 'relevant' docs.)

### Precision vs Recall
The precision vs recall metric helps understanding the trade-off that comes with choosing algorithms that increase either precision or recall, since they are inversely-correlated. In our scenario, Google has a straight line, since their results constitute our baseline. Duckduckgo and Bing have stricken a better balance of precision and recall for query 2, reaching about 0.3 precision up until 0.5 recall, while having 1.0 precision up until 0.2 recall for query 1, falling to 0.0 precision after these values. The value for precision fell the fastest for Yahoo, falling at 0.0 when recall is 0.2 for both queries.

### Single valued summaries

### Comparative evaluation
