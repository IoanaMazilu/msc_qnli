women_premise = 17
children_premise = 6

# the hypothesis mentions the same numbers of women and children as the premise
if women_hypothesis == women_premise and children_hypothesis == children_premise:
    # if the values in the hypothesis match the values in the premise, we can infer entailment
    label = "entailment"
else:
    # if the values in the hypothesis contradict the values in the premise, we can infer contradiction
    label = "contradiction"

print(label)
