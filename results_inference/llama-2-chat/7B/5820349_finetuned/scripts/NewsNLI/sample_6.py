capsizes_premise = 2
capsizes_hypothesis = 3

# the hypothesis mentions the number of times the boat capsized, which is also referenced in the premise
if capsizes_hypothesis!= capsizes_premise:
    # check if the number of capsizes in the hypothesis contradicts the number of capsizes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
