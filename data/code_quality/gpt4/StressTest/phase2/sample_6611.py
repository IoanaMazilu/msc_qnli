years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to the same situation as the premise but with a different estimate for the number of years in the future
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the premise which states 'in 18 years'
    label = "contradiction"
else:
    # the premise states 'in 18 years', any number of years larger than 18 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
