n_premise = 7
mark_sold_premise = n_premise - 7
ann_sold_premise = n_premise - 2

mark_sold_hypothesis = "more than 7 boxes less than n"
ann_sold_hypothesis = "2 boxes less than n"

# Check if Mark's sold quantity contradicts the premise
if mark_sold_hypothesis > mark_sold_premise:
    label = "contradiction"
elif ann_sold_hypothesis!= ann_sold_premise:
    # Check if Ann's sold quantity contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
