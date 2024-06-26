hours_premise = 6
hours_hypothesis = 1

# the hypothesis refers to the number of hours it takes to clean the entire house
if hours_hypothesis <= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours it takes to clean the entire house
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
