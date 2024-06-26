premise_percentage = 10
hypothesis_percentage = 20

# the hypothesis refers to the number of people who died by bombardment and the number of people who left the village on account of fear
if hypothesis_percentage <= premise_percentage:
    # check if the estimate of 'hypothesis_percentage' contradicts the number of people who died by bombardment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who died by bombardment
    # any number of people greater than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
