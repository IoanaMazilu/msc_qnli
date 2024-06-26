premise_percentage = 10
hypothesis_percentage = 30

# the hypothesis refers to the percentage of people who died by bombardment and the percentage of people who left the village on account of fear
if hypothesis_percentage <= premise_percentage:
    # check if the hypothesis value contradicts the estimate of more than 'premise_percentage'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of people who died by bombardment
    # any number of people greater than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
