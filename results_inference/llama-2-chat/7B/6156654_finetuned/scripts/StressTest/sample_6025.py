# the premise and hypothesis are talking about the same scenario
if_dana_gives_parents_percentage_premise = 6
if_dana_gives_parents_percentage_hypothesis = 4

# the hypothesis refers to the percentage of money given back to the parents each month, which is also mentioned in the premise
if if_dana_gives_parents_percentage_premise!= if_dana_gives_parents_percentage_hypothesis:
    # if the percentage in the hypothesis contradicts the percentage in the premise, we can infer entailment
    label = "entailment"
else:
    # if the percentage in the hypothesis matches the percentage in the premise, we can infer neutral
    label = "neutral"

print(label)
