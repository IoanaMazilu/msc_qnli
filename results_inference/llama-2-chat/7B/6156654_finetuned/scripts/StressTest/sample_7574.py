fred_speed = 2
sam_speed = 5

# the hypothesis refers to the speed of Fred and Sam, which are also mentioned in the premise
if fred_speed < 2:
    # check if the speed of Fred in the hypothesis contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed!= 5:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
