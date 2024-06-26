investment_premise = 100000
investment_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
years_premise = 3
years_hypothesis = 3

# the hypothesis talks about the investment amount, interest rate and time period, all of which are mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or years_hypothesis!= years_premise:
    # check if the interest rate or time period in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
