# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if fred_speed_hypothesis >= 7 or sam_speed_hypothesis!= 5:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
