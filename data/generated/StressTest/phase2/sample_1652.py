# Premise: If today in the morning Salley makes a payment of $7, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Hypothesis: If today in the morning Salley makes a payment of $2, for how many days, including today, will she be connected to the internet without any additional payments, given her initial balance was $0?
# Golden Label: contradiction

payment_premise = 7
payment_hypothesis = 2

# the hypothesis refers to the same payment mentioned in the premise
if payment_hypothesis != payment_premise:
    # check if the amount of payment in the hypothesis contradicts the amount of payment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

