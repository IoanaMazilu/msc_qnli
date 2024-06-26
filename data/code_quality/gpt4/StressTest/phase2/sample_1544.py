amount_premise = 3450
amount_hypothesis = 4450
rate_premise = 6
rate_hypothesis = 6

# the hypothesis talks about the amount from Anwar and the interest rate, both referenced in the premise
if amount_hypothesis < amount_premise or rate_hypothesis != rate_premise:
    # check if the amount or rate in the hypothesis contradicts the amount or rate mentioned in the premise
    label = "contradiction"
elif amount_hypothesis == amount_premise and rate_hypothesis == rate_premise:
    # if the amount and rate in the hypothesis are the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the amount in the hypothesis is greater than in the premise and the rate is the same, the relation is neutral
    label = "neutral"

print(label)
