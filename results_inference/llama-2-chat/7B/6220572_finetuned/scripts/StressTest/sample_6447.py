years_future_premise = 5
years_future_hypothesis = 8

# the hypothesis refers to the age difference between John and Frank mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
