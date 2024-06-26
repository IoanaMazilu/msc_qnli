average_shirts_premise = 40
average_shirts_hypothesis = 80
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned also in the premise
if average_shirts_premise + shirts_purchased >= average_shirts_hypothesis + shirts_purchased:
    # check if the hypothesis value contradicts the premise value plus the number of shirts purchased
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value plus the number of shirts purchased, we can infer entailment
    label = "entailment"

print(label)
