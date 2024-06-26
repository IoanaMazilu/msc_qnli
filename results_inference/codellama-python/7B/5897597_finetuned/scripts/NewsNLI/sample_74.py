generals_premise = 3
generals_hypothesis = 3

# the hypothesis mentions the arrest of three generals, which is also mentioned in the premise
if generals_hypothesis!= generals_premise:
    # check if the number of generals arrested in the hypothesis contradicts the number of generals arrested in the premise
    label = "contradiction"
else:
    # if the number of generals arrested in the hypothesis does not contradict the number of generals arrested in the premise, we can infer entailment
    label = "entailment"

print(label)
