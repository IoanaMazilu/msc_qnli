money_premise = 10000
money_hypothesis = 10000

# the hypothesis mentions the amount of money that must be declared, which is also mentioned in the premise
if money_hypothesis!= money_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the amount of money in the hypothesis matches the amount of money in the premise, we can infer entailment
    label = "entailment"

print(label)
