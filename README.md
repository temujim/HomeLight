# HomeLight

 ![HomeLight KW TagCloud](https://github.com/temujim/HomeLight/blob/master/KWTagCloud.png?raw=true)

## Relevant Links:
* [Python Script Used](https://github.com/temujim/HomeLight/blob/master/KWGapAnalysis.py)
*  [Final Top 100 Blog KWs](https://github.com/temujim/HomeLight/blob/master/Final/20220915_HomeLIght_Final-BlogContentKWGapV1.0.xlsx)

## Data Sources:
* Used SpyFu's organic competitive intelligence data to analyze relevant competition based on KW overlaps and traffic size.
 ![HomeLight KW TagCloud](https://i.imgur.com/ovS317l.png)
* Used SEMRush's domain comparison data to have some rough traffic estimation.
 ![HomeLight KW TagCloud](https://i.imgur.com/MjFPwo0.png)
* Used SEMRush's KW gap data to fetch relevant keywords which are segmented by: Missing, Weak, Untapped, Unique, Strong

## Scope and Size:
* About 20 sites are analyzed including Homelight
* Ran over 120k keywords overall.
* About 30 CSV's are being exported with a total of close to 50MB in size.
* Python Pandas is used to analyze the huge dataset, to clean, merge the data together and further do calculations.
* Since the keywords are meant for blog content, only KW's relating to a question is being included.

## KW Selection:
* Sort by KW value (highest search volume and CPC)
* Retain keywords which has 2 or more ranking competitors (measure of relevance)
* Select keywords with Competitor Quantile rankings of 10 or better (measure of relevance + value the competitor sites are currently getting)
* KWs which wherein Quantile Rankings has better current Homelight Ranking
* KW's wherein HomeLight is already ranking but still has some oppurtunity for improvement (low hanging fruits)
* Included KW's with quantile ranking of 10 or lower, but has 4 or more competitors

## Other Oppurtunities:
* Push the 120k analyze KW's and rankings to analyze overall KW market gaps
* Calculate metrics, KW difficulty, oppurtunities and categorize KWs
* Push data to a BI tool like Google data studio to easily visualize huge data inteactively


