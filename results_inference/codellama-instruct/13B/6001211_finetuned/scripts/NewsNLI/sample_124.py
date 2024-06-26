injuries_premise = 30
injuries_hypothesis = 30

# the hypothesis mentions the number of NTC fighter injuries, which is also referenced in the premise
if injuries_hypothesis!= injuries_premise:
    # check if the number of injuries in the hypothesis contradicts the number of injuries reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
