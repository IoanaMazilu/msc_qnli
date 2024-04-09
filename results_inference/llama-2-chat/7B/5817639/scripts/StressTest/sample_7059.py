time_premise = 90
time_hypothesis = 20

# the hypothesis talks about the time difference between Dan and Cara, referenced also in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of the time difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
