john_age_multiple_premise = 3
john_age_multiple_hypothesis = 3
time_past_premise = 5
time_past_hypothesis = 6

# the hypothesis talks about the age relation between John and Tom at a certain point in the past, referenced also in the premise
if john_age_multiple_hypothesis!= john_age_multiple_premise:
    # check if the multiple of John's age in relation to Tom's age in the hypothesis contradicts the same multiple in the premise
    label = "contradiction"
elif time_past_hypothesis <= time_past_premise:
    # check if the time in the past mentioned in the hypothesis contradicts the time in the past mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time in the past
    # any time greater than 'time_past_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
