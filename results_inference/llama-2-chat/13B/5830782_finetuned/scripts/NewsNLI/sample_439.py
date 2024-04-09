killed_premise = 3
killed_hypothesis = 3
injured_premise = 52
injured_hypothesis = 52

# the hypothesis mentions the number of killed and injured people, which are also mentioned in the premise
if killed_hypothesis < killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people reported in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
