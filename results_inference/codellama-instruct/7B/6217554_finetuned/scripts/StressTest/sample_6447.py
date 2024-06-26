# the hypothesis refers to the time when John will be twice as old as Frank, referenced also in the premise
if 5 >= 8:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
