injured_premise = 2
injured_hypothesis = 2

# the hypothesis mentions the number of people undergoing emergency surgery, which is also referenced in the premise
if injured_hypothesis != injured_premise:
    # check if the number of injured in the hypothesis contradicts the number of injured reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
