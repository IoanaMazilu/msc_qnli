killed_premise = 21
killed_hypothesis = 21
injured_premise = 35
injured_hypothesis = 35

# the hypothesis mentions the number of people who died and were injured, which are also mentioned in the premise
if killed_hypothesis < killed_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injuries from the hypothesis contradicts the number of injuries in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
