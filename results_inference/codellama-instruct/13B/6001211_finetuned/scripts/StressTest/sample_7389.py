efficiency_premise = 10
efficiency_hypothesis = 30

# the hypothesis refers to the efficiency of Rosy compared to Mary, also mentioned in the premise
if efficiency_premise >= efficiency_hypothesis:
    # check if the efficiency percentage in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the efficiency percentage in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
