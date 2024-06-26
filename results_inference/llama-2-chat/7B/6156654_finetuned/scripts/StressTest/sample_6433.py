investment_premise = 5000
investment_hypothesis = 8000
compound_interest_premise = 5
compound_interest_hypothesis = 5
years = 2

# the hypothesis refers to the investment amount, compound interest rate, and number of years, which are also mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the hypothesis value contradicts the premise value of investment amount
    label = "contradiction"
elif compound_interest_hypothesis!= compound_interest_premise:
    # check if the hypothesis value contradicts the premise value of compound interest rate
    label = "contradiction"
elif years!= 2:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
