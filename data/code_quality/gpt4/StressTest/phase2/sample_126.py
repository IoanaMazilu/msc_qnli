years_premise = 2
years_hypothesis = 7
interest_rate = 4

# The hypothesis refers to the number of years and the interest rate of a hypothetical situation also referenced in the premise
if years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of years, so any hypothesis with a number of years greater than 'years_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
