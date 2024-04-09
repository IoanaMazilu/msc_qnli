generals_arrested_premise = 3
generals_arrested_hypothesis = 3

# the hypothesis mentions the number of generals arrested, which is also referenced in the premise
if generals_arrested_hypothesis!= generals_arrested_premise:
    # check if the number of generals arrested in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of generals arrested in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
