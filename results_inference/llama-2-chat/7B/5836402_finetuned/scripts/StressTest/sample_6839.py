earned_premise = 9000
earned_hypothesis = 9000

# the hypothesis refers to the amount of money earned by he and Rick mentioned in the premise
if earned_hypothesis >= earned_premise:
    # check if the hypothesis value contradicts the amount of money earned in the premise
    label = "contradiction"
elif earned_hypothesis < earned_premise:
    # if the hypothesis value is less than the amount of money earned in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the amount of money earned in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
