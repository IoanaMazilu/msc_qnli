deaths_premise = 3
injured_premise = 52

deaths_hypothesis = 3
injured_hypothesis = 52

# the hypothesis mentions the number of deaths and injured people in Sri Lanka, which are also mentioned in the premise

# check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
if deaths_hypothesis!= deaths_premise:
    # if the number of deaths in the hypothesis contradicts the premise, then the label is contradiction
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # if the number of injured people in the hypothesis contradicts the premise, then the label is contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
