soc_premise = 4/3
soc_hypothesis = 1/3

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if soc_premise!= soc_hypothesis:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the ratio of ages in the hypothesis matches the ratio of ages in the premise, we can infer entailment
    label = "entailment"

print(label)
