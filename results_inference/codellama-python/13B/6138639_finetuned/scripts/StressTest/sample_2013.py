years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis talks about the number of years and interest rate, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
