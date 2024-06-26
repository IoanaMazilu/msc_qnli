loan_period_premise = 2
loan_period_hypothesis = 8
interest_rate = 4

# the hypothesis refers to the same loan situation as the premise, but with a different loan period
if loan_period_hypothesis != loan_period_premise:
    # check if the loan period in the hypothesis contradicts the loan period mentioned in the premise
    label = "contradiction"
else:
    # if the loan period in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
