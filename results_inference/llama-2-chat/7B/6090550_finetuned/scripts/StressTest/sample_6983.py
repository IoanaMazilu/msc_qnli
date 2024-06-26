 interest_rate_premise = 6%
interest_rate_hypothesis = 8%

# the hypothesis talks about the interest rate at which Nitin borrowed money, which is also referenced in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the interest rate in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)
