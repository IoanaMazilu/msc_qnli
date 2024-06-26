cds_premise = 4.0
shelves_hypothesis = 2.0

# compare the number of CDs in the premise and hypothesis
if cds_premise!= shelves_hypothesis:
    # if the number of CDs in the hypothesis is less than the number of shelves, it contradicts the premise
    label = "contradiction"
elif shelves_hypothesis < cds_premise:
    # if the number of shelves in the hypothesis is less than the number of CDs in the premise, it entails the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
