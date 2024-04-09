raman_butter_premise = 27
raman_butter_hypothesis = 47

# the hypothesis refers to the amount of butter mixed in the premise
if raman_butter_hypothesis <= raman_butter_premise:
    # check if the hypothesis value contradicts the estimate of 'raman_butter_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of butter mixed
    # any amount of butter less than 'raman_butter_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
