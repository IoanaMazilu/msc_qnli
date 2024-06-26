hours_premise = 11
hours_hypothesis = 21

# the hypothesis refers to the hours of work paid with x dollars, as mentioned in the premise
if hours_hypothesis <= hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of more than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
