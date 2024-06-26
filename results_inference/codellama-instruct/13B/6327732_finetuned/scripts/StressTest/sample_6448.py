years_premise = 8
years_hypothesis = 5

# the hypothesis refers to the number of years mentioned in the premise
if years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
