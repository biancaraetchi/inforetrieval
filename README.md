## Report

### Precision and Recall
This metric describes the percentage of relevant results out of the entire returned list (precision) and the percentage of results returned out of the entire list of relevant documents (recall). The list of relevant documents is Google's top 7 results. For Google, since their results are the baseline, the precision and recall are both 1. For Bing, query 1, the precision is 0.15 with the highest recall out of all of them, 0.43. For Duckduckgo, the precision was the lowest out of all for query 1, with only a 1, while the recall was 0.29. For query 2, both Bing and Duckduckgo had a precision of 0.2 and a recall of 0.57. And for Yahoo, the precision was 0.2, while the recall was only 0.14 for both queries.

(Observation to mention in comparative evaluation: it is weird how the precision is so low, while the recall is relatively high; this is because we selected such a short set of 'relevant' docs.)

### Precision vs Recall
The precision vs recall metric helps understanding the trade-off that comes with choosing algorithms that increase either precision or recall, since they are inversely-correlated. In our scenario, Google has a straight line, since their results constitute our baseline. Duckduckgo and Bing have stricken a better balance of precision and recall for query 2, reaching about 0.3 precision up until 0.5 recall, while having 1.0 precision up until 0.2 recall for query 1, falling to 0.0 precision after these values. The value for precision fell the fastest for Yahoo, falling at 0.0 when recall is 0.2 for both queries.

### Single valued summaries
The single-valued summaries provide a simplified evaluation by focusing on specific cutoffs for precision (P@5 and P@10) and combining precision and recall into a single F1-score. These metrics help give a quick sense of how well each algorithm performs at critical ranks and overall.

For query 1:

Google: As the baseline, Google achieves perfect scores with F1 = 1.0, P@5 = 1.0, and P@10 = 0.7. Since Google is the set of relevant documents used as the ground truth, it naturally achieves the best results.
Bing: For Bing, P@5 is 0.2, meaning 20% of the top 5 results are relevant, but P@10 rises to 0.3, which means Bing retrieves more relevant documents as you increase the results set. Its F1-score is 0.22, which shows a modest balance between precision and recall but is far from optimal.
DuckDuckGo: This engine’s P@5 is better at 0.4, suggesting stronger performance in the top 5, but P@10 falls to 0.2, showing that relevant results drop off quickly after the top 5. The F1-score is 0.15, which is the lowest among the search engines.
Yahoo: For Yahoo, P@5 and P@10 are the lowest, at 0.2 and 0.1, respectively. This suggests that Yahoo retrieves very few relevant results, and its F1-score of 0.17 reflects its overall poor performance.
For query 2:

Google again achieves the highest scores across the board, with F1 = 1.0, P@5 = 1.0, and P@10 = 0.7.
Bing and DuckDuckGo perform identically on query 2, with P@5 = 0.2, P@10 = 0.2, and F1 = 0.3. Both engines show better balance between precision and recall on this query but still fall behind Google.
Yahoo performs the weakest again with P@5 = 0.2, P@10 = 0.1, and F1 = 0.17, showing that Yahoo is unable to retrieve many relevant results compared to the others.

### Comparative evaluation
When comparing the performance of the three search engines across both queries, a few trends emerge:

Google consistently performs the best, achieving perfect precision and recall as expected since it serves as the baseline for relevant documents. It not only maintains high precision at ranks 5 and 10 but also scores highest on F1, reflecting a perfect balance between precision and recall.

Bing and DuckDuckGo perform similarly, with slight variations across the two queries. Both engines retrieve more relevant results in query 2 than in query 1, and their precision improves when looking at the top 10 results compared to the top 5. However, their F1 scores remain relatively low, indicating that they struggle to balance precision and recall.

Yahoo consistently performs the worst across both queries. Its precision and recall values are the lowest, and it struggles to retrieve relevant results at any rank. This is reflected in its very low P@5, P@10, and F1 scores. The steep drop-off in precision after the first few results shows that Yahoo has difficulty retrieving relevant documents as effectively as the other search engines.

Precision vs Recall Trade-offs: Bing and DuckDuckGo show an interesting trade-off in precision and recall, especially for query 2. While their precision scores drop quickly, they maintain relatively high recall, indicating that they retrieve a broad set of results but struggle to surface relevant ones near the top. This suggests that these engines might favor breadth over accuracy, resulting in a lower precision but a more comprehensive recall.

Overall, Google sets a high benchmark, and while Bing and DuckDuckGo offer a reasonable trade-off between precision and recall, Yahoo lags significantly behind. The performance gaps across the search engines can be attributed to their algorithms' ability (or inability) to prioritize relevant documents in the top ranks.
