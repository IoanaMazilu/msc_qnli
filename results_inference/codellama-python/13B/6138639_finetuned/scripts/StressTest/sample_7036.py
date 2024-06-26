fred_speed_premise = 8
sam_speed_premise = 5
fred_speed_hypothesis = 5
sam_speed_hypothesis = 5

# the hypothesis talks about the speed of Fred and Sam, referenced also in the premise
if fred_speed_hypothesis >= fred_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fred_speed_premise'
    label = "contradiction"
elif sam_speed_hypothesis!= sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Fred
    # any speed of Fred less than 'fred_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
