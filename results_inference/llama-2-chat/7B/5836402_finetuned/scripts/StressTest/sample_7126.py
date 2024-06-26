jog_hours_premise = 1
jog_hours_hypothesis = 3

# the hypothesis refers to the total hours Aaron spends jogging and walking, which is also mentioned in the premise
if jog_hours_hypothesis <= jog_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jog_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total jog hours
    # any total hours greater than 'jog_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
