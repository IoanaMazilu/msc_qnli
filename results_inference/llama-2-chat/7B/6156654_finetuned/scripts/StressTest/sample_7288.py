total_investment_premise = 64000
total_investment_hypothesis = 14000

# the hypothesis talks about the investment in a business that John jointly owns with James and Greg, which is also mentioned in the premise
if total_investment_hypothesis >= total_investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif total_investment_hypothesis < total_investment_premise:
    # check if the hypothesis value is less than the premise value
    # this is the case, as the hypothesis value is 14000, which is less than the premise value of 64000
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "neutral"

print(label)
