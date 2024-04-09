% labels = entailment, contradiction, neutral

premise = 5
hypothesis = 4

# check if the hypothesis value contradicts the estimate of 'premise'
if hypothesis <= premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people affected by the bombardment
    # any number of people greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
