interest_rate_premise = 4
interest_rate_hypothesis = 4
years_premise = 2
years_hypothesis = 8

# the hypothesis talks about the number of years and interest rate mentioned in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
elif years_hypothesis <= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years and interest rate
    # any number of years greater than 'years_premise' and any interest rate equal to 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
