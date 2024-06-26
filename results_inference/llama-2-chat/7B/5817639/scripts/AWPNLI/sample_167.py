girls_premise = 28.0
boys_premise = 35.0
total_children_premise = girls_premise + boys_premise
hypothesis_children = 61.0

# compare the number of children in the hypothesis with the total number of children in the premise
if hypothesis_children == total_children_premise:
    # if the number of children in the hypothesis matches the total number of children in the premise, we can infer entailment
    label = "entailment"
elif hypothesis_children > total_children_premise:
    # if the number of children in the hypothesis is greater than the total number of children in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
