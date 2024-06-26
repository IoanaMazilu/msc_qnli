efficiency_premise = 10
efficiency_hypothesis = 30

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_premise >= efficiency_hypothesis:
    # check if the efficiency difference in the premise contradicts the estimate of 'efficiency_hypothesis'
    label = "contradiction"
else:
    # if the efficiency difference in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
