interest_rate_premise = 8
interest_rate_hypothesis = 4

# the hypothesis talks about the interest rate at the end of two years, referenced also in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the interest rate in the hypothesis does not contradict the interest rate in the premise, we can infer entailment
    label = "entailment"

print(label)