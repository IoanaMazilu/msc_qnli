fred_speed_premise = 2
fred_speed_hypothesis = 2
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis and premise both refer to the speeds of Fred and Sam
if fred_speed_hypothesis <= fred_speed_premise:
    # check if the hypothesis value contradicts the premise speed of Fred
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
