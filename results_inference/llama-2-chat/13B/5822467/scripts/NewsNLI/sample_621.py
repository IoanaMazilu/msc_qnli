arrest_premise = 0.38
arrest_hypothesis = 0.4

# the hypothesis mentions the arrest risk for white males, which is also mentioned in the premise
if arrest_hypothesis!= arrest_premise:
    # check if the arrest risk in the hypothesis contradicts the arrest risk reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
