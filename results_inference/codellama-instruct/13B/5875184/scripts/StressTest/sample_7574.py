premise_speed_f = 2
premise_speed_s = 5
hypothesis_speed_f = 2
hypothesis_speed_s = 5

# the hypothesis refers to the speed of Fred and Sam, mentioned in the premise
if hypothesis_speed_f > premise_speed_f:
    # check if the estimate of 'hypothesis_speed_f' contradicts the speed of Fred in the premise
    label = "contradiction"
elif hypothesis_speed_s!= premise_speed_s:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
