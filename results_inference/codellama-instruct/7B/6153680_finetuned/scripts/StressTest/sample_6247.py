investment_premise = 600000
investment_hypothesis = 100000
interest_rate = 10
period = 3

# the hypothesis talks about the investment amount and interest rate, which are also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
