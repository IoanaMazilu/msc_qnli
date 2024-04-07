# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 40, if all of them reached a shopping mall in Delhi and purchased 14 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 10, if all of them reached a shopping mall in Delhi and purchased 14 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

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

