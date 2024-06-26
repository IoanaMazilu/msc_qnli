fred_speed_premise = 7
fred_speed_hypothesis = 2
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if fred_speed_hypothesis >= fred_speed_premise:
    # check if the speed of Fred in the hypothesis contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_hypothesis!= sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Fred
    # any speed of Fred less than 'fred_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
