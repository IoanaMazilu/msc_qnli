years_premise = 2
years_hypothesis = 5

# the hypothesis refers to a future date when John will be twice as old as Frank, which is also mentioned in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the premise statement of 'more than 2 years'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when John will be twice as old as Frank
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
