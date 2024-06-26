hours_premise = 1
hours_hypothesis = 6

# the hypothesis refers to the number of hours it takes to clean the entire house
if hours_hypothesis <= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
