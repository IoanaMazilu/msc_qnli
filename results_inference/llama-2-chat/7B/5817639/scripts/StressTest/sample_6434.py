invested_amount_premise = 8000
invested_amount_hypothesis = 2000
compound_interest_rate_premise = 5
compound_interest_rate_hypothesis = 5

# the hypothesis talks about the amount of money invested and the interest rate, which are also mentioned in the premise
if invested_amount_hypothesis <= invested_amount_premise:
    # check if the hypothesis value contradicts the estimate of the amount of money invested in the premise
    label = "contradiction"
elif compound_interest_rate_hypothesis!= compound_interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
