years_john_premise = 21
years_john_hypothesis = 71

# the hypothesis refers to the number of years in the future, mentioned in the premise
if years_john_hypothesis <= years_john_premise:
    # check if the estimate of 'years_john_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)