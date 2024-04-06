# Premise: As a rule of thumb, you should try not to use more than 10 percent of your credit limit when making purchases.
# Hypothesis: Expert:Use no more than 10 percent of your available credit.
# Golden Label: entailment

credit_limit_percentage_premise = 0.10
credit_limit_percentage_hypothesis = 0.10

# the hypothesis mentions the rule of thumb about credit limit usage, which is also mentioned in the premise
if credit_limit_percentage_hypothesis != credit_limit_percentage_premise:
    # check if the credit limit percentage in the hypothesis contradicts the credit limit percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

