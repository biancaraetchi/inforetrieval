## Report

### Precision and Recall
This metric describes the percentage of relevant results out of the entire returned list (precision) and the percentage of results returned out of the entire list of relevant documents (recall). The list of relevant documents is Google's top 7 results. For Google, since their results are the baseline, the precision and recall are both 1. For Bing, query 1, the precision is 0.15 with the highest recall out of all of them, 0.43. For Duckduckgo, the precision was the lowest out of all for query 1, with only a 1, while the recall was 0.29. For query 2, both Bing and Duckduckgo had a precision of 0.2 and a recall of 0.57. And for Yahoo, the precision was 0.2, while the recall was only 0.14 for both queries.

(Observation to mention in comparative evaluation: it is weird how the precision is so low, while the recall is relatively high; this is because we selected such a short set of 'relevant' docs.)

### Precision vs Recall
The precision vs recall metric helps understanding the trade-off that comes with choosing algorithms that increase either precision or recall, since they are inversely-correlated. In our scenario, Google has a straight line, since their results constitute our baseline. Duckduckgo and Bing have stricken a better balance of precision and recall for query 2, reaching about 0.3 precision up until 0.5 recall, while having 1.0 precision up until 0.2 recall for query 1, falling to 0.0 precision after these values. The value for precision fell the fastest for Yahoo, falling at 0.0 when recall is 0.2 for both queries.

### Single valued summaries
TThe single-valued summaries provide a simplified evaluation by focusing on specific cutoffs for precision (P@5 and P@10) and combining precision and recall into a single F1-score. These metrics help give a quick sense of how well each algorithm performs at critical ranks and overall.

For query 1:

Google: As the baseline, Google achieves perfect scores with F1 = 1.0, P@5 = 1.0, and P@10 = 1.0. Since Google is the set of relevant documents used as the ground truth, it naturally achieves the best results.
Bing: For Bing, P@5 is 0.2, meaning 20% of the top 5 results are relevant, and P@10 rises to 0.3, meaning Bing retrieves more relevant documents as more results are included. Its F1-score is 0.22, reflecting a modest balance between precision and recall.
DuckDuckGo: DuckDuckGo achieves P@5 = 0.4, showing stronger performance in the top 5 results, but P@10 drops to 0.2, indicating that relevant results diminish as more documents are considered. Its F1-score is 0.15, the lowest among the engines.
Yahoo: Yahoo performs similarly to DuckDuckGo with P@5 = 0.2 and P@10 = 0.2, resulting in a F1-score of 0.17.
For query 2:

Google again achieves perfect scores: F1 = 1.0, P@5 = 1.0, and P@10 = 1.0.
Bing and DuckDuckGo both have P@5 = 0.2, P@10 = 0.2, and F1 = 0.3, showing better balance in query 2 but still underperforming relative to Google.
Yahoo scores similarly in both queries, with P@5 = 0.2, P@10 = 0.2, and F1 = 0.17.

### Comparative evaluation
When comparing the performance of the three search engines across both queries, a few trends emerge:

Google consistently performs the best, achieving perfect precision and recall as expected since it serves as the baseline for relevant documents. It maintains high precision at ranks 5 and 10 and scores the highest F1, reflecting a perfect balance between precision and recall.

Bing and DuckDuckGo perform similarly, with slight variations across the two queries. Both engines retrieve more relevant results in query 2 than in query 1. Precision improves when looking at the top 10 results compared to the top 5, but their F1 scores remain relatively low, indicating they struggle to balance precision and recall.

Yahoo consistently performs the worst across both queries. It has the lowest precision and recall values and struggles to retrieve relevant results at any rank. Its P@5, P@10, and F1 scores reflect this, with performance lagging behind the other search engines.

Precision vs Recall Trade-offs: Bing and DuckDuckGo show an interesting trade-off in precision and recall, particularly for query 2. While their precision drops quickly, they maintain relatively high recall, suggesting that they retrieve a broad set of results but struggle to surface relevant ones at the top ranks. This implies a preference for breadth over accuracy, leading to lower precision but higher recall.

Overall, Google sets a high benchmark. While Bing and DuckDuckGo offer a reasonable trade-off between precision and recall, Yahoo lags significantly behind. The performance gap between search engines highlights the varying abilities of the algorithms to prioritize relevant documents in top results.