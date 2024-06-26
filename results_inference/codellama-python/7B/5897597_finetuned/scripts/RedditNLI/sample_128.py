payment_premise = 7.2
payment_hypothesis = 7.15

# the hypothesis and premise mention the amount of money Nestle is paying to Starbucks for coffee
if payment_hypothesis!= payment_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
