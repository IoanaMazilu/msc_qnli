# the hypothesis refers to the total time spent jogging and walking, which is also mentioned in the premise
if 3!= 4:
    # check if the total time in the hypothesis contradicts the total time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
