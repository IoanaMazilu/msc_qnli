boats_premise = 5.0
people_premise = 3.0
people_hypothesis = 15.0

# compare the number of boats and people in the premise and hypothesis
if boats_hypothesis == boats_premise and people_hypothesis == people_premise:
    # if the values and estimates in the hypothesis and premise match, we can infer entailment
    label = "entailment"
else:
    # if the values or estimates in the hypothesis contradict the premise, we can infer contradiction
    label = "contradiction"

print(label)
