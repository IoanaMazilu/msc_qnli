protesters_premise = 500000
protesters_hypothesis = 500000

# the hypothesis mentions the number of protesters in Taiz, which is also referenced in the premise
if protesters_hypothesis!= protesters_premise:
    # check if the number of protesters in the hypothesis contradicts the number of protesters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)