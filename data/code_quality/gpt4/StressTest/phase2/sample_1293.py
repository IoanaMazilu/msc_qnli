average_shirts_premise = 40
average_shirts_hypothesis = 10
shirts_purchased = 14

# the hypothesis refers to the average number of shirts of Salman, Ambani and Dalmiya, mentioned also in the premise
if average_shirts_premise <= average_shirts_hypothesis:
    # check if the hypothesis estimate contradicts the average number of shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
