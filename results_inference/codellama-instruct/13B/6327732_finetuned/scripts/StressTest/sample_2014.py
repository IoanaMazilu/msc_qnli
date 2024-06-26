interest_rate_premise = 4
interest_rate_hypothesis = 4
years_premise = 6
years_hypothesis = 2

# the hypothesis talks about the number of years and interest rate mentioned in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
elif years_hypothesis >= years_premise:
    # check if the number of years in the hypothesis is greater than or equal to the number of years in the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of years and interest rate
    # any number of years and interest rate less than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
