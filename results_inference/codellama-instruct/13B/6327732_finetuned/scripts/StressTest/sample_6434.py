premise_amount = 8000
premise_years = 2
premise_interest_rate = 5

hypothesis_amount = 2000
hypothesis_years = 2
hypothesis_interest_rate = 5

# the hypothesis refers to the amount invested and the interest rate mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount invested in the premise
    label = "contradiction"
elif hypothesis_interest_rate!= premise_interest_rate:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
