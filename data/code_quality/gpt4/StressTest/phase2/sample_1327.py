years_premise = 8
years_hypothesis = 2
interest_rate = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the number of years in the hypothesis contradicts the estimate of less than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
