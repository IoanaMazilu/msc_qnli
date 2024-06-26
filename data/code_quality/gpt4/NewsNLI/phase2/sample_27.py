people_premise = 700
people_hypothesis = 700

# the hypothesis mentions the number of people fleeing Syria for Turkey, which is also referenced in the premise
if people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # if the numbers in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
