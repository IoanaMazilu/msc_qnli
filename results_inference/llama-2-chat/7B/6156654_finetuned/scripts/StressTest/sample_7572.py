fred_speed = 2
sam_speed = 5
fred_speed_hypothesis = 7
sam_speed_hypothesis = 5

# the hypothesis talks about the speed of Fred and Sam
if fred_speed >= fred_speed_hypothesis:
    # check if the speed of Fred in the premise contradicts the hypothesis
    label = "contradiction"
elif sam_speed_hypothesis!= sam_speed:
    # check if the speed of Sam in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
