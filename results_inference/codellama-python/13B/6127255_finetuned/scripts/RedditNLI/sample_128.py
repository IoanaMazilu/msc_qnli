payment_premise = 7.2
payment_hypothesis = 7.15

# the hypothesis and premise mention the payment made by Nestle to Starbucks
if payment_hypothesis!= payment_premise:
    # check if the payment value in the hypothesis contradicts the payment value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
