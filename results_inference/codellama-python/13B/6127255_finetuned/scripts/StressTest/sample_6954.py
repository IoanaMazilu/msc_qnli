average_shirts_premise = 40
average_shirts_hypothesis = 80
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned in the premise
if average_shirts_premise + shirts_purchased >= average_shirts_hypothesis:
    # check if the new average number of shirts contradicts the hypothesis
    label = "contradiction"
else:
    # if the new average number of shirts does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
