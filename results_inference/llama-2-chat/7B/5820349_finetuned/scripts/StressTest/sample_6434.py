investment_premise = 8000
investment_hypothesis = 2000

# the hypothesis refers to the amount of money invested by Sachi, which is also mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount of money invested in the hypothesis contradicts the amount of money invested in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
