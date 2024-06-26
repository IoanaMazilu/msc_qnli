# the hypothesis mentions the number of member states, which is also mentioned in the premise
if entailment_premise is not 20:
    # check if the number of member states in the hypothesis contradicts the number of member states in the premise
    label = "contradiction"
elif entailment_hypothesis is not 20:
    # check if the number of member states in the hypothesis contradicts the number of member states in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
