raman_butter_premise = 84
raman_butter_hypothesis = 44

# the hypothesis refers to the quantity of butter mixed by Raman, which is also mentioned in the premise
if raman_butter_hypothesis >= raman_butter_premise:
    # check if the hypothesis value contradicts the estimate of less than 'raman_butter_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of butter mixed by Raman
    # any quantity of butter less than 'raman_butter_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
