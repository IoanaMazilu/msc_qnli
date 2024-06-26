money_premise = 45000
money_hypothesis = 45000

# the hypothesis mentions the amount of money stolen, which is also mentioned in the premise
if money_hypothesis!= money_premise:
    # check if the amount of money in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amounts in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
