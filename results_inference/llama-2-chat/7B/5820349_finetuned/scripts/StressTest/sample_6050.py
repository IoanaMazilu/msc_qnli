money_to_give_premise = 95
money_to_give_hypothesis = 55

# the hypothesis talks about the amount of money given to John, referenced also in the premise
if money_to_give_hypothesis!= money_to_give_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
