viewers_premise = 1200000
viewers_hypothesis = 1200000

# the hypothesis mentions the number of people who viewed a certain content, which is also referenced in the premise
if viewers_hypothesis > viewers_premise:
    # check if the number of viewers in the hypothesis contradicts the number of viewers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
