years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to Molly's age in a certain number of years, which is also mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific number of years for Molly's age
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
