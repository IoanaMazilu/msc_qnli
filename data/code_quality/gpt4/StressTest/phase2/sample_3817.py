fred_speed_premise = 1
fred_speed_hypothesis = 4
sam_speed_premise = 4
sam_speed_hypothesis = 4

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if fred_speed_premise >= fred_speed_hypothesis:
    # check if 'fred_speed_hypothesis' contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_premise != sam_speed_hypothesis:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
