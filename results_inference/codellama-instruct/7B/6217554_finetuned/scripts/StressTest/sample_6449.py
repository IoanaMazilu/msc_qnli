# the hypothesis refers to the time when John will be twice as old as Frank, referenced also in the premise
if 7!= 5:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
