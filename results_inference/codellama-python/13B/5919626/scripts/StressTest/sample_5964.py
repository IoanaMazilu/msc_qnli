hours_premise = 4
hours_hypothesis = 8

# the hypothesis talks about the number of hours taken to drive from City A to City B
# the premise gives an estimate for the number of hours taken to drive from City A to City B
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours taken to drive from City A to City B
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
