investment_premise = 8000
investment_hypothesis = 2000

# the hypothesis refers to the amount invested by Sachi, mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount invested in the hypothesis contradicts the amount invested reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
