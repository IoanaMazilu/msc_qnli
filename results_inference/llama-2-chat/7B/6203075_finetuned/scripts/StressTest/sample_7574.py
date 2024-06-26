fred_speed_premise = 2
sam_speed_premise = 5
fred_speed_hypothesis = 2
sam_speed_hypothesis = 5

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if fred_speed_hypothesis <= fred_speed_premise:
    # check if the speed of Fred in the hypothesis contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_hypothesis!= sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
