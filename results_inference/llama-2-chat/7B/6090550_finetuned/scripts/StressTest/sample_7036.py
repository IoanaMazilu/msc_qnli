fred_speed_premise = 8
fred_speed_hypothesis = 5
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis talks about the speed of Fred and Sam, which are also mentioned in the premise
if fred_speed_hypothesis >= fred_speed_premise:
    # check if the speed of Fred in the hypothesis contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_hypothesis!= sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
