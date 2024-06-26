average_shirts_premise = 40
average_shirts_hypothesis = 40
shirts_purchased_each = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned also in the premise
if average_shirts_hypothesis + shirts_purchased_each >= average_shirts_premise + shirts_purchased_each:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
