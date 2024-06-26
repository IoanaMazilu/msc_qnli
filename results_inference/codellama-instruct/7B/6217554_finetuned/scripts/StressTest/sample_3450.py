time_joined_premise = 2
time_joined_hypothesis = 8

# the hypothesis talks about the time of joining mentioned in the premise
if time_joined_hypothesis <= time_joined_premise:
    # check if the hypothesis value contradicts the time of joining in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of joining
    # any time of joining greater than 'time_joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
