premise = "More than a decade ago, Carl Lewis stood on the threshold of what was to become the greatest athletics career in history. He had just broken two of the legendary Jesse Owens' college records, but never believed he would become a corporate icon, the focus of hundreds of millions of dollars in advertising. His sport was still nominally amateur. Eighteen Olympic and World Championship gold medals and 21 world records later, Lewis has become the richest man in the history of track and field -- a multi-millionaire."
hypothesis = "Carl Lewis won eighteen gold medals and set 21 world records."

# extract the numerical entities from the premise
gold_medals_premise = 18
world_records_premise = 21

# extract the numerical entities from the hypothesis
gold_medals_hypothesis = 18
world_records_hypothesis = 21

# check if the hypothesis values and estimates contradict the premise values
if gold_medals_hypothesis!= gold_medals_premise or world_records_hypothesis!= world_records_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
